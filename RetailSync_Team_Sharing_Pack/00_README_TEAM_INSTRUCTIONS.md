# RetailSync WMS — Team Master Sharing Dossier
### DIU SE-231 Capstone Project 2 (Software System Analysis & Design)
**Daffodil International University | Department of Software Engineering | Section: SWE-44D**

---

## 👥 Project Team
* **Raisul Islam Likhon** (Team Lead — Architecture, Backend & Concurrency Engine) — ID: `251-35-508`
* **Shottobroto Dey** (Algorithm Engineering, Spatial Routing & Frontend UI) — ID: `251-35-017`
* **Golam Husnain Papon** (3NF Database Modeling, Test Automation & QA Audits) — ID: `251-35-529`

---

## 🌐 Live System URLs
* **Production Web Application**: https://retailsync-two.vercel.app/dashboard
* **Interactive Executive Showcase**: https://retailsync-two.vercel.app/showcase
* **Interactive Slide Engine**: https://retailsync-two.vercel.app/slides
* **GitHub Repository**: https://github.com/Likhon545466/retailsync

---

## 📁 Files Included in this Team Pack

| File Name | Format | Description & Usage |
| :--- | :--- | :--- |
| **`01_Capstone_Proposal_27Pages.pdf`** | PDF | **Official 27-Page Formal Capstone Proposal**. Includes executive problem statement, grounding in Bangladesh retail trade (Shwapno, Agora, Unimart), ROI financial payback model (2.80 months), and 12-week Gantt sprint roadmap. |
| **`01_Capstone_Proposal_27Pages.docx`** | DOCX | **Editable Microsoft Word version** of the Capstone Proposal for submissions or university document portals. |
| **`02_Master_Technical_Engineering_Suite_70Pages.pdf`** | PDF | **The 70-Page Master Technical Engineering Suite**. Contains complete Product Requirements Document (PRD), 4-tier C4 Architecture diagrams, 10 Architecture Decision Records (ADRs), 3NF Relational Schema with DDL, REST API endpoints, and full Sprint Backlog. |
| **`02_Master_Technical_Engineering_Suite_70Pages.docx`** | DOCX | **Editable Microsoft Word version** of the 70-Page Master Technical Engineering Suite. |
| **`03_Defense_Presentation_Deck.pptx`** | PPTX | **16:9 Presentation Slide Deck**. Ready for projection in the defense room or sharing with the supervisor. |
| **`04_Technical_Stack_And_Viva_Defense_Guide.md`** | Markdown | **Viva Voce Defense Master Bible (61 KB)**. Thoroughly answers 30 rigorous faculty defense questions, provides mathematical formulas for all 5 algorithms, explains why every technology was selected, and details a 15-minute live demonstration script. |
| **`05_Interactive_Web_Slides.html`** | HTML | **Interactive Web Slide Presentation Engine**. Can be opened directly in any browser (Chrome, Edge, Firefox) offline or online with speaker notes, rehearsal timer, and keyboard shortcuts (`N` for Notes, `T` for Timer, `F` for Fullscreen). |
| **`06_Interactive_Executive_Showcase.html`** | HTML | **Interactive Executive Showcase & Simulation Tool**. Full web-based simulator of POS concurrency, FEFO allocation, and warehouse shelf life tracking. |
| **`assets/`** | Directory | High-resolution architectural diagrams, system flowcharts, AI forecasting workflows, and SVG vector logos. |

---

## 🎯 Quick Viva Voce Defense Prep (What Each Teammate Should Master)

### 1. Raisul Islam Likhon (Lead & Architecture)
* **Core Topic**: 4-Tier Client-Server Architecture, FastAPI Async ASGI Event Loop, and PostgreSQL Concurrency (`SELECT ... FOR UPDATE SKIP LOCKED`).
* **Key Defense Point**: Explain how row-level pessimistic locking prevents race conditions and overselling when 50+ cashiers simultaneously scan the final unit of a perishable item during 7:00 PM evening rush hours in Dhaka.
* **SLA Metric**: P99 POS checkout latency guaranteed under 1.8 seconds.

### 2. Shottobroto Dey (Algorithms & Frontend)
* **Core Topic**: Automated FEFO (First-Expired, First-Out) batch allocation, Greasley's Dual-Variance Safety Stock formula, and Wilson Economic Order Quantity (EOQ).
* **Key Defense Point**: Explain how Greasley's formula ($SS = Z \times \sqrt{\bar{L} \cdot \sigma_D^2 + \bar{D}^2 \cdot \sigma_L^2}$) accounts for supplier delivery delays caused by Dhaka traffic jams and rainy seasons.
* **Metric**: 30% reduction in perishable spoilage and 18% fewer stockout incidents.

### 3. Golam Husnain Papon (Database & Quality Assurance)
* **Core Topic**: 3NF Database Normalization (8 entities), B-tree composite indexing, and immutable `stock_ledger_audits` trail.
* **Key Defense Point**: Prove why the database satisfies Third Normal Form (every non-key attribute depends on the key, the whole key, and nothing but the key), and explain how the immutable ledger guarantees financial auditability.
* **Metric**: Zero ghost inventory discrepancies, sub-50ms indexed ledger lookup times.

---

## ⚡ How to Run the System Locally
If running on a laptop during the presentation without Wi-Fi:
```bash
# 1. Clone repository
git clone https://github.com/Likhon545466/retailsync.git
cd retailsync

# 2. Activate virtual environment
source .venv/bin/activate  # on Linux/macOS
# or .venv\Scripts\activate on Windows

# 3. Launch Application
uvicorn retailsync_app.main:app --reload --port 8000
```
Open **`http://localhost:8000/dashboard`** in your browser. All documentation and slides are accessible from the top navigation bar `📁 Docs ▾` dropdown!
