import math
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from retailsync_app import models
from retailsync_app import schemas

class ReplenishmentService:
    @staticmethod
    def calculate_replenishment_recommendations(
        db: Session,
        service_level_z_score: float = 1.96, # 97.5% service level
        festival_multiplier: float = 1.0     # 1.0 = Normal, 1.5 = Ramadan/Eid rush
    ) -> schemas.ReplenishmentResponse:
        products = db.query(models.Product).filter(models.Product.is_active == True).all()
        suppliers = {s.supplier_id: s for s in db.query(models.Supplier).all()}
        default_supplier = list(suppliers.values())[0] if suppliers else None

        items: List[schemas.ReplenishmentItem] = []
        breached_count = 0

        for p in products:
            # Calculate current total available stock
            current_stock = (
                db.query(func.coalesce(func.sum(models.InventoryBatch.current_quantity), 0))
                .filter(
                    models.InventoryBatch.product_id == p.product_id,
                    models.InventoryBatch.status == models.BatchStatus.AVAILABLE,
                    models.InventoryBatch.expiry_date >= date.today()
                )
                .scalar()
            )

            # Match supplier
            sup = default_supplier
            lead_time = sup.lead_time_days if sup else 3
            lead_std = sup.lead_time_std_dev_days if sup else 0.5

            d_mean = p.daily_demand_mean * festival_multiplier
            d_std = p.daily_demand_std_dev * math.sqrt(festival_multiplier)

            # Greasley's Statistical Safety Stock formula factoring dual variances:
            # SS = Z * sqrt( (L * sigma_d^2) + (d^2 * sigma_L^2) )
            variance_demand_term = lead_time * (d_std ** 2)
            variance_lead_term = (d_mean ** 2) * (lead_std ** 2)
            greasley_ss = math.ceil(service_level_z_score * math.sqrt(variance_demand_term + variance_lead_term))

            # Dynamic Reorder Point: ROP = (d_mean * lead_time) + SS
            dynamic_rop = math.ceil((d_mean * lead_time) + greasley_ss)

            # Wilson Economic Order Quantity: EOQ = sqrt( (2 * D * S) / H )
            annual_demand = d_mean * 365
            order_cost_s = 650.0 # Standard BDT per PO placement
            holding_cost_h = max(p.unit_cost_bdt * 0.18, 5.0) # 18% annual capital & storage carrying cost
            eoq_qty = math.ceil(math.sqrt((2 * annual_demand * order_cost_s) / holding_cost_h))

            is_breached = current_stock <= dynamic_rop
            if is_breached:
                breached_count += 1

            items.append(
                schemas.ReplenishmentItem(
                    product_id=p.product_id,
                    sku_code=p.sku_code,
                    product_name=p.product_name,
                    category=p.category.value if hasattr(p.category, "value") else str(p.category),
                    current_stock=current_stock,
                    daily_demand_mean=round(d_mean, 1),
                    daily_demand_std_dev=round(d_std, 2),
                    lead_time_days=lead_time,
                    lead_time_std_dev=lead_std,
                    greasley_safety_stock=greasley_ss,
                    reorder_point=dynamic_rop,
                    eoq_suggested_order_qty=eoq_qty,
                    is_breached=is_breached,
                    supplier_id=sup.supplier_id if sup else 1,
                    supplier_name=sup.company_name if sup else "Central SCM",
                    unit_cost_bdt=p.unit_cost_bdt,
                    estimated_po_cost_bdt=round(eoq_qty * p.unit_cost_bdt, 2)
                )
            )

        # Sort breached items to top
        items.sort(key=lambda x: (not x.is_breached, x.current_stock - x.reorder_point))

        return schemas.ReplenishmentResponse(
            service_level_z_score=service_level_z_score,
            festival_multiplier=festival_multiplier,
            total_skus_evaluated=len(products),
            breached_skus_count=breached_count,
            items=items
        )
