import pytest
from fastapi.testclient import TestClient
from retailsync_app.main import app
from retailsync_app.database import SessionLocal
from retailsync_app import models

client = TestClient(app)

def test_global_typography_and_tabular_nums():
    """Verify Aptos/Arial global stack and tabular-nums rules in CSS."""
    res = client.get("/static/css/app.css")
    assert res.status_code == 200
    css = res.text

    # Global font stack
    assert "'Aptos', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;" in css

    # Tabular numbers on numeric elements
    assert "font-variant-numeric: tabular-nums;" in css
    assert "td, th, .tabular, .price, .pos-price-tag, .status-strip__val, .hero-bento-val, .metric-value, .lot-code, [data-tabular]" in css

    # Role titles must never truncate
    assert ".user-card-role" in css
    assert "white-space: normal;" in css
    assert "overflow: visible;" in css
    assert "max-width: none;" in css


def test_dashboard_retail_upgrades():
    """Verify Bay A-01 (Ambient), Spoilage Write-Off action, zero forbidden emojis, zero jargon on /dashboard."""
    res = client.get("/dashboard")
    assert res.status_code == 200
    html = res.text

    # Data fix: Bay A-01 (Ambient)
    assert "Bay A-01 (Ambient)" in html
    assert "Bay B Ambient" not in html
    assert "Bay 0 Ambient" not in html

    # Write-off button
    assert "Write-Off Damaged / Spoilage" in html
    assert "writeOffStock" in html

    # Zero forbidden emojis
    forbidden_emojis = ["🛒", "📥", "📦", "🗺️", "📈", "☀️", "🌙", "⚡", "📁", "📄", "📘", "📊", "📽️", "🧠"]
    for emoji in forbidden_emojis:
        assert emoji not in html, f"Found forbidden emoji: {emoji}"

    # Zero forbidden jargon
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
        assert jargon not in html, f"Found forbidden jargon: {jargon}"


def test_warehouse_shelf_tag_generator():
    """Verify 4\"x2\" shelf barcode tag generator on /warehouse."""
    res = client.get("/warehouse")
    assert res.status_code == 200
    html = res.text

    # Button in inspector
    assert "Print Bin Barcode Label" in html

    # 4x2 Shelf tag modal
    assert 'id="warehouseStickerModal"' in html
    assert 'id="whStickerPrintArea"' in html
    assert 'id="whStickerBinCoord"' in html
    assert 'id="whStickerTempBadge"' in html
    assert 'id="whStickerProductName"' in html
    assert 'id="whStickerLotExp"' in html
    assert "Print 4x2 Labels (Adhesive Roll)" in html


def test_pos_thermal_receipt_modal():
    """Verify 80mm ESC/POS thermal receipt modal on /pos with all required fields."""
    res = client.get("/pos")
    assert res.status_code == 200
    html = res.text

    # Header and tax registration
    assert "RetailSync Superstore • Dhanmondi Central" in html
    assert "VAT Reg # 002918274-0101 • Mushak 6.3" in html

    # Cashier and receipt metadata
    assert "Nusrat (Till #01)" in html
    assert "#RS-88219" in html
    assert 'id="receiptDate"' in html

    # Summary fields
    assert 'id="receiptSubtotal"' in html
    assert 'id="receiptVat"' in html
    assert 'id="receiptGrandTotal"' in html
    assert 'id="receiptTendered"' in html
    assert 'id="receiptChange"' in html

    # Footer and Barcode
    assert "Thank you for shopping at RetailSync!" in html
    assert 'id="receiptBarcodeText"' in html

    # Action buttons and keyboard shortcuts
    assert "Print Thermal Receipt (Ctrl+P)" in html
    assert "New Sale (Space)" in html
    assert "printThermalReceipt" in html


def test_pos_products_milk_vita_stock():
    """Verify Milk Vita Liquid Milk 1L has 32 units available stock."""
    res = client.get("/api/v1/pos/products")
    assert res.status_code == 200
    products = res.json()
    milk = next((p for p in products if p.get("sku_code") == "SKU-MILK-1L"), None)
    assert milk is not None
    assert milk.get("total_available_stock") == 32
    assert "Pasteurised Liquid Milk" in milk.get("product_name")


def test_write_off_endpoint_execution():
    """Verify /api/v1/warehouse/write-off endpoint deducts stock and records stock ledger entry."""
    db = SessionLocal()
    try:
        # Get Aarong Sweet Misti Doi batch LOT-MV-260903
        batch = db.query(models.InventoryBatch).filter(models.InventoryBatch.lot_number == "LOT-MV-260903").first()
        assert batch is not None
        initial_qty = batch.current_quantity

        payload = {
            "lot_number": "LOT-MV-260903",
            "quantity": 2,
            "reason": "Spoilage Write-Off Test"
        }
        res = client.post("/api/v1/warehouse/write-off", json=payload)
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "SUCCESS"
        assert data["quantity_written_off"] == 2
        assert data["previous_balance"] == initial_qty
        assert data["new_balance"] == initial_qty - 2
        assert "WO-" in data["reference_number"]

        # Verify ledger entry
        ledger = (
            db.query(models.StockLedger)
            .filter(models.StockLedger.reference_number == data["reference_number"])
            .first()
        )
        assert ledger is not None
        assert ledger.transaction_type == models.TransactionType.DAMAGE_QUARANTINE
        assert ledger.quantity_change == -2
        assert "Spoilage Write-Off" in ledger.notes

        # Restore quantity to initial
        batch.current_quantity = initial_qty
        db.commit()
    finally:
        db.close()


def test_auth_switch_role_endpoint():
    """Verify POST /api/v1/auth/switch-role works for all personas and sets session cookie."""
    roles = ["admin", "supervisor", "procurement", "cashier"]
    for role in roles:
        res = client.post("/api/v1/auth/switch-role", json={"role": role})
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "SUCCESS"
        assert data["user"]["role"] in ["ADMIN", "SUPERVISOR", "PROCUREMENT", "OPERATOR"]
        assert "retailsync_token" in res.cookies

    # Invalid role returns 400
    res_invalid = client.post("/api/v1/auth/switch-role", json={"role": "hacker"})
    assert res_invalid.status_code == 400


def test_manager_executive_suite_and_text_consistency():
    """Verify manager executive strip, dialog, bento copy, and product text consistency."""
    # Dashboard check
    res_dash = client.get("/dashboard")
    assert res_dash.status_code == 200
    html_dash = res_dash.text
    assert "Store Manager Executive Operations" in html_dash
    assert "Executive Controls" in html_dash
    assert "2 near-expiry batches, 1 stockout trigger" in html_dash

    # Putaway check
    res_putaway = client.get("/putaway")
    assert res_putaway.status_code == 200
    assert "Milk Vita Pasteurised Liquid Milk 1L" in res_putaway.text
    assert "Pran Pasteurised Liquid Milk 1L" not in res_putaway.text

    # Audits check
    res_audits = client.get("/audits")
    assert res_audits.status_code == 200
    assert 'data-expected="32"' in res_audits.text
    assert "SKU-SOYA-5L" in res_audits.text

    # CSS sizing scale-up check
    res_css = client.get("/static/css/app.css")
    assert res_css.status_code == 200
    assert "font-size: 15px;" in res_css.text


def test_speculative_loading_and_background_cache():
    """Verify Speculation Rules API, preloader, and Stale-While-Revalidate headers."""
    # HTML routes return Cache-Control headers
    res_dash = client.get("/dashboard")
    assert res_dash.status_code == 200
    assert "stale-while-revalidate" in res_dash.headers.get("cache-control", "").lower()

    res_pos = client.get("/pos")
    assert res_pos.status_code == 200
    assert "stale-while-revalidate" in res_pos.headers.get("cache-control", "").lower()

    html = res_dash.text
    # Speculation Rules tag present
    assert '<script type="speculationrules">' in html
    assert '"prefetch"' in html
    assert '"prerender"' in html

    # Background Cache Engine present
    assert "__retailsync_cache" in html
    assert "getRetailSyncCache" in html
    assert "pos_products" in html
    assert "inbound_pos" in html


def test_layout_alignments_and_box_harmony():
    """Verify standardized status strip, responsive split layout, and card alignment rules."""
    res_css = client.get("/static/css/app.css")
    assert res_css.status_code == 200
    css = res_css.text

    # Status strip 4-column layout
    assert "repeat(4, 1fr) !important;" in css

    # Responsive split layout
    assert ".dashboard-split-layout" in css
    assert "grid-template-columns: 1fr 440px !important;" in css

    # Brand text vertical stack
    assert ".brand-text-block" in css
    assert "flex-direction: column;" in css

    # Product title height alignment
    assert ".pos-product-title" in css
    assert "min-height: 38px !important;" in css

    # Table cell vertical alignment
    assert "vertical-align: middle !important;" in css


