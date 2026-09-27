# File and Workspace Organization Rules

## 1. Zero Root Clutter Rule
- The repository root must strictly contain only essential configuration and index files:
  - `README.md`
  - `docker-compose.yml`
  - `.gitignore` (if present)
  - Top-level directories: `proposal/`, `docs/`, `scripts/`, `archive/`, `venv/`.
- **NEVER** write loose `.docx`, `.pdf`, `.md`, `.sql`, `.html`, or temporary test/scratch scripts into the root directory.

## 2. Directory Allocation Standards
Any newly created or modified file MUST be placed directly into its dedicated subfolder:
- **`proposal/`**: All deliverables for the Capstone Proposal submission:
  - Proposal Word document (`RetailSync_WMS_Project_Proposal.docx`)
  - Proposal PDF document (`RetailSync_WMS_Project_Proposal.pdf`)
  - Proposal Markdown source (`PROJECT_PROPOSAL.md`)
  - Interactive UI showcase and ROI calculators (`interactive_showcase.html`)
- **`docs/`**: All technical system specifications, organized into numbered module subfolders:
  - `01_Product_Requirements/`: PRD markdown, Word, PDF.
  - `02_Software_Architecture/`: Architecture markdown, Word, PDF.
  - `03_Technology_Stack/`: Tech stack and ADRs markdown, Word, PDF.
  - `04_Database_Design/`: Schema markdown, DDL SQL, Word, PDF.
  - `05_API_Specifications/`: REST API contracts markdown, Word, PDF.
  - `06_Sprint_Planning/`: Scrum roadmap and backlog markdown, Word, PDF.
  - Root of `docs/`: Unified master engineering suite (`RetailSync_Master_Engineering_Suite.docx` & `.pdf`).
- **`scripts/`**: All Python generators, build tools, and formatting scripts.
- **`archive/`**: Deprecated drafts, intermediate test builds, and reference samples.

## 3. Automation & Script Constraints
- Any Python script that generates or converts files (`.docx`, `.pdf`, `.sql`, `.html`) must resolve paths relative to the project root and write directly into the appropriate subfolder.
- Temporary files must be cleaned up immediately or stored in the artifact scratch directory.
