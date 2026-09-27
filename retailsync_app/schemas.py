from datetime import date, datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# User & Auth
class LoginRequest(BaseModel):
    username_or_email: str
    password: str

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    full_name: str
    role: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in_seconds: int
    user: UserResponse

# Product & Inventory
class ProductResponse(BaseModel):
    product_id: int
    sku_code: str
    barcode: str
    product_name: str
    category: str
    temp_required: str
    unit_of_measure: str
    unit_cost_bdt: float
    selling_price_bdt: float
    min_safety_stock: int
    max_stock_capacity: int
    reorder_point: int
    daily_demand_mean: float
    daily_demand_std_dev: float
    shelf_life_days: int
    total_available_stock: Optional[int] = 0

    class Config:
        from_attributes = True

class BatchResponse(BaseModel):
    batch_id: int
    lot_number: str
    product_id: int
    bin_id: Optional[int]
    bin_code: Optional[str] = None
    current_quantity: int
    manufacturing_date: date
    expiry_date: date
    unit_cost_bdt: float
    status: str
    days_to_expiry: Optional[int] = None

    class Config:
        from_attributes = True

# POS Checkout & Concurrency
class PosItemRequest(BaseModel):
    barcode: str
    quantity: int = Field(gt=0, description="Quantity to checkout")

class PosCheckoutRequest(BaseModel):
    branch_code: str = "BR-DHANMONDI-01"
    payment_method: str = "CASH" # CASH, BKASH, CARD
    items: List[PosItemRequest]

class PosAllocatedItem(BaseModel):
    product_id: int
    product_name: str
    sku_code: str
    barcode: str
    batch_id: int
    lot_number: str
    expiry_date: str
    quantity: int
    unit_price_bdt: float
    subtotal_bdt: float

class PosCheckoutResponse(BaseModel):
    receipt_number: str
    transaction_time: str
    branch_code: str
    cashier_name: str
    total_amount_bdt: float
    payment_method: str
    latency_ms: float
    allocated_items: List[PosAllocatedItem]

# Inbound Receiving
class InboundReceiveItem(BaseModel):
    product_id: int
    lot_number: str
    manufacturing_date: date
    expiry_date: date
    quantity_received: int
    damaged_quantity: int = 0
    unit_cost_bdt: float

class InboundReceiveRequest(BaseModel):
    po_id: int
    notes: Optional[str] = "Normal delivery inspection"
    items: List[InboundReceiveItem]

class InboundReceiveResponse(BaseModel):
    grn_number: str
    po_id: int
    received_at: str
    total_cartons_received: int
    created_batches_count: int
    status: str

# Putaway
class PutawaySuggestRequest(BaseModel):
    batch_id: int

class PutawaySuggestResponse(BaseModel):
    batch_id: int
    lot_number: str
    product_name: str
    temp_category: str
    suggested_bin_id: int
    suggested_bin_code: str
    aisle: str
    rack: str
    shelf: int
    bin_position: int
    reason: str

class PutawayConfirmRequest(BaseModel):
    batch_id: int
    bin_id: int

# Replenishment & Decision Support System (DSS)
class ReplenishmentItem(BaseModel):
    product_id: int
    sku_code: str
    product_name: str
    category: str
    current_stock: int
    daily_demand_mean: float
    daily_demand_std_dev: float
    lead_time_days: int
    lead_time_std_dev: float
    greasley_safety_stock: int
    reorder_point: int
    eoq_suggested_order_qty: int
    is_breached: bool
    supplier_id: int
    supplier_name: str
    unit_cost_bdt: float
    estimated_po_cost_bdt: float

class ReplenishmentResponse(BaseModel):
    service_level_z_score: float
    festival_multiplier: float
    total_skus_evaluated: int
    breached_skus_count: int
    items: List[ReplenishmentItem]

class CreatePurchaseOrderRequest(BaseModel):
    supplier_id: int
    items: List[Dict[str, Any]] # product_id, quantity, unit_cost_bdt

# Warehouse Spatial Map
class BinGridItem(BaseModel):
    bin_id: int
    bin_code: str
    zone_code: str
    temp_category: str
    aisle_number: str
    rack_number: str
    shelf_tier: int
    bin_position: int
    is_occupied: bool
    current_weight_kg: float
    max_weight_kg: float
    batches_count: int
    nearest_expiry_days: Optional[int] = None
    items_summary: str = "Empty"

class WarehouseGridResponse(BaseModel):
    total_bins: int
    occupied_bins: int
    ambient_bins: int
    chilled_bins: int
    frozen_bins: int
    grid: List[BinGridItem]
