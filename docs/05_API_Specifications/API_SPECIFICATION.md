# REST API Specification & Contract

## RetailSync: Centralized Super Shop Warehouse Management System
**Subtitle:** RESTful OpenAPI 3.1 Aligned Endpoint Contracts, Data Schemas, and Response Envelopes  
**Course:** SE-231 (Software System Analysis & Design / Capstone Project 2)  
**Academic Institution:** Daffodil International University (DIU), Department of Software Engineering  
**Author:** Raisul Islam Likhon (Section: SWE-44D)  
**Date:** September 2026 | Version: 1.0.0-RELEASE  

---

## 1. Global API Conventions & Protocol Standards

### 1.1 Base URLs
* **Local Development:** `http://localhost:8000/api/v1`
* **Staging / Demonstration:** `https://staging-api.retailsync.com/api/v1`
* **Production Cluster:** `https://api.retailsync.com/api/v1`

### 1.2 Common HTTP Request Headers
```http
Authorization: Bearer <JWT_ACCESS_TOKEN>
Content-Type: application/json
Accept: application/json
X-Client-Version: 1.0.0
X-Idempotency-Key: e4b2d184-7832-4e92-9844-329810a911ab  (Mandatory for write/deduction endpoints)
```

### 1.3 Standard JSON Response Envelope
Every API response adheres to a predictable, strongly-typed envelope:

#### Success Response Envelope (HTTP 200 / 201)
```json
{
  "success": true,
  "status_code": 200,
  "data": { ... },
  "metadata": {
    "timestamp": "2026-09-27T17:15:00.124Z",
    "request_id": "req-98412-a1",
    "processing_time_ms": 18.4
  }
}
```

#### Error Response Envelope (HTTP 4xx / 5xx)
```json
{
  "success": false,
  "status_code": 409,
  "error": {
    "code": "STOCKOUT_ERROR",
    "message": "Requested quantity exceeds available unallocated stock for SKU.",
    "field": "quantity",
    "details": {
      "sku_code": "SKU-MILK-1L",
      "requested_qty": 5,
      "available_qty": 2
    }
  },
  "metadata": {
    "timestamp": "2026-09-27T17:15:00.180Z",
    "request_id": "req-98412-a2"
  }
}
```

---

## 2. API Endpoints by Domain Module

### 2.1 Module M-01: Authentication & Access Control

#### `POST /auth/login`
Authenticates a user and issues dual JWT tokens.
* **Access:** Public
* **Request Body:**
```json
{
  "username_or_email": "cashier.dhanmondi",
  "password": "Password123!"
}
```
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "user": {
      "user_id": 6,
      "username": "cashier.dhanmondi",
      "full_name": "Nusrat Jahan",
      "role": "OPERATOR"
    },
    "tokens": {
      "access_token": "eyJhbGciOiJIUzI1NiIs...",
      "token_type": "Bearer",
      "expires_in_seconds": 900
    }
  }
}
```
*(Refresh token is simultaneously dispatched in a secure `Set-Cookie: refresh_token=...; HttpOnly; Secure; SameSite=Strict` header).*

#### `POST /auth/refresh`
Rotates and issues a new access token using the valid HttpOnly refresh cookie.

---

### 2.2 Module M-02: Product Master & Barcode Interrogation

#### `GET /products/barcode/{barcode_ean}`
Instant sub-millisecond barcode lookup for handheld scanners and POS registers.
* **Access:** All Roles (`OPERATOR`, `CLERK`, `SUPERVISOR`, `PROCUREMENT`, `STORE_MANAGER`, `ADMIN`)
* **Path Parameter:** `barcode_ean` (e.g., `8941100234123`)
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "product_id": 1,
    "sku_code": "SKU-SOIL-1L",
    "barcode_ean": "8941100234123",
    "product_name": "Bashundhara Fortified Soyabean Oil 1L Bottle",
    "category": "FMCG_DRY",
    "storage_temp": "AMBIENT",
    "unit_of_measure": "BOTTLE",
    "unit_cost": 175.00,
    "total_on_hand_stock": 2150,
    "total_allocated_stock": 120,
    "available_to_promise": 2030,
    "active_batches_count": 2
  }
}
```

---

### 2.3 Module M-04: Inbound Receiving & Digital GRN

#### `POST /inbound/verify-scan`
Validates an incoming carton/pallet barcode against an open Purchase Order.
* **Access:** `CLERK`, `SUPERVISOR`, `ADMIN`
* **Request Body:**
```json
{
  "po_id": 1,
  "barcode_ean": "8941122450012",
  "batch_lot_number": "LOT-MILK-2026-0927",
  "mfg_date": "2026-09-27",
  "expiry_date": "2026-10-07",
  "scanned_quantity": 50
}
```
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "verification_status": "ACCEPTED",
    "product_name": "Milk Vita Pasteurized Liquid Milk 1L Pouch",
    "remaining_shelf_life_days": 10,
    "remaining_shelf_life_percentage": 100.0,
    "po_progress": {
      "ordered_quantity": 200,
      "previously_scanned": 100,
      "currently_scanned": 50,
      "remaining_expected": 50
    }
  }
}
```

#### `POST /inbound/grn/complete`
Commits the final Goods Receipt Note (GRN) into the ACID database.
* **Access:** `CLERK`, `SUPERVISOR`, `ADMIN`
* **Request Body:**
```json
{
  "po_id": 1,
  "supplier_invoice_ref": "INV-MV-8912",
  "notes": "Delivered on refrigerated truck Chilled temp 3.2C",
  "items": [
    {
      "product_id": 2,
      "batch_lot_number": "LOT-MILK-2026-0927",
      "location_id": 4,
      "mfg_date": "2026-09-27",
      "expiry_date": "2026-10-07",
      "accepted_quantity": 196,
      "damaged_quantity": 4,
      "damage_reason": "LEAKING_POUCH"
    }
  ]
}
```
* **Response (HTTP 201 Created):**
```json
{
  "success": true,
  "data": {
    "grn_id": 4,
    "grn_number": "GRN-2026-0004",
    "po_number": "PO-2026-0001",
    "total_accepted": 196,
    "total_damaged": 4,
    "credit_note_advisory_bdt": 360.00,
    "status": "COMPLETED",
    "timestamp": "2026-09-27T17:22:15Z"
  }
}
```

---

### 2.4 Module M-05: Directed Spatial Putaway

#### `POST /locations/putaway-recommendation`
Calculates optimal bin destination for a newly received pallet based on SKU velocity and temperature constraints.
* **Access:** `OPERATOR`, `CLERK`, `SUPERVISOR`
* **Request Body:**
```json
{
  "product_id": 2,
  "quantity": 196
}
```
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "recommended_location": {
      "location_id": 4,
      "zone_code": "ZONE-CHILL",
      "aisle_number": "A01",
      "rack_number": "R01",
      "shelf_tier": "S1",
      "bin_barcode": "BIN-CHL-A01-R01-S1-B01",
      "available_capacity_units": 252,
      "reason": "Chilled temperature match; Velocity Class-A closest to dispatch dock."
    }
  }
}
```

---

### 2.5 POS Synchronization: Real-Time Atomic Stock Deduction

#### `POST /pos/sync`
**CRITICAL SLA:** $\le 2.0$ seconds total round-trip (p95 $\le 800$ ms). Executes atomic row-level locking on earliest active FEFO batch.
* **Access:** Authorized POS Registers / Cashiers
* **Headers:** `X-Idempotency-Key: <UUIDv4>`
* **Request Body:**
```json
{
  "register_code": "POS-DHN-01",
  "receipt_number": "REC-DHN-2026-89142",
  "cashier_user_id": 6,
  "line_items": [
    {
      "barcode_ean": "8941122450012",
      "quantity": 2
    },
    {
      "barcode_ean": "8941100234123",
      "quantity": 1
    }
  ]
}
```
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "transaction_id": 14920,
    "sync_status": "CONFIRMED",
    "processed_items": [
      {
        "sku_code": "SKU-MILK-1L",
        "deducted_qty": 2,
        "batch_used": "LOT-MILK-2026-0925",
        "batch_expiry": "2026-10-01",
        "remaining_batch_qty": 46
      },
      {
        "sku_code": "SKU-SOIL-1L",
        "deducted_qty": 1,
        "batch_used": "LOT-SOIL-2026-08A",
        "batch_expiry": "2027-08-01",
        "remaining_batch_qty": 949
      }
    ],
    "execution_time_ms": 32.1
  }
}
```

#### `POST /pos/bulk-sync`
Bulk endpoint invoked by POS clients upon recovering from internet network outages.
* **Request Body:** An array of buffered sale transactions with client timestamps.
* **Response (HTTP 200 OK):** Itemizes committed transactions and flags any reconciliation discrepancies.

---

### 2.6 Module M-07: Replenishment & Decision Support Engine (DSS)

#### `GET /replenishment/calculate-eoq/{product_id}`
Computes dynamic Economic Order Quantity and Greasley's Statistical Safety Stock using live parameters.
* **Access:** `PROCUREMENT`, `SUPERVISOR`, `ADMIN`
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "product_id": 1,
    "sku_code": "SKU-SOIL-1L",
    "annual_demand_D": 24000,
    "fixed_order_cost_S": 1200.00,
    "annual_holding_cost_H": 18.00,
    "calculated_eoq_units": 1789,
    "greasley_safety_stock": {
      "average_daily_demand_d": 65.75,
      "demand_std_dev_sigma_d": 12.00,
      "average_lead_time_days_L": 7.00,
      "lead_time_std_dev_sigma_L": 1.50,
      "service_level_target": "95%",
      "z_score": 1.65,
      "safety_stock_units": 174
    },
    "reorder_point_rop": 634,
    "current_inventory_position": 610,
    "replenishment_status": "REORDER_TRIGGERED"
  }
}
```

---

### 2.7 Module M-09: Cycle Counting & Anomaly Detection

#### `POST /audit/cycle-count/submit`
Submits blind physical count entries from warehouse floor workers.
* **Access:** `OPERATOR`, `SUPERVISOR`
* **Request Body:**
```json
{
  "count_id": 1,
  "counts": [
    {
      "product_id": 1,
      "location_id": 1,
      "physical_counted_qty": 948
    }
  ]
}
```
* **Response (HTTP 200 OK):**
```json
{
  "success": true,
  "data": {
    "count_id": 1,
    "items_reconciled": 1,
    "discrepancies_found": 1,
    "variance_summary": [
      {
        "sku_code": "SKU-SOIL-1L",
        "expected_qty": 950,
        "counted_qty": 948,
        "variance": -2,
        "discrepancy_value_bdt": -350.00,
        "requires_supervisor_approval": true
      }
    ]
  }
}
```
