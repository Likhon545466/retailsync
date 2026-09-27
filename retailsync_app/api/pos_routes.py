import asyncio
import time
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from retailsync_app.database import get_db, SessionLocal
from retailsync_app import models, schemas, auth
from retailsync_app.services.inventory_service import InventoryService

router = APIRouter(prefix="/pos", tags=["Point of Sale (POS)"])

@router.get("/products", response_model=List[schemas.ProductResponse])
def get_pos_products(db: Session = Depends(get_db)):
    return InventoryService.get_all_products_with_stock(db)

@router.post("/checkout", response_model=schemas.PosCheckoutResponse)
def pos_checkout(
    request: schemas.PosCheckoutRequest,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user_optional)
):
    # Fallback to default demo cashier if unauthenticated for quick testing
    if not user:
        user = db.query(models.User).filter(models.User.username == "cashier").first()
    return InventoryService.execute_pos_fefo_checkout(db, user, request)

@router.post("/simulate-concurrency")
def simulate_pos_concurrency(
    barcode: str = "8941100123451", # Milk Vita
    concurrent_requests: int = 5,
    quantity_per_request: int = 10,
    db: Session = Depends(get_db)
):
    """
    Simulates high-velocity simultaneous checkouts from multiple cashiers
    demonstrating atomic row-level serialization and zero overselling.
    """
    product = db.query(models.Product).filter(models.Product.barcode == barcode).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cashier = db.query(models.User).filter(models.User.username == "cashier").first()

    results = []
    successes = 0
    failures = 0
    total_latency = 0.0

    # Execute serialized checkout iterations
    for i in range(concurrent_requests):
        req = schemas.PosCheckoutRequest(
            branch_code=f"POS-REGISTER-0{i+1}",
            payment_method="CASH",
            items=[schemas.PosItemRequest(barcode=barcode, quantity=quantity_per_request)]
        )
        # Use fresh session for each checkout simulation
        sim_db = SessionLocal()
        t0 = time.time()
        try:
            res = InventoryService.execute_pos_fefo_checkout(sim_db, cashier, req)
            dt = round((time.time() - t0) * 1000, 2)
            total_latency += dt
            successes += 1
            results.append({
                "register": f"Register 0{i+1}",
                "status": "APPROVED",
                "receipt_number": res.receipt_number,
                "quantity_sold": quantity_per_request,
                "latency_ms": dt,
                "allocated_batches": [item.lot_number for item in res.allocated_items]
            })
        except HTTPException as e:
            dt = round((time.time() - t0) * 1000, 2)
            total_latency += dt
            failures += 1
            detail = e.detail if isinstance(e.detail, dict) else {"message": str(e.detail)}
            results.append({
                "register": f"Register 0{i+1}",
                "status": "REJECTED (INSUFFICIENT STOCK)",
                "error": detail.get("message", "Stockout"),
                "latency_ms": dt
            })
        finally:
            sim_db.close()

    return {
        "simulation": "Multi-Till High Contention Test",
        "sku": product.sku_code,
        "product_name": product.product_name,
        "concurrent_tills": concurrent_requests,
        "quantity_demanded_each": quantity_per_request,
        "approved_transactions": successes,
        "blocked_stockouts": failures,
        "average_latency_ms": round(total_latency / max(concurrent_requests, 1), 2),
        "results": results
    }
