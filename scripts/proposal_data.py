"""
Structured Data for RetailSync Capstone Proposal
(Centralized Super Shop Warehouse Management System)
Department of Software Engineering, Daffodil International University
Course: SE-231 (System Analysis & Design / Capstone Project 2)
"""

# Market Indicators for Bangladesh Modern Trade & Grocery Retail
MARKET_INDICATORS = [
    ["Urban Population in Bangladesh", "Approx. 65.2 million people (39.7% of total population, Census 2022 / BBS). Rapid urbanization driving demand for centralized retail."],
    ["Modern Trade Grocery Share", "Currently ~2.5% to 3.2% of national grocery trade; projected to reach 10-12% by 2030 with a 16.5% CAGR in major metropolitan zones (Dhaka, Chittagong, Sylhet)."],
    ["FMCG Retail Wastage & Spoilage", "15% to 22% of perishable goods (dairy, fresh produce, meat, chilled foods) wasted annually across retail supply chains due to lack of FEFO batch tracking."],
    ["Retail Stockout Revenue Loss", "Estimated 7.5% to 11.2% in unrealized revenue caused by sudden out-of-stock events on high-velocity FMCG items and delayed procurement reorders."],
    ["Inventory Shrinkage Rate", "Average 1.8% to 2.4% of total inventory value lost to unrecorded shelf damages, theft, phantom inventory counts, and untracked supplier delivery discrepancies."],
    ["Central Warehouse Lead Time", "Average order-to-shelf replenishment cycle takes 48 to 72 hours from central distribution centers to retail outlets due to manual picking and sorting bottlenecks."],
    ["Barcode / Scanning Penetration", "Over 95% of packaged FMCG items carry standard GS1/EAN barcodes, but warehouse putaway and picking remains largely manual paper-manifest driven."]
]

# Section 3: Problem Statements (P-01 to P-09)
PROBLEMS = [
    ["P-01", "Disjointed Inbound Receiving and Error-Prone Manual GRN Verification", 
     "Inbound supplier deliveries are checked against paper purchase orders, leading to undetected quantity discrepancies, damaged packaging acceptance, and slow Goods Receipt Note (GRN) generation.",
     "Digital Inbound Verification with handheld barcode scanning, real-time PO reconciliation, and automated digital GRN generation with variance capture."],
    ["P-02", "Warehouse Opacity and Blind Spatial Putaway (Bin Search Latency)", 
     "Floor workers place received pallets in random, unindexed warehouse locations without systematic bin mapping, causing severe search latency and misplaced stock during picking.",
     "Directed Spatial Putaway Engine with real-time Zone-Aisle-Rack-Shelf-Bin spatial mapping and capacity-aware putaway suggestions."],
    ["P-03", "Perishable Spoilage and Financial Loss from Non-FEFO Picking", 
     "Warehouse operators pick goods on a naive LIFO or convenient nearest-bin basis rather than earliest expiry, resulting in billions of BDT in spoiled dairy, juices, and packaged food.",
     "Strict FEFO (First-Expired, First-Out) batch allocation algorithm that dynamically directs pickers to the batch with the nearest expiration date."],
    ["P-04", "Inventory Shrinkage, Unreconciled Discrepancies, and Phantom Stock", 
     "Physical stock levels consistently diverge from spreadsheet records due to unrecorded breakages, internal theft, and paper tally omissions, leading to 'phantom inventory'.",
     "Continuous Cycle Counting Module, immutable audit ledgers, and machine-learning-assisted anomaly/shrinkage detection."],
    ["P-05", "Inaccurate Stock Replenishment: The Overstocking vs. Understocking Trap", 
     "Procurement officers rely on intuitive guesswork, causing capital lockup in slow-moving items and disastrous stockouts during peak promotional weekends and holidays.",
     "Algorithmic Replenishment Engine integrating Economic Order Quantity (EOQ), Greasley's Statistical Safety Stock, and Dynamic Reorder Point (ROP)."],
    ["P-06", "Outbound Picking Inefficiencies and Order Assembly Bottlenecks", 
     "Outbound orders for multi-branch retail outlets are picked piece-by-piece with redundant travel paths across warehouse aisles, causing dock congestion and late store delivery.",
     "Optimized Wave and Batch Picking algorithms generating shortest-path picker routing and multi-store sortation staging."],
    ["P-07", "Supplier Performance and Lead-Time Volatility Opacity", 
     "Retailers have zero telemetry on supplier delivery timeliness, lead-time variance, or product rejection rates, crippling negotiation leverage and safety stock precision.",
     "Supplier SLA Performance Scorecards tracking fulfillment accuracy, lead-time standard deviation, and historical damage rates."],
    ["P-08", "Information Silos Between Central Warehouses and Branch Super Shops", 
     "Retail store managers cannot see real-time warehouse stock positions, leading to duplicate emergency store requisitions and uneven stock distribution across branches.",
     "Unified Multi-Store Requisition Portal with real-time central stock visibility, store stock reservation, and in-transit dispatch tracking."],
    ["P-09", "Regulatory Non-Compliance and Lack of Immutable Audit Ledgers", 
     "Failure to document batch origins and cold-chain compliance violates the Bangladesh Food Safety Act 2013 and BSTI standards, risking heavy penalties and brand damage.",
     "Complete Batch-to-Store Traceability, digital chain-of-custody logging, and automated compliance reporting."]
]

# Section 4: Existing Solution Gap & Competitor Comparison
COMPETITOR_COMPARISON = [
    ["Capability / Operational Dimension", "Manual Sheets / Paper", "Standalone POS (e.g. PrismPOS, Tally)", "Legacy Tier-1 ERP (e.g. SAP / Oracle)", "Proposed RetailSync"],
    ["Real-Time Barcode Inbound & GRN", "No (Manual logbooks)", "Limited (POS-centric)", "Yes (High complexity)", "Yes (Intuitive, fast mobile UI)"],
    ["Dynamic Spatial Bin & Rack Mapping", "No (Worker memory)", "No (Only SKU counts)", "Yes (Rigid setup)", "Yes (Visual 2D/3D zone bin map)"],
    ["Enforced FEFO Expiry Allocation", "No (Frequent spoilage)", "Rarely (Static FIFO only)", "Yes (Custom configuration)", "Yes (Native FEFO priority queue)"],
    ["Greasley Statistical Safety Stock", "No (Arbitrary min-max)", "No (Static thresholds)", "Partial (Requires manual tuning)", "Yes (Dynamic statistical model)"],
    ["Automated EOQ & Dynamic ROP", "No (Human guesswork)", "No (Basic reorder alert)", "Yes (Complex add-on module)", "Yes (Native DSS engine)"],
    ["Wave & Batch Picking Routing", "No (Random walking)", "No (Single order billing)", "Yes (Enterprise tier)", "Yes (Optimized pick-path wave)"],
    ["Multi-Branch Store Requisitions", "No (Phone calls / email)", "Limited (Separate databases)", "Yes (Centralized)", "Yes (Unified branch requisition portal)"],
    ["Cycle Counting & Discrepancy Audit", "No (Annual painful audit)", "Partial (End-of-day tally)", "Yes (Formal audit)", "Yes (Continuous cycle counting)"],
    ["Total Cost & Implementation Agility", "Low cost / high waste", "Low / Siloed functionality", "Extremely expensive (Crores BDT)", "Cost-effective, modern, modular"]
]

# Section 5: Product Positioning & Differentiation
DIFFERENTIATION_DIMENSIONS = [
    ["Operational Dimension", "Typical Retail Warehouse Software", "RetailSync Value Proposition"],
    ["Putaway Strategy", "Static bin allocation; items dumped wherever space is found.", "Directed spatial putaway based on product category, velocity (ABC classification), and bin capacity limits."],
    ["Perishable Handling", "Naive FIFO (First-In, First-Out) or unmanaged picking causing expiry loss.", "Strict FEFO (First-Expired, First-Out) batch routing, proactive expiry alert windows, and automated quarantine locks."],
    ["Inventory Replenishment", "Manual reordering based on panic when shelves empty.", "Mathematical DSS calculating dynamic EOQ, Greasley Safety Stock, and ROP factoring in supplier lead-time variance."],
    ["Outbound Assembly", "Single-order manual picking with excessive walking time.", "Consolidated wave/batch picking with intelligent pick-path ordering to minimize travel distance across aisles."],
    ["Store-Warehouse Sync", "Store managers call or email central DC with unverified orders.", "Dedicated Store Requisition Portal with live stock visibility, automated allocation, and dispatch delivery notes."],
    ["Operational Usability", "Bloated, complex enterprise interfaces requiring months of training.", "Clean, responsive mobile/tablet web UI with rapid barcode gun scanning and intuitive visual dashboards."]
]

# Section 6.3: Stock Alert & Severity Escalation Model
SEVERITY_MODEL = [
    ["Level", "Designation", "Trigger Conditions", "System Action & Floor Workflow", "Primary Stakeholders"],
    ["Level 0", "Normal Operating State", "Stock levels between Reorder Point (ROP) and Maximum Capacity; Expiry > 90 days.", "Standard operations; real-time dashboard telemetry updates; no intervention needed.", "Floor Operators, Supervisors"],
    ["Level 1", "Routine Replenishment Advisory", "Inventory position approaches ROP (within 10% buffer); or planned promotional demand surge.", "Automated advisory generated in Procurement Queue; suggested order quantity calculated via EOQ.", "Procurement Officers, Buyers"],
    ["Level 2", "Attention: Slow-Moving / Expiry Watch", "Stock turnover rate drops below 25th percentile for category; or batch expiry window between 30 and 60 days.", "Floor alert to trigger clearance allocation; automated notification to retail merchandising for promotional discounting.", "Inventory Supervisor, Store Managers"],
    ["Level 3", "Concern: Imminent Stockout / Safety Stock Breach", "Inventory Position drops strictly below Safety Stock threshold; or batch expiry within 14 days.", "High-priority alert badge; automated Draft Purchase Order dispatched to approved suppliers; store order quota rationing enabled.", "Procurement Officers, SCM Head"],
    ["Level 4", "Critical Emergency / Quarantine Lock", "Physical stock reaches zero (Stockout); or batch expiration date reached; or severe physical damage detected.", "Immediate system lock on SKU/batch to prevent picking; automated quarantine bin transfer order; urgent escalation alert to VP Supply Chain.", "All Floor Staff, Procurement, Executives"]
]

# Section 8: Target Users & Stakeholders
TARGET_USERS = [
    ["User Category", "Operational Role", "Primary Daily Responsibilities & Pain Points", "Key RetailSync Capabilities Utilized"],
    ["Warehouse Floor Operator", "Direct Operational (Floor)", "Pallet unloading, bin putaway, shelf picking, order packing. Pain: searching for misplaced boxes, heavy paperwork.", "Mobile scanner UI, directed putaway prompts, digital pick lists, instant barcode verification."],
    ["Inbound Receiving Clerk", "Tactical Operational (Dock)", "Inspecting supplier deliveries, validating purchase orders, logging damages. Pain: paper PO matching errors.", "Digital PO lookup, barcode printing, discrepancy logging, automated Goods Receipt Note (GRN) generation."],
    ["Inventory Floor Supervisor", "Tactical Management", "Stock accuracy, bin space utilization, cycle counting, shelf life tracking. Pain: phantom inventory, unrecorded shrinkage.", "Live 2D spatial bin monitor, cycle count assignment, expiry tracking dashboard, discrepancy reconciliation."],
    ["Procurement & SCM Officer", "Strategic Tactical", "Vendor negotiation, purchase order issuance, stock replenishment planning. Pain: unexpected stockouts, volatile supplier lead times.", "Algorithmic replenishment portal (EOQ/ROP), supplier SLA scorecard, automated reorder triggers, lead-time variance tracking."],
    ["Branch Super Shop Store Manager", "Operational Recipient (Store)", "Ordering store stock from central warehouse, receiving store deliveries, shelf restocking. Pain: unfulfilled requisitions, stockout shelves.", "Store Requisition Portal, live central DC inventory visibility, dispatch delivery tracking, transit loss reconciliation."],
    ["Warehouse Systems Admin / DevOps", "Technical Support", "User access provisioning, system uptime, database performance, audit trail integrity. Pain: database locks, unauthorized changes.", "Role-Based Access Control (RBAC), database indexing telemetry, system health monitors, immutable audit logs."],
    ["Executive Management (Director/VP)", "Strategic Executive", "Working capital efficiency, inventory turnover, perishable waste reduction, retail chain profitability. Pain: lack of high-level insights.", "Executive KPI dashboard, inventory turnover analytics, shrinkage reports, gross margin return on inventory (GMROI)."]
]

STAKEHOLDER_MATRIX = [
    ["Stakeholder Group", "Primary Role", "Core Interests & Strategic Drivers", "Influence", "Engagement Strategy"],
    ["Warehouse Floor Staff", "Direct System Users", "Ease of use, fast scanning, elimination of manual paperwork, fair workload tracking.", "High", "Co-design mobile scanner interfaces, conduct hands-on usability testing, iterative feedback."],
    ["Procurement & Supply Chain Team", "Operational Decision Makers", "High service levels (>98%), low holding costs, reliable supplier lead-time tracking, automated EOQ/ROP.", "High", "Collaborate on replenishment algorithms, validate supplier SLA metrics, bi-weekly reviews."],
    ["Super Shop Branch Managers", "Downstream Beneficiaries", "On-time full delivery (OTIF), accurate store consignments, zero damaged/expired goods received.", "High", "Design intuitive store requisition portal, provide clear in-transit order tracking."],
    ["Executive Committee / Sponsors", "Strategic Steering", "Working capital reduction, waste minimization, gross margin expansion, return on investment (ROI).", "High", "Executive KPI dashboards, sprint demos, comprehensive financial impact reporting."],
    ["Suppliers & Distributors", "External Partners", "Predictable purchase orders, fast dock turnaround, clear rejection rationale on damaged lots.", "Medium", "Standardized electronic POs, transparent digital GRN inspection notes, SLA scorecards."],
    ["Regulatory Bodies (BFSA, BSTI)", "Compliance & Legal", "Consumer food safety, strict expiration date adherence, batch traceability, hygienic storage.", "Medium", "Enforce strict FEFO controls, immutable batch audit logs, automated compliance reporting."]
]

# Grounded Value Taxonomy: Explicit Epistemological Classification for All Claimed Metrics
GROUNDED_VALUE_TAXONOMY = [
    ["Metric / Parameter", "Claimed Baseline / Target", "Formal Classification", "Empirical Grounding / Verification Protocol"],
    ["Perishable Spoilage Rate", "15% to 22% annual dairy/produce loss", "Industry Case Study & Literature Baseline", "Documented in Bangladesh Supermarket Owners Association (BSOA) field reports and FAO South Asia Post-Harvest Retail Loss assessments in urban grocery chains."],
    ["Phantom Shrinkage Write-offs", "1.8% to 2.4% unexplained inventory loss", "Industry Benchmark Baseline", "Aligned with National Retail Security Survey (NRSS) supermarket shrinkage baselines adapted for un-barcoded local FMCG supply chains in Dhaka."],
    ["Peak-Hour Stockout Losses", "7.5% to 11.2% lost retail revenue", "Industry Benchmark Baseline", "Derived from IHL Group retail out-of-stock studies during festive demand spikes (Ramadan, Eid-ul-Fitr, weekend rushes in Dhaka super shops)."],
    ["POS Checkout Scan Latency", "≤ 2.0s (p95 ≤ 800ms, p99 ≤ 1.5s)", "Empirical Engineering SLO", "Testable engineering SLA to be verified empirically via Locust multi-threaded load tests executing atomic row-level locks on PostgreSQL 16."],
    ["Barcode Decode Latency", "≤ 350 ms visual confirmation", "Empirical Hardware SLO", "Verified on physical consumer Android smartphone (Chrome PWA) paired with Bluetooth HID trigger scanner using ZXing/Html5-QRCode."],
    ["Post-Implementation Spoilage", "Reduced from 22% down to < 6%", "Modeled Simulation Assumption", "Mathematical pilot projection assuming 100% strict FEFO compliance and automated quarantine threshold (<= 3 days) eliminating rear-of-bin rotting."],
    ["Stockout Frequency Reduction", "> 60% reduction during surges", "Modeled Simulation Assumption", "Projected outcome of replacing static monthly manual reorders with automated 7-day rolling AI demand forecasting and Greasley dynamic safety stock."],
    ["Terminal Hardware Cost", "< 16,000 BDT per station (90% savings)", "Empirical Budget Benchmark", "Direct market quotation pairing consumer Android smartphone (12,000 BDT) with Bluetooth trigger grip (3,800 BDT) vs 60,000 BDT Zebra TC52."],
    ["Offline Queue Resilience", "Buffer ≥ 200 sales with 0 loss", "Empirical Software SLO", "Verified by simulating Wi-Fi disconnection on PWA client, storing sales in IndexedDB, and executing bulk idempotent sync upon reconnect."]
]

# Section 10.2: SMART Specific Objectives (O-01 to O-05) - Formally Structured
UPGRADED_SMART_OBJECTIVES = [
    ["ID", "Objective Domain", "SMART Target & Quantitative Metric", "Measurement Protocol & Verification Gate", "Sprint Target"],
    ["O-01", "Sub-Second POS Concurrency & ACID Integrity", 
     "Execute atomic stock deductions from retail cash registers via PostgreSQL row-level locks (SELECT ... FOR UPDATE), achieving p95 latency ≤ 800ms and p99 ≤ 1.5s with exactly zero deadlocks and zero negative balances across 10 concurrent registers.", 
     "Automated Locust multi-threaded load test simulating 10 concurrent cashiers competing for the last inventory batch.", 
     "Sprint 4 (Weeks 7–8)"],
    ["O-02", "Automated FEFO Priority & Food Safety Quarantine", 
     "Enforce database-level First-Expired, First-Out allocation ensuring 100% of store replenishment orders pick earliest expiring batches; automatically quarantine stock reaching ≤ 3 days to expiry, reducing spoilage to < 6% in pilot simulations.", 
     "Automated Pytest batch sorting assertions and Celery scheduled quarantine state transition triggers.", 
     "Sprint 3 (Weeks 5–6)"],
    ["O-03", "AI-Driven Demand Forecasting & Dynamic Replenishment", 
     "Deploy a Machine Learning Time-Series Forecasting engine (LightGBM/XGBoost) achieving MAPE ≤ 15% on high-velocity FMCG items; dynamically compute Reorder Points (ROP) using Greasley's Safety Stock with calendar festival embeddings (Ramadan, Eid).", 
     "Backtesting against 12-month FMCG sales series with walk-forward validation and automated draft PO comparison.", 
     "Sprint 5 (Weeks 9–10)"],
    ["O-04", "Frugal Hardware Architecture & Sub-350ms Scanning", 
     "Engineer a mobile Progressive Web Application (PWA) running on consumer Android smartphones paired with Bluetooth HID trigger grips (< 4,000 BDT), achieving barcode decode-to-render latency ≤ 350ms and cutting terminal capex by 90%.", 
     "Physical hardware testing on Android 13 smartphone using EAN-13 and Code-128 test carton labels.", 
     "Sprint 2 (Weeks 3–4)"],
    ["O-05", "Offline Network Resilience & Idempotent Replay", 
     "Implement Service Worker background sync and encrypted IndexedDB client storage to buffer ≥ 200 sales transactions during warehouse broadband outages, replaying idempotently via Redis X-Idempotency-Key upon connection restoration.", 
     "Manual and simulated network blackout drills with Wi-Fi disconnection during peak scanning.", 
     "Sprint 4 (Weeks 7–8)"]
]

# 4-Quadrant Defense-Proof Scope Boundaries
UPGRADED_SCOPE_MATRIX = [
    ["Boundary Dimension", "In-Scope Modules & Features", "Operational / Pilot Boundaries", "Explicit Out-of-Scope (Won't Have)"],
    ["Functional Capabilities", 
     "• Inbound barcode receiving & digital GRN\n• Directed spatial putaway (ABC velocity)\n• Real-time FEFO batch ledger & quarantine\n• Sub-2.0s POS concurrency deduction\n• AI Demand Forecasting & Dynamic ROP DSS\n• Blind cycle counting with supervisor signoff\n• Isolation Forest shrinkage anomaly ML",
     "• Pilot Testbed: 1 Central Distribution Center + up to 3 Retail Branch Stores\n• SKU Catalog: 500 representative FMCG items (Perishable, Chilled, Ambient, Household)\n• Concurrency: 10 concurrent POS registers + 10 mobile warehouse scanners",
     "• No full corporate double-entry general ledger or payroll accounting (exports CSV/JSON audit trails for external ERPs)\n• No autonomous robotic cranes (AGVs) or motorized conveyor belts\n• No direct-to-consumer delivery or rider tracking app\n• No credit card merchant banking payment gateways (POS handles financial settlement externally)"],
    ["Technical & Architecture", 
     "• Next.js 14 PWA (TypeScript, Tailwind CSS)\n• FastAPI asynchronous backend (Python 3.11+)\n• PostgreSQL 16 (3NF ACID Relational Ledger)\n• Redis 7 (Idempotency locks, session cache)\n• Celery / Redis Worker for AI inference\n• Docker Compose multi-container deployment",
     "• Cloud Staging VPS (4 vCPU, 8GB RAM)\n• Client: Android 13+ Chrome Mobile Browser\n• Scanner: Bluetooth HID 1D/2D Barcode Trigger\n• IoT Edge: ESP32 MCU dock gate scanner (MQTT)",
     "• No custom silicon ASIC development\n• No proprietary closed-source database engines\n• No native iOS Swift app (PWA standard covers cross-platform access)"],
    ["Assumptions & Dependencies", 
     "• Standard EAN-13 / Code-128 barcodes printed on packaging\n• Stable local Wi-Fi / 4G coverage at central DC (with offline fallback)\n• Super shop management cooperation for pilot catalog seed data",
     "• Pilot duration: 4 weeks of simulated operational runs\n• Baseline parameters derived from published BSOA & FAO retail studies",
     "• Does not assume uninterrupted high-speed internet (designed offline-first)\n• Does not require expensive Zebra or Honeywell handheld hardware"]
]

# Scenario-Based Validation Milestones
SCENARIO_VALIDATION_DATA = [
    ["Scenario ID & Title", "Operational Context & Injection Event", "System Behavior & Algorithmic Response", "Success / Acceptance Criteria", "Sprint Alignment"],
    ["Scenario A: Inbound Dock Quality Gate", 
     "Supplier delivers 100 crates of pasteurized milk; 10 crates carry expiration dates with only 2 days remaining (< 75% shelf-life threshold).", 
     "Clerk scans carton barcode; system evaluates remaining shelf-life percentage; mechanically locks the 10 short-dated crates to 'QUARANTINED'; generates digital GRN for 90 accepted units and auto-generates supplier credit note advisory.", 
     "Zero expired/short-dated units enter active warehouse bins; digital GRN variance accurately reflects supplier delivery penalty.", 
     "Sprint 2 (Week 4)"],
    ["Scenario B: Rush-Hour POS Concurrency", 
     "Friday 8:00 PM peak rush: 10 branch cashiers ring up the final 5 remaining units of 1L soybean oil simultaneously across registers.", 
     "FastAPI POS sync endpoint executes pessimistic row lock (SELECT ... FOR UPDATE) on the earliest active batch. The first 5 requests decrement inventory atomically in < 800ms. The remaining 5 requests receive immediate 'Out of Stock' response.", 
     "Zero overselling; exactly zero negative inventory balances; zero database deadlocks; p95 latency remains ≤ 800ms.", 
     "Sprint 4 (Week 8)"],
    ["Scenario C: Network Blackout & Replay", 
     "Central broadband fiber is severed during peak retail floor sales; 50 customer checkout transactions occur while offline.", 
     "PWA Service Worker detects offline status; queues encrypted sales transactions in client IndexedDB. Upon network recovery, client automatically submits bulk sync. Backend Redis checks X-Idempotency-Key and commits all 50 sales in order.", 
     "100% of offline sales recorded in database upon reconnect; zero duplicate deductions; zero transaction dropouts.", 
     "Sprint 4 (Week 8)"],
    ["Scenario D: Festival AI Demand Surge", 
     "14 days prior to holy Ramadan: historical baseline daily sales for cooking oil is 50 units/day; holiday surge spikes demand to 220 units/day.", 
     "The LightGBM time-series model identifies the upcoming Ramadan calendar embedding flag; projects 220 units/day demand; dynamically recalculates ROP and Greasley Safety Stock; triggers automated draft PO 10 days in advance.", 
     "Draft PO approved by procurement officer; stock arrives 3 days before festival; supermarket experiences 0% stockouts during rush.", 
     "Sprint 5 (Week 10)"]
]

# Section 10.2: SMART Specific Objectives (O-01 to O-06)
SMART_OBJECTIVES = [
    ["ID", "Objective Statement", "Target Metric & Verifiable Evaluation Criteria", "Timeline"],
    ["O-01", "Accelerate Inbound Receiving and Digital GRN Generation", "Reduce average inbound unloading-to-dock verification time from 45 minutes to under 12 minutes per shipment (73% reduction); achieve 100% digital GRN generation with zero paper manifests.", "Phase 2 (Sprint 2)"],
    ["O-02", "Eliminate Misplaced Stock via Directed Spatial Putaway", "Achieve 99.5% bin location accuracy across all warehouse zones; reduce putaway search and placement time by 60% through barcode-guided bin destination routing.", "Phase 3 (Sprint 3)"],
    ["O-03", "Minimize Perishable Spoilage via Automated FEFO Allocation", "Achieve 100% compliance with First-Expired, First-Out (FEFO) picking logic on perishable and dairy SKUs, reducing warehouse expiry wastage by at least 65% in pilot trials.", "Phase 3 (Sprint 4)"],
    ["O-04", "Optimize Inventory Replenishment with Mathematical DSS", "Deploy dynamic EOQ, Greasley Statistical Safety Stock, and ROP models, cutting stockouts on top-tier (Category A) FMCG items by 80% while reducing excess holding stock by 22%.", "Phase 4 (Sprint 4)"],
    ["O-05", "Streamline Outbound Multi-Store Picking and Dispatch", "Increase order picking throughput from 40 lines/hour to over 95 lines/hour using consolidated wave picking; eliminate store shipping discrepancy rate to <0.3%.", "Phase 4 (Sprint 5)"],
    ["O-06", "Enforce Complete Auditability, RBAC, and Sub-Second Telemetry", "Ensure all stock transactions are recorded in an immutable ACID ledger with complete user attribution; achieve sub-1.2 second average page load and scan latency across all modules.", "Phase 5 (Sprint 6)"]
]

# Section 13.1: Summary of Functional Requirements by Module
MODULE_SUMMARY = [
    ["Module ID & Name", "Requirement ID Range", "Core Functional Capabilities Covered", "MoSCoW Priority"],
    ["M-01: Authentication, RBAC & Profile", "FR-01 to FR-06", "Secure login, JWT tokens, RBAC roles (Operator, Clerk, Supervisor, Procurement, Store Manager, Admin), password reset, session audit.", "Must Have (MVP Core)"],
    ["M-02: Product Master & Hierarchy", "FR-07 to FR-13", "SKU management, barcode assignment, category hierarchy (FMCG, Perishable, Chilled, Dry), temperature requirements, shelf-life rules.", "Must Have (MVP Core)"],
    ["M-03: Supplier & Purchase Orders", "FR-14 to FR-20", "Supplier directory, lead-time variance tracking, digital Purchase Order generation, approval workflows, PO status lifecycle.", "Must Have (MVP Core)"],
    ["M-04: Inbound Receiving & Digital GRN", "FR-21 to FR-28", "Dock receiving, barcode scan verification against PO, damaged item logging, digital GRN generation, credit note flagging.", "Must Have (MVP Core)"],
    ["M-05: Spatial Bin & Putaway Engine", "FR-29 to FR-35", "Zone-Aisle-Rack-Shelf-Bin 2D mapping, capacity constraints, directed putaway suggestions based on SKU velocity and product class.", "Must Have (MVP Core)"],
    ["M-06: Real-Time Ledger & FEFO Engine", "FR-36 to FR-44", "Double-entry inventory ledger, batch/lot tracking, expiry date monitoring, FEFO priority picking queue, automated quarantine lock.", "Must Have (MVP Core)"],
    ["M-07: Replenishment & Decision Support", "FR-45 to FR-52", "Dynamic EOQ calculator, Greasley's Safety Stock with service levels (90-99%), dynamic ROP alerts, automated PO draft creation.", "Must Have (MVP Core)"],
    ["M-08: Outbound Store Wave Picking", "FR-53 to FR-60", "Multi-store requisition ingestion, wave creation, shortest-path digital pick-lists, pick verification scanning, staging, dispatch note.", "Must Have (MVP Core)"],
    ["M-09: Cycle Counting & Shrinkage Audit", "FR-61 to FR-66", "ABC-classified cycle counting schedules, blind physical count entry, discrepancy variance analysis, stock write-off approvals.", "Should Have / Must"],
    ["M-10: Reporting, Dashboards & Analytics", "FR-67 to FR-72", "Real-time floor telemetry, stockout risk heatmaps, supplier SLA scorecards, inventory turnover & GMROI metrics, PDF/Excel export.", "Should Have"],
    ["M-11: Security, Audit Trail & Compliance", "FR-73 to FR-78", "Immutable audit log for all stock movements, Bangladesh Food Safety Act compliance reports, PDPO 2025 privacy compliance.", "Must Have (Cross-Cutting)"]
]

# Section 13.2: Non-Functional Requirements (NFR-01 to NFR-14)
NFRS = [
    ["ID", "Category", "Requirement Statement & Verification Metric", "Priority"],
    ["NFR-01", "Security & Encryption", "All web and mobile traffic shall be encrypted using TLS 1.3. Sensitive database credentials and session tokens shall be encrypted at rest using AES-256.", "Must Have"],
    ["NFR-02", "Authentication & Passwords", "User passwords shall be hashed using Argon2id or bcrypt (work factor >= 12). Tokens shall expire within 8 hours with automatic refresh token rotation.", "Must Have"],
    ["NFR-03", "Data Integrity & ACID", "All inventory state transitions (receiving, transfer, picking, adjustment) shall execute inside atomic database transactions, guaranteeing zero negative balances.", "Must Have"],
    ["NFR-04", "System Performance", "Barcodes scanned via handheld readers or web UI shall be verified and processed within <= 350 milliseconds. Dashboard analytics pages shall render in <= 1.5 seconds.", "Must Have"],
    ["NFR-05", "Concurrent Workload", "The system shall support at least 50 concurrent active warehouse scanners and web dashboard sessions without performance degradation or database locking.", "Must Have"],
    ["NFR-06", "High Availability", "The backend services and database shall maintain 99.8% operational uptime during warehouse working hours (6:00 AM to 11:00 PM BST).", "Must Have"],
    ["NFR-07", "Fault Tolerance & Recovery", "In case of server crash or power failure, database Point-In-Time Recovery (PITR) shall ensure a Recovery Point Objective (RPO) <= 1 minute and RTO <= 15 minutes.", "Must Have"],
    ["NFR-08", "Usability & Ergonomics", "The mobile scanning UI shall be optimized for one-handed operation on 5.5-inch rugged smartphones with high-contrast text and audio-haptic feedback.", "Must Have"],
    ["NFR-09", "Mobile Responsiveness", "All operator workflows shall render seamlessly across desktop management consoles (1920x1080) and ruggedized Android barcode terminals (720x1280).", "Must Have"],
    ["NFR-10", "Maintainability & Modularity", "The codebase shall follow clean layered architecture with documented RESTful API endpoints and unit test coverage >= 80% for core algorithms.", "Must Have"],
    ["NFR-11", "Scalability", "The database schema and indexing strategy shall support up to 50,000 SKUs, 500,000 active inventory batches, and 5,000,000 transaction records without query lag.", "Should Have"],
    ["NFR-12", "Auditability & Logging", "Every stock adjustment, manual override, and permission change shall be logged with exact user ID, timestamp, IP address, and previous/new state.", "Must Have"],
    ["NFR-13", "Compliance & Safety", "Batch expiration tracking shall conform to Bangladesh Food Safety Act 2013 and BSTI standards, preventing any expired item from being dispatched.", "Must Have"],
    ["NFR-14", "Cost-Efficiency", "The system shall run on modern open-source software stacks (Node.js/Next.js, PostgreSQL, Docker) to maintain low total cost of ownership (TCO) for retail chains.", "Must Have"]
]

# Section 17: Comprehensive Risk Analysis (R-01 to R-12)
RISKS = [
    ["ID", "Identified Risk Scenario", "Likelihood", "Impact", "Proactive Mitigation Strategy"],
    ["R-01", "Resistance from warehouse floor workers unfamiliar with digital barcode tools", "Medium", "High", "Design dead-simple one-touch UI; support both Bangla and English; conduct intensive 3-day on-site floor training with visual cheat sheets."],
    ["R-02", "Inaccurate manual data entry during supplier receipt (wrong batch or expiry date)", "High", "High", "Implement mandatory barcode scanning; enforce strict regex validation on date formats; require double-entry confirmation on bulk perishables."],
    ["R-03", "Wi-Fi dead zones in metallic warehouse racking causing scan interruptions", "High", "Medium", "Implement Service Worker caching and IndexedDB offline queue on mobile scanners; auto-sync transactions chronologically upon reconnection."],
    ["R-04", "Extreme supplier lead-time unpredictability distorting safety stock calculations", "High", "High", "Utilize Greasley's statistical model factoring both demand and lead-time variance; configure conservative service factor (Z=1.96 / 97.5%)."],
    ["R-05", "Concurrent database write collisions during simultaneous wave picking across aisles", "Medium", "High", "Implement row-level locking (SELECT FOR UPDATE) on specific inventory batch allocations; use atomic PostgreSQL transactions to prevent double-picking."],
    ["R-06", "Barcode label damage, smudging, or non-scannable supplier packages", "High", "Medium", "Equip receiving dock with on-demand barcode label printers to re-label compromised packaging immediately upon dock inspection."],
    ["R-07", "Inventory shrinkage masked as legitimate stock adjustment or write-off", "Medium", "High", "Enforce dual-authorization workflow for all stock adjustments > 1,000 BDT; log all write-off reasons with mandatory photographic evidence."],
    ["R-08", "System performance degradation during massive monthly cycle counting", "Low", "Medium", "Offload heavy analytical and cycle count reconciliation queries to read-replicas or optimized materialized views refreshed asynchronously."],
    ["R-09", "Scope creep across specialized third-party logistics (3PL) or automated crane robotics", "High", "Medium", "Strictly enforce MoSCoW boundaries; classify automated robotics and external 3PL carrier integration as Phase 3 Future Scope."],
    ["R-10", "Hardware terminal hardware theft or unauthorized mobile device access", "Low", "High", "Enforce device token binding; implement automatic 15-minute idle session timeouts; restrict system access to warehouse local Wi-Fi subnet."],
    ["R-11", "Data corruption or loss due to unexpected server power grid failure in Bangladesh", "Medium", "High", "Deploy PostgreSQL with Write-Ahead Logging (WAL) and automated hourly automated snapshots backed up to cloud object storage."],
    ["R-12", "Legal compliance breach with Bangladesh Food Safety Act 2013 on expired goods", "Medium", "Critical", "Enforce automated system lockout that mechanically prevents generating pick-lists or dispatch notes for batches within 48 hours of expiration."]
]

print("Proposal structured data loaded successfully.")


# -------------------------------------------------------------------------
# RetailSync Operational Study Data (Empirical Field Realities)
# -------------------------------------------------------------------------

# Table 0: Real-World Problem to Solution Mapping (From Comprehensive Study)
RETAILSYNC_PROBLEM_MAPPING = [
    ["ID", "Real-World Problem", "Operational Impact", "RetailSync Solution"],
    ["P-01", "Data Isolation", "Sales data lives in the POS; warehouse data lives on clipboards.", "Centralized SQL Database serving both POS and Warehouse APIs."],
    ["P-02", "Undetected Stockouts", "High-demand items run out on shelves before restock is ordered.", "Automated Reorder Point (ROP) triggers sending alerts to managers."],
    ["P-03", "Perishable Waste", "Lack of batch tracking leads to expired goods.", "Strict FIFO/FEFO logic and expiry-date dashboard highlights."],
    ["P-04", "Supplier Delays", "Manual PO generation is slow and error-prone.", "Automated PO generation based on low-stock metrics."],
    ["P-05", "Internal Shrinkage", "Untraceable manual stock adjustments.", "Role-Based Access Control (RBAC) with immutable audit logging."]
]

# Table 1: Technical Architecture & Stack Recommendation (From Comprehensive Study)
RETAILSYNC_TECH_STACK = [
    ["Component", "Recommended Technology", "Justification for Capstone"],
    ["Database Layer", "MySQL / PostgreSQL", "Relational architecture is mandatory for retail to ensure ACID compliance (Atomicity, Consistency, Isolation, Durability) for financial transactions."],
    ["Backend API", "Python (Django/FastAPI) or Java", "Excellent handling of concurrent requests, complex rule engines, and automated task scheduling (e.g., nightly expiry checks)."],
    ["Frontend Dashboard", "React / Next.js", "Provides a highly responsive, single-page application (SPA) experience for managers, eliminating page-reload delays."],
    ["Local Testing Env.", "XAMPP / Beekeeper Studio", "Standard, accessible environment for developing and visualizing the relational schema during the capstone phase."]
]

# Table 2: Target User Personas (From Comprehensive Study)
RETAILSYNC_CORE_PERSONAS = [
    ["User Persona", "Role Description", "System Needs"],
    ["Store Manager", "Oversees supply chain and profitability.", "Needs automated PO drafts, shrinkage reports, and a macro-view of inventory health."],
    ["Cashier", "Processes direct consumer sales.", "Requires a minimalist interface. The system must never freeze during a scan, even if the internet drops momentarily."],
    ["Inventory Clerk", "Handles loading docks and physical counting.", "Needs fast, barcode-compatible interfaces for receiving large shipments accurately."]
]

# Table 3: Real-Life Scenarios (From Comprehensive Study)
RETAILSYNC_REAL_LIFE_SCENARIOS = [
    ["Scenario Title", "Physical Reality", "RetailSync Action"],
    ["The Festival Rush", "During Ramadan, sugar and oil sales quadruple. A cashier scans items rapidly.", "RetailSync utilizes optimistic concurrency control in the database, allowing multiple cashiers to sell sugar simultaneously without locking the system, updating the central database seamlessly."],
    ["The Expired Goods Audit", "A health inspector visits the store.", "The manager opens RetailSync's Expiry Dashboard, proving that the system actively tracks and flags items 7 days before expiry, ensuring no expired goods are on shelves."],
    ["The Network Drop", "The store's ISP connection fails for 5 minutes.", "The POS continues to scan items locally. Once the connection is restored, it bulk-syncs the transaction payload to the central RetailSync database (Resilience feature)."]
]

# Table 4: Core Functional Requirements (From Comprehensive Study)
RETAILSYNC_CORE_FRS = [
    ["ID", "Module", "Specific Requirement", "Priority"],
    ["FR-01", "Auth", "System shall enforce RBAC isolating Cashier, Clerk, and Manager views.", "Must"],
    ["FR-10", "Inventory", "System shall track Product ID, SKU, Batch Number, and Expiry Date.", "Must"],
    ["FR-11", "Inventory", "System shall allow status tagging: Available, Quarantined, Sold.", "Must"],
    ["FR-20", "Receiving", "System shall generate a Goods Receipt Note (GRN) linked to a specific PO.", "Must"],
    ["FR-21", "Receiving", "Clerks can flag received items as 'Damaged' upon intake.", "Should"],
    ["FR-30", "POS Sync", "API shall deduct inventory based on strict FIFO/FEFO batch logic.", "Must"],
    ["FR-40", "Alerts", "System shall allow Managers to configure a Reorder Point (ROP) per SKU.", "Must"],
    ["FR-41", "Alerts", "System shall flag batches expiring within X days (configurable).", "Must"],
    ["FR-50", "Auditing", "Every stock modification must log the timestamp, User ID, and old/new value.", "Must"]
]

# Table 5: Non-Functional Requirements Specific Metrics (From Comprehensive Study)
RETAILSYNC_CORE_NFRS = [
    ["ID", "Category", "Specific Metric"],
    ["NFR-01", "Latency", "The POS deduction API must respond in under 2.0 seconds under normal load."],
    ["NFR-02", "Data Integrity", "Database must use transaction blocks to prevent partial updates if a crash occurs."],
    ["NFR-03", "Security", "All passwords must be hashed (bcrypt/Argon2id). No plaintext credentials stored."],
    ["NFR-04", "Concurrency", "System must handle at least 5 simultaneous POS registers deducting stock."],
    ["NFR-05", "Auditability", "Audit logs must be immutable (append-only) via database-level restrictions."]
]

# Table 6: Risk Management in the Local Context (From Comprehensive Study)
RETAILSYNC_LOCAL_RISKS = [
    ["ID", "Technical Risk", "Likelihood", "Context & Mitigation Strategy"],
    ["R-01", "Database Concurrency Conflicts", "High", "Two cashiers sell the last unit of milk at the same millisecond. Mitigation: Use SQL Row-Level Locking (SELECT ... FOR UPDATE)."],
    ["R-02", "Internet Outages", "High", "Store loses connection to the central server. Mitigation: Implement a queue system on the POS that caches sales and bulk-syncs when online."],
    ["R-03", "Data Entry Errors at Receiving", "Medium", "Clerk enters 500 instead of 50 boxes. Mitigation: System warns if GRN exceeds the Purchase Order quantity by >5%."]
]

# 14-Week Capstone Implementation Roadmap (From Comprehensive Study)
RETAILSYNC_CAPSTONE_ROADMAP = [
    ["Academic Timeframe", "Core Engineering Modules & Deliverables", "Key Technical Milestones"],
    ["Weeks 1-3", "Database Normalization (MySQL/PostgreSQL), ERD design, and API scaffolding (Python/Java).", "Relational schema definition, 3NF normalization, baseline REST endpoints."],
    ["Weeks 4-6", "Inventory CRUD, Batch Management, and Expiry Logic implementation.", "Batch tracking, dynamic shelf-life calculations, FEFO/FIFO queue logic."],
    ["Weeks 7-9", "Supplier module, PO generation, and GRN workflows.", "Supplier SLA records, digital PO lifecycle, dock inspection & GRN generation."],
    ["Weeks 10-11", "POS Sync Simulation (building the checkout deduction logic and FIFO handling).", "Real-time POS API, atomic stock deduction, concurrency locking (<2s latency)."],
    ["Weeks 12-13", "Rule engines for low-stock alerts, reporting dashboards, and audit logs.", "Automated ROP triggers, draft PO generation, immutable audit logging."],
    ["Week 14", "System testing, concurrency stress testing, and final defense preparation.", "Stress testing (5+ concurrent POS), UAT validation, capstone presentation & defense."]
]

# -------------------------------------------------------------------------
# Merged Advanced Academic Artifacts (Synthesizing WarePulse & RetailSync)
# -------------------------------------------------------------------------

# Formal RACI Responsibility Assignment Matrix for RetailSync Lifecycle
RETAILSYNC_RACI_MATRIX = [
    ["Project Lifecycle Phase / Core Deliverable", "Floor Staff / Cashiers", "Floor Supervisors", "Procurement Officers", "Store Managers", "DevOps / SysAdmin", "Developer Team", "Academic Committee"],
    ["Requirements Elicitation & Domain Study", "Consulted", "Consulted", "Consulted", "Consulted", "Informed", "Responsible / Accountable", "Informed / Approver"],
    ["Relational 3NF Database Schema & DDL", "Informed", "Consulted", "Informed", "Informed", "Consulted", "Responsible / Accountable", "Consulted"],
    ["ACID Concurrency & Row-Locking Engine", "Informed", "Informed", "Informed", "Informed", "Consulted", "Responsible / Accountable", "Informed"],
    ["Sub-2.0s POS Sync & Real-Time API", "Consulted", "Informed", "Informed", "Consulted", "Consulted", "Responsible / Accountable", "Informed"],
    ["FEFO/FIFO Dynamic Queue Algorithm", "Informed", "Consulted", "Consulted", "Consulted", "Informed", "Responsible / Accountable", "Consulted"],
    ["Greasley Safety Stock & EOQ Engine", "Informed", "Consulted", "Responsible", "Consulted", "Informed", "Accountable", "Informed"],
    ["Mobile Barcode Scanning PWA Interface", "Responsible", "Responsible", "Informed", "Informed", "Informed", "Accountable", "Informed"],
    ["Immutable Audit Ledger & Security", "Informed", "Consulted", "Consulted", "Informed", "Responsible", "Accountable", "Informed"],
    ["Dual-Level Black-Box & White-Box QA", "Consulted", "Consulted", "Consulted", "Consulted", "Consulted", "Responsible / Accountable", "Consulted / Evaluator"],
    ["Final Manuscript, System Demo & Defense", "Informed", "Informed", "Informed", "Informed", "Informed", "Responsible / Accountable", "Accountable / Approver"]
]

# SDLC Comparative Model Evaluation Matrix
RETAILSYNC_SDLC_EVALUATION = [
    ["SDLC Model", "Core Engineering Strengths", "Critical Weaknesses for Retail WMS", "Capstone Suitability Verdict"],
    ["Waterfall Model", "Predictable linear stages, thorough upfront documentation, clear milestone stage gates.", "Completely rigid; assumes 100% frozen requirements upfront; fails to accommodate unexpected database concurrency conflicts or floor usability feedback discovered during testing.", "Unsuitable"],
    ["V-Model (Verification & Validation)", "Exceptional verification discipline; rigorous test-case traceability for every development phase.", "Retains Waterfall's rigidity; changes in POS API integration or barcode scan ergonomics late in the cycle require restarting requirements.", "Partially Suitable"],
    ["Spiral Model", "Deep risk analysis at every iteration; well suited for high-budget, high-uncertainty industrial projects.", "Excessive managerial overhead, heavy documentation burden, and complex milestone tracking impractical for a 14-week university capstone.", "Over-Engineered / Unsuitable"],
    ["Agile Scrum with Evolutionary Prototyping", "Rapid 2-week iterations, continuous stakeholder feedback, functional working MVP (schema + API) delivered in early sprint, continuous concurrency stress-testing, and rapid UI adaptation.", "Requires disciplined sprint timeboxing and active backlog management to prevent scope creep into hardware or robotics.", "Highly Recommended (Selected Model)"]
]

# Production-Ready Relational Database Schema Blueprint (8 Core Tables)
RETAILSYNC_DDL_TABLES_SUMMARY = [
    ["Table Name", "Primary Purpose & Operational Entity", "Primary Key & Unique Keys", "Key Foreign Key Constraints", "Index Optimization Strategy"],
    ["suppliers", "Supplier directory, contact terms, lead-time variance metrics for Greasley safety stock.", "supplier_id (PK)", "None (Root entity)", "B-Tree on company_name, email"],
    ["products", "Master SKU catalog, category classification, storage temperature, unit & holding costs.", "product_id (PK), sku_code (UQ), barcode_ean (UQ)", "supplier_id -> suppliers(supplier_id)", "B-Tree on sku_code, barcode_ean, category"],
    ["locations", "Warehouse spatial coordinates: Zone, Aisle, Rack, Shelf Tier, Bin, and capacity limits.", "location_id (PK), bin_barcode (UQ)", "None (Spatial domain entity)", "B-Tree on bin_barcode, zone_code"],
    ["product_batches", "Perishable batch lots, manufacturing date, expiration date, on-hand qty, quarantine status.", "batch_id (PK), batch_lot_number (UQ)", "product_id -> products(product_id), location_id -> locations(location_id)", "B-Tree on expiry_date, product_id, status (FEFO index)"],
    ["purchase_orders", "Digital PO tracking, supplier link, approval lifecycle, total cost, delivery deadline.", "po_id (PK), po_number (UQ)", "supplier_id -> suppliers(supplier_id)", "B-Tree on po_number, status, order_date"],
    ["goods_receipt_notes", "Inbound dock inspection, PO line validation, accepted vs damaged count, digital invoice link.", "grn_id (PK), grn_number (UQ)", "po_id -> purchase_orders(po_id)", "B-Tree on grn_number, po_id, received_at"],
    ["inventory_transactions", "Immutable append-only ACID ledger recording all stock movements with row-locking support.", "transaction_id (PK, BIGSERIAL)", "product_id, batch_id, location_id, user_id", "Composite B-Tree on (product_id, recorded_at DESC), batch_id"],
    ["pos_registers", "Authorized branch super shop checkout cash registers and real-time sync telemetry.", "register_id (PK), terminal_mac_ip (UQ)", "branch_store_id (Reference)", "B-Tree on register_code, store_code, status"]
]

# SQL DDL Conceptual Script
RETAILSYNC_SQL_DDL_SCRIPT = """-- ============================================================================
-- RetailSync Enterprise Relational Database Schema Blueprint (DDL)
-- Engine: PostgreSQL 16+ / MySQL 8.0+ (ACID Compliant, 3NF Normalized)
-- Course: SE-231 (Software System Analysis & Design / Capstone Project 2)
-- Author: Raisul Islam Likhon (Section: SWE-44D)
-- ============================================================================

-- 1. Suppliers Master Table
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    trade_license_no VARCHAR(80) UNIQUE,
    contact_email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(25) NOT NULL,
    avg_lead_time_days NUMERIC(5,2) NOT NULL DEFAULT 7.00,
    lead_time_std_dev NUMERIC(5,2) NOT NULL DEFAULT 1.50,
    payment_terms VARCHAR(50) DEFAULT 'Net 30',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Products Master Catalog
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    sku_code VARCHAR(50) UNIQUE NOT NULL,
    barcode_ean VARCHAR(30) UNIQUE NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL CHECK (category IN ('FMCG_DRY', 'PERISHABLE_PRODUCE', 'DAIRY_CHILLED', 'FROZEN', 'HOUSEHOLD')),
    storage_temp VARCHAR(30) NOT NULL DEFAULT 'AMBIENT',
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

-- 3. Spatial Warehouse Locations Topology
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    zone_code VARCHAR(15) NOT NULL,
    aisle_number VARCHAR(10) NOT NULL,
    rack_number VARCHAR(10) NOT NULL,
    shelf_tier VARCHAR(10) NOT NULL,
    bin_barcode VARCHAR(30) UNIQUE NOT NULL,
    capacity_units INT NOT NULL DEFAULT 200,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- 4. Inventory Batches (FEFO/FIFO Expiry Engine)
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
    quarantine_status VARCHAR(20) NOT NULL DEFAULT 'AVAILABLE' 
        CHECK (quarantine_status IN ('AVAILABLE', 'QUARANTINED', 'EXPIRED', 'DEPLETED')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Digital Purchase Orders (PO)
CREATE TABLE purchase_orders (
    po_id SERIAL PRIMARY KEY,
    po_number VARCHAR(50) UNIQUE NOT NULL,
    supplier_id INT NOT NULL REFERENCES suppliers(supplier_id) ON DELETE RESTRICT,
    total_amount NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    status VARCHAR(25) NOT NULL DEFAULT 'DRAFT' 
        CHECK (status IN ('DRAFT', 'ISSUED', 'PARTIAL_RECEIVED', 'COMPLETED', 'CANCELLED')),
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expected_delivery_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Goods Receipt Notes (GRN) Inbound Inspection
CREATE TABLE goods_receipt_notes (
    grn_id SERIAL PRIMARY KEY,
    grn_number VARCHAR(50) UNIQUE NOT NULL,
    po_id INT NOT NULL REFERENCES purchase_orders(po_id) ON DELETE RESTRICT,
    supplier_invoice_ref VARCHAR(80),
    accepted_quantity INT NOT NULL DEFAULT 0,
    rejected_damaged_quantity INT NOT NULL DEFAULT 0,
    receiving_clerk_id INT NOT NULL,
    received_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Immutable Inventory Transactions Audit Ledger (ACID Row-Locking)
CREATE TABLE inventory_transactions (
    transaction_id BIGSERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    batch_id INT REFERENCES product_batches(batch_id) ON DELETE RESTRICT,
    location_id INT NOT NULL REFERENCES locations(location_id) ON DELETE RESTRICT,
    transaction_type VARCHAR(30) NOT NULL CHECK (transaction_type IN 
        ('INBOUND_GRN', 'DIRECTED_PUTAWAY', 'POS_SALE_FEFO', 'STORE_DISPATCH', 'DAMAGE_QUARANTINE', 'CYCLE_COUNT_ADJUSTMENT')),
    quantity INT NOT NULL CHECK (quantity <> 0),
    reference_document_no VARCHAR(80),
    user_id INT NOT NULL,
    recorded_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 8. Branch POS Registers & Sync Registry
CREATE TABLE pos_registers (
    register_id SERIAL PRIMARY KEY,
    register_code VARCHAR(30) UNIQUE NOT NULL,
    store_branch_code VARCHAR(30) NOT NULL,
    terminal_ip_mac VARCHAR(60) NOT NULL,
    is_online BOOLEAN NOT NULL DEFAULT TRUE,
    last_sync_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Strategic B-Tree Indexes for Sub-Second Concurrency & Real-Time Telemetry
CREATE INDEX idx_products_barcode ON products(barcode_ean);
CREATE INDEX idx_products_sku ON products(sku_code);
CREATE INDEX idx_batches_fefo_queue ON product_batches(product_id, expiry_date, quarantine_status);
CREATE INDEX idx_transactions_product_date ON inventory_transactions(product_id, recorded_at DESC);
CREATE INDEX idx_transactions_batch_id ON inventory_transactions(batch_id);
CREATE INDEX idx_locations_bin_barcode ON locations(bin_barcode);
"""

# Dual-Level Verification & Validation (V&V) Testing Strategy
RETAILSYNC_TESTING_STRATEGY = [
    ["Testing Tier & Category", "Target Operational Dimension", "Test Case Scenario & Verification Methodology", "Verifiable Pass / Acceptance Criteria"],
    ["Tier 1: Black-Box Functional", "Barcode Interrogation & Scanning Latency", "Interrogate 1D/2D barcodes on mobile cameras and Bluetooth triggers across low and high ambient lighting (100–600 lux).", "100% SKU identification accuracy; UI updates and audible/haptic feedback trigger within <= 350 ms."],
    ["Tier 1: Black-Box Functional", "Inbound GRN vs. PO Automated Variance", "Simulate delivery of 50 cartons with 3 cartons flagged as crushed; generate digital GRN against open PO.", "GRN logs 47 accepted, 3 quarantined; automated supplier credit note generated; zero quarantined stock added to POS."],
    ["Tier 1: Black-Box Functional", "Offline Network Resilience & Bulk Sync", "Sever store ISP connection during 25 consecutive barcode checkouts; reconnect network after 5 minutes.", "Local client queue caches all 25 sales with timestamps; bulk POST executes automatically on reconnect with zero dropped sales."],
    ["Tier 2: White-Box Structural", "ACID Concurrency & Row-Locking (`SELECT FOR UPDATE`)", "Launch 10 parallel asynchronous POS worker threads attempting to purchase the last 2 available units of a dairy SKU simultaneously.", "Exactly 2 threads succeed; 8 threads receive clean out-of-stock messages; inventory balance remains exactly 0; zero database deadlocks."],
    ["Tier 2: White-Box Structural", "Strict FEFO Priority Queue Verification", "Seed database with 3 batches of milk expiring in 5 days, 15 days, and 45 days; issue automated checkout sales deductions.", "Database triggers strictly decrement stock from the 5-day expiry batch first; automatically switches to 15-day batch only when 5-day is depleted."],
    ["Tier 2: White-Box Structural", "SQL Injection & XSS Penetration Defense", "Inject SQL injection strings (' OR 1=1; DROP TABLE) and XSS payloads into barcode search, user login, and PO creation fields.", "All inputs sanitized via parameterized queries and ORM; malicious payloads rejected with HTTP 400; security access log records attack attempt."],
    ["Tier 2: White-Box Structural", "Mathematical Replenishment Engine Precision", "Execute algorithmic unit test suite across 100 historical SKU sales and lead-time distributions (EOQ, Greasley, ROP).", "Computed EOQ, Safety Stock, and ROP match analytical statistical benchmarks within 0.01% floating-point tolerance."]
]

# Hybrid Enterprise Edge Expansion: Integrating WarePulse IoT Gateways into RetailSync
RETAILSYNC_EDGE_IOT_EXPANSION = [
    ["Architecture Tier", "Component Specification", "Operational Function in Central Distribution Center"],
    ["Edge Hardware Station", "ESP32 Dual-Core 240MHz MCU + RC522 RFID / Industrial Fixed Barcode Portal", "Positioned at central warehouse inbound loading dock gates; interrogates incoming bulk pallet tags hands-free as forklifts pass through."],
    ["Edge Offline Buffering", "LittleFS Non-Volatile Flash Memory Cache", "Stores up to 10,000 scanned pallet events during factory Wi-Fi brownouts; guarantees zero telemetry loss during network dropouts."],
    ["Secure Telemetry Ingestion", "MQTT Broker (Mosquitto/EMQX) over TLS 1.3 with X.509 Auth", "Transmits dock gate scan events in sub-second JSON payloads directly to RetailSync's Inbound Ingestion Worker service."],
    ["Unified Enterprise Core", "RetailSync Central Relational Core (PostgreSQL / MySQL)", "Processes edge RFID/barcode dock events, automatically matches them to open Purchase Orders, and creates draft GRNs without human data entry."]
]

