import pytest
from fastapi.testclient import TestClient
import re
import os

from retailsync_app.main import app

client = TestClient(app)


def test_routes_status_and_theme():
    """Verify all 7 main HTML web routes return 200 and include dual theme support."""
    routes = [
        "/dashboard",
        "/pos",
        "/inbound",
        "/putaway",
        "/warehouse",
        "/procurement",
        "/audits",
    ]
    for route in routes:
        response = client.get(route)
        assert response.status_code == 200, f"Route {route} failed with status {response.status_code}"
        html = response.text

        # 1. Dual theme root attribute
        assert 'data-theme="light"' in html or 'data-theme' in html

        # 2. Navbar 3-Zone components
        assert 'id="themeToggleBtn"' in html
        assert 'v2.0-RELEASE' in html
        assert 'nav-zone-center' in html
        assert 'select-role-compact' in html
        assert 'Showcase ↗' in html
        assert 'Slides ↗' in html

        # 3. Heartbeat moved to footer
        assert "footer-telemetry" in html
        assert "PG16 3NF ACTIVE" in html

        # 4. Toast notification system & alert override
        assert 'id="toastContainer"' in html
        assert "showToast" in html
        assert "window.alert" in html
        assert "window.confirm" in html


def test_audits_superpowers():
    """Verify audits.html has live search, transaction type filter, and BFSA CSV export."""
    res = client.get("/audits")
    assert res.status_code == 200
    html = res.text

    # Search & Filter Bar
    assert 'id="ledgerSearchInput"' in html
    assert 'oninput="filterLedger()"' in html
    assert 'id="ledgerTypeFilter"' in html
    assert "POS_SALE_FEFO" in html
    assert "GRN_RECEIPT" in html
    assert "PUTAWAY" in html
    assert "WRITE_OFF" in html

    # Export CSV Button
    assert "exportLedgerCSV()" in html
    assert "RetailSync_Stock_Ledger_Audit.csv" in html

    # Table Formatting
    assert 'id="ledgerTable"' in html
    assert "retailsync-table" in html


def test_pos_critical_fixes():
    """Verify pos.html concurrency modal text, cash tender chips, and receipt modal."""
    res = client.get("/pos")
    assert res.status_code == 200
    html = res.text

    # Concurrency Modal
    assert 'id="concurrencyModal"' in html
    assert 'id="concurrencyResults"' in html
    assert "SELECT ... FOR UPDATE SKIP LOCKED" in html

    # Quick Cash Tender Chips
    assert "quickCashTender('EXACT')" in html or "Exact Cash" in html
    assert "quickCashTender(500)" in html
    assert "quickCashTender(1000)" in html

    # Web Audio Synthesizer Beep
    assert "playBarcodeBeep" in html
    assert "AudioContext" in html

    # Thermal Receipt Modal with Sawtooth
    assert 'id="receiptModal"' in html
    assert "receipt-paper" in html


def test_dashboard_guardrail_and_heartbeat():
    """Verify dashboard.html Card 1 text and heartbeat pill."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    assert "SELECT ... FOR UPDATE SKIP LOCKED" in html
    assert "PG16 3NF ACTIVE" in html


def test_inbound_shelflife_indicator():
    """Verify inbound.html 65% quality gate progress bar."""
    res = client.get("/inbound")
    assert res.status_code == 200
    html = res.text

    assert "shelflife-bar-container" in html
    assert "shelflife-zone-quarantine" in html
    assert "shelflife-zone-approved" in html
    assert "65% QUALITY GATE" in html


def test_procurement_scenario_presets():
    """Verify procurement.html scenario presets and CSV export."""
    res = client.get("/procurement")
    assert res.status_code == 200
    html = res.text

    assert "Normal Operations (1.0x)" in html
    assert "Friday Rush (1.4x)" in html
    assert "🌙 Ramadan Surge (2.5x)" in html
    assert 'id="replenishTable"' in html
    assert "exportTableToCSV" in html


def test_css_dual_theme_tokens():
    """Verify app.css defines all required Light and Dark mode variables."""
    css_path = os.path.join(os.path.dirname(__file__), "..", "retailsync_app", "static", "css", "app.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Day Mode tokens
    assert 'html[data-theme="light"]' in css
    assert "--bg-canvas: #eef2f6" in css
    assert "--bg-surface: #ffffff" in css
    assert "--primary-500: #2563eb" in css
    assert "--emerald-400: #059669" in css
    assert "--amber-400: #d97706" in css
    assert "--rose-400: #dc2626" in css
    assert "--cyan-400: #0284c7" in css
    assert "--table-th-bg: #e2e8f0" in css
    assert "--table-row-alt: #f8fafc" in css

    # Dark Mode tokens
    assert 'html[data-theme="dark"]' in css
    assert "--bg-canvas: #0b0f19" in css
    assert "--bg-surface: #111827" in css
    assert "--primary-500: #38bdf8" in css
    assert "--emerald-400: #10b981" in css
    assert "--amber-400: #f59e0b" in css
    assert "--rose-400: #f43f5e" in css
    assert "--cyan-400: #38bdf8" in css
    assert "--table-th-bg: #1e293b" in css
    assert "--table-row-alt: #162032" in css

    # Constraints
    assert "max-width: 1440px" in css
    assert "max-width: 1320px" in css
