import uuid
from datetime import datetime, timezone, date
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from retailsync_app import models
from retailsync_app import schemas

class InboundService:
    @staticmethod
    def get_open_purchase_orders(db: Session) -> List[Dict[str, Any]]:
        pos = db.query(models.PurchaseOrder).filter(
            models.PurchaseOrder.status.in_([models.POStatus.ISSUED, models.POStatus.PARTIAL_RECEIVED])
        ).all()
        results = []
        for po in pos:
            items = []
            for item in po.items:
                items.append({
                    "item_id": item.item_id,
                    "product_id": item.product_id,
                    "product_name": item.product.product_name,
                    "sku_code": item.product.sku_code,
                    "barcode": item.product.barcode,
                    "ordered_quantity": item.ordered_quantity,
                    "received_quantity": item.received_quantity,
                    "remaining_quantity": item.ordered_quantity - item.received_quantity,
                    "unit_cost_bdt": item.unit_cost_bdt,
                    "subtotal_bdt": item.subtotal_bdt
                })
            results.append({
                "po_id": po.po_id,
                "po_number": po.po_number,
                "supplier_name": po.supplier.company_name,
                "order_date": po.order_date.strftime("%Y-%m-%d"),
                "expected_delivery_date": po.expected_delivery_date.strftime("%Y-%m-%d"),
                "total_amount_bdt": po.total_amount_bdt,
                "status": po.status.value if hasattr(po.status, "value") else str(po.status),
                "items": items
            })
        return results

    @staticmethod
    def receive_goods(
        db: Session,
        clerk: models.User,
        request: schemas.InboundReceiveRequest
    ) -> schemas.InboundReceiveResponse:
        po = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.po_id == request.po_id).first()
        if not po:
            raise HTTPException(status_code=404, detail="Purchase Order not found")

        grn_number = f"GRN-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:4].upper()}"
        total_cartons = 0
        batches_created = 0
        today = date.today()

        for item_data in request.items:
            product = db.query(models.Product).filter(models.Product.product_id == item_data.product_id).first()
            if not product:
                continue

            # Shelf-life validation threshold (must have >= 65% shelf life remaining)
            total_shelf_life = max(product.shelf_life_days, 1)
            remaining_days = (item_data.expiry_date - today).days
            shelf_life_ratio = remaining_days / total_shelf_life

            batch_status = models.BatchStatus.AVAILABLE
            if shelf_life_ratio < 0.65 or remaining_days < 3:
                batch_status = models.BatchStatus.QUARANTINED

            valid_qty = item_data.quantity_received - item_data.damaged_quantity
            if valid_qty > 0:
                batch = models.InventoryBatch(
                    lot_number=item_data.lot_number,
                    product_id=product.product_id,
                    bin_id=None, # Inbound staging dock, awaits Putaway
                    initial_quantity=valid_qty,
                    current_quantity=valid_qty,
                    manufacturing_date=item_data.manufacturing_date,
                    expiry_date=item_data.expiry_date,
                    unit_cost_bdt=item_data.unit_cost_bdt,
                    status=batch_status,
                    grn_number=grn_number
                )
                db.add(batch)
                db.flush()
                batches_created += 1

                # Log to stock ledger
                ledger = models.StockLedger(
                    product_id=product.product_id,
                    batch_id=batch.batch_id,
                    transaction_type=models.TransactionType.INBOUND_GRN,
                    quantity_change=valid_qty,
                    previous_balance=0,
                    new_balance=valid_qty,
                    user_id=clerk.user_id,
                    reference_number=grn_number,
                    notes=f"Received at Inbound Dock from {po.supplier.company_name} (PO: {po.po_number})"
                )
                db.add(ledger)

            # Update PO Item received quantity
            po_item = db.query(models.PurchaseOrderItem).filter(
                models.PurchaseOrderItem.po_id == po.po_id,
                models.PurchaseOrderItem.product_id == product.product_id
            ).first()
            if po_item:
                po_item.received_quantity += item_data.quantity_received

            total_cartons += item_data.quantity_received

        # Check if PO completed
        all_received = all(item.received_quantity >= item.ordered_quantity for item in po.items)
        po.status = models.POStatus.COMPLETED if all_received else models.POStatus.PARTIAL_RECEIVED

        # Record GRN
        grn = models.GoodsReceiptNote(
            grn_number=grn_number,
            po_id=po.po_id,
            receiving_clerk_id=clerk.user_id,
            received_at=datetime.now(timezone.utc),
            total_cartons_received=total_cartons,
            status="COMPLETED",
            notes=request.notes
        )
        db.add(grn)
        db.commit()

        return schemas.InboundReceiveResponse(
            grn_number=grn_number,
            po_id=po.po_id,
            received_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            total_cartons_received=total_cartons,
            created_batches_count=batches_created,
            status=po.status.value if hasattr(po.status, "value") else str(po.status)
        )
