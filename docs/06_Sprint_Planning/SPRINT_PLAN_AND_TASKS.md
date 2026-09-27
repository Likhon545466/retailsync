# Sprint Implementation Plan & Engineering Task Breakdown

## RetailSync: Centralized Super Shop Warehouse Management System
**Subtitle:** 14-Week Agile Scrum Roadmap, Sprint Backlogs, Story Points, and Definition of Done  
**Course:** SE-231 (Software System Analysis & Design / Capstone Project 2)  
**Academic Institution:** Daffodil International University (DIU), Department of Software Engineering  
**Author:** Raisul Islam Likhon (Section: SWE-44D)  
**Date:** September 2026 | Version: 1.0.0-RELEASE  

---

## 1. Scrum Framework Overview & Velocity Model

RetailSync follows an **Agile Scrum Development Lifecycle** structured across **six 2-week sprints** and a final **2-week hardening and defense preparation phase** (14 weeks total):

* **Sprint Cadence:** 2 weeks per sprint.
* **Sprint Planning:** Day 1 of each sprint (2 hours).
* **Daily Standup:** Asynchronous or 10-minute sync.
* **Sprint Review & Demo:** Alternate Friday with academic supervisor / evaluators.
* **Definition of Done (DoD):** Code committed to Git, unit tests passing (`> 80%` coverage), API endpoints documented in OpenAPI, database migrations reproducible via Docker, and UI responsive on mobile viewport (375x667).

```
+--------------------------------------------------------------------------------------------------------+
|                                14-WEEK CAPSTONE IMPLEMENTATION ROADMAP                                 |
+--------------------------------------------------------------------------------------------------------+
| Sprint 1 (W01-W02) | Database Normalization, Core DDL Migrations, Auth & Next.js PWA Scaffolding       |
| Sprint 2 (W03-W04) | Inbound PO Lifecycle, Handheld Barcode Dock Scanning, and Digital GRN Generation  |
| Sprint 3 (W05-W06) | Directed Spatial Putaway Engine, 2D Floor Map & Real-Time FEFO Inventory Ledger  |
| Sprint 4 (W07-W08) | Sub-2.0s POS Concurrency Deduction Engine, Row-Locking & Offline Caching Queue    |
| Sprint 5 (W09-W10) | Replenishment DSS (EOQ, Greasley Safety Stock, ROP) & Outbound Wave Store Dispatch|
| Sprint 6 (W11-W12) | Blind Cycle Counting, Shrinkage Anomaly Detection & Executive Floor Telemetry     |
| Sprint 7 (W13-W14) | Concurrency Stress-Testing (Locust 50 req/s), Security Audit, Capstone Viva Demo |
+--------------------------------------------------------------------------------------------------------+
```

---

## 2. Sprint Backlogs & Granular Task Breakdowns

### 2.1 Sprint 1 (Weeks 1–2): Architecture, Relational Schema & Auth Core
* **Sprint Goal:** Establish the reproducible Docker environment, initialize the 3NF PostgreSQL database, and deliver secure JWT authentication with role-based access control.
* **Target Velocity:** 32 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-101** | Setup Docker Compose orchestrating PostgreSQL 16, Redis 7, FastAPI backend, and Next.js frontend. | DevOps & Infra | 5 | Single command `docker compose up -d` boots all containers with healthy status. |
| **TSK-102** | Implement Alembic migration scripts for 15 core database tables and composite B-Tree indexes. | Data Modeling | 8 | `alembic upgrade head` runs cleanly; database schema passes 3NF verification audit. |
| **TSK-103** | Load initial authentic seed data (5 suppliers, 7 SKUs, 6 bins, 6 batches, 3 stores). | Data Modeling | 3 | Seed script populates DB; verify foreign key constraints prevent orphaned records. |
| **TSK-104** | Develop User entity, Argon2id password hashing, and JWT token issuance (`/api/v1/auth/login`). | Security & Auth | 5 | Pytest confirms valid token issued; invalid credentials return HTTP 401. |
| **TSK-105** | Implement RBAC middleware enforcing permissions for Cashier, Operator, Clerk, Supervisor, Procurement. | Security & Auth | 5 | Test unauthorized route access returns `HTTP 403 Forbidden`. |
| **TSK-106** | Scaffold Next.js 14 frontend design system with Tailwind CSS and responsive high-contrast layout. | Frontend PWA | 6 | Dashboard renders cleanly on mobile screen (375px) and desktop monitor (1920px). |

---

### 2.2 Sprint 2 (Weeks 3–4): Inbound PO & Handheld Barcode Dock Receiving
* **Sprint Goal:** Deliver working dock receiving workflow allowing clerks to scan delivered carton barcodes against open POs and commit digital GRNs with damaged quarantine handling.
* **Target Velocity:** 34 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-201** | Develop Supplier and Purchase Order CRUD API endpoints (`/api/v1/suppliers`, `/api/v1/inbound/po`). | Inbound Receiving | 5 | OpenAPI docs render PO status lifecycle transitions cleanly. |
| **TSK-202** | Integrate `Html5-QRCode` / `ZXing` camera and Bluetooth scanner input in Next.js PWA. | Mobile Scanning | 8 | Scanner decodes EAN-13 barcodes in $< 350$ ms with audio beep feedback. |
| **TSK-203** | Build PO line-item scan verification endpoint with remaining shelf-life check ($\ge 75\%$). | Inbound Receiving | 5 | Batches with $< 75\%$ shelf life are flagged with visual rejection banner. |
| **TSK-204** | Implement damaged carton logging with optional photo upload and quarantine status assignment. | Inbound Receiving | 5 | Quarantined units saved to `product_batches` with `quarantine_status='QUARANTINED'`. |
| **TSK-205** | Build atomic GRN completion transaction generating digital GRN and supplier credit note advisory. | Inbound Receiving | 8 | Commits GRN; creates `inventory_transactions` records; updates PO to `COMPLETED`. |
| **TSK-206** | Design printable internal warehouse carton/pallet barcode labels (EAN-128 format). | Inbound Receiving | 3 | Label layout prints cleanly on 4x6 inch thermal receipt/label printer. |

---

### 2.3 Sprint 3 (Weeks 5–6): Directed Putaway & Real-Time FEFO Inventory Ledger
* **Sprint Goal:** Enable guided pallet putaway into warehouse bins and enforce automated First-Expired, First-Out (FEFO) batch priority allocation.
* **Target Velocity:** 35 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-301** | Implement warehouse spatial bin layout API (`locations`) with zone and capacity constraints. | Spatial Putaway | 5 | Database rejects putaway suggestions into bins exceeding 500 kg or 300 units. |
| **TSK-302** | Develop Directed Putaway recommendation algorithm factoring SKU velocity (ABC) and temperature. | Spatial Putaway | 8 | Class-A chilled milk correctly routed to Chilled Zone Aisle 1 near dispatch dock. |
| **TSK-303** | Build mobile Directed Putaway PWA screen requiring destination bin scan confirmation. | Mobile Scanning | 5 | Operator cannot commit putaway without scanning the correct target bin barcode. |
| **TSK-304** | Develop Real-Time FEFO Priority Queue sorting batches by ascending `expiry_date`. | FEFO Engine | 8 | API test verifies stock allocation always selects nearest valid expiry batch. |
| **TSK-305** | Implement automated Expiry Watchlist background job (Safe, Watch, Warning, Critical $\le 14$ days). | FEFO Engine | 5 | Batches reaching expiration are automatically locked to `quarantine_status='EXPIRED'`. |
| **TSK-306** | Build interactive 2D spatial bin occupancy floor map in Next.js using CSS Grid / Canvas. | Frontend Visual | 4 | Bins color-code dynamically: Green ($< 70\%$), Amber ($70-90\%$), Red ($> 90\%$). |

---

### 2.4 Sprint 4 (Weeks 7–8): Sub-2.0s POS Sync API & Concurrency Row-Locking
* **Sprint Goal:** Build and stress-test the real-time POS stock deduction API, guaranteeing sub-2.0s response times and zero deadlocks across multiple registers, backed by offline client caching.
* **Target Velocity:** 36 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-401** | Implement `/api/v1/pos/sync` with pessimistic row-level locking (`SELECT ... FOR UPDATE`). | POS Concurrency | 8 | Automated benchmark demonstrates database lock duration $< 25$ milliseconds. |
| **TSK-402** | Implement `X-Idempotency-Key` token validation in Redis with 48-hour TTL. | POS Concurrency | 5 | Replaying duplicate POST request returns cached confirmation without double-deduction. |
| **TSK-403** | Develop POS register registry and telemetry heartbeat tracking online/offline status. | POS Concurrency | 5 | Dashboards highlight disconnected store cash registers in real time. |
| **TSK-404** | Implement client-side Service Worker and encrypted IndexedDB offline sales queue. | Offline Resilience | 8 | Disconnecting network allows 20 scans locally; auto-syncs upon link reconnect. |
| **TSK-405** | Develop bulk synchronization endpoint (`/api/v1/pos/bulk-sync`) for network recovery replay. | Offline Resilience | 5 | Bulk sync correctly processes 50 buffered offline transactions in order. |
| **TSK-406** | Build Locust load-test script simulating 10 POS cashiers competing for the last unit of milk. | QA & Testing | 5 | 100% of race conditions resolve cleanly; zero negative inventory balances occur. |

---

### 2.5 Sprint 5 (Weeks 9–10): Replenishment DSS & Outbound Wave Dispatch
* **Sprint Goal:** Implement mathematical inventory decision support models (EOQ, Greasley Safety Stock, ROP) and multi-branch outbound store wave picking.
* **Target Velocity:** 33 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-501** | Implement Dynamic EOQ formula module using historical annual demand and holding costs. | Decision Support | 5 | Computed EOQ matches manual mathematical formula verification within $0.01\%$. |
| **TSK-502** | Implement Greasley's Statistical Safety Stock formula factoring daily demand and vendor lead-time variance. | Decision Support | 8 | Output accounts for configured Z-scores (90%, 95%, 99%) and vendor $\sigma_L$. |
| **TSK-503** | Build dynamic ROP alert engine triggering automated draft Purchase Orders for procurement review. | Decision Support | 5 | Falling below ROP generates pre-filled draft PO ready for one-click approval. |
| **TSK-504** | Develop Branch Store Requisition Portal allowing store managers to submit weekly orders. | Store Requisition | 5 | Store order displays real-time central warehouse stock availability. |
| **TSK-505** | Build Wave Picking consolidation algorithm aggregating multiple store requisitions into one wave. | Outbound Picking | 5 | Aggregates duplicate SKU requests into single bulk pick task. |
| **TSK-506** | Implement shortest-path pick-list routing ordering picker travel by Aisle and Shelf sequence. | Outbound Picking | 5 | Picker walking distance reduced by $> 40\%$ compared to unsequenced list. |

---

### 2.6 Sprint 6 (Weeks 11–12): Cycle Counting, Anomaly Detection & BI Dashboards
* **Sprint Goal:** Implement continuous blind cycle counting, unsupervised ML shrinkage anomaly detection, and executive KPI analytics.
* **Target Velocity:** 30 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-601** | Implement Blind Cycle Counting sheets (system quantities hidden from floor counters). | Stocktaking & Audit | 5 | Mobile UI requires manual number input; reveals discrepancy only after submission. |
| **TSK-602** | Build supervisor discrepancy approval workflow with mandatory reason codes and photo proofs. | Stocktaking & Audit | 5 | Adjustments $> 1,000$ BDT require supervisor authorization before ledger commit. |
| **TSK-603** | Implement Scikit-learn `IsolationForest` model to detect anomalous shrinkage clusters. | Machine Learning | 8 | Model flags synthetic theft clusters across specific shift operators ($F1 > 0.85$). |
| **TSK-604** | Build Executive KPI Dashboard (Total Inventory Value, GMROI, Turnover Ratio, Spoilage Rate). | Executive BI | 6 | Dashboard renders historical trends using Chart.js / Recharts with sub-1.5s load. |
| **TSK-605** | Enforce database-level immutable audit ledger trigger on `inventory_transactions`. | Security & Audit | 6 | Direct SQL `DELETE` or `UPDATE` statements are blocked by database trigger exception. |

---

### 2.7 Sprint 7 (Weeks 13–14): Concurrency Stress-Testing, UAT & Viva Defense
* **Sprint Goal:** Conduct comprehensive load testing (50 req/s), complete end-to-end user acceptance testing (UAT), and prepare the interactive defense presentation.
* **Target Velocity:** 25 Story Points

| Task ID | Task Description | Epic | Est. Points | DoD Verification Step |
| :--- | :--- | :--- | :---: | :--- |
| **TSK-701** | Execute high-throughput Locust stress test (50 concurrent scanners, 10 POS registers). | Stress Testing | 8 | 99th percentile response time remains $< 1.5$ seconds with zero database errors. |
| **TSK-702** | Conduct OWASP ZAP security vulnerability scan on all authentication and API endpoints. | Security Audit | 5 | Zero Critical or High vulnerabilities identified; SSL Labs A+ rating verified. |
| **TSK-703** | Execute complete end-to-end UAT scenario covering receiving dock to retail POS checkout. | System Testing | 5 | All 6 personas execute workflows seamlessly on test hardware. |
| **TSK-704** | Finalize Capstone Project Proposal Part 1 & Part 2 documentation and interactive slides. | Academic Defense | 7 | Deliverables compiled to PDF; interactive showcase dashboard deployed online. |
