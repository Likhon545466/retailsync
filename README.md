# RetailSync: Centralized Super Shop Warehouse Management System

> **“Your retail inventory, synchronized and secure.”**  
> An automated, high-concurrency retail warehouse management and inventory optimization system engineered for Bangladeshi modern trade (Shwapno, Agora, Meena Bazar, Unimart, Daily Shopping) with real-time POS synchronization, directed spatial putaway, strict FEFO/FIFO batch tracking, and algorithmic replenishment.

---

## Academic Metadata

* **Institution:** Daffodil International University (DIU)
* **Faculty:** Faculty of Science and Information Technology
* **Department:** Department of Software Engineering
* **Course:** SE-231 (Software System Analysis & Design / Capstone Project 2)
* **Author:** **Raisul Islam Likhon** | Section: **SWE-44D**
* **Term:** Fall 2026 | September 2026

---

## Repository Structure & Navigation Map

```
Project Proposal Maker/
├── README.md                                  # Complete Project Overview & Navigation Index
├── docker-compose.yml                         # Local Dev Stack (PostgreSQL 16, Redis 7, MinIO)
│
├── proposal/                                  # Capstone Project Proposal (Official 20-Page Deliverable)
│   ├── RetailSync_WMS_Project_Proposal.docx   # Official 20-Page Word Document (DIU Format)
│   ├── RetailSync_WMS_Project_Proposal.pdf    # Official 20-Page PDF Document (Submission Ready)
│   ├── PROJECT_PROPOSAL.md                    # Proposal Markdown Source with Mathematical Models
│   └── interactive_showcase.html              # Interactive Browser Simulation & ROI Calculator
│
├── docs/                                      # Software Engineering Specifications Suite
│   ├── RetailSync_Master_Engineering_Suite.docx  # Unified Master Engineering Specification (55 Pages)
│   ├── RetailSync_Master_Engineering_Suite.pdf   # Unified Master Engineering PDF (55 Pages)
│   ├── 01_Product_Requirements/              # Module 1: PRD (Personas, Epics, SLOs)
│   ├── 02_Software_Architecture/              # Module 2: SAD (4-Tier C4 Architecture, Locking)
│   ├── 03_Technology_Stack/                   # Module 3: Tech Stack & ADRs (Next.js, FastAPI, Postgres)
│   ├── 04_Database_Design/                    # Module 4: 3NF Relational Schema, Dictionary & SQL DDL
│   ├── 05_API_Specifications/                # Module 5: OpenAPI 3.1 REST API Specification
│   └── 06_Sprint_Planning/                    # Module 6: 14-Week Agile Scrum Backlog & DoD
│
├── scripts/                                   # Document Generators & Build Automation
│   ├── build_trimmed_proposal.py              # Compiles the 20-page DIU proposal docx & pdf
│   ├── convert_docs_to_docx.py                # Compiles all markdown specifications to docx & master suite
│   ├── generate_proposal_docx.py              # DIU Academic Word styling and table formatting engine
│   ├── proposal_data.py                       # Proposal content matrices, formulas & citations
│   └── proposal_appendices_data.py            # Budget breakdown, RACI matrix & test cases
│
└── archive/                                   # Historical Materials & Reference Assets
    ├── legacy_drafts/                         # Previous 70-page draft, early markdown notes & builds
    ├── reference_samples/                     # DIU sample PDF reference documents
    └── rendered_previews/                     # High-resolution page inspection renders
```

---

## Complete Project Documentation Suite

All project deliverables are provided in **Markdown (.md)**, **Microsoft Word (.docx)**, and **Adobe Acrobat (.pdf)** formats:

### 1. Capstone Project Proposal (Official Submission)

| Deliverable | Description | Formats |
| :--- | :--- | :---: |
| **RetailSync Capstone Proposal** | Streamlined **20-page** proposal tailored for DIU SE-231. Focuses strictly on Agile Scrum, empirical problem statements, 3NF schema, mathematical formulations (EOQ, Greasley's Safety Stock), and enterprise architecture without extraneous model comparisons. | [**Word (.docx)**](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/proposal/RetailSync_WMS_Project_Proposal.docx)<br>[**PDF (.pdf)**](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/proposal/RetailSync_WMS_Project_Proposal.pdf)<br>[**Markdown (.md)**](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/proposal/PROJECT_PROPOSAL.md) |
| **Interactive Showcase & ROI Simulator** | Interactive browser-based simulation featuring real-time Greasley Safety Stock calculator, EOQ visualizer, and simulated POS concurrency test harness. | [**Showcase (.html)**](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/proposal/interactive_showcase.html) |

### 2. Modular Engineering Specifications Suite

| Module | Primary Technical Scope | Markdown | Word (.docx) | PDF (.pdf) |
| :--- | :--- | :---: | :---: | :---: |
| **Master Engineering Suite** | Consolidated 55-page master volume encompassing all 6 modules and complete DDL SQL. | [`docs/`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/) | [**`.docx`**](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/RetailSync_Master_Engineering_Suite.docx) | [**`.pdf`**](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/RetailSync_Master_Engineering_Suite.pdf) |
| **01. Product Requirements (PRD)** | 4 Personas, end-to-end user journeys, Gherkin acceptance criteria, MoSCoW prioritization, quantitative SLOs. | [`PRD.md`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/01_Product_Requirements/PRD.md) | [`PRD.docx`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/01_Product_Requirements/PRD.docx) | [`PRD.pdf`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/01_Product_Requirements/PRD.pdf) |
| **02. Software Architecture (SAD)** | Decoupled 4-tier cyber-physical architecture, C4 container views, row-level locking sequences, offline sync replay. | [`ARCHITECTURE.md`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/02_Software_Architecture/ARCHITECTURE.md) | [`ARCHITECTURE.docx`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/02_Software_Architecture/ARCHITECTURE.docx) | [`ARCHITECTURE.pdf`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/02_Software_Architecture/ARCHITECTURE.pdf) |
| **03. Technology Stack & ADRs** | Next.js 14 PWA, FastAPI, PostgreSQL 16, Redis 7, frugal Android barcode scanning, 5 formal ADR decisions. | [`TECH_STACK.md`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/03_Technology_Stack/TECH_STACK.md) | [`TECH_STACK.docx`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/03_Technology_Stack/TECH_STACK.docx) | [`TECH_STACK.pdf`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/03_Technology_Stack/TECH_STACK.pdf) |
| **04. Database Design & DDL** | 3NF relational schema (10 tables), check constraints, compound indexes, triggers, and full production DDL script. | [`DATABASE_SCHEMA.md`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/04_Database_Design/DATABASE_SCHEMA.md)<br>[`Schema (.sql)`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/04_Database_Design/DATABASE_SCHEMA.sql) | [`DATABASE_SCHEMA.docx`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/04_Database_Design/DATABASE_SCHEMA.docx) | [`DATABASE_SCHEMA.pdf`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/04_Database_Design/DATABASE_SCHEMA.pdf) |
| **05. REST API Specifications** | OpenAPI 3.1 endpoints, request/response envelopes, RFC 7807 error handling, POS synchronization contract. | [`API_SPECIFICATION.md`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/05_API_Specifications/API_SPECIFICATION.md) | [`API_SPECIFICATION.docx`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/05_API_Specifications/API_SPECIFICATION.docx) | [`API_SPECIFICATION.pdf`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/05_API_Specifications/API_SPECIFICATION.pdf) |
| **06. Sprint Planning & Tasks** | 14-week Agile Scrum plan, 6 sprints, story point estimates, Definition of Done, automated CI/CD pipeline. | [`SPRINT_PLAN_AND_TASKS.md`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/06_Sprint_Planning/SPRINT_PLAN_AND_TASKS.md) | [`SPRINT_PLAN_AND_TASKS.docx`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/06_Sprint_Planning/SPRINT_PLAN_AND_TASKS.docx) | [`SPRINT_PLAN_AND_TASKS.pdf`](file:///media/likhon/Pheeww/Programming/Capstone%20Project%202/Project%20Proposal%20Maker/docs/06_Sprint_Planning/SPRINT_PLAN_AND_TASKS.pdf) |

---

## Key Technical Highlights

1. **Sub-2.0s POS Concurrency Synchronization:** Employs pessimistic row-level locking (`SELECT ... FOR UPDATE`) on the earliest active batch in PostgreSQL, preventing deadlocks and overselling during festival shopping surges.
2. **Strict FEFO Priority Allocation:** Dynamic priority queue dynamically sorts batches by nearest expiration date; expired or damaged items are mechanically quarantined to comply with the Bangladesh Food Safety Act 2013.
3. **Mathematical Decision Support (DSS):** Built-in algorithms for:
   * **Dynamic Economic Order Quantity (EOQ):** $\sqrt{\frac{2DS}{H}}$
   * **Greasley's Statistical Safety Stock:** $SS = Z \times \sqrt{(\overline{L} \times \sigma_d^2) + (\overline{d}^2 \times \sigma_L^2)}$
   * **Dynamic Reorder Point (ROP):** $(\overline{d} \times \overline{L}) + SS$
4. **Offline Resilience:** Service Workers and client-side encrypted IndexedDB buffers cache sales during network drops; idempotent bulk replay (`X-Idempotency-Key`) executes upon link recovery.
5. **Hybrid Enterprise Edge Extension:** Seamlessly integrates stationary automated dock RFID/barcode readers (ESP32 MCU over MQTT/TLS) for high-throughput central distribution center gate intake.

---

## Quickstart & Local Development Guide

### Prerequisites
* **Docker Engine** `26.0+` & **Docker Compose** `v2.27+`
* **Python** `3.11.9+` & **Node.js** `18.20+` (LTS)
* **Git** `2.40+`

### 1. Clone & Setup Environment
```bash
git clone <repository_url> retailsync
cd retailsync
```

### 2. Boot Local Database & Cache via Docker
```bash
# Starts PostgreSQL 16 on port 5432 and Redis 7 on port 6379
docker compose up -d retailsync-db retailsync-redis
```

### 3. Initialize Relational Schema & Load Seed Data
```bash
# Execute the complete DDL schema and authentic Bangladeshi super shop seeds
docker exec -i retailsync-db psql -U retailsync_user -d retailsync_db < docs/04_Database_Design/DATABASE_SCHEMA.sql
```

### 4. Start the Backend API Service (FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run ASGI server with hot-reload
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# Interactive Swagger UI available at: http://localhost:8000/docs
```

### 5. Start the Frontend PWA (Next.js)
```bash
cd ../frontend
npm install
npm run dev
# PWA available at: http://localhost:3000
```

---

## Testing & Concurrency Validation

```bash
# 1. Run Backend Unit & Integration Tests
pytest backend/tests/ -v --cov=backend

# 2. Run POS Concurrency Stress Test (Locust)
locust -f tests/locust_pos_stress.py --headless -u 50 -r 10 --run-time 2m --host http://localhost:8000
```

---

## License & Intellectual Property
Developed as an academic capstone software engineering project at **Daffodil International University (DIU)**.  
Copyright © 2026 Raisul Islam Likhon. All rights reserved.
