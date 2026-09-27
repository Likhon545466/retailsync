-- ============================================================================
-- RetailSync Enterprise Relational Database Schema Blueprint & Seed Data (DDL)
-- Database Engine: PostgreSQL 16+ (ACID Compliant, 3NF Normalized)
-- Course: SE-231 (Software System Analysis & Design / Capstone Project 2)
-- Author: Raisul Islam Likhon (Section: SWE-44D)
-- Academic Institution: Daffodil International University (DIU)
-- Date: September 2026 | Version: 1.0.0-RELEASE
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 0. DATABASE EXTENSIONS
-- ----------------------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ----------------------------------------------------------------------------
-- 1. ENUMS & DOMAIN TYPES
-- ----------------------------------------------------------------------------
CREATE TYPE user_role_enum AS ENUM (
    'OPERATOR', 
    'CLERK', 
    'SUPERVISOR', 
    'PROCUREMENT', 
    'STORE_MANAGER', 
    'ADMIN'
);

CREATE TYPE product_category_enum AS ENUM (
    'FMCG_DRY', 
    'PERISHABLE_PRODUCE', 
    'DAIRY_CHILLED', 
    'FROZEN_FOODS', 
    'HOUSEHOLD_NONFOOD'
);

CREATE TYPE storage_temp_enum AS ENUM (
    'AMBIENT', 
    'AIR_CONDITIONED', 
    'CHILLED_COLD', 
    'DEEP_FROZEN'
);

CREATE TYPE batch_status_enum AS ENUM (
    'AVAILABLE', 
    'QUARANTINED', 
    'EXPIRED', 
    'DEPLETED'
);

CREATE TYPE po_status_enum AS ENUM (
    'DRAFT', 
    'PENDING_APPROVAL', 
    'ISSUED', 
    'PARTIAL_RECEIVED', 
    'COMPLETED', 
    'CANCELLED'
);

CREATE TYPE transaction_type_enum AS ENUM (
    'INBOUND_GRN', 
    'DIRECTED_PUTAWAY', 
    'POS_SALE_FEFO', 
    'STORE_DISPATCH', 
    'DAMAGE_QUARANTINE', 
    'CYCLE_COUNT_ADJUSTMENT', 
    'SUPPLIER_RETURN'
);

CREATE TYPE requisition_status_enum AS ENUM (
    'SUBMITTED', 
    'ALLOCATED', 
    'PICKING_WAVE', 
    'IN_TRANSIT', 
    'DELIVERED', 
    'RECONCILED'
);

-- ----------------------------------------------------------------------------
-- 2. TABLE DEFINITIONS (3NF NORMALIZED)
-- ----------------------------------------------------------------------------

-- 2.1 Users & Role-Based Access Control
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    role user_role_enum NOT NULL DEFAULT 'OPERATOR',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login_at TIMESTAMP WITH TIME ZONE
);

-- 2.2 Suppliers Master
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    trade_license_no VARCHAR(80) UNIQUE,
    contact_person VARCHAR(100),
    contact_email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(25) NOT NULL,
    avg_lead_time_days NUMERIC(5,2) NOT NULL DEFAULT 7.00,
    lead_time_std_dev NUMERIC(5,2) NOT NULL DEFAULT 1.50,
    payment_terms VARCHAR(50) DEFAULT 'Net 30',
    is_approved BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.3 Master Product Catalog
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    sku_code VARCHAR(50) UNIQUE NOT NULL,
    barcode_ean VARCHAR(30) UNIQUE NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    category product_category_enum NOT NULL,
    storage_temp storage_temp_enum NOT NULL DEFAULT 'AMBIENT',
    unit_of_measure VARCHAR(20) NOT NULL DEFAULT 'UNIT',
    unit_cost NUMERIC(10,2) NOT NULL CHECK (unit_cost > 0),
    holding_cost_annual NUMERIC(10,2) NOT NULL CHECK (holding_cost_annual >= 0),
    ordering_cost_fixed NUMERIC(10,2) NOT NULL CHECK (ordering_cost_fixed >= 0),
    min_shelf_life_receiving_pct NUMERIC(5,2) NOT NULL DEFAULT 75.00,
    reorder_point INT NOT NULL DEFAULT 0,
    safety_stock_threshold INT NOT NULL DEFAULT 0,
    supplier_id INT REFERENCES suppliers(supplier_id) ON DELETE RESTRICT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.4 Spatial Warehouse Location Topology
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    zone_code VARCHAR(15) NOT NULL,
    aisle_number VARCHAR(10) NOT NULL,
    rack_number VARCHAR(10) NOT NULL,
    shelf_tier VARCHAR(10) NOT NULL,
    bin_barcode VARCHAR(30) UNIQUE NOT NULL,
    capacity_units INT NOT NULL DEFAULT 300,
    capacity_kg NUMERIC(8,2) NOT NULL DEFAULT 500.00,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- 2.5 Perishable & Batch Inventory (FEFO/FIFO Engine)
CREATE TABLE product_batches (
    batch_id SERIAL PRIMARY KEY,
    batch_lot_number VARCHAR(60) UNIQUE NOT NULL,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    location_id INT NOT NULL REFERENCES locations(location_id) ON DELETE RESTRICT,
    mfg_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    initial_quantity INT NOT NULL CHECK (initial_quantity > 0),
    current_quantity INT NOT NULL CHECK (current_quantity >= 0),
    allocated_quantity INT NOT NULL DEFAULT 0 CHECK (allocated_quantity >= 0),
    quarantine_status batch_status_enum NOT NULL DEFAULT 'AVAILABLE',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_batch_quantities CHECK (allocated_quantity <= current_quantity),
    CONSTRAINT chk_mfg_before_expiry CHECK (mfg_date <= expiry_date)
);

-- 2.6 Digital Purchase Orders (PO)
CREATE TABLE purchase_orders (
    po_id SERIAL PRIMARY KEY,
    po_number VARCHAR(50) UNIQUE NOT NULL,
    supplier_id INT NOT NULL REFERENCES suppliers(supplier_id) ON DELETE RESTRICT,
    total_amount NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    status po_status_enum NOT NULL DEFAULT 'DRAFT',
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expected_delivery_date DATE NOT NULL,
    approved_by_user_id INT REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.7 Purchase Order Line Items
CREATE TABLE po_line_items (
    po_line_id SERIAL PRIMARY KEY,
    po_id INT NOT NULL REFERENCES purchase_orders(po_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    ordered_quantity INT NOT NULL CHECK (ordered_quantity > 0),
    received_quantity INT NOT NULL DEFAULT 0 CHECK (received_quantity >= 0),
    unit_price NUMERIC(10,2) NOT NULL CHECK (unit_price > 0),
    CONSTRAINT uq_po_product UNIQUE (po_id, product_id)
);

-- 2.8 Inbound Goods Receipt Notes (GRN)
CREATE TABLE goods_receipt_notes (
    grn_id SERIAL PRIMARY KEY,
    grn_number VARCHAR(50) UNIQUE NOT NULL,
    po_id INT NOT NULL REFERENCES purchase_orders(po_id) ON DELETE RESTRICT,
    supplier_invoice_ref VARCHAR(80),
    accepted_quantity INT NOT NULL DEFAULT 0,
    rejected_damaged_quantity INT NOT NULL DEFAULT 0,
    receiving_clerk_id INT NOT NULL REFERENCES users(user_id),
    notes TEXT,
    received_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.9 Immutable Inventory Transactions Audit Ledger (ACID Row-Locking)
CREATE TABLE inventory_transactions (
    transaction_id BIGSERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    batch_id INT REFERENCES product_batches(batch_id) ON DELETE RESTRICT,
    location_id INT NOT NULL REFERENCES locations(location_id) ON DELETE RESTRICT,
    transaction_type transaction_type_enum NOT NULL,
    quantity INT NOT NULL CHECK (quantity <> 0),
    reference_document_no VARCHAR(80),
    user_id INT NOT NULL REFERENCES users(user_id),
    recorded_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 2.10 Retail Branch Stores Directory
CREATE TABLE branch_stores (
    store_id SERIAL PRIMARY KEY,
    store_code VARCHAR(30) UNIQUE NOT NULL,
    store_name VARCHAR(150) NOT NULL,
    location_area VARCHAR(100) NOT NULL,
    store_manager_user_id INT REFERENCES users(user_id),
    contact_phone VARCHAR(25) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.11 Retail Branch POS Cash Registers & Sync Telemetry
CREATE TABLE pos_registers (
    register_id SERIAL PRIMARY KEY,
    register_code VARCHAR(30) UNIQUE NOT NULL,
    store_id INT NOT NULL REFERENCES branch_stores(store_id) ON DELETE RESTRICT,
    terminal_ip_mac VARCHAR(60) NOT NULL,
    is_online BOOLEAN NOT NULL DEFAULT TRUE,
    last_sync_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.12 Store Stock Requisitions
CREATE TABLE store_requisitions (
    requisition_id SERIAL PRIMARY KEY,
    requisition_no VARCHAR(50) UNIQUE NOT NULL,
    store_id INT NOT NULL REFERENCES branch_stores(store_id) ON DELETE RESTRICT,
    status requisition_status_enum NOT NULL DEFAULT 'SUBMITTED',
    required_by_date DATE NOT NULL,
    dispatch_vehicle_plate VARCHAR(30),
    submitted_by_user_id INT NOT NULL REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.13 Store Requisition Line Items
CREATE TABLE requisition_line_items (
    req_line_id SERIAL PRIMARY KEY,
    requisition_id INT NOT NULL REFERENCES store_requisitions(requisition_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    requested_qty INT NOT NULL CHECK (requested_qty > 0),
    allocated_qty INT NOT NULL DEFAULT 0,
    dispatched_qty INT NOT NULL DEFAULT 0,
    received_qty INT NOT NULL DEFAULT 0,
    CONSTRAINT uq_req_product UNIQUE (requisition_id, product_id)
);

-- 2.14 Physical Stocktaking Cycle Counts
CREATE TABLE cycle_counts (
    count_id SERIAL PRIMARY KEY,
    count_code VARCHAR(50) UNIQUE NOT NULL,
    zone_code VARCHAR(15) NOT NULL,
    scheduled_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status VARCHAR(25) NOT NULL DEFAULT 'IN_PROGRESS' CHECK (status IN ('IN_PROGRESS', 'PENDING_APPROVAL', 'COMPLETED')),
    conducted_by_user_id INT NOT NULL REFERENCES users(user_id),
    approved_by_user_id INT REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2.15 Cycle Count Items (Blind Physical Verification)
CREATE TABLE cycle_count_items (
    count_item_id SERIAL PRIMARY KEY,
    count_id INT NOT NULL REFERENCES cycle_counts(count_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    location_id INT NOT NULL REFERENCES locations(location_id) ON DELETE RESTRICT,
    system_expected_qty INT NOT NULL,  -- Masked from floor counter UI
    physical_counted_qty INT,          -- Entered blindly by counter
    variance_qty INT GENERATED ALWAYS AS (physical_counted_qty - system_expected_qty) STORED,
    discrepancy_reason VARCHAR(100),
    counted_at TIMESTAMP WITH TIME ZONE
);

-- ----------------------------------------------------------------------------
-- 3. STRATEGIC B-TREE INDEXES FOR SUB-SECOND PERFORMANCE
-- ----------------------------------------------------------------------------
CREATE INDEX idx_products_barcode ON products(barcode_ean);
CREATE INDEX idx_products_sku ON products(sku_code);
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_batches_fefo_queue ON product_batches(product_id, expiry_date ASC, quarantine_status) WHERE quarantine_status = 'AVAILABLE';
CREATE INDEX idx_batches_expiry ON product_batches(expiry_date);
CREATE INDEX idx_transactions_product_date ON inventory_transactions(product_id, recorded_at DESC);
CREATE INDEX idx_transactions_batch_id ON inventory_transactions(batch_id);
CREATE INDEX idx_locations_bin_barcode ON locations(bin_barcode);
CREATE INDEX idx_po_number ON purchase_orders(po_number);
CREATE INDEX idx_pos_registers_store ON pos_registers(store_id);

-- ----------------------------------------------------------------------------
-- 4. DATABASE INTEGRITY TRIGGERS
-- ----------------------------------------------------------------------------

-- 4.1 Enforce Immutable Append-Only Ledger (Block UPDATE & DELETE)
CREATE OR REPLACE FUNCTION prevent_transaction_modification()
RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'Security Violation: Records in inventory_transactions are immutable and cannot be updated or deleted.';
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_immutable_inventory_transactions
BEFORE UPDATE OR DELETE ON inventory_transactions
FOR EACH ROW
EXECUTE FUNCTION prevent_transaction_modification();

-- ----------------------------------------------------------------------------
-- 5. SEED DATA (AUTHENTIC BANGLADESHI SUPER SHOP DOMAIN)
-- ----------------------------------------------------------------------------

-- 5.1 System Users (Default Password: "Password123!" hashed with bcrypt)
INSERT INTO users (username, email, password_hash, full_name, role) VALUES
('likhon.admin', 'likhon@retailsync.com', '$2b$12$eX8m3Ym1d6zWz9tK2jK8OeZfQ3U8L2yE5q5K8Z7wQ3U8L2yE5q5K8', 'Raisul Islam Likhon', 'ADMIN'),
('tariqul.floor', 'tariqul@retailsync.com', '$2b$12$eX8m3Ym1d6zWz9tK2jK8OeZfQ3U8L2yE5q5K8Z7wQ3U8L2yE5q5K8', 'Tariqul Islam', 'SUPERVISOR'),
('salma.procure', 'salma@retailsync.com', '$2b$12$eX8m3Ym1d6zWz9tK2jK8OeZfQ3U8L2yE5q5K8Z7wQ3U8L2yE5q5K8', 'Salma Akter', 'PROCUREMENT'),
('clerk.dock', 'clerk@retailsync.com', '$2b$12$eX8m3Ym1d6zWz9tK2jK8OeZfQ3U8L2yE5q5K8Z7wQ3U8L2yE5q5K8', 'Rafiqul Hasan', 'CLERK'),
('operator.kamal', 'kamal@retailsync.com', '$2b$12$eX8m3Ym1d6zWz9tK2jK8OeZfQ3U8L2yE5q5K8Z7wQ3U8L2yE5q5K8', 'Kamal Hossain', 'OPERATOR'),
('cashier.dhanmondi', 'cashier1@retailsync.com', '$2b$12$eX8m3Ym1d6zWz9tK2jK8OeZfQ3U8L2yE5q5K8Z7wQ3U8L2yE5q5K8', 'Nusrat Jahan', 'OPERATOR');

-- 5.2 Suppliers (Major Bangladeshi FMCG & Dairy Brands)
INSERT INTO suppliers (company_name, trade_license_no, contact_person, contact_email, phone_number, avg_lead_time_days, lead_time_std_dev, payment_terms) VALUES
('Bashundhara Food & Beverage Ltd.', 'TL-DHK-2018-9841', 'Farhan Chowdhury', 'farhan@bashundhara.com', '+8801711223344', 7.00, 1.50, 'Net 30'),
('Milk Vita (Bangladesh Milk Producers Co-Operative)', 'TL-DHK-2015-1120', 'Aminul Islam', 'orders@milkvita.org.bd', '+8801819334455', 2.00, 0.50, 'Net 15'),
('Square Consumer Products Ltd. (Radhuni/Chashi)', 'TL-DHK-2017-4521', 'Tanvir Ahmed', 'supply@squaregroup.com', '+8801912445566', 5.00, 1.20, 'Net 30'),
('PRAN Agro Business Ltd.', 'TL-DHK-2016-8742', 'Mahmudur Rahman', 'dispatch@prangroup.com', '+8801613556677', 6.00, 1.80, 'Net 30'),
('Akij Food & Beverage Ltd.', 'TL-DHK-2019-3321', 'Saiful Karim', 'orders@akij.net', '+8801514667788', 4.00, 1.00, 'Net 15');

-- 5.3 Master Products Catalog
INSERT INTO products (sku_code, barcode_ean, product_name, category, storage_temp, unit_of_measure, unit_cost, holding_cost_annual, ordering_cost_fixed, min_shelf_life_receiving_pct, reorder_point, safety_stock_threshold, supplier_id) VALUES
('SKU-SOIL-1L', '8941100234123', 'Bashundhara Fortified Soyabean Oil 1L Bottle', 'FMCG_DRY', 'AMBIENT', 'BOTTLE', 175.00, 18.00, 1200.00, 75.00, 1218, 320, 1),
('SKU-MILK-1L', '8941122450012', 'Milk Vita Pasteurized Liquid Milk 1L Pouch', 'DAIRY_CHILLED', 'CHILLED_COLD', 'POUCH', 90.00, 22.00, 500.00, 80.00, 250, 85, 2),
('SKU-RICE-5K', '8941144781290', 'Chashi Aromatic Chinigura Rice 5kg Poly', 'FMCG_DRY', 'AMBIENT', 'BAG', 720.00, 35.00, 1500.00, 70.00, 180, 45, 3),
('SKU-SUGR-1K', '8941100341908', 'Fresh Refined White Sugar 1kg Packet', 'FMCG_DRY', 'AMBIENT', 'PACKET', 135.00, 12.00, 800.00, 85.00, 400, 110, 1),
('SKU-TURM-200G', '8941144120934', 'Radhuni Pure Turmeric Powder 200g Foil', 'FMCG_DRY', 'AMBIENT', 'FOIL', 95.00, 8.00, 450.00, 80.00, 150, 35, 3),
('SKU-YGRT-500G', '8941122901234', 'Milk Vita Sweetened Dahi (Yogurt) 500g Cup', 'DAIRY_CHILLED', 'CHILLED_COLD', 'CUP', 120.00, 28.00, 600.00, 80.00, 120, 40, 2),
('SKU-JUIC-1L', '8941155981245', 'PRAN Frooto Mango Juice 1L Tetra Pak', 'FMCG_DRY', 'AMBIENT', 'PACK', 110.00, 15.00, 700.00, 75.00, 220, 60, 4);

-- 5.4 Spatial Warehouse Locations (Tejgaon Central Distribution Center)
INSERT INTO locations (zone_code, aisle_number, rack_number, shelf_tier, bin_barcode, capacity_units, capacity_kg) VALUES
('ZONE-DRY', 'A01', 'R01', 'S1', 'BIN-DRY-A01-R01-S1-B01', 500, 800.00),
('ZONE-DRY', 'A01', 'R01', 'S2', 'BIN-DRY-A01-R01-S2-B02', 500, 800.00),
('ZONE-DRY', 'A02', 'R01', 'S1', 'BIN-DRY-A02-R01-S1-B01', 400, 600.00),
('ZONE-CHILL', 'A01', 'R01', 'S1', 'BIN-CHL-A01-R01-S1-B01', 300, 400.00),
('ZONE-CHILL', 'A01', 'R01', 'S2', 'BIN-CHL-A01-R01-S2-B02', 300, 400.00),
('ZONE-BULK', 'B01', 'R01', 'S1', 'BIN-BLK-B01-R01-S1-P01', 1000, 2000.00);

-- 5.5 Product Batches (FEFO Test Batches: Some Expiring Soon, Some Fresh)
INSERT INTO product_batches (batch_lot_number, product_id, location_id, mfg_date, expiry_date, initial_quantity, current_quantity, allocated_quantity, quarantine_status) VALUES
-- Soyabean Oil (Stable FMCG)
('LOT-SOIL-2026-08A', 1, 1, '2026-08-01', '2027-08-01', 1000, 950, 0, 'AVAILABLE'),
('LOT-SOIL-2026-09B', 1, 2, '2026-09-01', '2027-09-01', 1200, 1200, 0, 'AVAILABLE'),
-- Milk Vita (High Perishable - FEFO Test: Batch A expires in 4 days, Batch B in 10 days)
('LOT-MILK-2026-0925', 2, 4, '2026-09-25', '2026-10-01', 200, 48, 0, 'AVAILABLE'),
('LOT-MILK-2026-0927', 2, 5, '2026-09-27', '2026-10-07', 300, 300, 0, 'AVAILABLE'),
-- Sweet Dahi (Perishable Dairy)
('LOT-YGRT-2026-0920', 6, 4, '2026-09-20', '2026-10-05', 150, 35, 0, 'AVAILABLE'),
('LOT-YGRT-2026-0926', 6, 5, '2026-09-26', '2026-10-18', 200, 200, 0, 'AVAILABLE');

-- 5.6 Branch Stores
INSERT INTO branch_stores (store_code, store_name, location_area, contact_phone) VALUES
('STORE-DHK-DHN', 'Shwapno Dhanmondi Flagship Outlet', 'Road 27, Dhanmondi, Dhaka', '+8801711998877'),
('STORE-DHK-UTT', 'Shwapno Uttara Sector 3 Branch', 'Sector 3, Uttara, Dhaka', '+8801811887766'),
('STORE-DHK-GUL', 'Shwapno Gulshan 2 Express Outlet', 'Gulshan Avenue, Dhaka', '+8801911776655');

-- 5.7 POS Cash Registers
INSERT INTO pos_registers (register_code, store_id, terminal_ip_mac, is_online) VALUES
('POS-DHN-01', 1, '192.168.10.101 / 00:1A:2B:3C:4D:5E', TRUE),
('POS-DHN-02', 1, '192.168.10.102 / 00:1A:2B:3C:4D:5F', TRUE),
('POS-UTT-01', 2, '192.168.20.101 / 00:1A:2B:3C:4D:6A', TRUE),
('POS-GUL-01', 3, '192.168.30.101 / 00:1A:2B:3C:4D:7B', TRUE);

-- 5.8 Initial Sample Inbound Transactions
INSERT INTO inventory_transactions (product_id, batch_id, location_id, transaction_type, quantity, reference_document_no, user_id) VALUES
(1, 1, 1, 'INBOUND_GRN', 1000, 'GRN-2026-0001', 4),
(2, 3, 4, 'INBOUND_GRN', 200, 'GRN-2026-0002', 4),
(6, 5, 4, 'INBOUND_GRN', 150, 'GRN-2026-0003', 4);

-- End of DDL & Seed Script
