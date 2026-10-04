import pytest
from fastapi.testclient import TestClient

from retailsync_app.main import app

client = TestClient(app)


def test_proposal_pdf_endpoints():
    """Verify all routes pointing to the official Capstone Proposal PDF return 200 and application/pdf."""
    pdf_routes = [
        "/proposal",
        "/proposal/pdf",
        "/proposal.pdf",
        "/RetailSync_WMS_Project_Proposal.pdf",
    ]
    for route in pdf_routes:
        res = client.get(route)
        assert res.status_code == 200, f"Failed on {route}"
        assert res.headers.get("content-type") == "application/pdf"
        assert len(res.content) > 500_000  # Should be ~1.9 MB


def test_proposal_docx_endpoints():
    """Verify all routes pointing to the official Capstone Proposal DOCX return 200 and docx MIME type."""
    docx_routes = [
        "/proposal/docx",
        "/proposal.docx",
        "/RetailSync_WMS_Project_Proposal.docx",
    ]
    for route in docx_routes:
        res = client.get(route)
        assert res.status_code == 200, f"Failed on {route}"
        assert "wordprocessingml" in res.headers.get("content-type")
        assert len(res.content) > 300_000  # Should be ~740 KB


def test_deck_pptx_endpoints():
    """Verify all routes pointing to the presentation slide deck (.pptx) return 200."""
    pptx_routes = [
        "/deck",
        "/deck/pptx",
        "/slides/pptx",
        "/RetailSync_Capstone_Proposal_Defense_Deck.pptx",
    ]
    for route in pptx_routes:
        res = client.get(route)
        assert res.status_code == 200, f"Failed on {route}"
        assert "presentationml" in res.headers.get("content-type")
        assert len(res.content) > 500_000  # Should be ~1.1 MB


def test_master_engineering_suite_pdf_endpoints():
    """Verify all routes pointing to the 70-page Master Technical Engineering Suite PDF return 200."""
    suite_pdf_routes = [
        "/engineering-suite",
        "/engineering-suite/pdf",
        "/engineering-suite.pdf",
        "/docs/master-suite.pdf",
        "/RetailSync_Master_Engineering_Suite.pdf",
    ]
    for route in suite_pdf_routes:
        res = client.get(route)
        assert res.status_code == 200, f"Failed on {route}"
        assert res.headers.get("content-type") == "application/pdf"
        assert len(res.content) > 500_000  # Should be ~760 KB


def test_master_engineering_suite_docx_endpoints():
    """Verify all routes pointing to the Master Technical Engineering Suite DOCX return 200."""
    suite_docx_routes = [
        "/engineering-suite/docx",
        "/engineering-suite.docx",
        "/docs/master-suite.docx",
        "/RetailSync_Master_Engineering_Suite.docx",
    ]
    for route in suite_docx_routes:
        res = client.get(route)
        assert res.status_code == 200, f"Failed on {route}"
        assert "wordprocessingml" in res.headers.get("content-type")
        assert len(res.content) > 50_000  # Should be ~94 KB


def test_technical_defense_guide_endpoints():
    """Verify all routes pointing to the Viva Defense & Technical Stack Guide return 200."""
    guide_routes = [
        "/technical-guide",
        "/tech-guide",
        "/TECHNICAL_STACK_AND_DEFENSE_GUIDE.md",
    ]
    for route in guide_routes:
        res = client.get(route)
        assert res.status_code == 200, f"Failed on {route}"
        assert "markdown" in res.headers.get("content-type")
        assert len(res.content) > 40_000  # Should be ~61 KB


def test_interactive_showcase_links():
    """Verify the interactive showcase HTML contains working absolute links to all documents."""
    res = client.get("/showcase")
    assert res.status_code == 200
    html = res.text

    assert 'href="/slides"' in html
    assert 'href="/deck"' in html
    assert 'href="/proposal/pdf"' in html
    assert 'href="/proposal/docx"' in html
    assert 'href="/engineering-suite/pdf"' in html
    assert 'href="/engineering-suite/docx"' in html
    assert 'href="/technical-guide"' in html
    assert "70-Page Tech Suite" in html or "70p Tech Suite" in html


def test_presentation_deck_navigation():
    """Verify the presentation slide deck contains direct action links to live app and deliverables."""
    res = client.get("/slides")
    assert res.status_code == 200
    html = res.text

    assert 'href="/dashboard"' in html
    assert 'href="/showcase"' in html
    assert 'href="/proposal/pdf"' in html
    assert 'href="/engineering-suite/pdf"' in html
    assert 'href="/technical-guide"' in html


def test_dashboard_deliverables_bento_card():
    """Verify the main operational dashboard renders the Academic Deliverables & 70p Suite Bento Card."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    assert "Academic Deliverables & Master Technical Suite" in html
    assert "70-Page Master Technical Engineering Suite" in html or "55+ Pages / 70p DDL" in html
    assert 'href="/engineering-suite/pdf"' in html
    assert 'href="/engineering-suite/docx"' in html
    assert 'href="/proposal/pdf"' in html
    assert 'href="/proposal/docx"' in html
    assert 'href="/deck"' in html
