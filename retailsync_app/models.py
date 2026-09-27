import enum
from datetime import datetime, timezone
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, Date, ForeignKey, Enum, Text, Index
)
from sqlalchemy.orm import relationship
from retailsync_app.database import Base

# Enums aligned with 3NF database design
class UserRole(str, enum.Enum):
    OPERATOR = "OPERATOR"
    CLERK = "CLERK"
    SUPERVISOR = "SUPERVISOR"
    PROCUREMENT = "PROCUREMENT"
    STORE_MANAGER = "STORE_MANAGER"
    ADMIN = "ADMIN"

class ProductCategory(str, enum.Enum):
    FMCG_DRY = "FMCG_DRY"
    PERISHABLE_PRODUCE = "PERISHABLE_PRODUCE"
    DAIRY_CHILLED = "DAIRY_CHILLED"
    FROZEN_FOODS = "FROZEN_FOODS"
    HOUSEHOLD_NONFOOD = "HOUSEHOLD_NONFOOD"

class StorageTempCategory(str, enum.Enum):
    AMBIENT = "AMBIENT"
    AIR_CONDITIONED = "AIR_CONDITIONED"
    CHILLED_COLD = "CHILLED_COLD"
    DEEP_FROZEN = "DEEP_FROZEN"

class BatchStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    QUARANTINED = "QUARANTINED"
    EXPIRED = "EXPIRED"
    DEPLETED = "DEPLETED"

class POStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    ISSUED = "ISSUED"
    PARTIAL_RECEIVED = "PARTIAL_RECEIVED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class TransactionType(str, enum.Enum):
    INBOUND_GRN = "INBOUND_GRN"
    DIRECTED_PUTAWAY = "DIRECTED_PUTAWAY"
    POS_SALE_FEFO = "POS_SALE_FEFO"
    STORE_DISPATCH = "STORE_DISPATCH"
    DAMAGE_QUARANTINE = "DAMAGE_QUARANTINE"
    CYCLE_COUNT_ADJUSTMENT = "CYCLE_COUNT_ADJUSTMENT"
    SUPPLIER_RETURN = "SUPPLIER_RETURN"


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.OPERATOR)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_login_at = Column(DateTime, nullable=True)

    pos_transactions = relationship("PosTransaction", back_populates="cashier")
    stock_ledger_entries = relationship("StockLedger", back_populates="user")


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(150), nullable=False, index=True)
    trade_license_no = Column(String(80), unique=True, nullable=True)
    contact_person = Column(String(100), nullable=True)
    phone = Column(String(30), nullable=False)
    email = Column(String(100), nullable=True)
    lead_time_days = Column(Integer, nullable=False, default=3)
    lead_time_std_dev_days = Column(Float, nullable=False, default=0.5)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")


class WarehouseZone(Base):
    __tablename__ = "warehouse_zones"

    zone_id = Column(Integer, primary_key=True, index=True)
    zone_code = Column(String(20), unique=True, nullable=False)
    zone_name = Column(String(100), nullable=False)
    temp_category = Column(Enum(StorageTempCategory), nullable=False, default=StorageTempCategory.AMBIENT)
    target_temp_celsius = Column(Float, nullable=False, default=24.0)

    bins = relationship("WarehouseBin", back_populates="zone")


class WarehouseBin(Base):
    __tablename__ = "warehouse_bins"

    bin_id = Column(Integer, primary_key=True, index=True)
    bin_code = Column(String(30), unique=True, nullable=False, index=True)
    zone_id = Column(Integer, ForeignKey("warehouse_zones.zone_id"), nullable=False)
    aisle_number = Column(String(10), nullable=False)
    rack_number = Column(String(10), nullable=False)
    shelf_tier = Column(Integer, nullable=False)
    bin_position = Column(Integer, nullable=False)
    max_weight_kg = Column(Float, nullable=False, default=500.0)
    max_volume_m3 = Column(Float, nullable=False, default=1.5)
    current_weight_kg = Column(Float, nullable=False, default=0.0)
    current_volume_m3 = Column(Float, nullable=False, default=0.0)
    is_active = Column(Boolean, nullable=False, default=True)
    is_occupied = Column(Boolean, nullable=False, default=False)

    zone = relationship("WarehouseZone", back_populates="bins")
    batches = relationship("InventoryBatch", back_populates="bin")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    sku_code = Column(String(50), unique=True, nullable=False, index=True)
    barcode = Column(String(60), unique=True, nullable=False, index=True)
    product_name = Column(String(180), nullable=False, index=True)
    category = Column(Enum(ProductCategory), nullable=False, default=ProductCategory.FMCG_DRY)
    temp_required = Column(Enum(StorageTempCategory), nullable=False, default=StorageTempCategory.AMBIENT)
    unit_of_measure = Column(String(20), nullable=False, default="PCS")
    unit_cost_bdt = Column(Float, nullable=False)
    selling_price_bdt = Column(Float, nullable=False)
    min_safety_stock = Column(Integer, nullable=False, default=20)
    max_stock_capacity = Column(Integer, nullable=False, default=500)
    reorder_point = Column(Integer, nullable=False, default=50)
    daily_demand_mean = Column(Float, nullable=False, default=15.0)
    daily_demand_std_dev = Column(Float, nullable=False, default=3.5)
    shelf_life_days = Column(Integer, nullable=False, default=365)
    is_active = Column(Boolean, nullable=False, default=True)

    batches = relationship("InventoryBatch", back_populates="product")
    po_items = relationship("PurchaseOrderItem", back_populates="product")
    pos_items = relationship("PosTransactionItem", back_populates="product")


class InventoryBatch(Base):
    __tablename__ = "inventory_batches"

    batch_id = Column(Integer, primary_key=True, index=True)
    lot_number = Column(String(60), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False, index=True)
    bin_id = Column(Integer, ForeignKey("warehouse_bins.bin_id"), nullable=True, index=True)
    initial_quantity = Column(Integer, nullable=False)
    current_quantity = Column(Integer, nullable=False)
    manufacturing_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=False, index=True) # Essential for FEFO queries
    unit_cost_bdt = Column(Float, nullable=False)
    status = Column(Enum(BatchStatus), nullable=False, default=BatchStatus.AVAILABLE, index=True)
    grn_number = Column(String(60), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    product = relationship("Product", back_populates="batches")
    bin = relationship("WarehouseBin", back_populates="batches")
    pos_items = relationship("PosTransactionItem", back_populates="batch")
    stock_ledger_entries = relationship("StockLedger", back_populates="batch")


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    po_id = Column(Integer, primary_key=True, index=True)
    po_number = Column(String(50), unique=True, nullable=False, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), nullable=False)
    order_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    expected_delivery_date = Column(Date, nullable=False)
    status = Column(Enum(POStatus), nullable=False, default=POStatus.ISSUED)
    total_amount_bdt = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    supplier = relationship("Supplier", back_populates="purchase_orders")
    items = relationship("PurchaseOrderItem", back_populates="purchase_order", cascade="all, delete-orphan")
    grns = relationship("GoodsReceiptNote", back_populates="purchase_order")


class PurchaseOrderItem(Base):
    __tablename__ = "purchase_order_items"

    item_id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.po_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    ordered_quantity = Column(Integer, nullable=False)
    received_quantity = Column(Integer, nullable=False, default=0)
    unit_cost_bdt = Column(Float, nullable=False)
    subtotal_bdt = Column(Float, nullable=False)

    purchase_order = relationship("PurchaseOrder", back_populates="items")
    product = relationship("Product", back_populates="po_items")


class GoodsReceiptNote(Base):
    __tablename__ = "goods_receipt_notes"

    grn_id = Column(Integer, primary_key=True, index=True)
    grn_number = Column(String(50), unique=True, nullable=False, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.po_id"), nullable=False)
    receiving_clerk_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    received_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    total_cartons_received = Column(Integer, nullable=False, default=0)
    status = Column(String(30), nullable=False, default="COMPLETED")
    notes = Column(Text, nullable=True)

    purchase_order = relationship("PurchaseOrder", back_populates="grns")
    clerk = relationship("User")


class PosTransaction(Base):
    __tablename__ = "pos_transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    receipt_number = Column(String(60), unique=True, nullable=False, index=True)
    cashier_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    branch_code = Column(String(30), nullable=False, default="BR-DHANMONDI-01")
    transaction_time = Column(DateTime, default=lambda: datetime.now(timezone.utc), index=True)
    total_amount_bdt = Column(Float, nullable=False)
    payment_method = Column(String(30), nullable=False, default="CASH") # CASH, BKASH, CARD
    latency_ms = Column(Float, nullable=False, default=120.0)

    cashier = relationship("User", back_populates="pos_transactions")
    items = relationship("PosTransactionItem", back_populates="transaction", cascade="all, delete-orphan")


class PosTransactionItem(Base):
    __tablename__ = "pos_transaction_items"

    item_id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("pos_transactions.transaction_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    batch_id = Column(Integer, ForeignKey("inventory_batches.batch_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price_bdt = Column(Float, nullable=False)
    subtotal_bdt = Column(Float, nullable=False)

    transaction = relationship("PosTransaction", back_populates="items")
    product = relationship("Product", back_populates="pos_items")
    batch = relationship("InventoryBatch", back_populates="pos_items")


class StockLedger(Base):
    __tablename__ = "stock_ledger"

    ledger_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False, index=True)
    batch_id = Column(Integer, ForeignKey("inventory_batches.batch_id"), nullable=False, index=True)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    quantity_change = Column(Integer, nullable=False) # e.g. -2 for sale, +50 for GRN
    previous_balance = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), index=True)
    reference_number = Column(String(80), nullable=True) # e.g. POS receipt or GRN
    notes = Column(Text, nullable=True)

    product = relationship("Product")
    batch = relationship("InventoryBatch", back_populates="stock_ledger_entries")
    user = relationship("User", back_populates="stock_ledger_entries")


class CycleCount(Base):
    __tablename__ = "cycle_counts"

    audit_id = Column(Integer, primary_key=True, index=True)
    audit_code = Column(String(50), unique=True, nullable=False)
    scheduled_date = Column(Date, nullable=False)
    supervisor_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    status = Column(String(30), nullable=False, default="OPEN") # OPEN, RECONCILED
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    items = relationship("CycleCountItem", back_populates="cycle_count", cascade="all, delete-orphan")


class CycleCountItem(Base):
    __tablename__ = "cycle_count_items"

    item_id = Column(Integer, primary_key=True, index=True)
    audit_id = Column(Integer, ForeignKey("cycle_counts.audit_id"), nullable=False)
    bin_id = Column(Integer, ForeignKey("warehouse_bins.bin_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    expected_quantity = Column(Integer, nullable=False)
    counted_quantity = Column(Integer, nullable=False)
    variance_quantity = Column(Integer, nullable=False)
    reason_code = Column(String(50), nullable=True) # SPOILAGE, THEFT, MISPLACED, DAMAGED
    is_resolved = Column(Boolean, nullable=False, default=False)

    cycle_count = relationship("CycleCount", back_populates="items")
    bin = relationship("WarehouseBin")
    product = relationship("Product")
