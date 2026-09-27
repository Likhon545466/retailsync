"""
Detailed Functional Requirements (FR-01 to FR-78), Traceability Matrix,
and Glossary for RetailSync Proposal.
Department of Software Engineering, Daffodil International University.
Course: SE-231 (System Analysis & Design / Capstone Project 2).
"""

# Appendix A: Detailed Functional Requirements (78 Detailed Specifications)
# Format: [ID, Module, Requirement Statement, Priority (M/S/C), Problem Link]
# M = Must Have (MVP), S = Should Have, C = Could Have (Enhancement)
DETAILED_FUNCTIONAL_REQUIREMENTS = [
    # A.1 Account, RBAC & Security (FR-01 to FR-06)
    ["FR-01", "Account & Access", "The system shall allow authorized warehouse personnel to log in securely using username/email and password with JWT token-based authentication.", "M", "P-09"],
    ["FR-02", "Account & Access", "The system shall enforce Role-Based Access Control (RBAC) with predefined roles: Warehouse Operator, Receiving Clerk, Floor Supervisor, Procurement Officer, Store Manager, and System Administrator.", "M", "P-09"],
    ["FR-03", "Account & Access", "The system shall support secure password reset functionality via email verification token.", "M", "P-09"],
    ["FR-04", "Account & Access", "The system shall automatically terminate user sessions after 15 minutes of inactivity on mobile scanning terminals to prevent unauthorized floor access.", "M", "P-09"],
    ["FR-05", "Account & Access", "The system shall allow administrators to create, update, deactivate, and assign specific operational zone permissions to warehouse worker accounts.", "M", "P-09"],
    ["FR-06", "Account & Access", "The system shall record every login, logout, and failed authentication attempt in an immutable security access log.", "S", "P-09"],

    # A.2 Product Master & Category Hierarchy (FR-07 to FR-13)
    ["FR-07", "Product Master", "The system shall manage a centralized product catalog storing SKU code, product name, brand, barcode (EAN-13/UPC/GS1-128), unit of measurement (UOM), and packaging dimensions.", "M", "P-01"],
    ["FR-08", "Product Master", "The system shall classify products into hierarchical categories: FMCG Dry Food, Perishable Produce, Chilled Dairy & Meat, Frozen Foods, Personal Care, and Household Non-Food.", "M", "P-02"],
    ["FR-09", "Product Master", "The system shall enforce temperature and storage classification attributes for each SKU (Ambient, Air-Conditioned 18-22°C, Chilled 2-4°C, Deep Frozen -18°C).", "M", "P-02"],
    ["FR-10", "Product Master", "The system shall maintain product shelf-life parameters, including total expected shelf life in days, minimum allowable receiving shelf life (%), and retail store dispatch threshold.", "M", "P-03"],
    ["FR-11", "Product Master", "The system shall allow configuration of financial costing parameters per SKU: unit purchase cost, estimated annual holding cost percentage, and fixed order processing cost.", "M", "P-05"],
    ["FR-12", "Product Master", "The system shall support bulk product master data import and export via standardized CSV/Excel templates.", "S", "P-01"],
    ["FR-13", "Product Master", "The system shall maintain ABC-velocity classification (Class A: High-turnover fast-moving; Class B: Medium; Class C: Slow-moving) recalculated monthly.", "M", "P-02"],

    # A.3 Supplier & Purchase Order Management (FR-14 to FR-20)
    ["FR-14", "Supplier & PO", "The system shall maintain a supplier directory containing company legal name, contact persons, phone numbers, trade license, lead time history, and payment terms.", "M", "P-07"],
    ["FR-15", "Supplier & PO", "The system shall allow procurement officers to create, edit, and issue digital Purchase Orders (POs) linked to specific approved suppliers.", "M", "P-05"],
    ["FR-16", "Supplier & PO", "The system shall automatically populate PO line items with recommended order quantities derived from the algorithmic EOQ/ROP decision engine.", "M", "P-05"],
    ["FR-17", "Supplier & PO", "The system shall support a multi-tier PO approval workflow (Draft -> Pending Approval -> Approved & Issued -> Partially Received -> Completed -> Cancelled).", "M", "P-05"],
    ["FR-18", "Supplier & PO", "The system shall track supplier delivery performance, automatically calculating on-time delivery rate, fulfillment accuracy, and lead-time standard deviation.", "S", "P-07"],
    ["FR-19", "Supplier & PO", "The system shall allow attaching supplier contracts, quality certificates, and digital invoice copies to corresponding PO records.", "C", "P-07"],
    ["FR-20", "Supplier & PO", "The system shall notify suppliers and procurement officers via email when a PO is issued or approaching its agreed delivery deadline.", "S", "P-07"],

    # A.4 Inbound Receiving & Goods Receipt Note (GRN) (FR-21 to FR-28)
    ["FR-21", "Inbound & GRN", "The system shall allow receiving clerks to look up open Purchase Orders by PO number, supplier name, or arrival schedule.", "M", "P-01"],
    ["FR-22", "Inbound & GRN", "The system shall validate delivered goods against PO line items in real time via handheld barcode scanner interrogation.", "M", "P-01"],
    ["FR-23", "Inbound & GRN", "The system shall record mandatory batch/lot numbers, manufacturing dates, and expiration dates for every received perishable and FMCG shipment.", "M", "P-03"],
    ["FR-24", "Inbound & GRN", "The system shall automatically reject or flag received batches failing to meet the minimum acceptable shelf-life threshold (e.g., less than 75% remaining life).", "M", "P-03"],
    ["FR-25", "Inbound & GRN", "The system shall record damaged, spoiled, or non-conforming items with reason codes and optional photographic evidence attachment.", "M", "P-01"],
    ["FR-26", "Inbound & GRN", "The system shall generate a formal digital Goods Receipt Note (GRN) upon receiving completion, categorizing accepted, rejected, and short-shipped quantities.", "M", "P-01"],
    ["FR-27", "Inbound & GRN", "The system shall automatically generate credit note advisories for short-shipped or rejected quantities to reconcile supplier invoicing.", "S", "P-01"],
    ["FR-28", "Inbound & GRN", "The system shall generate and print standardized warehouse internal pallet/carton barcode labels containing SKU, Batch ID, Expiry Date, and GRN number.", "M", "P-01"],

    # A.5 Warehouse Spatial Bin Layout & Putaway (FR-29 to FR-35)
    ["FR-29", "Spatial Putaway", "The system shall model warehouse spatial topology using a hierarchical structure: Zone (Dry, Chilled, Bulk, Pickface) -> Aisle -> Rack -> Shelf Tier -> Bin.", "M", "P-02"],
    ["FR-30", "Spatial Putaway", "The system shall assign a unique alphanumeric barcode and coordinate identifier to every physical bin location (e.g., Z1-A03-R02-S1-B04).", "M", "P-02"],
    ["FR-31", "Spatial Putaway", "The system shall enforce bin volumetric and weight capacity constraints, preventing putaway suggestions into overloaded bins.", "M", "P-02"],
    ["FR-32", "Spatial Putaway", "The system shall generate directed putaway instructions guiding operators to the optimal bin based on SKU velocity (Class A near dispatch docks) and temperature compatibility.", "M", "P-02"],
    ["FR-33", "Spatial Putaway", "The system shall require scanning the destination bin barcode to confirm physical placement before committing the inventory location change.", "M", "P-02"],
    ["FR-34", "Spatial Putaway", "The system shall provide a visual 2D interactive floor map displaying real-time bin utilization, occupancy percentage, and category zoning.", "S", "P-02"],
    ["FR-35", "Spatial Putaway", "The system shall allow authorized supervisors to execute internal bin-to-bin stock transfers with mandatory source and target bin scan verification.", "M", "P-02"],

    # A.6 Real-Time Inventory Ledger & Batch Expiry (FEFO) (FR-36 to FR-44)
    ["FR-36", "Ledger & FEFO", "The system shall maintain an immutable, append-only inventory transaction ledger recording every stock movement (Inbound, Putaway, Pick, Transfer, Adjustment, Write-Off).", "M", "P-04"],
    ["FR-37", "Ledger & FEFO", "The system shall compute real-time on-hand, allocated (reserved), and available-to-promise (ATP) inventory levels per SKU and batch.", "M", "P-04"],
    ["FR-38", "Ledger & FEFO", "The system shall enforce strict First-Expired, First-Out (FEFO) allocation logic, automatically queuing the batch with the earliest valid expiration date for outbound picking.", "M", "P-03"],
    ["FR-39", "Ledger & FEFO", "The system shall support FIFO (First-In, First-Out) fallback allocation for non-perishable goods that do not carry manufacturer expiration dates.", "M", "P-03"],
    ["FR-40", "Ledger & FEFO", "The system shall provide dynamic expiry alert windows, automatically classifying batches into: Safe (>60 days), Watch (31-60 days), Warning (15-30 days), and Critical (<=14 days).", "M", "P-03"],
    ["FR-41", "Ledger & FEFO", "The system shall automatically lock expired or recalled batches, mechanically preventing operators from picking them and transferring them to a Quarantine Bin.", "M", "P-03"],
    ["FR-42", "Ledger & FEFO", "The system shall enforce strict database ACID transactions to ensure stock decrements and allocations never result in negative stock balances.", "M", "P-04"],
    ["FR-43", "Ledger & FEFO", "The system shall provide complete forward and backward batch traceability (Supplier Lot -> GRN -> Warehouse Bin -> Store Dispatch -> Retail Outlet).", "M", "P-09"],
    ["FR-44", "Ledger & FEFO", "The system shall support cold-chain temperature logging history linked to specific perishable inventory batches.", "C", "P-09"],

    # A.7 Replenishment Engine & Decision Support (EOQ/ROP/SS) (FR-45 to FR-52)
    ["FR-45", "DSS Replenishment", "The system shall calculate the Economic Order Quantity (EOQ) dynamically using historical annual demand, fixed order cost, and unit holding cost.", "M", "P-05"],
    ["FR-46", "DSS Replenishment", "The system shall calculate statistical Safety Stock using Greasley’s dual-variance model, accounting for daily demand variance and supplier lead-time variance.", "M", "P-05"],
    ["FR-47", "DSS Replenishment", "The system shall allow procurement officers to configure desired Customer Service Levels (e.g., 90%, 95%, 97.5%, 99%) mapping to statistical Z-scores.", "M", "P-05"],
    ["FR-48", "DSS Replenishment", "The system shall compute Dynamic Reorder Points (ROP = (Average Daily Demand * Average Lead Time) + Safety Stock) for every active SKU.", "M", "P-05"],
    ["FR-49", "DSS Replenishment", "The system shall trigger automated replenishment alerts when an item's Inventory Position (On-Hand + On-Order - Allocated) breaches its ROP threshold.", "M", "P-05"],
    ["FR-50", "DSS Replenishment", "The system shall automatically compile suggested replenishment orders into draft Purchase Orders awaiting one-click procurement officer review.", "M", "P-05"],
    ["FR-51", "DSS Replenishment", "The system shall incorporate promotional demand uplift multipliers configured by merchandisers for festival periods (e.g., Eid, Ramadan, Puja).", "S", "P-05"],
    ["FR-52", "DSS Replenishment", "The system shall provide simulated 'what-if' cost-benefit modeling comparing current inventory carrying costs against proposed algorithmic parameters.", "C", "P-05"],

    # A.8 Outbound Store Requisition, Wave Picking & Dispatch (FR-53 to FR-60)
    ["FR-53", "Outbound Picking", "The system shall provide a multi-branch store portal allowing retail super shop managers to submit stock requisition orders to the central warehouse.", "M", "P-08"],
    ["FR-54", "Outbound Picking", "The system shall consolidate individual branch orders into optimized wave picking batches based on delivery vehicle schedules and warehouse zones.", "M", "P-06"],
    ["FR-55", "Outbound Picking", "The system shall generate optimized picking sequences ordering items by aisle and rack sequence to minimize picker walking distance.", "M", "P-06"],
    ["FR-56", "Outbound Picking", "The system shall require pickers to scan the bin barcode and product barcode to verify item identity and FEFO batch compliance during picking.", "M", "P-06"],
    ["FR-57", "Outbound Picking", "The system shall allow operators to flag short-picked items or damaged bin stock, immediately triggering dynamic replenishment or split-order handling.", "M", "P-06"],
    ["FR-58", "Outbound Picking", "The system shall support a staging and packing module where picked items are sorted into store-specific dispatch rolling cages or pallets.", "M", "P-06"],
    ["FR-59", "Outbound Picking", "The system shall generate an official Delivery Chalan / Dispatch Note and manifest linked to outbound transport vehicle plate numbers.", "M", "P-08"],
    ["FR-60", "Outbound Picking", "The system shall allow branch store managers to digitally acknowledge receipt of outbound shipments, reconciling in-transit variances.", "M", "P-08"],

    # A.9 Stocktaking, Cycle Counting & Discrepancy Auditing (FR-61 to FR-66)
    ["FR-61", "Cycle Counting", "The system shall support continuous cycle counting schedules based on ABC classification (Class A counted monthly, Class B quarterly, Class C biannually).", "M", "P-04"],
    ["FR-62", "Cycle Counting", "The system shall generate blind cycle count sheets where expected system quantities are masked from counters to prevent confirmation bias.", "M", "P-04"],
    ["FR-63", "Cycle Counting", "The system shall compare physical scan counts against book inventory, highlighting positive (surplus) and negative (shrinkage) discrepancies.", "M", "P-04"],
    ["FR-64", "Cycle Counting", "The system shall require supervisor approval and mandatory discrepancy reason codes (Breakage, Spoilage, Theft, Mislabeling) for inventory adjustments.", "M", "P-04"],
    ["FR-65", "Cycle Counting", "The system shall support an unsupervised machine-learning module (Isolation Forest) to detect unusual shrinkage clusters across SKUs, shifts, and zones.", "C", "P-04"],
    ["FR-66", "Cycle Counting", "The system shall generate financial shrinkage variance reports summarizing total inventory loss value over time.", "S", "P-04"],

    # A.10 Reporting, Dashboards & Analytics (FR-67 to FR-72)
    ["FR-67", "Reporting & BI", "The system shall provide an executive dashboard rendering real-time KPIs: Total Inventory Value, GMROI, Inventory Turnover Ratio, and Stockout Frequency.", "M", "P-09"],
    ["FR-68", "Reporting & BI", "The system shall render real-time floor telemetry: Active Inbound Unloading, Open Pick Waves, Bin Occupancy %, and Dispatch Dock Status.", "M", "P-02"],
    ["FR-69", "Reporting & BI", "The system shall generate a Perishable Expiry Watchlist report categorizing stock at risk of expiration within 7, 14, and 30 days.", "M", "P-03"],
    ["FR-70", "Reporting & BI", "The system shall provide a Supplier Performance Scorecard displaying On-Time In-Full (OTIF) rates, lead-time variance, and quality rejections.", "S", "P-07"],
    ["FR-71", "Reporting & BI", "The system shall provide an Outbound Store Fulfillment report analyzing branch requisition turnaround time and fulfillment accuracy.", "S", "P-08"],
    ["FR-72", "Reporting & BI", "The system shall allow export of all tabular data, reports, and audit logs into PDF and Excel (.xlsx) formats.", "M", "P-09"],

    # A.11 System Configuration, Audit Trail & Data Protection (FR-73 to FR-78)
    ["FR-73", "Config & Audit", "The system shall maintain an immutable, tamper-evident audit log of all system configuration changes, role updates, and manual inventory overrides.", "M", "P-09"],
    ["FR-74", "Config & Audit", "The system shall record client IP address, user agent, user ID, timestamp, and before/after values for all administrative database modifications.", "M", "P-09"],
    ["FR-75", "Config & Audit", "The system shall allow system administrators to configure system-wide parameters (default service level Z, expiry warning thresholds, warehouse operating hours).", "M", "P-09"],
    ["FR-76", "Config & Audit", "The system shall comply with the Bangladesh Personal Data Protection Ordinance 2025, ensuring worker and supplier contact details are encrypted and access-restricted.", "M", "P-09"],
    ["FR-77", "Config & Audit", "The system shall provide automated scheduled database backup utilities with off-site cloud storage synchronization.", "M", "P-09"],
    ["FR-78", "Config & Audit", "The system shall support multi-lingual user interface toggling between Bangla and English for all floor operator screens.", "S", "P-02"]
]

# Appendix B: Requirements Traceability Matrix
# Format: [Problem ID, Problem Description, Addressed by Objectives, Addressed by Functional Requirements, Addressed by NFRs]
TRACEABILITY_MATRIX = [
    ["P-01", "Disjointed Inbound Receiving & Manual GRN Verification", "O-01", "FR-07, FR-12, FR-21 to FR-28", "NFR-04, NFR-08, NFR-09"],
    ["P-02", "Warehouse Opacity & Blind Spatial Putaway (Bin Latency)", "O-02", "FR-08, FR-09, FR-13, FR-29 to FR-35, FR-68, FR-78", "NFR-04, NFR-08, NFR-11"],
    ["P-03", "Perishable Spoilage & Wastage from Non-FEFO Picking", "O-03", "FR-10, FR-23, FR-24, FR-38 to FR-41, FR-69", "NFR-03, NFR-12, NFR-13"],
    ["P-04", "Inventory Shrinkage, Phantom Stock & Discrepancies", "O-06", "FR-36, FR-37, FR-42, FR-61 to FR-66", "NFR-03, NFR-05, NFR-12"],
    ["P-05", "Inaccurate Replenishment: Over/Understocking Trap", "O-04", "FR-11, FR-15, FR-16, FR-17, FR-45 to FR-52", "NFR-04, NFR-10, NFR-14"],
    ["P-06", "Outbound Picking Inefficiencies & Wave Assembly Lag", "O-05", "FR-54 to FR-58", "NFR-04, NFR-05, NFR-08"],
    ["P-07", "Supplier Performance & Lead-Time Volatility Opacity", "O-04", "FR-14, FR-18, FR-19, FR-20, FR-70", "NFR-04, NFR-10, NFR-11"],
    ["P-08", "Information Silos Between Central DC & Branch Stores", "O-05", "FR-53, FR-59, FR-60, FR-71", "NFR-01, NFR-04, NFR-06"],
    ["P-09", "Regulatory Non-Compliance & Lack of Immutable Audit", "O-06", "FR-01 to FR-06, FR-43, FR-44, FR-72 to FR-77", "NFR-01, NFR-02, NFR-12, NFR-13"],
    ["Cross-Cutting", "Enterprise Security, Concurrency & Data Privacy", "O-06", "FR-01 to FR-06, FR-73 to FR-77", "NFR-01, NFR-02, NFR-03, NFR-05"],
    ["Cross-Cutting", "High Availability, Maintainability & Cost Efficiency", "O-06", "FR-72, FR-75, FR-77", "NFR-06, NFR-07, NFR-10, NFR-14"]
]

# Appendix C: Comprehensive Glossary of Terms (24 Industry Terms)
GLOSSARY = [
    ["SKU (Stock Keeping Unit)", "A distinct type of item for sale, such as a product and all of its attributes (size, flavor, packaging). Each unique item in the super shop warehouse is assigned a unique SKU code."],
    ["GRN (Goods Receipt Note)", "A formal digital or physical receipt issued by the receiving warehouse acknowledging that products delivered by a supplier have been physically received and inspected."],
    ["FEFO (First-Expired, First-Out)", "An inventory allocation and picking methodology where batches with the earliest expiration dates are dispatched first, regardless of when they physically arrived in the warehouse."],
    ["FIFO (First-In, First-Out)", "An inventory management method where the oldest physical stock is picked and dispatched first. Used in RetailSync as a fallback for non-perishable goods lacking manufacturer expiry dates."],
    ["EOQ (Economic Order Quantity)", "A mathematical formulation that determines the ideal order quantity a company should purchase to minimize total inventory costs, balancing order setup fees against holding costs."],
    ["Safety Stock (SS)", "A buffer level of extra stock held in the warehouse to mitigate the risk of stockouts caused by unpredictable fluctuations in consumer demand or supplier delivery delays."],
    ["ROP (Reorder Point)", "The specific inventory level that triggers the purchase of replenishment stock. Formulated as lead time demand plus safety stock: ROP = (d * L) + SS."],
    ["Putaway", "The physical and systematic process of moving received goods from the inbound unloading dock to their designated optimal storage bin location on the warehouse racks."],
    ["Pickface", "The designated front-facing, ground-accessible warehouse rack location from which operators physically pick goods to assemble outbound store orders."],
    ["Wave Picking", "A picking method where multiple store orders are grouped into consolidated 'waves' based on delivery routes or departure times to optimize picker travel efficiency."],
    ["Batch Picking", "A fulfillment technique where an operator picks the total required quantity of an item across multiple orders simultaneously in a single pass, sorting them at a staging station."],
    ["Cycle Counting", "An ongoing inventory auditing procedure where a small subset of warehouse inventory is physically counted on a continuous cyclical schedule without freezing entire warehouse operations."],
    ["Shrinkage", "The loss of inventory that can be attributed to factors such as employee theft, customer shoplifting, administrative paperwork errors, vendor fraud, and product breakage."],
    ["Phantom Inventory", "A discrepancy where the inventory management software records stock as available on-hand, but the physical item does not actually exist in the physical bin location."],
    ["Lead Time (L)", "The total elapsed latency from the moment a purchase order is submitted to a supplier until the goods are physically delivered, inspected, and made available in the warehouse."],
    ["On-Time In-Full (OTIF)", "A premier supply chain KPI measuring the percentage of supplier deliveries that arrived within the agreed delivery window containing 100% of the ordered quantities."],
    ["ABC Classification", "An inventory categorization method based on the Pareto Principle (80/20 rule), classifying goods into Class A (high-value / fast-moving), Class B (moderate), and Class C (low)."],
    ["Quarantine Bin", "A dedicated physical and logical storage area in the warehouse reserved strictly for expired, recalled, or damaged items, mechanically locked from outbound picking."],
    ["Cross-Docking", "A logistics practice where inbound goods from a supplier are transferred directly to outbound store dispatch staging with minimal or zero intermediate warehouse storage."],
    ["Delivery Chalan", "A legal transport document and dispatch note accompanying outbound goods delivered to retail branch stores, detailing line item quantities and transport details."],
    ["GS1-128 / EAN-13", "International barcode standards used across the retail supply chain to encode product identification, batch lot numbers, weight, and expiration dates."],
    ["ACID Compliance", "Database properties (Atomicity, Consistency, Isolation, Durability) ensuring reliable execution of stock transaction ledgers without concurrency collisions or negative stock balances."],
    ["PDPO (2025)", "The Personal Data Protection Ordinance 2025 of Bangladesh, regulating the collection, storage, processing, and protection of personal data of warehouse staff and suppliers."],
    ["GMROI", "Gross Margin Return on Investment: A retail inventory profitability evaluation metric analyzing a firm's ability to turn inventory into cash above the cost of the inventory."]
]

# Section 14.2: Implemented Now vs Future Scope Matrix
IMPLEMENTATION_SCOPE_MATRIX = [
    ["Functional Capability", "Available Industrial Tech", "Included in Capstone MVP", "Deferred to Future Scope"],
    ["Inbound Barcode Scans", "Handheld Android terminals, 2D Barcode scanners", "Web-based camera scan + USB/Bluetooth barcode scanner integration", "Automated high-speed conveyor tunnel scanners"],
    ["Spatial Bin Putaway", "2D/3D digital twin warehouse maps, pick-to-light", "Visual 2D Zone-Aisle-Rack-Bin layout with capacity validation", "Automated Guided Vehicles (AGVs) and robotic shuttle putaway"],
    ["FEFO Expiry Allocation", "Relational database date indexing, dynamic queues", "Native PostgreSQL date indexing with automated quarantine locks", "Automated RFID sensor tags measuring real-time produce decay"],
    ["Replenishment Decision", "Statistical engines, complex enterprise ERP", "Dynamic EOQ, Greasley Statistical Safety Stock, and ROP triggers", "Deep Reinforcement Learning multi-echelon neural networks"],
    ["Multi-Store Wave Picking", "Voice picking, automated pick-to-light carts", "Consolidated wave creation, shortest-path digital pick-lists", "Autonomous robotic mobile picking arms"],
    ["Cycle Count Discrepancy", "Cycle counting software, RFID drone flyover", "Blind cycle count entry, automated variance calculation", "Autonomous drone inventory scanning across vertical racks"],
    ["Store Requisition Portal", "B2B web portals, electronic data interchange", "Responsive web portal for branch managers to request stock", "Nationwide retail Electronic Data Interchange (EDI) network"]
]

# Section 15: Agile 6-Iteration Sprint Breakdown
AGILE_SPRINTS = [
    ["Iteration", "Sprint Focus", "Requirements Addressed", "Sprint Deliverable & Milestone"],
    ["Sprint 1 (Weeks 1-3)", "Architecture & Foundation", "FR-01 to FR-06, FR-07 to FR-13, NFR-01 to NFR-03", "Core system architecture, normalized PostgreSQL schema, JWT authentication, RBAC, Product Master catalog."],
    ["Sprint 2 (Weeks 3-5)", "Supplier & Inbound Receiving", "FR-14 to FR-28, NFR-04, NFR-08", "Supplier directory, PO workflow, mobile dock receiving module, barcode scan verification, digital GRN generator."],
    ["Sprint 3 (Weeks 5-8)", "Spatial Putaway & FEFO Ledger", "FR-29 to FR-44, NFR-03, NFR-09", "Warehouse spatial bin mapping, directed putaway engine, immutable transaction ledger, FEFO allocation queue."],
    ["Sprint 4 (Weeks 8-10)", "Replenishment DSS Engine", "FR-45 to FR-52, NFR-10, NFR-14", "Dynamic EOQ, Greasley's Statistical Safety Stock, dynamic ROP alerting, automated draft PO creation module."],
    ["Sprint 5 (Weeks 10-12)", "Wave Picking & Store Portal", "FR-53 to FR-60, FR-61 to FR-66, NFR-05", "Multi-store requisition portal, wave picking engine, pick-path optimization, cycle count auditing, dispatch chalan."],
    ["Sprint 6 (Weeks 12-14)", "Analytics, Hardening & Evaluation", "FR-67 to FR-78, All NFRs", "Executive KPI dashboard, security hardening, user acceptance testing (UAT), final report manuscript and capstone defense."]
]

# Section 16.1: Resources Planning
RESOURCES_PLAN = [
    ["Resource Category", "Specific Technology / Asset", "Purpose in Project Implementation", "Acquisition & Budget Strategy"],
    ["Development Framework", "Next.js (React), Node.js / Express or Python Fastify", "Responsive frontend web portal and high-throughput REST API services.", "Open source; zero licensing cost."],
    ["Database & Caching", "PostgreSQL 16 with B-Tree indexes, Redis for caching", "ACID-compliant relational ledger, spatial bin tracking, and session cache.", "Open source; locally hosted / Docker."],
    ["Barcode Scanning", "Bluetooth 1D/2D Handheld Barcode Scanner + Smartphone Camera", "Physical barcode interrogation for inbound receiving, putaway, and picking.", "Existing personal devices & low-cost USB barcode reader."],
    ["Containerization", "Docker & Docker Compose", "Reproducible development, local multi-service testing, and deployment.", "Free community edition."],
    ["Cloud & Hosting", "Vercel / Supabase / Render / Academic Cloud Tier", "Staging environment for remote testing and capstone committee evaluation.", "Free academic student developer tier."],
    ["Testing & CI/CD", "Jest, Supertest, GitHub Actions", "Automated unit testing of mathematical models and continuous integration.", "Free open-source tooling."],
    ["Documentation & Diagrams", "Mermaid.js, Draw.io, MS Word / LibreOffice", "UML diagrams, flowcharts, ERD schemas, and academic project manuscripts.", "Included in academic software suite."]
]

print("Appendices and sprint data loaded successfully.")
