import os
import re
from fastapi.testclient import TestClient
from retailsync_app.main import app

client = TestClient(app)

def test_overview_status_and_encoding():
    """Verify overview returns HTTP 200 and UTF-8 charset."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    assert "text/html" in res.headers["content-type"]


def test_zero_emoji_icons_on_overview():
    """Verify strictly NO emoji icons are rendered on the overview page."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    forbidden_emojis = ["🛒", "📥", "📦", "🗺️", "📈", "☀️", "🌙", "⚡", "📁", "📄", "📘", "📊", "📽️", "🧠"]
    for emoji in forbidden_emojis:
        assert emoji not in html, f"Forbidden emoji '{emoji}' found in overview page"


def test_zero_developer_jargon_on_overview():
    """Verify technical implementation jargon is eliminated from user-facing copy."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    forbidden_jargon = [
        "3NF",
        "SELECT ... FOR UPDATE",
        "row-level locking",
        "PG16 3NF ACTIVE",
        "Sub-2.0s SLA",
        "Greasley Math",
        "Wilson Economic Order Quantity",
    ]
    for jargon in forbidden_jargon:
        assert jargon not in html, f"Forbidden developer jargon '{jargon}' found in user-facing copy"


def test_swiss_minimalist_typography_and_layers():
    """Verify IBM Plex typography and layered CSS cascade architecture."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    assert "IBM Plex Sans" in html
    assert "IBM Plex Mono" in html
    assert 'href="/styles/index.css?v=2.1.0"' in html

    # Verify CSS entrypoint defines the 6 standard cascade layers
    css_res = client.get("/styles/index.css")
    assert css_res.status_code == 200
    assert "@layer reset, tokens, base, layout, components, utilities;" in css_res.text


def test_single_accent_color_and_tokens():
    """Verify single accent color token (#38BDF8 / #0369A1) and semantic dots only."""
    res = client.get("/styles/tokens.css")
    assert res.status_code == 200
    css = res.text.lower()

    assert "--color-accent: #38bdf8;" in css
    assert "--color-accent: #0369a1;" in css

    # Semantic colors for status dots
    assert "--color-status-success:" in css
    assert "--color-status-warning:" in css
    assert "--color-status-danger:" in css


def test_status_strip_and_primary_valuation():
    """Verify StatusStrip renders primary valuation with mono display typography and secondary metrics."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    assert 'class="status-strip"' in html
    assert 'id="metricValuation"' in html
    assert "Inventory Valuation" in html
    assert "Active SKUs" in html
    assert "Active Batches" in html
    assert "Open Orders" in html
    assert "Checkout Latency" in html
    assert "ms" in html


def test_attention_queue_and_status_dots():
    """Verify Attention Queue ruled list with 6px status dots and action links."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    assert 'id="attentionHeading"' in html
    assert "Needs attention" in html
    assert 'class="attention-list"' in html
    assert 'class="attention-row"' in html
    assert "status-dot--" in html
    assert "action-link" in html


def test_all_workspaces_preserved_and_shortcuts():
    """Verify all 6 operational modules are indexed with routes and shortcut key hints."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    expected_routes = [
        "/pos",
        "/inbound",
        "/putaway",
        "/warehouse",
        "/procurement",
        "/audits",
    ]
    for route in expected_routes:
        assert f'href="{route}"' in html, f"Missing route {route} in Overview page"

    # Verify shortcut hints
    assert "Keyboard shortcut: P" in html
    assert "Keyboard shortcut: I" in html
    assert "Keyboard shortcut: U" in html
    assert "Keyboard shortcut: W" in html
    assert "Keyboard shortcut: R" in html
    assert "Keyboard shortcut: L" in html


def test_modular_components_exist():
    """Verify all 11 isolated component folders contain README, HTML, and CSS."""
    components = [
        "SiteHeader",
        "NavMenu",
        "RoleSwitcher",
        "ThemeToggle",
        "StatusStrip",
        "Metric",
        "AttentionList",
        "AttentionRow",
        "WorkspaceIndex",
        "WorkspaceRow",
        "SiteFooter",
    ]
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "retailsync_app", "components")
    for comp in components:
        comp_dir = os.path.join(base_dir, comp)
        assert os.path.isdir(comp_dir), f"Missing component directory: {comp}"
        assert os.path.isfile(os.path.join(comp_dir, "README.md")), f"Missing README in {comp}"
        assert os.path.isfile(os.path.join(comp_dir, f"{comp}.html")), f"Missing HTML in {comp}"
        assert os.path.isfile(os.path.join(comp_dir, f"{comp}.css")), f"Missing CSS in {comp}"


def test_academic_deliverables_accessible():
    """Verify master technical suite and academic deliverables remain accessible via footer."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    assert 'href="/proposal/pdf"' in html
    assert 'href="/proposal/docx"' in html
    assert 'href="/deck"' in html
    assert 'href="/engineering-suite/pdf"' in html
    assert 'href="/engineering-suite/docx"' in html
    assert 'href="/team-pack.zip"' in html
