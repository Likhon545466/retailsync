from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from retailsync_app.database import get_db
from retailsync_app import models, schemas, auth
from retailsync_app.services.inventory_service import InventoryService
from retailsync_app.services.audit_service import AuditService

router = APIRouter(prefix="/putaway", tags=["Directed Putaway"])

@router.get("/unallocated-batches")
def get_unallocated_batches(db: Session = Depends(get_db)):
    return AuditService.get_unallocated_batches(db)

@router.get("/suggest/{batch_id}", response_model=schemas.PutawaySuggestResponse)
def suggest_putaway_bin(batch_id: int, db: Session = Depends(get_db)):
    return InventoryService.suggest_putaway_bin(db, batch_id)

@router.post("/confirm")
def confirm_putaway(
    request: schemas.PutawayConfirmRequest,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user_optional)
):
    if not user:
        user = db.query(models.User).filter(models.User.username == "operator").first()
    return InventoryService.confirm_putaway(db, request.batch_id, request.bin_id, user)
