from datetime import date
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import func

from retailsync_app import models
from retailsync_app import schemas

class AuditService:
    @staticmethod
    def get_warehouse_spatial_grid(db: Session) -> schemas.WarehouseGridResponse:
        bins = db.query(models.WarehouseBin).filter(models.WarehouseBin.is_active == True).all()
        grid_items: List[schemas.BinGridItem] = []

        occupied_count = 0
        ambient_count = 0
        chilled_count = 0
        frozen_count = 0
        today = date.today()

        for b in bins:
            temp_cat = b.zone.temp_category.value if hasattr(b.zone.temp_category, "value") else str(b.zone.temp_category)
            if "AMBIENT" in temp_cat:
                ambient_count += 1
            elif "CHILLED" in temp_cat:
                chilled_count += 1
            elif "FROZEN" in temp_cat:
                frozen_count += 1

            # Active batches in this bin
            batches = db.query(models.InventoryBatch).filter(
                models.InventoryBatch.bin_id == b.bin_id,
                models.InventoryBatch.current_quantity > 0,
                models.InventoryBatch.status == models.BatchStatus.AVAILABLE
            ).all()

            is_occ = len(batches) > 0
            if is_occ:
                occupied_count += 1

            nearest_exp = None
            if batches:
                nearest_date = min(batch.expiry_date for batch in batches)
                nearest_exp = (nearest_date - today).days

            summary = "Empty"
            if batches:
                summary = f"{len(batches)} batches ({sum(x.current_quantity for x in batches)} units)"

            grid_items.append(
                schemas.BinGridItem(
                    bin_id=b.bin_id,
                    bin_code=b.bin_code,
                    zone_code=b.zone.zone_code,
                    temp_category=temp_cat,
                    aisle_number=b.aisle_number,
                    rack_number=b.rack_number,
                    shelf_tier=b.shelf_tier,
                    bin_position=b.bin_position,
                    is_occupied=is_occ,
                    current_weight_kg=b.current_weight_kg,
                    max_weight_kg=b.max_weight_kg,
                    batches_count=len(batches),
                    nearest_expiry_days=nearest_exp,
                    items_summary=summary
                )
            )

        return schemas.WarehouseGridResponse(
            total_bins=len(bins),
            occupied_bins=occupied_count,
            ambient_bins=ambient_count,
            chilled_bins=chilled_count,
            frozen_bins=frozen_count,
            grid=grid_items
        )

    @staticmethod
    def get_audit_ledger(db: Session, limit: int = 50) -> List[Dict[str, Any]]:
        entries = (
            db.query(models.StockLedger)
            .order_by(models.StockLedger.timestamp.desc())
            .limit(limit)
            .all()
        )
        results = []
        for e in entries:
            results.append({
                "ledger_id": e.ledger_id,
                "timestamp": e.timestamp.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "product_name": e.product.product_name if e.product else "Unknown",
                "sku_code": e.product.sku_code if e.product else "N/A",
                "lot_number": e.batch.lot_number if e.batch else "N/A",
                "transaction_type": e.transaction_type.value if hasattr(e.transaction_type, "value") else str(e.transaction_type),
                "quantity_change": e.quantity_change,
                "previous_balance": e.previous_balance,
                "new_balance": e.new_balance,
                "user_name": e.user.full_name if e.user else "System Process",
                "reference_number": e.reference_number,
                "notes": e.notes
            })
        return results

    @staticmethod
    def get_unallocated_batches(db: Session) -> List[Dict[str, Any]]:
        batches = db.query(models.InventoryBatch).filter(
            models.InventoryBatch.bin_id == None,
            models.InventoryBatch.current_quantity > 0,
            models.InventoryBatch.status == models.BatchStatus.AVAILABLE
        ).all()
        results = []
        for b in batches:
            results.append({
                "batch_id": b.batch_id,
                "lot_number": b.lot_number,
                "product_name": b.product.product_name,
                "sku_code": b.product.sku_code,
                "barcode": b.product.barcode,
                "temp_required": b.product.temp_required.value if hasattr(b.product.temp_required, "value") else str(b.product.temp_required),
                "current_quantity": b.current_quantity,
                "expiry_date": b.expiry_date.strftime("%Y-%m-%d"),
                "grn_number": b.grn_number
            })
        return results
