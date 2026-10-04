import pytest
from fastapi.testclient import TestClient
import re
import os

from retailsync_app.main import app

client = TestClient(app)


def test_routes_status_and_theme():
    """Verify all 7 main HTML web routes return 200 and include dual theme support."""
    # Overview (/dashboard) follows the Swiss Minimalist design system
    dash_res = client.get("/dashboard")
    assert dash_res.status_code == 200
    dash_html = dash_res.text
    assert 'data-theme="light"' in dash_html or 'data-theme' in dash_html
    assert 'id="themeToggleBtn"' in dash_html
    assert 'v2.0-RELEASE' in dash_html

    routes = [
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

        # 3. Heartbeat in footer
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
    """Verify Swiss Minimalist Overview page: no developer jargon, IBM Plex fonts, clean telemetry."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    # Verify absence of developer jargon from user-facing copy
    assert "SELECT ... FOR UPDATE SKIP LOCKED" not in html
    assert "PG16 3NF ACTIVE" not in html

    # Verify Swiss Minimalist architecture & typography
    assert "IBM Plex Sans" in html
    assert "IBM Plex Mono" in html
    assert "status-strip" in html
    assert "attention-section" in html
    assert "workspaces-index" in html


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
    """Verify app.css defines all required Light and Dark mode variables for Apple Bento Clean."""
    css_path = os.path.join(os.path.dirname(__file__), "..", "retailsync_app", "static", "css", "app.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Typography
    assert "--font-heading: 'Manrope'" in css
    assert "--font-body: 'Inter'" in css
    assert "--font-mono: 'JetBrains Mono'" in css

    # Day Mode tokens (Apple Calm Mist)
    assert 'html[data-theme="light"]' in css
    assert "--bg-canvas: #f5f6f8" in css
    assert "--bg-surface: #ffffff" in css
    assert "--primary: #2563eb" in css
    assert "--emerald: #059669" in css
    assert "--amber: #d97706" in css
    assert "--rose: #dc2626" in css
    assert "--cyan: #0284c7" in css
    assert "--table-th-bg: #f9fafb" in css
    assert "--table-row-alt: #fcfdfe" in css
    assert "--radius-card: 16px" in css
    assert "--shadow-bento:" in css

    # Dark Mode tokens (Apple Space Charcoal)
    assert 'html[data-theme="dark"]' in css
    assert "--bg-canvas: #0c0e14" in css
    assert "--bg-surface: #151821" in css
    assert "--primary: #38bdf8" in css
    assert "--emerald: #10b981" in css
    assert "--amber: #f59e0b" in css
    assert "--rose: #f43f5e" in css
    assert "--cyan: #38bdf8" in css
    assert "--table-th-bg: #1c202d" in css
    assert "--table-row-alt: #181c27" in css

    # Constraints
    assert "max-width: 1440px" in css
    assert "max-width: 1280px" in css

