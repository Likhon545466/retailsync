# RetailSync: Centralized Super Shop Warehouse Management System
## Capstone Project Proposal — Part 1: Project Planning & Definition

**Course:** SE-231 (Software System Analysis & Design / Capstone Project 2)  
**Department:** Department of Software Engineering, Faculty of Science and Information Technology  
**Institution:** Daffodil International University (DIU), Dhaka, Bangladesh  
**Student / Author:** **Raisul Islam Likhon** (Section: **SWE-44D**)  
**Submission Term:** Fall 2026 | September 2026 | Version: 1.0.0-RELEASE  

---

## Executive Summary & Project Abstract

**RetailSync** is a high-performance, centralized enterprise Warehouse Management System (WMS) engineered specifically for the fast-evolving modern grocery retail and super shop sector in Bangladesh (e.g., Shwapno, Agora, Meena Bazar, Unimart, Daily Shopping). The platform bridges the destructive operational chasm between central distribution centers and frontline retail checkout counters (POS). 

By enforcing strict Third Normal Form (3NF) relational database integrity, sub-2.0s atomic POS inventory deductions, dynamic spatial putaway, and automated First-Expired, First-Out (FEFO) batch allocation, RetailSync directly eliminates the three largest profit leaks in modern trade:
1. **Perishable food & dairy spoilage** (15% to 22% annual loss).
2. **Phantom inventory & shrinkage write-offs** (1.8% to 2.4% unexplained loss).
3. **Peak-hour stockouts & POS freezes during festival rushes** (7.5% to 11.2% lost sales).

Architecturally, RetailSync is deployed as a 4-tier cyber-physical platform combining a Next.js 14 Progressive Web Application (PWA), an asynchronous FastAPI (Python 3.11+) backend, a normalized PostgreSQL 16 relational ledger, and an in-memory Redis 7 caching and idempotency tier. To minimize capital expenditure, RetailSync adopts a frugal hardware strategy pairing standard consumer Android smartphones with low-cost Bluetooth barcode trigger grips (< 4,000 BDT), eliminating the need for expensive 60,000 BDT industrial handheld terminals while maintaining native compatibility with stationary automated dock gate scanners (ESP32 MCU over MQTT/TLS).

> **Core Capstone Thesis & Quantifiable SLO Targets:**  
> * **Primary Research Question:** How can centralized relational concurrency and automated FEFO prioritization eliminate retail stockouts and perishable spoilage in high-density grocery operations?  
> * **Key SLO Target:** Sub-2.0s POS checkout deduction latency across 10 concurrent branch registers with 0 deadlocks.  
> * **Methodology:** 14-Week Agile Scrum Lifecycle delivering an incremental, Dockerized production-grade MVP across 6 sprints.

---

## Document Architecture & Table of Contents

| Section | Title | Summary Scope |
| :--- | :--- | :--- |
| **Section 1** | Industry Background & Problem Statement | Operational context, profit leaks, and problem-to-feature mapping |
| **Section 2** | Project Objectives & Scope Boundaries | SMART goals, MoSCoW prioritization matrix, in-scope vs out-of-scope |
| **Section 3** | Target Personas & Operational Workflows | User profiles (Manager, Cashier, Operator, Procurement) and use cases |
| **Section 4** | Core Functional Modules & Feature Breakdown | 8 core modules: Auth, POs, Inbound, Putaway, FEFO, POS, DSS, Audit |
| **Section 5** | Non-Functional Requirements & Performance SLOs | Latency, throughput, ACID concurrency, security, and food safety compliance |
| **Section 6** | System Architecture & Technical Design | 4-tier architecture, PostgreSQL 16 schema, row-level locking, offline sync |
| **Section 7** | Curated Technology Stack & Hardware Strategy | Next.js 14 PWA, FastAPI, PostgreSQL, Redis, and frugal barcode scanner model |
| **Section 8** | Development Methodology: Agile Scrum Framework | Scrum rationale, 14-week sprint roadmap, sprint backlogs, Definition of Done |
| **Section 9** | Resource Allocation, Budget & Risk Management | RACI matrix, hardware expenditure (< 35,000 BDT), and local risk mitigations |
| **Section 10** | Verification, Testing, ROI Impact & Conclusion | Testing strategy, expected financial ROI, academic roadmap, and references |

---

## 1. Industry Background & Problem Statement

### 1.1 The Modern Grocery Retail Landscape in Bangladesh
The supermarket and organized grocery retail sector in Bangladesh is experiencing rapid compound annual growth driven by rising urbanization, dual-income households, and an expanding middle class seeking convenience and food safety assurances. Major retail chains such as Shwapno (over 450 outlets), Agora, Meena Bazar, Unimart, and Daily Shopping handle thousands of high-velocity fast-moving consumer goods (FMCG) and perishable food items daily across dense metropolitan hubs like Dhaka and Chattogram.

However, behind modern retail checkout counters lies a fragile, disjointed warehouse and supply chain infrastructure. While front-of-house Point of Sale (POS) billing systems have modernized, back-of-house warehouse storage, stock allocation, and central distribution center operations remain heavily dependent on manual pen-and-paper logs, fragmented spreadsheets, or legacy ERP modules lacking real-time synchronization.

### 1.2 The Three Critical Profit Leaks in Super Shop Operations
* **1. Perishable Food & Dairy Spoilage:** Modern supermarkets lose 15% to 22% of perishable inventory annually due to lack of batch-level expiration visibility. Floor workers routinely pull newer stock from front shelves while older batches rot unnoticed at the back of warehouse bins, directly violating the Bangladesh Food Safety Act 2013.
* **2. Phantom Inventory & Operational Shrinkage:** A severe operational disconnect exists between what the central database reports and what physically exists on warehouse shelves. This 'phantom inventory' (1.8% to 2.4% shrinkage write-offs) stems from untracked damage, unrecorded pilferage, and delayed end-of-day spreadsheet reconciliations.
* **3. Peak-Hour Stockouts & POS Freezing:** During peak shopping windows (Ramadan, Eid-ul-Fitr, weekend evenings), high-velocity items (e.g., 1L soyabean oil, milk, sugar) sell out in minutes. Because POS registers do not deduct warehouse stock atomically, replenishment orders lag by 6 to 12 hours, resulting in 7.5% to 11.2% lost revenue from customer walkouts.

### 1.3 Operational Gaps in Current Commercial Solutions
Existing commercial Enterprise Resource Planning (ERP) systems and legacy WMS platforms fail Bangladeshi super shops across three critical dimensions: 
1. **Prohibitive Cost:** Enterprise solutions (SAP, Oracle, Odoo Enterprise) demand tens of thousands of dollars in licensing and require 60,000 BDT industrial handheld terminals;
2. **Batch Blindness:** Generic ERPs treat stock as aggregate quantities without enforcing strict First-Expired, First-Out (FEFO) picking queues;
3. **Network Fragility:** Cloud-only systems freeze completely during frequent local broadband outages, halting checkout queues.

### 1.4 Problem-to-Feature Mapping
| ID | Real-World Problem | Operational Impact | RetailSync Solution |
| :---: | :--- | :--- | :--- |
| **P-01** | Data Isolation | Sales data lives in POS; warehouse data lives on clipboards. | Centralized SQL database serving both POS and warehouse APIs. |
| **P-02** | Undetected Stockouts | High-demand items run out on shelves before restock is ordered. | Automated Reorder Point (ROP) alerts sent to floor staff. |
| **P-03** | Expired Product Waste | Milk and bread expire in the back of shelves unseen. | Mandatory FEFO picking logic enforced by mobile scanners. |
| **P-04** | Discrepancies & Pilferage | Phantom inventory identified only during quarterly stock takes. | Continuous blind cycle counting with supervisor discrepancy alerts. |
| **P-05** | Inventory Holding Cost | Overstocking bulky items ties up operating capital. | Economic Order Quantity (EOQ) formula calculating batch sizes. |

---

## 2. Project Objectives & Scope Boundaries

### 2.1 SMART Project Objectives
* **Sub-2.0s POS Concurrency:** Execute atomic stock deductions from retail cash registers via PostgreSQL row-level locks, achieving p95 latency ≤ 800ms with zero overselling across 10 concurrent registers.
* **Automated FEFO Priority:** Enforce strict First-Expired, First-Out picking logic that mechanically quarantines batches within 3 days of expiry, reducing perishable spoilage from 22% to under 6%.
* **Algorithmic Replenishment DSS:** Integrate Dynamic Economic Order Quantity (EOQ) and Greasley's Statistical Safety Stock factoring vendor lead-time variances, reducing stockouts by > 60%.
* **Frugal Hardware Architecture:** Engineer a responsive Progressive Web Application (PWA) compatible with consumer Android smartphones and Bluetooth trigger scanners (< 4,000 BDT), cutting hardware costs by 90%.
* **Offline Network Resilience:** Implement client-side Service Workers and encrypted IndexedDB queues to buffer up to 500 sales transactions during internet dropouts, replaying idempotently upon recovery.

### 2.2 Scope Boundaries & MoSCoW Prioritization
| Category | In-Scope Modules / Engineering Features | Sprint Alignment | Target Deliverable |
| :--- | :--- | :---: | :--- |
| **Must Have (MVP)** | Auth & RBAC, Master Catalog, Supplier & Digital POs, Inbound Barcode Scanning & GRN, Spatial Putaway, Real-Time FEFO Ledger, Sub-2.0s POS Deductions, Dynamic EOQ & Safety Stock DSS. | Sprints 1 to 4 | Functional core platform operating end-to-end. |
| **Should Have (Enhancements)** | Outbound Wave Picking, Branch Store Requisition Portal, Blind Cycle Counting with Discrepancy Workflows, Offline POS Service Worker Caching with Idempotent Auto-Sync. | Sprints 5 to 6 | Hardened enterprise feature set for multi-branch trials. |
| **Could Have (Future Post-Capstone)** | Unsupervised ML Shrinkage Anomaly Detection (Isolation Forest), Stationary Automated Dock Gate Scanner (ESP32 MCU over MQTT/TLS), BLE Cold-Chain Sensor Telemetry. | Future Roadmap | Proof-of-concept enterprise edge expansions. |
| **Won't Have (Out of Scope)** | Autonomous robotic picking cranes (AGVs), physical warehouse conveyor belts, full corporate double-entry general ledger accounting ERP, custom silicon hardware. | Out of Scope | Avoids unrealistic hardware and accounting bloat. |

---

## 3. Target Personas & Operational Workflows

### 3.1 Core Target Personas
| User Persona | Role Description | Key Responsibility & System Interaction |
| :--- | :--- | :--- |
| **Store Manager** | Supervises store operations and inventory health. | Views executive analytics dashboard, reviews shrinkage anomalies, approves reorder proposals, monitors gross margins. |
| **Warehouse Operator** | Executes floor movement: receiving, putaway, picking. | Operates mobile PWA scanner, confirms PO intake, follows directed bin routes, scans batch barcodes for FEFO pick verification. |
| **POS Cashier** | Frontline checkout cashier ringing up customer sales. | Scans product barcodes at register, triggers atomic inventory deductions in < 2.0s, handles offline queue during network drops. |
| **Procurement Officer** | Manages supplier relations and purchase orders. | Evaluates vendor delivery performance, reviews algorithmic EOQ reorder suggestions, issues digital POs. |

### 3.2 End-to-End Operational Lifecycle Workflow
1. **Inbound Receiving & GRN Verification:** Supplier deliveries are scanned against active digital POs. Expiration dates, lot numbers, and damaged cartons are captured, generating an immutable Goods Receipt Note (GRN).
2. **Directed Spatial Putaway:** The system computes the optimal bin coordinate (Zone-Aisle-Rack-Shelf-Bin) factoring temperature and SKU velocity. The operator scans the destination bin to confirm docking.
3. **Real-Time POS Inventory Deduction:** At checkout, the POS issues an atomic deduction. The backend executes a pessimistic row lock (`SELECT ... FOR UPDATE`) on the earliest active batch in < 2.0 seconds with zero overselling.
4. **Strict FEFO Outbound Allocation:** Store requisitions allocate stock strictly from earliest expiring batches. Expired or quarantined lots are mechanically excluded.
5. **Algorithmic Replenishment Trigger:** When net stock breaches the Reorder Point (ROP), the system automatically generates a draft PO populated with the optimal EOQ quantity.

---

## 4. Core Functional Modules & Feature Breakdown

* **M-01: Authentication, RBAC & Audit Ledger:** Argon2id password hashing, stateless JWT session tokens (15-min access, 8-hour refresh), role-based permissions, and append-only audit trail.
* **M-02: Master Catalog & Supplier PO Lifecycle:** SKU master catalog, EAN-13 barcodes, climate classifications, and digital Purchase Order states (DRAFT, ISSUED, PARTIAL, COMPLETED, CANCELLED).
* **M-03: Handheld Inbound Receiving & Digital GRN:** Mobile barcode interrogation, variance tracking (ordered vs. received), and digital GRN generation.
* **M-04: Directed Spatial Putaway Engine:** 3D bin routing based on SKU turnover velocity (Class-A near dispatch), climate zones (Chiller, Freezer, Ambient), and weight capacities.
* **M-05: Real-Time FEFO Inventory Ledger:** Batch-level tracking (`product_batches`), automated FEFO picking prioritization, and automated quarantine locks.
* **M-06: Sub-2.0s Point of Sale (POS) Concurrency Sync:** Pessimistic row-level locking (`SELECT ... FOR UPDATE`) guaranteeing atomic stock updates with zero deadlocks and zero phantom sales.
* **M-07: Algorithmic Replenishment DSS:** Mathematical optimization factoring demand and lead-time variances:
  * **Dynamic Economic Order Quantity:** $EOQ = \sqrt{\frac{2 \times D \times S}{H}}$
  * **Greasley's Statistical Safety Stock:** $SS = Z \times \sqrt{(\overline{L} \times \sigma_d^2) + (\overline{d}^2 \times \sigma_L^2)}$
  * **Dynamic Reorder Point:** $ROP = (\overline{d} \times \overline{L}) + SS$
* **M-08: Continuous Blind Cycle Counting:** ABC-classified counting sheets with system quantities hidden to eliminate confirmation bias, flagging discrepancies > 2%.

---

## 5. Non-Functional Requirements & Performance SLOs

| ID | Category | Specific Metric & Target | Verification Method |
| :---: | :--- | :--- | :--- |
| **NFR-01** | Scan Latency | Barcode decode to visual confirmation ≤ 350 ms. | Automated mobile browser profiler with Bluetooth HID trigger. |
| **NFR-02** | POS Sync Latency | Deduction transaction completes in ≤ 2.0s (p95 ≤ 800ms, p99 ≤ 1.5s). | Locust stress test simulating 10 concurrent registers. |
| **NFR-03** | Concurrency Isolation | Handle ≥ 50 concurrent floor scanners and 10 POS cash registers with zero deadlocks. | Multi-threaded test runner executing concurrent checkout deductions. |
| **NFR-04** | Data Integrity | Complete ACID transaction compliance; zero negative stock balances. | Automated race condition test asserting stock balance constraints. |
| **NFR-05** | Availability | 99.8% operational uptime during business hours (06:00 to 23:00 BST). | Automated health-check monitoring via Prometheus and Uptime Kuma. |
| **NFR-06** | Disaster Recovery | Point-In-Time Recovery (PITR) with RPO ≤ 1 min, RTO ≤ 15 min. | Automated database backup verification and WAL restore drills. |

---

## 6. System Architecture & Technical Design

### 6.1 4-Tier Cyber-Physical Architecture
1. **Tier 1: Client Edge (Handheld & POS PWA):** Responsive Next.js 14 Progressive Web App with pure JS barcode scanning (ZXing / Html5-QRCode) and Service Worker IndexedDB offline queues.
2. **Tier 2: Edge Gateway & Security Layer:** Nginx reverse proxy terminating TLS 1.3, managing rate limiting and CORS policies. ESP32 microcontroller with RFID/fixed barcode readers communicating over MQTT/TLS for dock gates.
3. **Tier 3: Core Application Services Tier:** Asynchronous Python 3.11+ FastAPI backend with isolated domain services for Inbound, Putaway, FEFO, POS, and DSS.
4. **Tier 4: Enterprise Data & In-Memory Storage:** PostgreSQL 16 3NF normalized relational database paired with Redis 7 for session tokens and idempotency caching.

### 6.2 High-Throughput Concurrency Control: Row-Level Locking
To prevent overselling and race conditions when multiple cash registers ring up the same SKU:
```sql
SELECT id, current_qty 
FROM product_batches 
WHERE product_id = :p_id AND current_qty > 0 
ORDER BY expiry_date ASC 
LIMIT 1 
FOR UPDATE;
```
This locks exclusively the earliest active batch record. Concurrent POS requests queue safely for milliseconds without deadlocking or reading stale stock balances.

---

## 7. Curated Technology Stack & Hardware Strategy

| Component | Technology | Version | Engineering Justification |
| :--- | :--- | :---: | :--- |
| **Frontend PWA** | Next.js / React | `14.2+` | Single Page Application (SPA) speed with server-side rendering (SSR) for dashboards; eliminates page-reload latency on mobile scanning terminals. |
| **Backend API** | FastAPI / Python | `3.11+` | Asynchronous ASGI framework with native async/await event loop, sub-millisecond route execution, and automatic OpenAPI schema generation. |
| **Database Core** | PostgreSQL | `16+` | ACID-compliant relational core with native row-level locking (`SELECT ... FOR UPDATE`), partial indexes, and JSONB support for audit payloads. |
| **In-Memory Cache** | Redis | `7.2+` | Sub-millisecond distributed cache for session management, rate-limiting tokens, and idempotency key locks (`X-Idempotency-Key`). |
| **Barcode Scanner** | Html5-QRCode / ZXing | Latest | Pure JavaScript barcode engine reading 1D (EAN-13, Code 128) and 2D (QR) barcodes directly from smartphone cameras and Bluetooth trigger guns. |

### Frugal Barcode Hardware Strategy
Traditional industrial terminals (Zebra TC52) cost upwards of 60,000 BDT. RetailSync runs on standard consumer Android smartphones (10,000–12,000 BDT) paired with ergonomic Bluetooth barcode trigger grips (< 4,000 BDT), cutting hardware costs by 90% while achieving sub-350ms scan speeds.

---

## 8. Development Methodology: Agile Scrum Framework

### 8.1 Methodology Rationale: Why Agile Scrum Over Waterfall?
RetailSync is developed strictly following the **Agile Scrum Framework**. Sequential methodologies (Waterfall, V-Model) are deliberately rejected due to the dynamic operational realities of modern retail grocery environments:
* **The Failure of Waterfall in Supermarkets:** Sequential models assume static, unchanging requirements over a 6-month lifecycle. In reality, Bangladeshi supermarket operations experience frequent shifts in supplier terms, festival volume surges (Eid/Ramadan), and unexpected broadband dropouts. Deferring integration and stress testing to Month 4 results in catastrophic concurrency deadlocks and race conditions discovered only on launch day.
* **The Agile Scrum Advantage:** Scrum provides **empirical process control** through transparent, time-boxed 2-week iterations. Delivering a potentially shippable increment every 14 days allows supermarket supervisors, floor operators, and DIU academic evaluators to test real scanning speeds, mobile UX ergonomics, and database concurrency on physical hardware throughout the project lifecycle.

### 8.2 Scrum Team Roles & Responsibilities
* **Product Owner (PO):** Maximizes product business value, manages and prioritizes the product backlog, defines acceptance criteria, and validates user stories against operational ROI targets.
* **Scrum Master (SM):** Facilitates all Scrum ceremonies, shields the team from external distractions, eliminates technical and architectural blockers, and enforces the Definition of Done.
* **Cross-Functional Engineering Team:** Full-stack developers delivering vertical end-to-end features spanning FastAPI backend routes, Next.js 14 PWA frontend views, and PostgreSQL 16 database schemas.

### 8.3 Core Scrum Ceremonies & Timeboxes
1. **Sprint Planning (4 Hours / Bi-Weekly):** The Product Owner presents prioritized backlog items; the engineering team decomposes them into technical tasks, estimates effort via Planning Poker (Fibonacci scale), and commits to a formal Sprint Goal.
2. **Daily Scrum / Standup (15 Mins / Daily):** Time-boxed morning synchronization addressing three questions: What was completed yesterday? What will be built today? Are there any architectural blockers or database deadlocks?
3. **Continuous Backlog Refinement (2 Hours / Mid-Sprint):** The team clarifies emerging retail edge cases (split vendor shipments, batch returns, quarantine overrides), splits oversized epics, and finalizes Acceptance Criteria.
4. **Sprint Review & Live Demo (2 Hours / Bi-Weekly):** Live software demonstration of the working increment to super shop managers and DIU faculty on consumer Android smartphones and POS registers.
5. **Sprint Retrospective (1.5 Hours / Bi-Weekly):** Team inspection of sprint velocity, CI/CD automated test metrics, and identification of actionable process and code improvements.

### 8.4 14-Week Capstone Implementation Roadmap
| Phase / Sprint | Timeframe | Core Engineering Modules & Deliverables | Story Points |
| :--- | :---: | :--- | :---: |
| **Sprint 1** | Weeks 01–02 | Project Setup, 3NF Database Schema, Docker Compose, JWT Auth & RBAC | 26 pts |
| **Sprint 2** | Weeks 03–04 | Master Product Catalog, Supplier Lifecycle, Mobile Inbound Barcode Receiving & GRN | 30 pts |
| **Sprint 3** | Weeks 05–06 | Directed Spatial Putaway, Real-Time FEFO Inventory Ledger, Expiry Watchlist Engine | 34 pts |
| **Sprint 4** | Weeks 07–08 | Sub-2.0s POS Concurrency Deductions, Row-Level Locking, Offline PWA Caching | 38 pts |
| **Sprint 5** | Weeks 09–10 | Replenishment DSS (EOQ & Greasley Safety Stock), Multi-Store Requisitions & Wave Picking | 32 pts |
| **Sprint 6** | Weeks 11–12 | Blind Cycle Counting, Shrinkage Anomaly Detection & Executive Floor Telemetry | 28 pts |
| **Sprint 7** | Weeks 13–14 | Locust Stress Testing, Concurrency Hardening, Documentation & Defense Presentation | 20 pts |

### 8.5 Definition of Done (DoD) & Quality Gates
A user story or sprint task is declared **DONE** and permitted into the production build only when all six quality gates are satisfied:
1. **Code Complete & Reviewed:** Code committed to Git with conventional commits, merged via Pull Request with peer review and zero linter warnings.
2. **Automated Test Coverage:** Pytest unit and integration test suites pass with $\ge$ 80% line coverage in the CI/CD pipeline.
3. **Concurrency & ACID Validated:** Locust multi-threaded stress tests confirm zero database deadlocks and zero negative balances under simulated 10-cashier peak traffic.
4. **OpenAPI Schema Documented:** FastAPI endpoints registered with comprehensive Pydantic request/response schemas and error models in Swagger/OpenAPI.
5. **Containerized Staging Build:** Multi-stage Docker Compose builds and passes automated health checks (`/healthz` returns HTTP 200).
6. **Mobile Responsive & Ergonomics:** Handheld PWA interface verified on a 375x667 viewport with camera-based barcode scanning decode speed under 350ms.

---

## 9. Resource Allocation, Budget & Risk Management

### 9.1 Hardware & Operational Budget Breakdown
* **Android Test Smartphone (Android 13, 4GB RAM):** 12,500 BDT
* **Bluetooth Barcode Trigger Grips (Qty: 2):** 7,600 BDT
* **Thermal Label & Receipt Printer (4-inch USB/BT):** 6,500 BDT
* **EAN-128 Adhesive Labels (3,000 labels):** 1,950 BDT
* **Cloud Staging VPS Hosting (6 Months):** 5,500 BDT
* **Total Estimated Budget:** **34,050 BDT**

### 9.2 Local Operational Risk Management
* **Network Outages:** Solved via Service Worker and encrypted IndexedDB client caching with idempotent replay (`X-Idempotency-Key`).
* **Database Deadlocks under Surge:** Solved via deterministic batch sorting (`ORDER BY expiry_date ASC LIMIT 1 FOR UPDATE`) and connection pooling.
* **Worker Resistance to Barcode Scanners:** Solved via low-latency audio beep confirmations and simple high-contrast PWA interface.

---

## 10. Verification, ROI Impact & Conclusion

### 10.1 Multi-Tier Verification & Testing Strategy
* **Unit Testing (PyTest / Vitest):** > 80% code coverage across business rules, EOQ calculations, and FEFO sorting logic.
* **Concurrency Stress Testing (Locust):** 50 concurrent floor scanners and 10 POS cash registers verifying sub-2.0s response times and zero deadlocks.
* **User Acceptance Testing (UAT):** Real-world floor workflows with super shop retail staff.

### 10.2 Expected Operational & Financial Impact (ROI)
* **Perishable Spoilage:** Reduced from 22% down to < 6% (saving millions of BDT in annual food waste).
* **POS Checkout Scan Latency:** Maintained ≤ 2.0s (p95 ≤ 800ms) with zero overselling.
* **Phantom Inventory Shrinkage:** Reduced from 2.4% down to < 0.4% via immutable double-entry ledger.
* **Inbound Unloading Time:** Reduced from 60 minutes to < 15 minutes per delivery truck.
* **Stockouts during Rush Hours:** Reduced from 11.2% down to < 2.5% via statistical safety stock alerting.

### 10.3 Conclusion & Roadmap to Part 2
RetailSync delivers an empirically grounded, technically sophisticated, and economically viable Warehouse Management System engineered for the Bangladeshi retail landscape. The completion of Part 1 (Project Planning and Definition) establishes the definitive architectural foundation for immediate execution in Part 2 (System Design, Prototyping, and Concurrency Validation).
