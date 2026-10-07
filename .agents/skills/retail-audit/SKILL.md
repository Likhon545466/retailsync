---
name: retail-audit
description: >-
  Executes comprehensive multi-gate audits and cross-checking on RetailSync WMS before confirming tasks.
  Verifies automated unit tests, database invariants, typography tokens, content guardrails,
  POS 80mm ESC/POS receipts, and warehouse 4x2 shelf barcode tags.
---

# RetailSync Multi-Gate Audit Skill

Use this skill whenever you need to perform an end-to-end quality assurance pass, verify compliance against project rules, or cross-check implementations before declaring a task complete.

## Quick Execution

Run the built-in automated audit cross-checker:

```bash
./.venv/bin/python scripts/audit_cross_check.py
```

## The 7 Verification Gates

When performing an audit, verify that each of the following 7 gates has passed:

1. **Automated Test Gate**: Run `./.venv/bin/pytest tests/` (expect 33+ passing tests, 0 failures).
2. **Database Invariants Gate**: Ensure zero negative batch stocks, Milk Vita LOT-MV-260901 equals 32 units, and stock ledger entries maintain valid balance math.
3. **Typography & Styling Gate**: Check `app.css` for Aptos/Arial font stack, `font-variant-numeric: tabular-nums`, and non-truncating `.user-card-role`.
4. **Content Guardrails Gate**: Ensure zero forbidden emojis (`🛒`, `📥`, `📦`, `🗺️`, etc.) and zero technical jargon on `/dashboard`.
5. **POS Thermal Receipt Gate**: Ensure 80mm ESC/POS layout renders Dhanmondi Superstore header, Mushak 6.3 VAT reg, Nusrat cashier, subtotal, VAT, total, tendered, change, barcode, and `Ctrl+P`/`Space` shortcuts.
6. **Warehouse Shelf Tag Gate**: Ensure Bin Inspector features `[ Print Bin Barcode Label ]` and produces standard 4"x2" tags with coordinate, product, lot, expiry, and temperature badge.
7. **HTTP Route Availability Gate**: Ensure all 7 core routes (`/dashboard`, `/pos`, `/inbound`, `/putaway`, `/warehouse`, `/procurement`, `/audits`) return HTTP 200.

## Outcome Protocol
- If all gates pass: Return confirmation report with gate-by-gate pass status.
- If any gate fails: Report the exact failing gate and failure reason, fix the issue, and re-execute `scripts/audit_cross_check.py` before confirming.
