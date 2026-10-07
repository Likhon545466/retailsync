#!/usr/bin/env python3
"""
RetailSync WMS — Automated Audit & Pre-Confirmation Cross-Checking Script
Author: RetailSync Audit Subagent
Purpose: Execute comprehensive verification across test suites, database integrity,
         design tokens, UI typography, forbidden content guardrails, and API endpoints
         before confirming any feature or refactoring task.
"""

import sys
import subprocess
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ANSI Colors for Terminal Output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(title: str):
    print(f"\n{BOLD}{CYAN}=== [AUDIT GATE] {title} ==={RESET}")

def print_pass(message: str):
    print(f"  {GREEN}✓ PASS:{RESET} {message}")

def print_fail(message: str):
    print(f"  {RED}✗ FAIL:{RESET} {message}")

def print_warn(message: str):
    print(f"  {YELLOW}⚠ WARN:{RESET} {message}")


def run_gate_pytest() -> bool:
    print_header("1. Automated Unit & Regression Test Suite")
    cmd = [sys.executable, "-m", "pytest", "tests/", "-q"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        passed_line = [line for line in proc.stdout.splitlines() if "passed" in line]
        summary = passed_line[-1] if passed_line else "All tests passed"
        print_pass(f"Pytest regression suite clean: {summary}")
        return True
    else:
        print_fail("Pytest suite reported failures:\n" + proc.stdout + proc.stderr)
        return False


def run_gate_database() -> bool:
    print_header("2. Database Invariants & Stock Ledger Integrity")
    success = True
    try:
        from retailsync_app.database import SessionLocal
        from retailsync_app import models

        db = SessionLocal()
        try:
            # 1. Negative stock check
            negative_batches = db.query(models.InventoryBatch).filter(models.InventoryBatch.current_quantity < 0).all()
            if negative_batches:
                print_fail(f"Found {len(negative_batches)} batches with negative quantity!")
                success = False
            else:
                print_pass("Zero negative stock quantities detected across all batches.")

            # 2. Milk Vita stock check (must match 32 units)
            mv_batch = db.query(models.InventoryBatch).filter(models.InventoryBatch.lot_number == "LOT-MV-260901").first()
            if mv_batch and mv_batch.current_quantity == 32:
                print_pass(f"Milk Vita LOT-MV-260901 stock is aligned at exactly {mv_batch.current_quantity} units.")
            else:
                curr = mv_batch.current_quantity if mv_batch else 'None'
                print_fail(f"Milk Vita LOT-MV-260901 expected 32 units, found: {curr}")
                success = False

            # 3. Stock ledger audit balance check
            ledger_entries = db.query(models.StockLedger).order_by(models.StockLedger.ledger_id.desc()).limit(20).all()
            inconsistent_ledger = []
            for e in ledger_entries:
                if e.new_balance != (e.previous_balance + e.quantity_change):
                    inconsistent_ledger.append(e.reference_number)
            if inconsistent_ledger:
                print_fail(f"Inconsistent ledger math detected on refs: {inconsistent_ledger}")
                success = False
            else:
                print_pass("Stock ledger math balance (prev + delta = new) verified 100% consistent.")

            # 4. Reference numbers not null
            empty_refs = [e for e in ledger_entries if not e.reference_number]
            if empty_refs:
                print_fail(f"Found {len(empty_refs)} ledger records missing audit reference numbers.")
                success = False
            else:
                print_pass("All recent stock ledger entries possess audit reference numbers.")

        finally:
            db.close()
    except Exception as e:
        print_fail(f"Database invariant check raised exception: {e}")
        return False

    return success


def run_gate_typography_css() -> bool:
    print_header("3. Corporate Typography & Tabular Numerals CSS")
    success = True
    css_path = os.path.join(os.path.dirname(__file__), "..", "retailsync_app", "static", "css", "app.css")
    if not os.path.exists(css_path):
        print_fail("app.css not found!")
        return False

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Aptos / Arial corporate stack
    if "'Aptos', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;" in css:
        print_pass("Global Aptos/Arial corporate typography stack configured in body.")
    else:
        print_fail("Global Aptos/Arial typography stack missing or altered in app.css.")
        success = False

    # Tabular numbers
    if "font-variant-numeric: tabular-nums;" in css:
        print_pass("Tabular numerals rule (font-variant-numeric: tabular-nums) active for numbers and tables.")
    else:
        print_fail("Tabular numerals rule missing in app.css.")
        success = False

    # Monospace strictly scoped
    if ".lot-code, code.lot-code, .barcode-string, .barcode-text, .code-128" in css:
        print_pass("Monospace font strictly scoped to lot codes and barcode strings.")
    else:
        print_fail("Monospace scope definition missing in app.css.")
        success = False

    # Role truncation prevention
    if "overflow: visible;" in css and "white-space: normal;" in css:
        print_pass("Role titles configured with overflow: visible and white-space: normal (no truncation).")
    else:
        print_fail("Role title truncation guardrail missing in app.css.")
        success = False

    return success


def run_gate_content_guardrails() -> bool:
    print_header("4. Content Guardrails & Forbidden Jargon / Emojis")
    success = True
    from fastapi.testclient import TestClient
    from retailsync_app.main import app

    client = TestClient(app)
    dash_res = client.get("/dashboard")
    if dash_res.status_code != 200:
        print_fail(f"/dashboard returned HTTP {dash_res.status_code}")
        return False
    html = dash_res.text

    # Forbidden emojis on /dashboard
    forbidden_emojis = ["🛒", "📥", "📦", "🗺️", "📈", "☀️", "🌙", "⚡", "📁", "📄", "📘", "📊", "📽️", "🧠"]
    found_emojis = [e for e in forbidden_emojis if e in html]
    if found_emojis:
        print_fail(f"Forbidden emojis found on /dashboard: {found_emojis}")
        success = False
    else:
        print_pass("Zero forbidden emojis detected on /dashboard.")

    # Forbidden developer jargon on /dashboard
    forbidden_jargon = [
        "3NF",
        "SELECT ... FOR UPDATE",
        "row-level locking",
        "PG16 3NF ACTIVE",
        "Sub-2.0s SLA",
        "Greasley Math",
        "Wilson Economic Order Quantity",
    ]
    found_jargon = [j for j in forbidden_jargon if j in html]
    if found_jargon:
        print_fail(f"Forbidden technical jargon found on /dashboard: {found_jargon}")
        success = False
    else:
        print_pass("Zero forbidden developer jargon detected on /dashboard user copy.")

    # Data typo check
    if "Bay B Ambient" in html or "Bay 0 Ambient" in html:
        print_fail("Obsolete 'Bay B Ambient' or 'Bay 0 Ambient' found on /dashboard.")
        success = False
    elif "Bay A-01 (Ambient)" in html:
        print_pass("Standardized coordinate 'Bay A-01 (Ambient)' verified on /dashboard.")
    else:
        print_warn("Could not find 'Bay A-01 (Ambient)' in /dashboard HTML.")

    return success


def run_gate_features() -> bool:
    print_header("5. Enterprise Features: POS 80mm Receipt & 4x2 Shelf Tag")
    success = True
    from fastapi.testclient import TestClient
    from retailsync_app.main import app

    client = TestClient(app)

    # 1. POS 80mm Receipt Modal
    pos_res = client.get("/pos")
    if pos_res.status_code == 200:
        pos_html = pos_res.text
        pos_checks = [
            ("Receipt Paper Container", 'class="receipt-paper"'),
            ("Header Store Title", "RetailSync Superstore • Dhanmondi Central"),
            ("Mushak VAT Reg #", "VAT Reg # 002918274-0101 • Mushak 6.3"),
            ("Cashier Name & Till", "Nusrat (Till #01)"),
            ("Print Shortcut Button", "Print Thermal Receipt (Ctrl+P)"),
            ("New Sale Shortcut Button", "New Sale (Space)"),
            ("Code-128 Barcode Graphic", 'id="receiptBarcodeText"')
        ]
        all_pos_ok = True
        for label, token in pos_checks:
            if token not in pos_html:
                print_fail(f"POS Receipt missing: {label} ({token})")
                all_pos_ok = False
        if all_pos_ok:
            print_pass("80mm ESC/POS Thermal Receipt modal verified complete on /pos.")
        else:
            success = False
    else:
        print_fail(f"/pos returned HTTP {pos_res.status_code}")
        success = False

    # 2. Warehouse 4"x2" Shelf Tag
    wh_res = client.get("/warehouse")
    if wh_res.status_code == 200:
        wh_html = wh_res.text
        wh_checks = [
            ("Inspector Action Button", "Print Bin Barcode Label"),
            ("Tag Generator Modal", 'id="warehouseStickerModal"'),
            ("Printable 4x2 Area", 'id="whStickerPrintArea"'),
            ("Bin Coordinate Element", 'id="whStickerBinCoord"'),
            ("Temperature Badge Element", 'id="whStickerTempBadge"'),
            ("Adhesive Roll Print Button", "Print 4x2 Labels (Adhesive Roll)")
        ]
        all_wh_ok = True
        for label, token in wh_checks:
            if token not in wh_html:
                print_fail(f"Warehouse Shelf Tag missing: {label} ({token})")
                all_wh_ok = False
        if all_wh_ok:
            print_pass("4\"x2\" Shelf Barcode Tag generator verified complete on /warehouse.")
        else:
            success = False
    else:
        print_fail(f"/warehouse returned HTTP {wh_res.status_code}")
        success = False

    # 3. Write-off API
    wo_res = client.post("/api/v1/warehouse/write-off", json={"lot_number": "NON_EXISTENT_LOT", "quantity": 1})
    if wo_res.status_code == 404:
        print_pass("POST /api/v1/warehouse/write-off endpoint active (handled 404 cleanly).")
    else:
        print_fail(f"Write-off endpoint returned unexpected status: {wo_res.status_code}")
        success = False

    return success


def run_gate_endpoints() -> bool:
    print_header("6. HTTP Route Availability & Status 200 Verification")
    from fastapi.testclient import TestClient
    from retailsync_app.main import app

    client = TestClient(app)
    routes = ["/dashboard", "/pos", "/inbound", "/putaway", "/warehouse", "/procurement", "/audits"]
    all_ok = True
    for route in routes:
        res = client.get(route)
        if res.status_code == 200:
            print_pass(f"Route {route:<14} -> HTTP 200 ({len(res.text):>5} bytes)")
        else:
            print_fail(f"Route {route:<14} -> HTTP {res.status_code}")
            all_ok = False
    return all_ok


def main():
    print(f"\n{BOLD}===================================================================={RESET}")
    print(f"{BOLD}       RETAILSYNC WMS — PRE-CONFIRMATION AUDIT GATE RUNNER          {RESET}")
    print(f"{BOLD}===================================================================={RESET}")

    gates = [
        ("Automated Tests", run_gate_pytest),
        ("Database Invariants", run_gate_database),
        ("Typography & CSS", run_gate_typography_css),
        ("Content Guardrails", run_gate_content_guardrails),
        ("Enterprise Features", run_gate_features),
        ("Route Availability", run_gate_endpoints),
    ]

    results = []
    for name, gate_func in gates:
        ok = gate_func()
        results.append((name, ok))

    print(f"\n{BOLD}--------------------------------------------------------------------{RESET}")
    print(f"{BOLD} AUDIT SUMMARY REPORT{RESET}")
    print(f"{BOLD}--------------------------------------------------------------------{RESET}")
    all_passed = True
    for name, ok in results:
        status = f"{GREEN}PASSED{RESET}" if ok else f"{RED}FAILED{RESET}"
        if not ok:
            all_passed = False
        print(f"  {name:<25} : {status}")

    if all_passed:
        print(f"\n{BOLD}{GREEN}✓ ALL AUDIT GATES PASSED! CODEBASE IS VERIFIED FOR CONFIRMATION.{RESET}\n")
        sys.exit(0)
    else:
        print(f"\n{BOLD}{RED}✗ AUDIT GATES FAILED! DO NOT CONFIRM BEFORE RESOLVING ISSUES.{RESET}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
