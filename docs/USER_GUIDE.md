# RetailSync WMS — Master User Guide & Operational Manual
**Author:** Raisul Islam Likhon, Shottobroto Dey, Golam Husnain Papon  
**Institution:** Daffodil International University (SWE-44D Capstone)  
**Version:** 2.0 Enterprise Release  
**System Target:** Supermarket & Warehouse Unified Operating System  

---

## Table of Contents
1. [Chapter 1: System Overview & Architecture](#chapter-1-system-overview--architecture)
2. [Chapter 2: Hardware Architecture & Peripherals](#chapter-2-hardware-architecture--peripherals)
3. [Chapter 3: Teammate Personas & Role Switcher](#chapter-3-teammate-personas--role-switcher)
4. [Chapter 4: Overview Dashboard & Command Center](#chapter-4-overview-dashboard--command-center)
5. [Chapter 5: Frontline Touch Point of Sale (POS)](#chapter-5-frontline-touch-point-of-sale-pos)
6. [Chapter 6: Inbound Receiving Dock & Quality Gates](#chapter-6-inbound-receiving-dock--quality-gates)
7. [Chapter 7: Directed Spatial Putaway & FEFO Slotting](#chapter-7-directed-spatial-putaway--fefo-slotting)
8. [Chapter 8: 2D & 3D Interactive Warehouse Digital Twin](#chapter-8-2d--3d-interactive-warehouse-digital-twin)
9. [Chapter 9: Replenishment DSS Optimizer & Forecasting](#chapter-9-replenishment-dss-optimizer--forecasting)
10. [Chapter 10: Immutable Stock Ledger & Multi-Gate Audits](#chapter-10-immutable-stock-ledger--multi-gate-audits)
11. [Chapter 11: Keyboard Shortcuts & Power Operator Cheatsheet](#chapter-11-keyboard-shortcuts--power-operator-cheatsheet)
12. [Chapter 12: Troubleshooting, Offline Mode & Resilience](#chapter-12-troubleshooting-offline-mode--resilience)

---

## Chapter 1: System Overview & Architecture

RetailSync is a real-time, hybrid Warehouse Management System (WMS) and Point of Sale (POS) engineered specifically for fast-moving consumer goods (FMCG) and perishable grocery retail in Bangladesh.

### Core Architectural Invariants
* **Strict First-Expired, First-Out (FEFO) Enforcement**: Perishable batches (such as dairy, fresh poultry, produce) are sorted chronologically by expiry date. Frontline POS automatically deducts inventory from the earliest expiring available batch.
* **Atomic Double-Entry Stock Ledger**: Every movement—whether dock receiving, bin relocation, or customer POS checkout—records an immutable row in the `stock_ledger` table with verifiable audit numbers (`WO-XXXX`, `POS-XXXX`, `PO-XXXX`).
* **Zero Negative Stock Invariant**: Inventory quantities (`current_quantity >= 0`) can never drop below zero. Any attempt to decrement past zero raises an atomic transactional rollback.
* **Sub-2.0s SLA**: All spatial lookups, POS checkout commits, and 3D visualizer renders complete well under the corporate performance threshold.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   RETAILSYNC SYSTEM ARCHITECTURE                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   [ Client Browser / Handheld Scanner / Touch Kiosk ]                                   │
│        │                 │                       │                                     │
│        ▼ (HTTP / JSON)   ▼ (WebGL / Three.js)    ▼ (Web Audio API)                     │
│   FastAPI Web Engine   3D Digital Twin      Barcode Laser Chime                        │
│        │                                                                               │
│        ▼ (SQLAlchemy 2.0 ORM / Pydantic v2)                                            │
│   [ Business Logic Layer ]                                                             │
│    ├── POS Checkout Engine (Mushak 6.3 VAT 5% + FEFO Deductions)                       │
│    ├── Inbound Dock Quality Inspector (Temp Verification)                              │
│    ├── Directed Spatial Putaway Engine (Weight & Zone Checking)                        │
│    └── Replenishment DSS (Wilson EOQ + Greasley Safety Stock)                          │
│        │                                                                               │
│        ▼ (ACID Transactions / Row-Level Locking)                                       │
│   [ Relational Database (PostgreSQL 16 / SQLite Engine) ]                              │
│    ├── batches (lot_code, expiry_date, current_quantity)                               │
│    ├── warehouse_bins (bay, aisle, shelf_tier, weight_capacity)                        │
│    ├── stock_ledger (immutable audit log: previous_balance + delta == new_balance)     │
│    └── users (role-based credentials & security hashes)                                │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Chapter 2: Hardware Architecture & Peripherals

RetailSync is designed to operate seamlessly with standard enterprise retail peripherals without requiring external proprietary drivers.

### 1. 80mm ESC/POS Thermal Receipt Printer
* **Connection**: USB, Ethernet (TCP 9100), or Bluetooth.
* **Paper Spec**: 80mm continuous thermal paper roll.
* **Standards Compliance**: NBR Mushak 6.3 VAT regulations.
* **Print Trigger**:
  * Keyboard: `Ctrl + P` on POS Terminal.
  * Screen: Tap the green `[ Print Thermal Receipt (Ctrl+P) ]` button.
* **Receipt Elements**:
  * Store Header: `RetailSync Superstore • Dhanmondi Central`.
  * VAT Registration: `VAT Reg # 002918274-0101 • Mushak 6.3`.
  * Cashier Details: `Nusrat (Till #01)`, Invoice `#RS-88219`.
  * Itemized Breakdown: SKU, Description, Qty, Unit Price, Line Total.
  * Taxes: Subtotal, Mushak 5% VAT, Grand Total (`৳`).
  * Tender: Cash Tendered, Change Due.
  * Barcode: Code-128 graphic barcode for fast return scanning.

### 2. 4"x2" Warehouse Shelf Barcode Label Printer
* **Connection**: Zebra ZPL / TSC TSPL / Generic Raster Printer.
* **Media**: 4-inch by 2-inch adhesive roll labels.
* **Location**: Warehouse receiving docks and forklift mobile carts.
* **Print Trigger**: In `/warehouse`, select any occupied bin and click `[ Print Bin Barcode Label ]`.
* **Label Contents**:
  * Spatial Coordinate: `BAY A-01 • TIER 02 • SLOT 01`.
  * Product Name: Normalized product description (e.g. `Milk Vita Liquid Milk 1L`).
  * Lot & Expiry: `LOT-MV-260901 • Exp: 28-SEP-2026`.
  * Machine-Readable Barcode: High-density Code-128 barcode.
  * Temperature Badge: `Chiller: 2°C - 4°C` or `Ambient: 20°C - 25°C`.

### 3. Handheld Barcode Scanners
* **Types**: 1D Laser (Honeywell, Zebra) or 2D Image Imagers (Datalogic).
* **Mode**: USB HID Keyboard Wedge (auto Enter suffix `\r\n`).
* **Hardware Audio**: Handheld scanner generates hardware beeps; web interface supplements with Web Audio API chime (0KB external audio assets).

---

## Chapter 3: Teammate Personas & Role Switcher

RetailSync includes pre-configured operational personas representing the DIU software engineering team:

| Teammate | Operational Role | Key Access & Responsibilities |
|---|---|---|
| **Raisul Islam Likhon** | General Manager (Project Lead) | Complete store oversight, financial metrics, executive price markdowns, PO approvals. |
| **Shottobroto Dey** | Floor Supervisor & Auditor | Shelf stock allocation, FEFO batch inspection, stock discrepancy audits, bin labeling. |
| **Golam Husnain Papon** | Supply Chain Manager | Supplier relations, purchase orders, reorder point thresholds, dock unloading. |
| **Nusrat Jahan** | Frontline Cashier (Till #01) | Fast touchscreen checkout, barcode scanning, cash tendering, Mushak 6.3 thermal printing. |

### How to Switch Personas in 1 Click
1. **Top Navigation Bar**: In the top-right header, click any teammate avatar pill:
   * `RL (Likhon)`
   * `SD (Shottobroto)`
   * `GP (Papon)`
2. **Dashboard Roster Card**: On `/dashboard`, click any row in the **"Floor Leadership On Duty"** card.
3. **Sidebar Footer**: Click the active profile card at the bottom of the left sidebar to open the Frosted Glass Persona Modal.

---

## Chapter 4: Overview Dashboard & Command Center

The Overview Dashboard (`/dashboard`) serves as the central command cockpit.

### Key Sections:
1. **Executive Metrics Strip**:
   * Total Real-time Inventory Valuation (`৳`).
   * Active SKUs & Batches.
   * Near-Expiry FEFO Risk Count (<7 days remaining).
   * Dock Inbound Receiving Throughput.
2. **Store Manager Executive Controls Suite**:
   * Accessible by pressing `M` or clicking `[ Executive Controls ]`.
   * Fast PO Dock Approval.
   * Till Cash Drawer Reconciliation.
   * Emergency 20% Near-Expiry Markdown Authorization.
3. **Floor Leadership Roster**: Real-time team roster with 1-click persona switching.
4. **Universal Spotlight Palette (`⌘K` / `Ctrl+K`)**: Instant search across all products, batches, bays, and operational commands.

---

## Chapter 5: Frontline Touch Point of Sale (POS)

Path: `/pos` | Hotkey: `2`

### Standard Checkout Workflow:
1. **Add Products to Cart**:
   * **Barcode Scan**: Point your laser scanner at the product barcode (`SKU-MILK-1L`, `SKU-YOGURT-500`, etc.).
   * **Touch Catalog**: Tap any item in the category grid (Dairy, Bakery, Beverages, Pantry).
   * **Search Box**: Type product name or SKU.
2. **Review Automatic FEFO Allocation**:
   * The system automatically binds the cart line item to the earliest expiring lot in warehouse stock.
   * Expiry badge appears in green (safe) or yellow/red (markdown priority).
3. **Tender Payment**:
   * Enter cash amount in the `Tendered (৳)` field (e.g. `500.00`).
   * The system calculates exact change in real time.
4. **Complete Checkout**:
   * Tap `[ Complete Sale & Print Receipt ]` or press `Space`.
   * Stock ledger is instantly updated atomically.
   * 80mm ESC/POS Thermal Receipt dialog opens automatically.

---

## Chapter 6: Inbound Receiving Dock & Quality Gates

Path: `/inbound` | Hotkey: `3`

### Receiving Workflow:
1. **Select Purchase Order (PO)**: Select the pending vendor delivery from the arrival queue.
2. **Temperature & Quality Verification**:
   * For Chilled Dairy: Probe temperature must read between `2.0°C` and `4.0°C`.
   * For Frozen Goods: Probe temperature must read `<= -18.0°C`.
   * For Ambient Goods: Temperature reads normal (`20°C - 25°C`).
3. **Batch Code & Expiry Entry**:
   * Verify vendor manufacturing lot code (e.g. `LOT-MV-2610-01`).
   * Enter physical expiration date stamped on packaging.
4. **Approve Dock Gate**:
   * Tap `[ Accept & Stage for Putaway ]`.
   * Staged delivery is placed in the dock staging buffer awaiting putaway.

---

## Chapter 7: Directed Spatial Putaway & FEFO Slotting

Path: `/putaway` | Hotkey: `4`

### Putaway Rules:
* System analyzes batch storage requirements (temperature, weight, volume).
* Directed Putaway algorithm computes optimal bin:
  * Heaviest pallets routed to Lower Tiers (Tier 01).
  * High-turnover FEFO items routed to front picking aisles (`Aisle A01`, `Aisle C01`).
* Operator confirms slotting by scanning shelf barcode tag.

---

## Chapter 8: 2D & 3D Interactive Warehouse Digital Twin

Path: `/warehouse` | Hotkey: `5`

### Features:
1. **2D Spatial Rack Grid**:
   * Color-coded bays: Green (Occupied & Fresh), Yellow (Near Expiry <7d), Gray (Available/Empty).
   * Displays bay aisle, tier, current payload weight, and capacity percentage.
2. **3D WebGL Digital Twin (Three.js)**:
   * **Interactive 360° Orbit**: Left-click and drag to rotate the camera around the warehouse aisles.
   * **Zoom & Pan**: Mouse wheel to zoom; right-click and drag to pan.
   * **Preset Views**:
     * `Default Perspective` (Isometric overview).
     * `Aisle A Ambient` (Focus on dry groceries).
     * `Aisle C Chilled` (Focus on cold-chain dairy).
     * `Top Down Plan` (Birds-eye 2D layout).
   * **Interactive Click**: Click any pallet or rack in 3D to inspect its details in the side panel.
3. **Interactive Empty Shelf Putaway**:
   * Click any empty rack cell in either 2D or 3D.
   * The inspector displays the green button: `[ Put Away Stock Here (Allocate Slot) ]`.
   * Tap the button to select an inbound batch and lock it directly to that bin with 1 click.
4. **4"x2" Shelf Barcode Tag Printing**:
   * Tap `[ Print Bin Barcode Label ]` to open the printable adhesive label generator.

---

## Chapter 9: Replenishment DSS Optimizer & Forecasting

Path: `/procurement` | Hotkey: `6`

### Scientific Inventory Optimization:
* **Wilson Economic Order Quantity (EOQ)**: Calculates the order quantity that minimizes holding and order setup costs:
  $$EOQ = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$
* **Greasley Safety Stock Formula**: Protects against supplier delivery lead-time jitter:
  $$SS = Z \cdot \sigma_L \cdot \sqrt{L}$$
* **Ramadan Surge Demand Multiplier**:
  * Toggle the `🌙 Ramadan Surge (2.5x)` demand scenario to instantly recalculate replenishment thresholds for staples (edible oil, chickpeas, dates, sugar, milk).

---

## Chapter 10: Immutable Stock Ledger & Multi-Gate Audits

Path: `/audits` | Hotkey: `7`

### Audit Trail Compliance:
* Every movement is strictly recorded in `stock_ledger` with:
  * `previous_balance`
  * `quantity_delta`
  * `new_balance` (Verified formula: `previous_balance + delta == new_balance`)
  * `audit_ref` (`WO-XXXX`, `POS-XXXX`, `PO-XXXX`)
* Discrepancy Reconciliation Tool:
  * Select any SKU.
  * Enter physical cycle count observed on the shelf.
  * System records an authorized audit entry and reconciles variance.

---

## Chapter 11: Keyboard Shortcuts & Power Operator Cheatsheet

Press `?` anywhere to open the interactive keyboard cheat sheet.

| Shortcut | Description | Location |
|---|---|---|
| `⌘K` or `Ctrl + K` | Universal Spotlight & Command Palette | All Pages |
| `?` | Show Keyboard Shortcuts Cheatsheet | All Pages |
| `T` | Toggle Day / Night Color Theme | All Pages |
| `M` | Open Executive Controls Modal | All Pages (Admin) |
| `1` | Jump to Overview Dashboard (`/dashboard`) | All Pages |
| `2` | Jump to POS Terminal (`/pos`) | All Pages |
| `3` | Jump to Inbound Dock (`/inbound`) | All Pages |
| `4` | Jump to Directed Putaway (`/putaway`) | All Pages |
| `5` | Jump to Warehouse Map (`/warehouse`) | All Pages |
| `6` | Jump to Replenishment DSS (`/procurement`) | All Pages |
| `7` | Jump to Stock Ledger (`/audits`) | All Pages |
| `8` | Jump to Master User Guide (`/guide`) | All Pages |
| `Ctrl + P` | Print 80mm ESC/POS Receipt or 4"x2" Tag | POS / Warehouse |
| `Space` | Start New Sale Transaction | POS Terminal |
| `Esc` | Dismiss Open Modal / Drawer | All Pages |

---

## Chapter 12: Troubleshooting, Offline Mode & Resilience

### Offline Network Simulation:
* Click the `Cloud Synced` badge in the top bar to toggle offline mode.
* The system caches pending POS transactions in local IndexedDB.
* Upon reconnection, queued transactions synchronize with the cloud database.

### Common Questions & Solutions:
1. **Why does my cart show a different batch than what I picked?**
   * RetailSync enforces strict FEFO. The system always allocates the oldest expiry batch first to prevent grocery spoilage.
2. **How do I print a shelf barcode label?**
   * Go to `/warehouse`, click any occupied shelf bin, and click `[ Print Bin Barcode Label ]`.
3. **How do I switch to my teammate's account?**
   * Click any teammate badge in the top right (`RL`, `SD`, `GP`) or click their profile in the dashboard roster.

---
*End of Master User Guide • RetailSync WMS v2.0 Enterprise Release*
