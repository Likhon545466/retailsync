import uuid
from datetime import datetime, timezone, date, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from retailsync_app.database import get_db
from retailsync_app import models, schemas, auth
from retailsync_app.services.replenishment_service import ReplenishmentService

router = APIRouter(prefix="/procurement", tags=["Procurement & Replenishment DSS"])

@router.get("/replenishment", response_model=schemas.ReplenishmentResponse)
def get_replenishment_suggestions(
    z_score: float = 1.96,
    multiplier: float = 1.0,
    db: Session = Depends(get_db)
):
    return ReplenishmentService.calculate_replenishment_recommendations(
        db, service_level_z_score=z_score, festival_multiplier=multiplier
    )

@router.post("/po/create")
def create_purchase_order(
    request: schemas.CreatePurchaseOrderRequest,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user_optional)
):
    supplier = db.query(models.Supplier).filter(models.Supplier.supplier_id == request.supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    po_number = f"PO-{datetime.now().strftime('%Y%m')}-{uuid.uuid4().hex[:4].upper()}"
    exp_delivery = date.today() + timedelta(days=supplier.lead_time_days)

    total_amt = 0.0
    po = models.PurchaseOrder(
        po_number=po_number,
        supplier_id=supplier.supplier_id,
        order_date=datetime.now(timezone.utc),
        expected_delivery_date=exp_delivery,
        status=models.POStatus.ISSUED,
        total_amount_bdt=0.0
    )
    db.add(po)
    db.flush()

    for item in request.items:
        prod = db.query(models.Product).filter(models.Product.product_id == item["product_id"]).first()
        if not prod:
            continue
        qty = item["quantity"]
        cost = item.get("unit_cost_bdt", prod.unit_cost_bdt)
        subtotal = qty * cost
        total_amt += subtotal

        po_item = models.PurchaseOrderItem(
            po_id=po.po_id,
            product_id=prod.product_id,
            ordered_quantity=qty,
            received_quantity=0,
            unit_cost_bdt=cost,
            subtotal_bdt=subtotal
        )
        db.add(po_item)

    po.total_amount_bdt = total_amt
    db.commit()

    return {
        "status": "CREATED",
        "po_id": po.po_id,
        "po_number": po.po_number,
        "supplier_name": supplier.company_name,
        "total_amount_bdt": total_amt,
        "expected_delivery_date": exp_delivery.strftime("%Y-%m-%d")
    }
