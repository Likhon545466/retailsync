# Pre-Confirmation Audit Rules & Mandatory Verification Gates

This document establishes the binding quality assurance rules that any agent working on the RetailSync codebase must execute and pass before confirming completion of any feature, refactoring, or bug fix.

---

## The Rule of Evidence
> **Never confirm a task based on assumption or code inspection alone. Every claim of completion must be backed by live verification evidence from automated tests and runtime checks.**

---

## Gate 0: Mandatory Pre-Execution Implementation Plan ("Plan Before Live Mutation")
- **Non-Negotiable Directive:** Before touching any files, making code edits, or pushing changes live—**regardless of how small or simple the modification is (even a single-line typo, minor CSS variable adjustment, or simple config flag)**—the agent MUST FIRST state the **Implementation Plan** to the user.
- **Required Plan Format:**
  1. **Scope & Files:** Which exact files will be touched.
  2. **Technical Actions:** What code, functions, routes, or CSS rules are being added, edited, or removed.
  3. **Verification Plan:** How the change will be tested (pytest commands, audit runner, browser checks).
  4. **Risk / Invariant Check:** Assurance that existing test suites, database invariants, and UI tokens will not be broken.

---

## The Seven Mandatory Pre-Confirmation Gates

### Gate 1: Automated Regression Suite (Zero Failures)
- **Command:** `./.venv/bin/pytest tests/`
- **Criteria:** All tests (33/33+) must pass with exit code `0`.
- **Constraint:** Zero tolerated regressions. If a test fails, do not comment out or weaken the test assertion; diagnose and resolve the root cause.

### Gate 2: Database Invariants & FEFO Stock Accounting
- **Non-Negative Inventory:** All batches in `InventoryBatch` must have `current_quantity >= 0`.
- **Benchmark Stock Alignment:** `Milk Vita Liquid Milk 1L` (`SKU-MILK-1L` / `LOT-MV-260901`) must always have 32 units available stock (matching dashboard and POS catalog).
- **Atomic Ledger Auditing:** Every transaction that alters stock (e.g. sale, putaway, receipt, write-off) must insert an atomic record into `stock_ledger` with:
  - `previous_balance` and `new_balance` strictly satisfying `previous_balance + quantity_change = new_balance`.
  - Non-null audit reference number (e.g., `WO-YYMMDD-XXXX`, `POS-XXXX`, `GRN-XXXX`).
  - Appropriate `TransactionType` enum (`DAMAGE_QUARANTINE`, `POS_SALE_FEFO`, etc.).

### Gate 3: Corporate Typography & Tabular Numerals
- **Global Font Stack:** `font-family: 'Aptos', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;` must be active globally on `body` and regular headings.
- **Tabular Numerals:** `font-variant-numeric: tabular-nums` must be explicitly declared on table cells, prices, lot numbers, and metric counters to ensure vertical optical alignment of decimal numbers.
- **Monospace Restriction:** Monospace (`'JetBrains Mono'`) must strictly be reserved for raw alphanumeric strings (`lot-code`, barcodes, `code-128`). Monospaced typewriter fonts must NEVER be used for regular UI labels, instructions, or buttons.
- **Zero Role Truncation:** User profile cards (`.user-card-role`) must define `white-space: normal; overflow: visible; text-overflow: clip; max-width: none;` to ensure full corporate titles like `General Manager (Store Admin)` are never truncated with ellipses (`...`).

### Gate 4: Content Guardrails & Copy Standards
- **Zero Forbidden Emojis on `/dashboard`:** Overview page must strictly exclude visual emojis:
  `["🛒", "📥", "📦", "🗺️", "📈", "☀️", "🌙", "⚡", "📁", "📄", "📘", "📊", "📽️", "🧠"]`.
- **Zero Developer Jargon on `/dashboard`:** User-facing management copy must exclude technical implementation jargon:
  `["3NF", "SELECT ... FOR UPDATE", "row-level locking", "PG16 3NF ACTIVE", "Sub-2.0s SLA", "Greasley Math", "Wilson Economic Order Quantity"]`.
- **Standardized Spatial Coordinates:** Bay coordinates must use standard notation: `Bay A-01 (Ambient)` (never obsolete `Bay B Ambient` or `Bay 0 Ambient`).
- **Product Title Sanitization:** No truncated or misspelled product strings (`Pasteurised Liquid Milk`, never `Pastcurised Li` or `Pastcurised`).

### Gate 5: POS 80mm ESC/POS Thermal Receipt Verification
When validating POS sales functionality, the receipt modal must render:
- **Header:** `RetailSync Superstore • Dhanmondi Central`
- **Statutory Tax Info:** `VAT Reg # 002918274-0101 • Mushak 6.3`
- **Metadata:** Formatted date & time, receipt number (`#RS-88219`), Cashier: `Nusrat (Till #01)`.
- **Financial Breakdown:** Line items (Qty, Unit Price, Subtotal), Subtotal, 5% Mushak VAT, Grand Total (`৳`), Cash Tendered, and Change.
- **Barcode & Footer:** Code-128 visual barcode with `*RS-88219*` and `"Thank you for shopping at RetailSync!"`.
- **Keyboard Shortcuts:** `Print Thermal Receipt (Ctrl+P)` and `New Sale (Space)`.

### Gate 6: Warehouse 4"x2" Shelf Barcode Tag Generator
When validating warehouse layout or bin inspection:
- **Inspector Action:** Button labeled `[ Print Bin Barcode Label ]`.
- **Adhesive Shelf Tag Preview:** Rendered in standard 4"x2" proportions with:
  - Bin Coordinate (`BAY A-01 • TIER 02`).
  - Product Name and SKU (`Milk Vita Liquid Milk 1L (SKU-MILK-1L)`).
  - Lot # & Expiry (`LOT-MV-260901 • Exp: 28-SEP-2026`).
  - Temperature Badge (`Chiller: 2°C - 4°C` or category-specific badge).
  - Code-128 visual barcode graphic.

### Gate 7: HTTP Route Availability & Repository Cleanliness
- **All 7 Core Routes Return 200:**
  1. `/dashboard`
  2. `/pos`
  3. `/inbound`
  4. `/putaway`
  5. `/warehouse`
  6. `/procurement`
  7. `/audits`
- **Zero Root Clutter:** Never leave loose debug scripts, temporary JSON dumps, or scratch files in the repository root. All temporary scripts belong in `scripts/` or scratch directories.

---

## One-Click Audit Verification Command
Before presenting your final response to the user, run the automated cross-check:
```bash
./.venv/bin/python scripts/audit_cross_check.py
```
If this script exits with status `0`, all gates are satisfied and confirmation may proceed.
