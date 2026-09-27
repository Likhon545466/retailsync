# Product Requirements Document (PRD)

## RetailSync: Centralized Super Shop Warehouse Management System
**Subtitle:** Real-Time POS Synchronization, Dynamic Putaway, FEFO Batch Tracking, and Algorithmic Replenishment  
**Course:** SE-231 (Software System Analysis & Design / Capstone Project 2)  
**Academic Institution:** Daffodil International University (DIU), Department of Software Engineering  
**Author:** Raisul Islam Likhon (Section: SWE-44D)  
**Date:** September 2026 | Version: 1.0.0-RELEASE  

---

## 1. Executive Summary & Product Vision

### 1.1 The Vision
**RetailSync** is a high-performance, centralized enterprise Warehouse Management System (WMS) purpose-built for the fast-evolving modern grocery retail and super shop sector in Bangladesh (e.g., Shwapno, Agora, Meena Bazar, Unimart, Daily Shopping). 

RetailSync bridges the destructive chasm between **central distribution centers** and **frontline retail checkout counters (POS)**. By enforcing strict Third Normal Form (3NF) relational database integrity, sub-2.0s transactional POS inventory deductions, dynamic spatial putaway, and automated First-Expired, First-Out (FEFO) batch allocation, RetailSync eliminates the three largest profit leaks in modern trade:
1. **Perishable food & dairy spoilage** (15% to 22% annual loss).
2. **Phantom inventory & unrecorded shrinkage** (1.8% to 2.4% inventory write-offs).
3. **High-velocity stockouts during festival rush periods** (7.5% to 11.2% lost revenue).

### 1.2 Core Product Value Propositions
* **Sub-2.0 Second POS Concurrency Sync:** Cashiers process high-speed barcode sales while the backend executes atomic row-level locks (`SELECT ... FOR UPDATE`), preventing overselling and phantom stock.
* **Strict FEFO (First-Expired, First-Out) Priority Queues:** Eliminates human picking bias by dynamically routing pickers to the batch with the nearest expiration date, backed by automated quarantine locks.
* **Algorithmic Replenishment Decision Support System (DSS):** Directly integrates Dynamic Economic Order Quantity (EOQ), Greasley's Statistical Safety Stock (factoring demand and vendor lead-time variances), and dynamic Reorder Points (ROP) to replace managerial guesswork with mathematical precision.
* **Frugal & Ergonomic Hardware Strategy:** Built as a responsive Progressive Web Application (PWA) supporting consumer Android smartphones paired with low-cost Bluetooth barcode trigger grips (< 4,000 BDT) or built-in camera scanning, eliminating the need for expensive 60,000 BDT ruggedized industrial terminals.
* **Hybrid Enterprise Edge Extensibility:** Native architectural compatibility with stationary automated dock gates (ESP32 MCU + RFID / fixed scanners over MQTT/TLS) for high-throughput distribution center intake.

---

## 2. Target Personas & User Journeys

RetailSync explicitly addresses the real-world operational challenges of six core user personas:

### 2.1 Persona 1: Cashier (Frontline Retail POS)
* **Demographics:** Frontline staff, fast-paced environment, high customer pressure during rush hours (Ramadan, Eid, weekend evenings).
* **Primary Objective:** Scan items rapidly, execute sales transactions in under 2 seconds, and never experience system freezes.
* **Key Frustrations:** System freezing when checking warehouse stock; customer disputes over out-of-stock items; having to restart sales due to internet drops.
* **RetailSync User Journey:**
  1. Cashier scans barcode on consumer item.
  2. POS client interrogates RetailSync local/central deduction endpoint.
  3. RetailSync locks the earliest active FEFO batch in the database, decrements inventory by the scanned quantity, and returns confirmation in `< 350 ms`.
  4. If internet disconnects, POS writes to an offline IndexedDB queue, displays green indicator, and bulk-syncs chronologically when connection restores.

### 2.2 Persona 2: Inbound Receiving Clerk (Warehouse Dock)
* **Demographics:** Operates on concrete loading docks; inspects supplier delivery trucks; exposed to dust and noise.
* **Primary Objective:** Verify delivered goods against Purchase Orders (POs) quickly, reject damaged goods, and generate digital Goods Receipt Notes (GRNs).
* **Key Frustrations:** Paper manifests with missing pages; manual math errors on carton counts; being blamed for accepting near-expiry dairy batches.
* **RetailSync User Journey:**
  1. Clerk selects open PO from tablet/phone.
  2. Scans incoming master carton barcodes; inputs batch lot number and manufacturer expiry date.
  3. System automatically evaluates minimum acceptable shelf-life threshold (e.g., rejects batch if `< 75%` remaining shelf life).
  4. Clerk flags 2 crushed cartons as "Damaged/Quarantine"; completes GRN. System prints internal pallet/carton barcode labels with internal tracking IDs.

### 2.3 Persona 3: Warehouse Floor Operator (Putaway & Picking)
* **Demographics:** Moves constantly across warehouse aisles; operates forklifts or manual pallet jacks; one hand often occupied.
* **Primary Objective:** Know exactly where to place incoming pallets and which bins to pick items from with zero wasted walking distance.
* **Key Frustrations:** Wandering through warehouse searching for empty bins; misplaced boxes causing delayed store shipments; hard-to-read mobile screens in dim racking aisles.
* **RetailSync User Journey:**
  1. Operator scans internal pallet barcode on receiving dock.
  2. RetailSync displays Directed Putaway prompt: `Zone: Chilled Dairy -> Aisle A02 -> Rack R04 -> Shelf S1 -> Bin B03`.
  3. Operator travels to bin, scans destination bin barcode to confirm physical placement. Database updates location atomically.
  4. For outbound orders, operator receives digital pick list sorted by shortest aisle path, scanning each bin and item barcode to confirm FEFO batch compliance.

### 2.4 Persona 4: Inventory Floor Supervisor
* **Demographics:** Tactical floor manager; responsible for stock accuracy, shift productivity, and loss prevention.
* **Primary Objective:** Maintain `> 99.5%` bin location accuracy, conduct non-disruptive cycle counts, and investigate shrinkage.
* **Key Frustrations:** Painful annual physical stock counts; unexplained missing stock discovered days after theft/breakage; unrecorded stock adjustments.
* **RetailSync User Journey:**
  1. Supervisor monitors real-time 2D spatial bin occupancy map on tablet.
  2. Schedules automated blind cycle counts for Class-A velocity SKUs (expected quantities hidden from counters).
  3. Reviews variance reports; approves adjustments with mandatory photographic proof and reason codes (Breakage, Theft, Spoilage).
  4. Reviews Isolation Forest ML anomaly alerts flagging abnormal shrinkage spikes in specific zones or shifts.

### 2.5 Persona 5: Procurement & SCM Officer
* **Demographics:** Office-based supply chain strategist; manages millions of BDT in purchasing budgets.
* **Primary Objective:** Prevent stockouts of high-velocity goods while minimizing capital tied up in slow-moving inventory.
* **Key Frustrations:** Overstocking items that expire on shelves; supplier delivery delays causing sudden stockouts; calculating order sizes using intuition.
* **RetailSync User Journey:**
  1. Officer opens Procurement Queue dashboard.
  2. System highlights SKUs breaching dynamic Reorder Point (`ROP = (d * L) + SS`).
  3. System provides pre-calculated Economic Order Quantity (EOQ) and Greasley Safety Stock based on historical lead-time standard deviation.
  4. Officer reviews suggested order with one click, modifies quantity if promotional demand is expected, and issues digital PO to supplier.

### 2.6 Persona 6: Branch Super Shop Store Manager
* **Demographics:** Manages a retail outlet (e.g., Shwapno Dhanmondi); responsible for branch revenue, shelf fullness, and customer satisfaction.
* **Primary Objective:** Ensure retail store shelves are never empty and received consignments match what was ordered.
* **Key Frustrations:** Calling central warehouse repeatedly to check dispatch status; receiving items expiring in 3 days; receiving wrong quantities.
* **RetailSync User Journey:**
  1. Manager logs into Branch Requisition Portal; views live central warehouse stock availability.
  2. Submits weekly store stock replenishment order.
  3. Tracks dispatch status in real time: `Submitted -> Pick Wave Allocated -> In-Transit (Driver: Jamal, Truck: DHK-METRO-11-2345) -> Delivered`.
  4. Scans received delivery totes; confirms receipt and closes requisition.

---

## 3. Scope Boundaries & MoSCoW Prioritization

### 3.1 In-Scope: Capstone MVP (Must Have - Sprints 1 to 4)
* **User Authentication & RBAC:** Secure JWT authentication with 6 distinct roles (Cashier, Clerk, Operator, Supervisor, Procurement, Admin).
* **Master Catalog Management:** Hierarchical product classification (Dry FMCG, Perishable Produce, Chilled Dairy, Frozen, Household) with barcode, dimensions, and temperature attributes.
* **Supplier & Purchase Order Lifecycle:** Digital PO generation, multi-tier status lifecycle (`DRAFT`, `ISSUED`, `PARTIAL`, `COMPLETED`, `CANCELLED`).
* **Digital Inbound Receiving & GRN:** Handheld barcode scanning against PO line items, variance capture, damaged quarantine tagging, and digital GRN generation.
* **Directed Spatial Putaway:** Zone-Aisle-Rack-Shelf-Bin 2D topology with volumetric and weight capacity constraints.
* **Real-Time FEFO/FIFO Inventory Ledger:** Immutable double-entry transaction ledger; automated allocation of earliest-expiring batch; quarantine lock on expired/damaged lots.
* **Sub-2.0s POS Concurrency Deduction:** High-performance REST API supporting atomic stock deductions with row-level locking (`SELECT ... FOR UPDATE`).
* **Dynamic Decision Support System (DSS):** Mathematical formulas for EOQ, Greasley's Statistical Safety Stock ($Z = 1.28, 1.65, 2.33$), and dynamic ROP alerting.

### 3.2 Should Have: Enhancements (Sprints 5 to 6)
* **Outbound Wave & Batch Picking:** Consolidated picking across multi-branch requisitions with shortest-path aisle sequencing.
* **Store Requisition & Dispatch Portal:** Branch-specific ordering, in-transit dispatch manifest generation, and delivery acknowledgement.
* **Continuous Blind Cycle Counting:** ABC-classified stocktaking schedules with blind quantity entry and supervisor adjustment workflows.
* **Offline POS Caching & Auto-Sync:** Service Worker and IndexedDB client-side cache allowing cashiers to continue scanning during internet dropouts.
* **Supplier SLA Performance Scorecard:** Automated metrics on vendor on-time delivery rate, fulfillment accuracy, and lead-time standard deviation.

### 3.3 Could Have: Future Enterprise Features (Post-Capstone)
* **Unsupervised ML Anomaly Detection:** Isolation Forest algorithm detecting unusual shrinkage clusters across SKUs, operators, and shifts.
* **Automated Dock Gate IoT Portal:** Integration with stationary ESP32 + RC522 RFID / fixed barcode readers over TLS-encrypted MQTT.
* **IoT Cold-Chain Telemetry:** Real-time BLE temperature sensor logging attached to refrigerated transport totes.
* **Customer-Facing Self-Checkout Integration:** Dedicated self-scanning kiosk APIs.

### 3.4 Won't Have: Out-of-Scope (Delimitations)
* Physical automated robotic cranes, Automated Guided Vehicles (AGVs), or mechanized sortation conveyor belts.
* Full double-entry corporate accounting / financial general ledger (system integrates via clean REST APIs to external ERPs).
* Custom silicon / ASIC hardware fabrication.
* International cross-border customs bond clearing workflows.

---

## 4. Detailed Feature Specifications & User Stories

### 4.1 Module M-01: Authentication, Access Control & Security
* **FR-01 (JWT Authentication):** The system shall authenticate users via email/username and password, issuing cryptographically signed JSON Web Tokens (access token valid for 15 minutes, refresh token valid for 8 hours).
* **FR-02 (RBAC Enforcement):** The system shall enforce role-based access control isolating Cashier, Floor Operator, Receiving Clerk, Supervisor, Procurement Officer, Store Manager, and Administrator.
* **FR-04 (Terminal Session Timeout):** Mobile scanning terminals shall automatically lock after 15 minutes of inactivity to prevent unauthorized floor access.
* **User Story US-01:**
  > *As a Warehouse Floor Operator,*  
  > *I want to log in using my 4-digit PIN / credential on a shared mobile scanner,*  
  > *So that I can immediately access my assigned putaway tasks without seeing unauthorized managerial or pricing data.*  
  > **Acceptance Criteria (Gherkin):**  
  > - **Given** an operator with role `OPERATOR`,  
  > - **When** the operator enters valid credentials on the mobile web portal,  
  > - **Then** the system returns an access token restricted to `/api/v1/putaway` and `/api/v1/picking`,  
  > - **And** any attempt to access `/api/v1/suppliers` or `/api/v1/finance` returns `HTTP 403 Forbidden`.

### 4.2 Module M-02 & M-03: Product Catalog & Supplier PO Lifecycle
* **FR-07 (Master SKU Management):** The system shall maintain unique SKU codes, EAN-13/GS1-128 barcodes, packaging dimensions, category hierarchy, and temperature classification.
* **FR-10 (Shelf-Life Rules):** The system shall enforce minimum receiving shelf-life rules (e.g., minimum 75% remaining shelf life required at dock).
* **FR-15 (Digital PO Creation):** Procurement officers shall create digital Purchase Orders linked to approved suppliers with delivery deadlines and unit purchase prices.
* **User Story US-02:**
  > *As a Procurement Officer,*  
  > *I want the system to generate a draft PO populated with the mathematically optimal EOQ when an item breaches its ROP,*  
  > *So that I can review and approve supplier replenishments in under 30 seconds.*  
  > **Acceptance Criteria (Gherkin):**  
  > - **Given** SKU `SKU-SOIL-1L` has an inventory position of 1,180 units and an ROP of 1,218 units,  
  > - **When** the nightly replenishment cron or real-time sales trigger executes,  
  > - **Then** a new PO in status `DRAFT` is created for supplier `Bashundhara Food & Beverage`,  
  > - **And** the recommended order quantity is exactly set to the calculated EOQ (1,265 units).

### 4.3 Module M-04: Inbound Receiving & Digital GRN
* **FR-22 (Barcode Interrogation vs. PO):** The receiving clerk shall scan delivered carton/pallet barcodes to validate quantities and item identity against open PO line items.
* **FR-23 (Batch Lot & Expiry Capture):** The system shall require entering manufacturer batch numbers, production dates, and expiration dates for every perishable shipment.
* **FR-26 (Digital GRN Generation):** Upon receiving completion, the system shall generate a formal Goods Receipt Note (GRN) itemizing accepted units, short-shipped units, and damaged units.
* **User Story US-03:**
  > *As an Inbound Receiving Clerk,*  
  > *I want to record damaged cartons immediately during dock unloading,*  
  > *So that damaged stock is quarantined and an automated credit note advisory is issued to the supplier.*  
  > **Acceptance Criteria (Gherkin):**  
  > - **Given** PO `PO-2026-0891` specifies 100 cartons of milk,  
  > - **When** the clerk enters 96 accepted cartons and 4 damaged/leaking cartons,  
  > - **Then** GRN `GRN-2026-0412` is committed with 96 units marked `AVAILABLE` and 4 units marked `QUARANTINED`,  
  > - **And** the 4 quarantined units are excluded from sellable POS stock balances,  
  > - **And** a credit advisory for 4 units is logged for supplier accounts reconciliation.

### 4.4 Module M-05 & M-06: Directed Putaway & Real-Time FEFO Inventory Ledger
* **FR-32 (Directed Spatial Putaway):** The system shall recommend the optimal bin destination based on SKU velocity (Class A near dispatch docks), temperature zones, and available bin cubic capacity.
* **FR-38 (Strict FEFO Expiry Queue):** The system shall strictly allocate outbound stock from the batch with the earliest valid expiration date.
* **FR-41 (Automated Quarantine Lock):** Any batch reaching its expiration date or manually flagged as damaged shall be mechanically locked from picking.
* **User Story US-04:**
  > *As a Warehouse Picker,*  
  > *I want my digital pick list to direct me strictly to the earliest expiring batch of yogurt,*  
  > *So that we eliminate perishable waste and never dispatch expired stock to retail stores.*  
  > **Acceptance Criteria (Gherkin):**  
  > - **Given** Bin B01 contains Batch `LOT-A` expiring in 6 days, and Bin B04 contains Batch `LOT-B` expiring in 25 days,  
  > - **When** a store requisition requests 10 units of yogurt,  
  > - **Then** the pick instruction directs the operator exclusively to Bin B01 for Batch `LOT-A`,  
  > - **And** scanning the barcode for Batch `LOT-B` triggers an audible error: `"FEFO Violation: Pick Batch LOT-A First"`.

### 4.5 Module M-07 & POS: Sub-2.0s POS Concurrency Synchronization
* **FR-30 (Atomic Checkout Deduction):** When a retail cashier scans an item at checkout, the API shall deduct stock inside an atomic database transaction using row-level locking (`SELECT ... FOR UPDATE`).
* **FR-36 (Immutable Audit Ledger):** Every stock movement shall append a record to `inventory_transactions` with user ID, timestamp, transaction type, and reference number.
* **User Story US-05:**
  > *As a Retail Cashier,*  
  > *I want item barcode deductions to complete in under 2 seconds without database locking errors,*  
  > *So that long customer checkout lines move quickly without delay.*  
  > **Acceptance Criteria (Gherkin):**  
  > - **Given** 10 concurrent POS cash registers scanning items simultaneously across branches,  
  > - **When** checkout API calls hit `/api/v1/pos/sync`,  
  > - **Then** 99% of requests complete with `HTTP 200 OK` in `< 1.2 seconds`,  
  > - **And** the inventory on-hand balance matches total initial stock minus total sold units exactly, with zero negative stock states.

---

## 5. Non-Functional Requirements (NFRs) & Performance SLOs

| ID | Requirement Category | Specific Metric & Quantitative Target | Verification Methodology |
| :--- | :--- | :--- | :--- |
| **NFR-01** | **Scan Latency** | Barcode interrogation to visual UI confirmation $\le 350$ milliseconds. | Automated browser performance profiler with Bluetooth HID trigger. |
| **NFR-02** | **POS API Latency** | Checkout deduction API response time $\le 2.0$ seconds (p95 $\le 800$ ms, p99 $\le 1.5$ s). | Locust load test simulating 50 concurrent requests/sec. |
| **NFR-03** | **Concurrency Isolation** | Handle at least 50 concurrent scanners and 10 POS cash registers with zero deadlocks. | Stress test suite with parallel asynchronous worker threads. |
| **NFR-04** | **Data Integrity** | Complete ACID transaction compliance; zero instances of negative stock balances. | Multi-threaded race condition tests on last remaining stock unit. |
| **NFR-05** | **System Availability** | 99.8% operational uptime during warehouse operational hours (6:00 AM to 11:00 PM BST). | Automated health-check monitoring via Prometheus / Uptime Kuma. |
| **NFR-06** | **Disaster Recovery** | Point-In-Time Recovery (PITR) with Recovery Point Objective (RPO) $\le 1$ min, RTO $\le 15$ min. | Simulated database crash and WAL recovery drills. |
| **NFR-07** | **Security & Encryption** | TLS 1.3 encryption in transit; AES-256 for credentials at rest; Argon2id password hashing. | SSL Labs SSL test (A+ grade) and OWASP ZAP penetration scan. |
| **NFR-08** | **Ergonomics & Display** | High-contrast UI (WCAG 2.1 AA compliant); one-handed mobile navigation; audio/haptic beeps. | Usability field trial with warehouse operators under 150 lux light. |
| **NFR-09** | **Scalability** | Support up to 50,000 SKUs, 500,000 active batches, and 5,000,000 transaction records. | Database benchmark with 5M synthetic records using B-Tree indexes. |
| **NFR-10** | **Regulatory Compliance** | 100% adherence to Bangladesh Food Safety Act 2013 and BSTI batch expiration standards. | Automated audit verifying zero expired units ever dispatched. |

---

## 6. Edge Cases, Failure Modes & Resilience Protocols

### 6.1 Edge Case 1: The Zero-Stock Concurrency Collision
* **Scenario:** Two cashiers at different retail branches scan the very last available unit of full-cream milk at the exact same millisecond.
* **System Action:** 
  1. Both transactions request a row-level lock on the active inventory batch via `SELECT current_quantity FROM product_batches WHERE batch_id = :id FOR UPDATE`.
  2. Transaction A acquires the lock first, decrements quantity from `1` to `0`, commits, and releases the lock.
  3. Transaction B acquires the lock, detects `current_quantity = 0`, immediately releases the lock, and returns `HTTP 409 Conflict: {"error": "OUT_OF_STOCK", "sku": "MILK-FC-1L"}`.
  4. Cashier B's POS notifies the cashier gracefully; inventory never drops below zero.

### 6.2 Edge Case 2: Store Internet Drop (Network Outage)
* **Scenario:** The local ISP fiber connection at the Dhanmondi retail outlet is severed for 10 minutes during peak hours.
* **System Action:**
  1. The POS PWA detects network failure and toggles to **Local Resilient Mode**.
  2. Scanned sales are appended to an encrypted browser `IndexedDB` transaction buffer with client timestamps.
  3. A visual amber badge alerts the cashier: *"Offline Mode: 14 Sales Buffered"*.
  4. When connection is restored, the client executes an idempotent bulk sync (`POST /api/v1/pos/bulk-sync`) with `X-Idempotency-Key` headers. The central server validates and commits all 14 sales chronologically.

### 6.3 Edge Case 3: Damaged or Smudged Barcode Label
* **Scenario:** An incoming carton has its manufacturer barcode torn or smudged with oil.
* **System Action:**
  1. Operator toggles mobile scanner to "Manual SKU / Batch Lookup".
  2. Typing the first 3 letters of the product name returns autocomplete suggestions with product thumbnail images.
  3. Clerk selects product, confirms batch expiry from legible text, and clicks "Print Replacement Barcode".
  4. Connected dock label printer instantly outputs a fresh GS1-compliant internal barcode sticker.

---

## 7. Business KPIs & Operational Success Metrics

| Strategic Metric | Baseline (Traditional Manual Super Shop) | RetailSync Target (Pilot Benchmark) | Business Impact & Financial Value |
| :--- | :--- | :--- | :--- |
| **Perishable Spoilage Rate** | 15% to 22% of dairy/produce wasted annually. | **$< 6\%$** (Over 65% waste reduction). | Saves millions of BDT in prevented stock write-offs. |
| **Stockout Frequency (Class A SKUs)** | 7.5% to 11.2% lost sales from empty shelves. | **$< 1.5\%$** (80% stockout reduction). | Immediate gross revenue expansion during peak shopping hours. |
| **Inbound Unloading-to-GRN Cycle** | 45 to 75 minutes per delivery truck. | **$< 12$ minutes** (73% cycle time reduction). | Eliminates dock congestion and supplier waiting detention fees. |
| **Bin Location Accuracy** | 78% to 84% (Frequent lost pallets and misplaced stock). | **$> 99.5\%$** spatial location accuracy. | Eliminates picker search latency and delayed store deliveries. |
| **Store Dispatch Accuracy** | 3.2% error rate (Store receives wrong quantities/items). | **$< 0.2\%$** shipment discrepancy rate. | Eliminates store-warehouse disputes and inter-branch inventory leakage. |
| **Inventory Turnover Ratio (ITR)** | 6.2 turns per year. | **9.5+ turns per year**. | Drastically lowers capital lockup in holding inventory. |
