from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from retailsync_app.database import get_db
from retailsync_app import models, schemas, auth
from retailsync_app.services.inbound_service import InboundService

router = APIRouter(prefix="/inbound", tags=["Inbound Dock Receiving"])

@router.get("/open-pos")
def get_open_purchase_orders(db: Session = Depends(get_db)):
    return InboundService.get_open_purchase_orders(db)

@router.post("/receive", response_model=schemas.InboundReceiveResponse)
def receive_shipment(
    request: schemas.InboundReceiveRequest,
    db: Session = Depends(get_db),
    user: models.User = Depends(auth.get_current_user_optional)
):
    if not user:
        user = db.query(models.User).filter(models.User.username == "clerk").first()
    return InboundService.receive_goods(db, user, request)
