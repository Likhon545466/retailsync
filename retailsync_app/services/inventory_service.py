import time
import uuid
from datetime import datetime, timezone, date
from typing import List, Dict, Any, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status

from retailsync_app import models
from retailsync_app import schemas

class InventoryService:
    @staticmethod
    def get_all_products_with_stock(db: Session) -> List[Dict[str, Any]]:
        products = db.query(models.Product).filter(models.Product.is_active == True).all()
        results = []
        for p in products:
            total_stock = (
                db.query(func.coalesce(func.sum(models.InventoryBatch.current_quantity), 0))
                .filter(
                    models.InventoryBatch.product_id == p.product_id,
                    models.InventoryBatch.status == models.BatchStatus.AVAILABLE,
                    models.InventoryBatch.expiry_date >= date.today()
                )
                .scalar()
            )
            item_dict = {
                "product_id": p.product_id,
                "sku_code": p.sku_code,
                "barcode": p.barcode,
                "product_name": p.product_name,
                "category": p.category.value if hasattr(p.category, "value") else str(p.category),
                "temp_required": p.temp_required.value if hasattr(p.temp_required, "value") else str(p.temp_required),
                "unit_of_measure": p.unit_of_measure,
                "unit_cost_bdt": p.unit_cost_bdt,
                "selling_price_bdt": p.selling_price_bdt,
                "min_safety_stock": p.min_safety_stock,
                "max_stock_capacity": p.max_stock_capacity,
                "reorder_point": p.reorder_point,
                "daily_demand_mean": p.daily_demand_mean,
                "daily_demand_std_dev": p.daily_demand_std_dev,
                "shelf_life_days": p.shelf_life_days,
                "total_available_stock": total_stock
            }
            results.append(item_dict)
        return results

    @staticmethod
    def execute_pos_fefo_checkout(
        db: Session,
        cashier: models.User,
        request: schemas.PosCheckoutRequest
    ) -> schemas.PosCheckoutResponse:
        start_time = time.time()
        receipt_no = f"REC-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        
        allocated_items: List[schemas.PosAllocatedItem] = []
        total_amount = 0.0

        # Sort requested items to avoid deadlock conditions
        sorted_requests = sorted(request.items, key=lambda x: x.barcode)

        for item_req in sorted_requests:
            product = db.query(models.Product).filter(
                models.Product.barcode == item_req.barcode,
                models.Product.is_active == True
            ).first()
            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Barcode {item_req.barcode} not found in product catalog."
                )

            remaining_to_deduct = item_req.quantity

            # FEFO Priority: Order available batches by nearest expiry date
            # SQLite does not support SELECT FOR UPDATE; PostgreSQL does natively
            batches_query = db.query(models.InventoryBatch).filter(
                models.InventoryBatch.product_id == product.product_id,
                models.InventoryBatch.status == models.BatchStatus.AVAILABLE,
                models.InventoryBatch.current_quantity > 0,
                models.InventoryBatch.expiry_date >= date.today()
            ).order_by(models.InventoryBatch.expiry_date.asc())

            try:
                # Use row-level locking where supported
                batches = batches_query.with_for_update().all()
            except Exception:
                # Fallback gracefully for SQLite
                batches = batches_query.all()

            available_total = sum(b.current_quantity for b in batches)
            if available_total < remaining_to_deduct:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail={
                        "code": "STOCKOUT_ERROR",
                        "message": f"Insufficient available FEFO stock for {product.product_name}.",
                        "product_name": product.product_name,
                        "barcode": product.barcode,
                        "requested_qty": remaining_to_deduct,
                        "available_qty": available_total
                    }
                )

            for b in batches:
                if remaining_to_deduct <= 0:
                    break
                deduct_from_batch = min(b.current_quantity, remaining_to_deduct)
                prev_bal = b.current_quantity
                b.current_quantity -= deduct_from_batch
                new_bal = b.current_quantity
                if b.current_quantity == 0:
                    b.status = models.BatchStatus.DEPLETED

                remaining_to_deduct -= deduct_from_batch
                line_subtotal = deduct_from_batch * product.selling_price_bdt
                total_amount += line_subtotal

                # Record in Stock Ledger
                ledger_entry = models.StockLedger(
                    product_id=product.product_id,
                    batch_id=b.batch_id,
                    transaction_type=models.TransactionType.POS_SALE_FEFO,
                    quantity_change=-deduct_from_batch,
                    previous_balance=prev_bal,
                    new_balance=new_bal,
                    user_id=cashier.user_id,
                    reference_number=receipt_no,
                    notes=f"POS Sale at {request.branch_code}"
                )
                db.add(ledger_entry)

                allocated_items.append(
                    schemas.PosAllocatedItem(
                        product_id=product.product_id,
                        product_name=product.product_name,
                        sku_code=product.sku_code,
                        barcode=product.barcode,
                        batch_id=b.batch_id,
                        lot_number=b.lot_number,
                        expiry_date=b.expiry_date.strftime("%Y-%m-%d"),
                        quantity=deduct_from_batch,
                        unit_price_bdt=product.selling_price_bdt,
                        subtotal_bdt=line_subtotal
                    )
                )

        latency_ms = round((time.time() - start_time) * 1000, 2)

        # Create master POS Transaction
        pos_tx = models.PosTransaction(
            receipt_number=receipt_no,
            cashier_id=cashier.user_id,
            branch_code=request.branch_code,
            transaction_time=datetime.now(timezone.utc),
            total_amount_bdt=total_amount,
            payment_method=request.payment_method,
            latency_ms=latency_ms
        )
        db.add(pos_tx)
        db.flush()

        for alloc in allocated_items:
            tx_item = models.PosTransactionItem(
                transaction_id=pos_tx.transaction_id,
                product_id=alloc.product_id,
                batch_id=alloc.batch_id,
                quantity=alloc.quantity,
                unit_price_bdt=alloc.unit_price_bdt,
                subtotal_bdt=alloc.subtotal_bdt
            )
            db.add(tx_item)

        db.commit()

        return schemas.PosCheckoutResponse(
            receipt_number=receipt_no,
            transaction_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            branch_code=request.branch_code,
            cashier_name=cashier.full_name,
            total_amount_bdt=round(total_amount, 2),
            payment_method=request.payment_method,
            latency_ms=latency_ms,
            allocated_items=allocated_items
        )

    @staticmethod
    def suggest_putaway_bin(db: Session, batch_id: int) -> schemas.PutawaySuggestResponse:
        batch = db.query(models.InventoryBatch).filter(models.InventoryBatch.batch_id == batch_id).first()
        if not batch:
            raise HTTPException(status_code=404, detail="Batch not found")

        product = batch.product
        required_temp = product.temp_required

        # Match Zone by temperature
        target_zone = db.query(models.WarehouseZone).filter(models.WarehouseZone.temp_category == required_temp).first()
        if not target_zone:
            target_zone = db.query(models.WarehouseZone).first()

        # Find empty bin in target zone
        empty_bin = db.query(models.WarehouseBin).filter(
            models.WarehouseBin.zone_id == target_zone.zone_id,
            models.WarehouseBin.is_active == True,
            models.WarehouseBin.is_occupied == False
        ).order_by(
            models.WarehouseBin.aisle_number.asc(),
            models.WarehouseBin.rack_number.asc(),
            models.WarehouseBin.shelf_tier.asc()
        ).first()

        if not empty_bin:
            # Fallback to any active bin in that zone
            empty_bin = db.query(models.WarehouseBin).filter(
                models.WarehouseBin.zone_id == target_zone.zone_id,
                models.WarehouseBin.is_active == True
            ).first()

        return schemas.PutawaySuggestResponse(
            batch_id=batch.batch_id,
            lot_number=batch.lot_number,
            product_name=product.product_name,
            temp_category=str(required_temp.value if hasattr(required_temp, "value") else required_temp),
            suggested_bin_id=empty_bin.bin_id,
            suggested_bin_code=empty_bin.bin_code,
            aisle=empty_bin.aisle_number,
            rack=empty_bin.rack_number,
            shelf=empty_bin.shelf_tier,
            bin_position=empty_bin.bin_position,
            reason=f"Optimal match for {required_temp.value if hasattr(required_temp, 'value') else required_temp} zone with lowest floor travel distance."
        )

    @staticmethod
    def confirm_putaway(db: Session, batch_id: int, bin_id: int, operator: models.User):
        batch = db.query(models.InventoryBatch).filter(models.InventoryBatch.batch_id == batch_id).first()
        bin_obj = db.query(models.WarehouseBin).filter(models.WarehouseBin.bin_id == bin_id).first()
        if not batch or not bin_obj:
            raise HTTPException(status_code=404, detail="Batch or Bin not found")

        batch.bin_id = bin_obj.bin_id
        bin_obj.is_occupied = True

        ledger = models.StockLedger(
            product_id=batch.product_id,
            batch_id=batch.batch_id,
            transaction_type=models.TransactionType.DIRECTED_PUTAWAY,
            quantity_change=0,
            previous_balance=batch.current_quantity,
            new_balance=batch.current_quantity,
            user_id=operator.user_id,
            reference_number=f"PUTAWAY-{bin_obj.bin_code}",
            notes=f"Placed into bin {bin_obj.bin_code} by {operator.full_name}"
        )
        db.add(ledger)
        db.commit()
        return {"status": "SUCCESS", "bin_code": bin_obj.bin_code, "batch_id": batch.batch_id}
