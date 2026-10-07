# RetailSync WMS — Engineering Directives & Rules for AI Agents

All AI agents working within this repository must strictly adhere to the following rules:

---

## 1. MANDATORY: Tell Implementation Plan Before Going Live
> **CRITICAL RULE:**
> Before applying ANY code edits, modifying files, executing database migrations, or going live with changes—**NO MATTER HOW SMALL OR TRIVIAL THE CHANGE IS (even a 1-line typo fix, single CSS variable adjustment, or minor template copy edit)**—the agent MUST FIRST state the **Implementation Plan** to the user.

The Implementation Plan must explicitly specify:
1. **Target Files & Components:** Exact file paths being modified.
2. **Specific Technical Changes:** Exact functions, classes, template blocks, or CSS rules being modified.
3. **Verification & Audit Plan:** Commands and automated tests to run (e.g. `./.venv/bin/pytest tests/`, `scripts/audit_cross_check.py`).
4. **Safety & Invariant Assessment:** Confirmation that existing test suites, database invariants, and UI tokens remain intact.

---

## 2. Seven Mandatory Pre-Confirmation Gates

Never declare a task or ticket complete without passing all 7 verification gates:

1. **Gate 1: Automated Test Suite (Pytest)**
   - All tests in `tests/` (33+ tests) must pass with exit code `0`.
   - Zero tolerated regressions. Never weaken test assertions.
2. **Gate 2: Database Invariants & FEFO Accounting**
   - Zero negative batch quantities (`current_quantity >= 0`).
   - Milk Vita `LOT-MV-260901` (`SKU-MILK-1L`) must remain aligned at exactly 32 units.
   - All stock mutations must record atomic entries in `stock_ledger` with `previous_balance + delta == new_balance` and non-null audit reference numbers (`WO-XXXX`, `POS-XXXX`, etc.).
3. **Gate 3: Global Corporate Typography & Tabular Numerals**
   - Global font stack: `'Aptos', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;`.
   - `font-variant-numeric: tabular-nums` active on all numbers, tables, metrics, and lot codes.
   - Monospace (`JetBrains Mono`) strictly reserved for lot numbers and barcode strings. Never use typewriter monospace on regular UI copy.
   - User role titles in profile cards (`.user-card-role`) must define `overflow: visible; white-space: normal; max-width: none;` (never truncated).
4. **Gate 4: Content Guardrails & Copy Standards**
   - Zero visual emojis on `/dashboard` (`["🛒", "📥", "📦", "🗺️", "📈", "☀️", "🌙", "⚡", "📁", "📄", "📘", "📊", "📽️", "🧠"]`).
   - Zero developer jargon in management-facing copy on `/dashboard` (`["3NF", "SELECT ... FOR UPDATE", "row-level locking", "PG16 3NF ACTIVE", "Sub-2.0s SLA", "Greasley Math", "Wilson Economic Order Quantity"]`).
   - Spatial coordinate notation: strictly `Bay A-01 (Ambient)` (never `Bay B Ambient` or `Bay 0 Ambient`).
   - Product name normalization: `Pasteurised Liquid Milk` (never `Pastcurised Li`).
5. **Gate 5: POS 80mm ESC/POS Thermal Receipt Standards**
   - Header: `RetailSync Superstore • Dhanmondi Central`, `VAT Reg # 002918274-0101 • Mushak 6.3`.
   - Cashier: `Nusrat (Till #01)`, Receipt: `#RS-88219`.
   - Line items breakdown, Subtotal, 5% Mushak VAT, Grand Total (`৳`), Cash Tendered, Change.
   - Code-128 visual barcode + `"Thank you for shopping at RetailSync!"`.
   - Active keyboard shortcuts: `[ Print Thermal Receipt (Ctrl+P) ]` and `[ New Sale (Space) ]`.
6. **Gate 6: Warehouse 4"x2" Shelf Barcode Tag Standards**
   - Inspector action button labeled `[ Print Bin Barcode Label ]`.
   - Printable 4"x2" adhesive tag rendering Coordinate (`BAY A-01 • TIER 02`), Product (`Milk Vita Liquid Milk 1L (SKU-MILK-1L)`), Lot & Expiry (`LOT-MV-260901 • Exp: 28-SEP-2026`), Code-128 barcode, and Temperature badge (`Chiller: 2°C - 4°C`).
7. **Gate 7: Route Availability & Clean Repository**
   - All 7 core HTML routes (`/dashboard`, `/pos`, `/inbound`, `/putaway`, `/warehouse`, `/procurement`, `/audits`) return HTTP 200.
   - Zero untracked scratch files dumped in the project root.

---

## 3. Automated Cross-Check Runner
Run before confirming any task:
```bash
./.venv/bin/python scripts/audit_cross_check.py
```
