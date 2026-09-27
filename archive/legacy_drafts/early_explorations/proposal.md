## WarePulse: An IoT-Enabled Autonomous Warehouse

Management & Stochastic Inventory Optimization System

## 2. Background & Industry Context

### 2.1 The Global and National Economic Stakes

The transformation of supply chains from labor-intensive manual record-keeping to autonomous, digitized operations is a strategic imperative. In emerging industrial hubs—most notably Bangladesh—the **Ready-Made Garment (RMG)** sector represents the foundation of national economic prosperity:

* It contributes over **80% of total export earnings**.
* It employs more than **4.4 million workers** across 4,500+ factories.
* Bangladesh is currently navigating its impending graduation from **Least Developed Country (LDC)** status scheduled for **2026**.

Graduation from LDC status will trigger the phase-out of preferential trade agreements (e.g., Generalised Scheme of Preferences / Duty-Free Quota-Free access in key global markets). To offset the resultant tariff spikes, the RMG and allied manufacturing sectors can no longer compete solely on low labor wages; they must radically optimize operational turnaround time and logistics efficiency.

### 2.2 The Problem Statement: The 90–120 Day Lead Time Crisis

A persistent bottleneck threatening manufacturing competitiveness is lead time:

* Primary global competitors like **China** maintain international fulfillment cycles of **30 to 35 days**.
* **Vietnam** operates within a **45 to 60-day** window.
* In contrast, Bangladesh's supply chain frequently stagnates between **90 and 120 days**.

A major driver of this prolonged turnaround is **warehouse opacity and fragmented internal logistics**. Small and Medium Enterprises (SMEs) and even large tiered manufacturers still depend on:

1. **Manual Paper Manifests & Disjointed Spreadsheets:** Physical counts take hours or days, leading to frequent data entry errors, phantom inventory, and inventory mismatches between warehouse floors and procurement offices.
2. **The Overstocking vs. Understocking Trap:**
   * *Overstocking:* Freezes vital working capital, consumes warehouse cubic capacity, and exposes materials (fabrics, trims, dyes, high-value components) to degradation, mold, pest damage, and obsolescence.
   * *Understocking:* Causes severe stockouts, triggering assembly line shutdowns, production penalties, and exorbitant emergency air-freight shipping costs.
3. **Physical-Digital Latency:** Material check-ins and check-outs are recorded hours or days after physical movement, meaning managers base multi-million-taka procurement decisions on obsolete snapshots.

## 3. Project Objectives

### 3.1 Primary (General) Objective

To design, model, and prototype an end-to-end, IoT-driven Smart Inventory Management and Warehouse Automation System that bridges the physical-digital divide by automating real-time material tracking at the warehouse edge, enforcing relational ledger integrity, and mathematically optimizing inventory replenishment through integrated Decision Support System (DSS) models.

### 3.2 Specific (S.M.A.R.T.) Objectives

1. **Edge Hardware Automation:** Build a low-cost, resilient IoT scanning station using an **ESP32 microcontroller** and **RC522 High-Frequency (13.56 MHz) RFID reader** communicating over SPI to automate tag reading at receiving and dispatch bottlenecks.
2. **Resilient Offline Edge Buffering:** Implement flash memory caching using the **LittleFS / SPIFFS** file system on the ESP32 to prevent telemetry data loss during factory Wi-Fi brownouts, automatically syncing records upon reconnection.
3. **Secure Real-Time Telemetry:** Deploy an **MQTT publish-subscribe pipeline encapsulated in TLS (Transport Layer Security)** with topic-level Access Control Lists (ACLs) to transmit telemetry payloads within sub-second latencies.
4. **Relational ACID Ledger:** Design and implement a normalized **PostgreSQL** schema enforcing strict referential integrity, indexing strategies, and transactional audit trails for all stock movements.
5. **Algorithmic Replenishment Optimization:** Integrate mathematical models directly into the application layer:
   * Dynamic **Economic Order Quantity (EOQ)** to minimize ordering and holding costs.
   * Variance-based **Greasley Statistical Safety Stock** modeling demand volatility and supplier lead-time variance across varying customer service levels (e.g., 90%, 95%, 99%).
   * Dynamic **Reorder Point (ROP)** calculation with automated alert triggers.
6. **Interactive Role-Based Dashboard:** Develop a responsive, generative web dashboard (Next.js / React) providing real-time spatial stock visualization, stockout risk indicators, and procurement action recommendations.

## 4. Project Scope and Delimitations

### 4.1 In-Scope

* **Edge Layer:** Physical ESP32 + RC522 prototype circuit, status LEDs/OLED indicator, LittleFS offline buffer, and SPI bus interface.
* **Network Layer:** MQTT Broker configuration (e.g., Eclipse Mosquitto or EMQX) with TLS certificate authentication, structured JSON payloads, and QoS (Quality of Service) 1 delivery guarantees.
* **Data Layer:** PostgreSQL relational database with tables for Products, Suppliers, Physical Warehouse Locations (Aisle/Rack/Bin), Inventory Batches, and Transaction Ledgers.
* **Logic & Analytics Layer:** Implementation of EOQ, Greasley's Safety Stock, and ROP calculations based on synthetic/historical transaction streams.
* **Application Layer:** Role-Based Access Control (RBAC) web portal for Operators, Inventory Managers, Procurement Officers, and Executives.
* **Documentation & Analysis (SAD):** Context Diagram, Level-0 and Level-1 Data Flow Diagrams (DFDs), Entity-Relationship Diagram (ERD), Use Case Specifications, and Test Plans.

### 4.2 Out-of-Scope (Delimitations)

* Physical Automated Guided Vehicles (AGVs), robotic gantry cranes, or motorized automated conveyor belts (simulated via stationary dock gate portals).
* Ultra-High Frequency (UHF) multi-meter warehouse-wide radar triangulation (HF 13.56 MHz proximity scanning is chosen for low-cost feasibility and metallic containment).
* Full enterprise-wide financial general ledger accounting / ERP replacement (the system exposes clean REST/GraphQL APIs for ERP integration instead).
* Custom silicon ASIC fabrication.

## 5. Stakeholder Analysis and RACI Matrix

### 5.1 Stakeholder Identification & Profile

| Stakeholder Role | Level | Primary Pain Points | System Benefits & Value Realization |
| --- | --- | --- | --- |
| **Warehouse Operators** | Operational (Direct) | Tedious paper logbooks, manual barcode line-of-sight aiming, blame for counting discrepancies, physical fatigue. | Automated RFID touchless logging, instantaneous audio-visual scan feedback, no manual paperwork. |
| **Inventory Floor Supervisors** | Tactical (Direct) | Inability to verify real-time physical bin contents, inventory shrinkage, lost pallets, time wasted searching racks. | Live 2D spatial bin mapping, immediate discrepancy logging, automated alert when misplaced items are scanned. |
| **Procurement & SCM Officers** | Strategic (Direct) | Guesswork in purchasing, uncoordinated purchase order timing, frequent stockouts of critical raw materials. | Algorithmic reorder suggestions (EOQ + ROP), vendor lead-time variance tracking, data-driven order scheduling. |
| **Warehouse Systems Admin / DevOps** | Technical (Direct) | Unsecured IoT gadgets prone to botnets, network downtime corrupting databases, schema migration conflicts. | X.509 mutual TLS authentication, offline edge buffering, declarative database migrations via pgschema. |
| **Executive Management (C-Suite / GM)** | Strategic (Indirect) | Tied-up working capital in excess stock, long delivery lead times leading to buyer cancellations, LDC graduation pressure. | Macro-level inventory turnover dashboards, reduced holding costs, lower operational lead times, competitive agility. |

### 5.2 RACI Matrix

| System Lifecycle Phase / Deliverable | Warehouse Operators | Inventory Supervisors | Procurement Officers | DevOps / SysAdmin | Project Team / Developers | Executive Sponsors |
| --- | --- | --- | --- | --- | --- | --- |
| **Requirements Gathering & SRS** | Consulted | Informed | Consulted | Consulted | Accountable / Responsible | Informed |
| **Hardware Node Circuit & Firmware** | Informed | Informed | - | Consulted | Accountable / Responsible | - |
| **Network & Security Setup (TLS/MQTT)** | - | - | - | Consulted | Accountable / Responsible | - |
| **Database Schema & DDL Design** | - | Consulted | Consulted | Consulted | Accountable / Responsible | - |
| **Algorithm Engine (EOQ / Safety Stock)** | - | Consulted | Consulted | - | Accountable / Responsible | Informed |
| **UI Dashboard & Usability Testing** | Responsible | Responsible | Responsible | - | Accountable | Informed |
| **Final Deployment & Acceptance** | Informed | Consulted | Consulted | Responsible | Accountable | Responsible / Approver |

*(R = Responsible, A = Accountable, C = Consulted, I = Informed)*

## 6. Software Development Life Cycle (SDLC) Methodology Evaluation

Selecting the appropriate SDLC is a crucial decision in System Analysis & Design. The table below evaluates the primary candidate models against the specific demands of an integrated IoT hardware-software system:

| SDLC Model | Strengths | Critical Weaknesses for this Project | Suitability Verdict |
| --- | --- | --- | --- |
| **Waterfall Model** | Linear, predictable stage gates, thorough documentation upfront. | Rigid; assumes 100% frozen requirements. Cannot handle unpredictable physical IoT risks (e.g., radio interference, SPI bus jitter, hardware component delays). | **Unsuitable** |
| **V-Model (Verification & Validation)** | Exceptional verification discipline and test case traceability. | Retains Waterfall's rigidity; changes in sensor hardware late in the cycle require restarting requirements. | **Partially Suitable** |
| **Spiral Model** | Deep risk analysis at every iteration; ideal for high-budget, high-uncertainty industrial projects. | Heavy managerial overhead, excessively complex milestone tracking for a 1-semester / 2-semester academic capstone. | **Over-engineered** |
| **Agile Scrum with Evolutionary Prototyping** | Incremental delivery in 2-week sprints, continuous hardware-software integration, early working prototype (MVP), adaptability to empirical testing feedback. | Requires disciplined timeboxing and continuous documentation maintenance. | **Highly Recommended (Selected Model)** |

### 6.1 Justification for the Selected Model: Agile Evolutionary Prototyping

An IoT warehouse automation system inherently involves **hardware-software co-design**:

1. **Empirical Edge Reality:** Firmware interaction with physical transponders cannot be validated theoretically on paper. Issues such as tag detuning near metal shelving, SPI timing conflicts, and Wi-Fi disconnect recovery must be uncovered through working prototypes.
2. **Early Value Demonstration:** An initial Minimum Viable Product (MVP)—one ESP32 + RC522 publishing an RFID UID over MQTT to insert a row in PostgreSQL—can be operational within Sprint 2.
3. **Continuous Algorithmic Refinement:** Subsequent sprints layer in mathematical modules (EOQ, Safety Stock, ROP) and UI enhancements without risking project failure or blocking parallel development.

## 7. Requirement Analysis

### 7.1 Functional Requirements (FR)

#### Module 1: Edge Computing & Hardware Data Capture

* **FR-01 (Tag Interrogation):** The edge reader shall interrogate passive ISO/IEC 14443A (13.56 MHz) RFID transponders within a proximity range of 0 to 5 cm and extract their unique 4-byte or 7-byte UID.
* **FR-02 (Physical Indication):** The edge node shall provide visual (LED) and auditory (buzzer) feedback confirming a successful tag read within 200 ms of interrogation.
* **FR-03 (Offline Resilient Buffering):** If network connectivity to the MQTT broker drops, the ESP32 shall persist scanned records (UID + epoch timestamp + gate ID) to non-volatile LittleFS storage without dropping events.
* **FR-04 (Auto-Reconnection & Catch-Up Sync):** Upon Wi-Fi link restoration, the edge node shall automatically reconnect, re-authenticate, flush buffered records chronologically to the broker, and prune local flash storage upon broker ACK.

#### Module 2: Telemetry Pipeline & Transaction Ledger

* **FR-05 (Telemetry Publishing):** The edge node shall package scan events into structured JSON payloads and publish them to designated hierarchical topics (warehouse/{zone}/{dock\_id}/inbound or outbound) under MQTT QoS 1.
* **FR-06 (Immutable Audit Ledger):** The backend ingestion worker shall insert every valid scan into an append-only inventory\_transactions ledger with foreign key references to products, locations, and reader nodes.
* **FR-07 (Atomic Stock Level Updates):** Inbound transactions shall increment physical on-hand stock and outbound transactions shall decrement stock inside an atomic database transaction (ACID compliance), preventing negative or corrupted balances.

#### Module 3: Decision Support System (DSS) & Inventory Algorithms

* **FR-08 (EOQ Calculation):** The system shall calculate the optimal order quantity using historical annual demand ($D$), procurement setup cost ($S$), and annual unit holding cost ($H$).
* **FR-09 (Dynamic Safety Stock):** The system shall compute statistical safety stock utilizing Greasley’s dual-variance formula based on configured service levels ($Z = 1.28, 1.65, 2.33$).
* **FR-10 (Reorder Point Alerting):** The system shall calculate the Reorder Point ($ROP = (d \times L) + SS$) and autonomously flag SKUs whose Inventory Position falls below this threshold.

#### Module 4: Web Application & Management Interface

* **FR-11 (Role-Based Authentication):** The web platform shall enforce role-based access control (Operator, Supervisor, Procurement, Admin) with secure session token management.
* **FR-12 (Live Telemetry Dashboard):** The application shall render real-time stock telemetry updates without full page reloads via WebSockets / Server-Sent Events.
* **FR-13 (Warehouse Spatial Visualization):** The dashboard shall present an interactive visual map of warehouse zones, racks, and bins, indicating utilization percentages and stock density.
* **FR-14 (Procurement Requisition Generation):** When an item breaches its ROP, the system shall generate a structured digital Purchase Requisition draft indicating the recommended EOQ.

### 7.2 Non-Functional Requirements (NFR)

* **NFR-01 (End-to-End Latency):** The total time elapsed from an RFID tag scan at the edge to its visual rendering on the web dashboard shall not exceed **1.5 seconds** under normal operating conditions.
* **NFR-02 (Edge Read Latency):** Tag identification and local verification on the ESP32 shall execute in **under 150 milliseconds**.
* **NFR-03 (Security & Confidentiality):** All MQTT telemetry and HTTP web traffic shall be encrypted via **TLS 1.3**. Edge nodes shall authenticate using unique cryptographic **X.509 client certificates**.
* **NFR-04 (Database Concurrency & Integrity):** The database shall handle concurrent scan writes across at least 20 simultaneous edge nodes without deadlocks, maintaining complete ACID compliance.
* **NFR-05 (Fault Tolerance & Availability):** The edge hardware shall operate autonomously during network dropouts for at least 72 hours, with flash storage supporting a minimum of 10,000 cached scan records.
* **NFR-06 (Data Recovery):** In the event of a system crash, the database shall support point-in-time recovery (PITR) with a Recovery Point Objective (RPO) $\le 1$ minute.
* **NFR-07 (Usability):** The web dashboard interface shall adhere to responsive design principles, rendering clearly on both desktop management screens and ruggedized warehouse tablet displays.

## 8. System Architecture & Technical Specifications

+-----------------------------------------------------------------------------------+
| EDGE COMPUTING LAYER |
| |
| +--------------------+ SPI Bus +-----------------------------------+ |
| | RC522 RFID | <--------------> | ESP32 MCU | |
| | Reader (13.56MHz)| | Dual-Core 240MHz, Wi-Fi / BLE | |
| +--------------------+ +-----------------------------------+ |
| | | | |
| Passive RFID Tags Flash LittleFS LED/Buzzer |
| (Goods / Pallets) (Offline Buffer) Feedback |
+------------------------------------------------------|----------------------------+
 |
 MQTT over TLS 1.3
 (Port 8883, X.509 Auth)
 |
+------------------------------------------------------v----------------------------+
| BROKER & INGESTION LAYER |
| |
| +-------------------------------------------------------+ |
| | MQTT Broker (Eclipse Mosquitto / EMQX) | |
| | - TLS Termination | |
| | - Topic ACL Authorization | |
| +-------------------------------------------------------+ |
| | |
| Telemetry Ingestion Worker |
| (Node.js / Go / Python Service) |
+--------------------------------------|--------------------------------------------+
 |
+--------------------------------------v--------------------------------------------+
| DATA & DECISION LAYER |
| |
| +------------------------------------+ +-----------------------------------+ |
| | PostgreSQL Database | | Optimization Algorithm Engine | |
| | - Normalized Relational Tables | | - Continuous EOQ Computation | |
| | - Append-Only Transaction Ledger | | - Greasley Safety Stock ($Z$) | |
| | - B-Tree Indexes on Foreign Keys | | - Dynamic ROP Alerts | |
| +------------------------------------+ +-----------------------------------+ |
+--------------------------------------|--------------------------------------------+
 |
+--------------------------------------v--------------------------------------------+
| PRESENTATION LAYER (WEB UI) |
| |
| +---------------------------------------------------------------------------+ |
| | Next.js / React Dashboard (Tailored Modern Interface) | |
| | - Live Stock Monitor - Spatial Warehouse Bin Map | |
| | - Automated Reorder Portal - Historical Lead-Time Analytics | |
| +---------------------------------------------------------------------------+ |
+-----------------------------------------------------------------------------------+

### 8.1 Database Schema Blueprint (DDL Conceptual Design)

-- 1. Suppliers Table
CREATE TABLE suppliers (
 supplier\_id SERIAL PRIMARY KEY,
 company\_name VARCHAR(150) NOT NULL,
 contact\_email VARCHAR(100),
 avg\_lead\_time\_days NUMERIC(5,2) NOT NULL DEFAULT 14.0,
 lead\_time\_std\_dev NUMERIC(5,2) NOT NULL DEFAULT 2.5,
 created\_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT\_TIMESTAMP
);

-- 2. Products / SKUs Master
CREATE TABLE products (
 product\_id SERIAL PRIMARY KEY,
 sku\_code VARCHAR(50) UNIQUE NOT NULL,
 name VARCHAR(200) NOT NULL,
 unit\_cost NUMERIC(10,2) NOT NULL,
 holding\_cost\_annual NUMERIC(10,2) NOT NULL,
 ordering\_cost\_fixed NUMERIC(10,2) NOT NULL,
 current\_stock INT NOT NULL DEFAULT 0 CHECK (current\_stock >= 0),
 safety\_stock\_threshold INT NOT NULL DEFAULT 0,
 reorder\_point INT NOT NULL DEFAULT 0,
 supplier\_id INT REFERENCES suppliers(supplier\_id) ON DELETE RESTRICT,
 created\_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT\_TIMESTAMP
);

-- 3. Warehouse Spatial Locations
CREATE TABLE locations (
 location\_id SERIAL PRIMARY KEY,
 zone\_code VARCHAR(10) NOT NULL,
 aisle\_number VARCHAR(10) NOT NULL,
 shelf\_tier VARCHAR(10) NOT NULL,
 bin\_id VARCHAR(20) UNIQUE NOT NULL,
 capacity\_limit INT NOT NULL DEFAULT 500
);

-- 4. RFID Tags Binding
CREATE TABLE rfid\_tags (
 tag\_uid VARCHAR(32) PRIMARY KEY,
 product\_id INT REFERENCES products(product\_id) ON DELETE CASCADE,
 batch\_lot\_number VARCHAR(50),
 assigned\_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT\_TIMESTAMP
);

-- 5. Immutable Inventory Transactions Ledger
CREATE TABLE inventory\_transactions (
 transaction\_id BIGSERIAL PRIMARY KEY,
 tag\_uid VARCHAR(32) NOT NULL,
 product\_id INT REFERENCES products(product\_id) ON DELETE RESTRICT,
 location\_id INT REFERENCES locations(location\_id) ON DELETE RESTRICT,
 reader\_node\_id VARCHAR(50) NOT NULL,
 transaction\_type VARCHAR(20) NOT NULL CHECK (transaction\_type IN ('INBOUND', 'OUTBOUND', 'INTERNAL\_TRANSFER', 'AUDIT\_ADJUSTMENT')),
 quantity INT NOT NULL CHECK (quantity <> 0),
 recorded\_at TIMESTAMP WITH TIME ZONE NOT NULL,
 synced\_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT\_TIMESTAMP
);

-- Strategic Indexing for Real-Time Query Performance
CREATE INDEX idx\_transactions\_product\_id ON inventory\_transactions(product\_id);
CREATE INDEX idx\_transactions\_recorded\_at ON inventory\_transactions(recorded\_at DESC);
CREATE INDEX idx\_products\_sku ON products(sku\_code);

## 9. Algorithmic Inventory Decision Support Models

The core differentiator of this system over a standard CRUD inventory database is its active mathematical Decision Support System (DSS).

### 9.1 Economic Order Quantity (EOQ)

The EOQ calculates the optimal order batch size ($Q^\*$) that minimizes the sum of annual ordering costs and holding costs:

$$EOQ = \sqrt{\frac{2 \times D \times S}{H}}$$

* $D$ = Annual Demand (units/year) extracted dynamically from transactional consumption history.
* $S$ = Ordering Setup Cost per purchase order (administrative, documentation, logistics fee).
* $H$ = Unit Holding Cost per year (cost of warehouse footprint, tied-up capital, insurance, obsolescence).

### 9.2 Statistical Safety Stock (Greasley Model)

Unlike naive safety stock heuristics that assume constant lead times or static demand, Greasley’s statistical model accounts for independent variances in both customer demand rate and vendor lead times:

$$SS = Z \times \sqrt{\left(\overline{L} \times \sigma\_d^2\right) + \left(\overline{d}^2 \times \sigma\_L^2\right)}$$

Where:

* $Z$ = Service level factor ($Z=1.28$ for 90%, $Z=1.65$ for 95%, $Z=2.33$ for 99%).
* $\overline{L}$ = Average supplier lead time in days.
* $\sigma\_L$ = Standard deviation of supplier lead time in days.
* $\overline{d}$ = Average daily demand in units.
* $\sigma\_d$ = Standard deviation of daily demand in units.

### 9.3 Dynamic Reorder Point (ROP)

The trigger point to initiate replenishment:

$$ROP = (\overline{d} \times \overline{L}) + SS$$

### 9.4 Concrete Numerical Demonstration (RMG Case Example)

Consider a high-demand raw material in a garment manufacturing facility (e.g., Grade-A Poly Cotton Twill Fabric Rolls):

* **Annual Demand ($D$):** 24,000 rolls ($\overline{d} = 65.75$ rolls/day, $\sigma\_d = 12$ rolls/day)
* **Order Cost ($S$):** $150.00 USD per purchase order
* **Holding Cost ($H$):** $4.50 USD per roll/year
* **Supplier Lead Time:** $\overline{L} = 14$ days, $\sigma\_L = 3$ days
* **Target Service Level:** 95% ($Z = 1.65$)

**1. EOQ Calculation:** $$EOQ = \sqrt{\frac{2 \times 24000 \times 150}{4.50}} = \sqrt{1,600,000} = 1,265 \text{ rolls}$$

**2. Safety Stock Calculation:** $$SS = 1.65 \times \sqrt{\left(14 \times 12^2\right) + \left(65.75^2 \times 3^2\right)}$$ $$SS = 1.65 \times \sqrt{(14 \times 144) + (4323.06 \times 9)} = 1.65 \times \sqrt{2,016 + 38,907.54}$$ $$SS = 1.65 \times \sqrt{40,923.54} = 1.65 \times 202.30 \approx 334 \text{ rolls}$$

**3. Reorder Point (ROP):** $$ROP = (65.75 \times 14) + 334 = 920.5 + 334 \approx 1,255 \text{ rolls}$$

**Managerial Decision Output:**
When total inventory position falls to **1,255 rolls**, the system automatically drafts an order for **1,265 rolls**, providing a 95% statistical guarantee that stock will not deplete prior to delivery.

## 10. Work Breakdown Structure (WBS) & Semester Timeline

This project is structured across five 3-week iterative sprints matching a standard academic capstone semester (15 weeks total):

gantt
 title Capstone Project Implementation Schedule (15 Weeks)
 dateFormat YYYY-MM-DD
 section Phase 1: Inception
 Problem Analysis & Requirements Elicitation :done, p1, 2026-09-21, 2026-10-05
 Literature Review & Sensor Prototyping Planning :done, p2, 2026-09-28, 2026-10-10
 System Requirements Specification (SRS) Draft :active, p3, 2026-10-05, 2026-10-17

 section Phase 2: Edge & Ingestion
 ESP32-RC522 Circuit Assembly & SPI Driver :p4, 2026-10-18, 2026-10-31
 LittleFS Offline Buffer & Reconnection Routine :p5, 2026-10-25, 2026-11-07
 MQTT Broker Config & TLS X.509 Setup :p6, 2026-11-01, 2026-11-14

 section Phase 3: Database & Algorithms
 PostgreSQL Schema, Constraints & Indexes :p7, 2026-11-08, 2026-11-21
 Ingestion Worker & ACID Transaction Ledger :p8, 2026-11-15, 2026-11-28
 EOQ, Greasley Safety Stock & ROP Engine Logic :p9, 2026-11-22, 2026-12-05

 section Phase 4: UI & Integration
 Next.js Web Portal & Real-Time Dashboards :p10, 2026-11-29, 2026-12-12
 Interactive 2D Spatial Bin Map :p11, 2026-12-06, 2026-12-19
 End-to-End System Integration & Benchmarking :p12, 2026-12-13, 2026-12-26

 section Phase 5: Testing & Defense
 Black-Box Hardware Tests & White-Box SQL Audits :p13, 2026-12-27, 2027-01-09
 Final Capstone Manuscript & Defense Preparation :p14, 2027-01-03, 2027-01-16

## 11. Testing and Quality Assurance Strategy

The project will enforce a dual-level verification and validation framework:

1. **Black-Box Physical & Functional Testing:**
   * *Physical Interrogation Accuracy:* Measure tag read success rates at varying angles (0°, 45°, 90°) and distances (1 cm to 5 cm) across metallic and non-metallic packaging.
   * *Offline Buffer Verification:* Intentionally disconnect the Wi-Fi AP while 100 consecutive tags are scanned. Reconnect Wi-Fi and verify that all 100 transactions are populated in PostgreSQL with original timestamps.
   * *Web Latency Validation:* Interrogate a tag and verify via automated browser timing that the stock count increments on screen within 1.5 seconds.
2. **White-Box Structural & Security Testing:**
   * *Database Integrity Audits:* Attempt concurrent transactions picking the last available unit of stock; verify that ACID isolation prevents negative inventory states.
   * *MQTT Security Penetration:* Attempt connection from unauthorized MQTT clients lacking X.509 client certificates; verify immediate broker rejection.
   * *Input Sanitization:* Inject malformed JSON packets and SQL/XSS strings into the telemetry stream; verify that ingestion handlers drop invalid packets without service disruption.

## 12. Conclusion

The proposed project addresses an urgent operational vulnerability in global manufacturing and warehousing logistics. By uniting low-cost edge computing (ESP32 + RFID), fault-tolerant communication (MQTT + TLS + LittleFS buffering), relational data integrity (PostgreSQL), and mathematical inventory optimization models (EOQ, Greasley Safety Stock, ROP), this capstone project transcends traditional static software development to deliver a complete, industry-relevant cyber-physical solution.
