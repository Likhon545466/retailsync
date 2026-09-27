#!/usr/bin/env python3
"""
RetailSync High-Resolution Diagram Generator.
Generates 4 publication-quality, 300-DPI color diagrams for the Word document
and interactive HTML showcase:
1. 4-Tier Cyber-Physical Architecture with AI Demand Forecasting Engine
2. End-to-End Operational Lifecycle & Process Data Flow
3. AI Demand Forecasting & Predictive Replenishment ML Pipeline
4. 14-Week Capstone Engineering Roadmap & Scenario-Based Gantt Chart
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Path Setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ASSETS_DIR = os.path.join(PROJECT_ROOT, "proposal", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Font Setup
FONT_BOLD_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_font(size, bold=False):
    path = FONT_BOLD_PATH if bold else FONT_REG_PATH
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

# Color Palette
CLR_BG = (248, 250, 252)          # #F8FAFC
CLR_WHITE = (255, 255, 255)
CLR_NAVY = (27, 54, 93)           # #1B365D
CLR_SLATE = (43, 76, 126)         # #2B4C7E
CLR_DARK_TEXT = (30, 41, 59)      # #1E293B
CLR_MUTED_TEXT = (100, 116, 139)  # #64748B
CLR_BORDER = (203, 213, 225)      # #CBD5E1
CLR_BORDER_LIGHT = (226, 232, 240)# #E2E8F0

CLR_CYAN = (2, 132, 199)          # #0284C7
CLR_CYAN_BG = (240, 249, 255)     # #F0F9FF
CLR_TEAL = (13, 148, 136)         # #0D9488
CLR_TEAL_BG = (240, 253, 250)     # #F0FDFA
CLR_EMERALD = (16, 185, 129)      # #10B981
CLR_EMERALD_BG = (236, 253, 245)  # #ECFDF5
CLR_PURPLE = (124, 58, 237)       # #7C3AED
CLR_PURPLE_BG = (245, 243, 255)   # #F5F3FF
CLR_AMBER = (217, 119, 6)         # #D97706
CLR_AMBER_BG = (254, 243, 199)    # #FEF3C7
CLR_ROSE = (225, 29, 72)          # #E11D48
CLR_ROSE_BG = (255, 241, 242)     # #FFF1F2

def draw_rounded_card(draw, xy, fill=CLR_WHITE, outline=CLR_BORDER, radius=16, shadow=True):
    x0, y0, x1, y1 = xy
    if shadow:
        # Subtle drop shadow
        draw.rounded_rectangle([x0+4, y0+4, x1+4, y1+4], radius=radius, fill=(226, 232, 240, 180))
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline, width=2)

def draw_header_banner(draw, xy, title, subtitle=None, bg_color=CLR_NAVY, text_color=CLR_WHITE):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=bg_color)
    f_title = get_font(34, bold=True)
    draw.text((x0 + 30, y0 + 18), title, font=f_title, fill=text_color)
    if subtitle:
        f_sub = get_font(20, bold=False)
        draw.text((x0 + 30, y0 + 64), subtitle, font=f_sub, fill=(203, 213, 225))

def draw_arrow(draw, start, end, color=CLR_SLATE, width=4, arrow_size=16):
    x0, y0 = start
    x1, y1 = end
    draw.line([x0, y0, x1, y1], fill=color, width=width)
    
    # Calculate arrowhead
    import math
    angle = math.atan2(y1 - y0, x1 - x0)
    x_a = x1 - arrow_size * math.cos(angle - math.pi / 6)
    y_a = y1 - arrow_size * math.sin(angle - math.pi / 6)
    x_b = x1 - arrow_size * math.cos(angle + math.pi / 6)
    y_b = y1 - arrow_size * math.sin(angle + math.pi / 6)
    draw.polygon([(x1, y1), (x_a, y_a), (x_b, y_b)], fill=color)

# ==============================================================================
# DIAGRAM 1: 4-TIER CYBER-PHYSICAL ARCHITECTURE WITH AI FORECASTING ENGINE
# ==============================================================================
def generate_architecture_diagram():
    W, H = 2400, 1480
    im = Image.new("RGB", (W, H), CLR_BG)
    draw = ImageDraw.Draw(im)

    # Header Banner
    draw_header_banner(
        draw, [60, 40, W - 60, 150],
        "Figure 1: RetailSync 4-Tier Cyber-Physical System Architecture",
        "Stateless FastAPI, Next.js PWA, Redis Idempotency, 3NF PostgreSQL 16 & AI Time-Series Forecasting Worker"
    )

    tiers = [
        ("TIER 1: PHYSICAL HARDWARE & EDGE CAPTURE LAYER", CLR_CYAN_BG, CLR_CYAN, 190, 430),
        ("TIER 2: API GATEWAY, REVERSE PROXY & MQTT INGESTION", CLR_PURPLE_BG, CLR_PURPLE, 470, 710),
        ("TIER 3: CORE APPLICATION MICROSERVICES & AI FORECASTING ENGINE", CLR_TEAL_BG, CLR_TEAL, 750, 1140),
        ("TIER 4: ENTERPRISE PERSISTENCE, CACHE & OBJECT STORAGE", CLR_AMBER_BG, CLR_AMBER, 1180, 1420)
    ]

    for title, bg_col, border_col, y0, y1 in tiers:
        # Tier bounding box
        draw.rounded_rectangle([70, y0, W - 70, y1], radius=16, fill=bg_col, outline=border_col, width=2)
        # Tier Title
        f_tier = get_font(22, bold=True)
        draw.text((100, y0 + 16), title, font=f_tier, fill=border_col)

    # --- Tier 1 Boxes ---
    t1_boxes = [
        ("Handheld Barcode Scanners", "Bluetooth HID 1D/2D Trigger Guns\nScan Decode Latency < 350ms\nPaired with Android Phones", 100, 250, 600, 400),
        ("Mobile PWA Terminals", "Consumer Android 13+ Smartphones\nCamera ZXing / Html5-QRCode\nOffline IndexedDB Buffer Queue", 640, 250, 1140, 400),
        ("Retail POS Cash Registers", "Frontline Super Shop Checkouts\nSub-2.0s Atomic Deduction API\nLocal Cashier Offline Fallback", 1180, 250, 1680, 400),
        ("Automated Dock Gate (IoT)", "Stationary ESP32 MCU Scanner\nFixed RFID / Laser Array\nCommunicates over MQTT/TLS", 1720, 250, 2220, 400),
    ]
    for b_title, b_desc, x0, y0, x1, y1 in t1_boxes:
        draw_rounded_card(draw, [x0, y0, x1, y1], fill=CLR_WHITE, outline=CLR_CYAN)
        draw.text((x0 + 20, y0 + 16), b_title, font=get_font(20, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 20, y0 + 50), b_desc, font=get_font(16), fill=CLR_DARK_TEXT)

    # --- Tier 2 Boxes ---
    t2_boxes = [
        ("Nginx Reverse Proxy & Load Balancer", "SSL/TLS 1.3 Termination | HTTP/2 & WebSockets\nRate Limiting (100 req/s per IP) | Security Headers\nGzip / Brotli Static Asset Compression", 100, 530, 800, 680),
        ("Stateless API Gateway & Auth Guard", "JWT Token Validation (15-min access, 8-hr refresh)\nArgon2id Hash Authentication | Strict CORS Guard\nRequest Schema Validation via Pydantic v2", 840, 530, 1540, 680),
        ("MQTT Broker (Mosquitto/EMQX)", "MQTTS Port 8883 (TLS & Device Certificates)\nTelemetry from Automated Receiving Dock Gates\nPallet Weight & Arrival Sensor Feeds", 1580, 530, 2220, 680),
    ]
    for b_title, b_desc, x0, y0, x1, y1 in t2_boxes:
        draw_rounded_card(draw, [x0, y0, x1, y1], fill=CLR_WHITE, outline=CLR_PURPLE)
        draw.text((x0 + 20, y0 + 16), b_title, font=get_font(20, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 20, y0 + 50), b_desc, font=get_font(16), fill=CLR_DARK_TEXT)

    # --- Tier 3 Boxes ---
    t3_boxes = [
        ("Inbound & Digital GRN", "PO line matching\nVariance & damage logs\n75% Shelf-life verification", 100, 810, 500, 950),
        ("Directed Spatial Putaway", "ABC velocity zoning\nChilled vs. Ambient routing\nBin capacity enforcement", 530, 810, 930, 950),
        ("Real-Time FEFO Ledger", "Batch expiry tracking\nStrict FEFO priority queues\nQuarantine auto-locks", 960, 810, 1360, 950),
        ("POS Concurrency Lock", "SELECT ... FOR UPDATE\nRow-level pessimistic lock\np95 < 800ms / 0 deadlocks", 1390, 810, 1790, 950),
        ("Continuous Cycle Count", "Blind counting tally\nDiscrepancy reconciliation\nImmutable audit trigger", 1820, 810, 2220, 950),
    ]
    for b_title, b_desc, x0, y0, x1, y1 in t3_boxes:
        draw_rounded_card(draw, [x0, y0, x1, y1], fill=CLR_WHITE, outline=CLR_TEAL)
        draw.text((x0 + 16, y0 + 14), b_title, font=get_font(19, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 16, y0 + 44), b_desc, font=get_font(15), fill=CLR_DARK_TEXT)

    # Tier 3 Feature Box: AI Forecasting & Anomaly Worker (Spans bottom of Tier 3)
    draw_rounded_card(draw, [100, 980, 2220, 1110], fill=CLR_WHITE, outline=CLR_ROSE)
    draw.text((120, 996), "★ AI DEMAND FORECASTING ENGINE & ML ANOMALY WORKER (Async Celery & Redis Queue)", font=get_font(21, bold=True), fill=CLR_ROSE)
    ai_subtext = (
        "• LightGBM / XGBoost Time-Series Regressor: 7-day and 14-day rolling demand forecasting with holiday/festival embeddings (Ramadan, Eid, Paydays).\n"
        "• Dynamic Safety Stock & Reorder Point: Replaces static mean demand with predicted future demand (d_hat), factoring lead-time variance.\n"
        "• Unsupervised Shrinkage Detection: Scikit-learn Isolation Forest identifying anomalous inventory adjustments and theft patterns."
    )
    draw.text((120, 1032), ai_subtext, font=get_font(15), fill=CLR_DARK_TEXT)

    # --- Tier 4 Boxes ---
    t4_boxes = [
        ("PostgreSQL 16 Relational Database", "Strict 3NF Schema | 15 Normalized Core Tables\nACID Append-Only Ledger (`inventory_transactions`)\nComposite B-Tree Indexes & Connection Pooling", 100, 1230, 900, 1390),
        ("Redis 7 In-Memory Cache & Token Lock", "Sub-millisecond Session Tokens & Rate Limits\n`X-Idempotency-Key` Locks (48h TTL)\nCelery Task Queue Broker for ML Jobs", 940, 1230, 1640, 1390),
        ("WAL Archival & PITR Object Storage", "Continuous Write-Ahead Log (WAL) Streaming\nPoint-In-Time Recovery (RPO <= 1m, RTO <= 15m)\nEncrypted Cold-Chain Telemetry Backups", 1680, 1230, 2220, 1390),
    ]
    for b_title, b_desc, x0, y0, x1, y1 in t4_boxes:
        draw_rounded_card(draw, [x0, y0, x1, y1], fill=CLR_WHITE, outline=CLR_AMBER)
        draw.text((x0 + 20, y0 + 16), b_title, font=get_font(20, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 20, y0 + 50), b_desc, font=get_font(16), fill=CLR_DARK_TEXT)

    # Inter-tier Data Flow Connectors
    draw_arrow(draw, (350, 400), (350, 530), color=CLR_CYAN, width=3)
    draw_arrow(draw, (890, 400), (890, 530), color=CLR_CYAN, width=3)
    draw_arrow(draw, (1430, 400), (1430, 530), color=CLR_CYAN, width=3)
    draw_arrow(draw, (1970, 400), (1970, 530), color=CLR_CYAN, width=3)

    draw_arrow(draw, (450, 680), (450, 810), color=CLR_PURPLE, width=3)
    draw_arrow(draw, (1190, 680), (1190, 810), color=CLR_PURPLE, width=3)
    draw_arrow(draw, (1900, 680), (1900, 810), color=CLR_PURPLE, width=3)

    draw_arrow(draw, (500, 1110), (500, 1230), color=CLR_TEAL, width=3)
    draw_arrow(draw, (1290, 1110), (1290, 1230), color=CLR_TEAL, width=3)
    draw_arrow(draw, (1950, 1110), (1950, 1230), color=CLR_TEAL, width=3)

    out_file = os.path.join(ASSETS_DIR, "figure1_system_architecture.png")
    im.save(out_file, dpi=(300, 300))
    print(f"Generated: {out_file}")

# ==============================================================================
# DIAGRAM 2: END-TO-END OPERATIONAL LIFECYCLE & PROCESS FLOW
# ==============================================================================
def generate_operational_flow_diagram():
    W, H = 2400, 1380
    im = Image.new("RGB", (W, H), CLR_BG)
    draw = ImageDraw.Draw(im)

    draw_header_banner(
        draw, [60, 40, W - 60, 150],
        "Figure 2: RetailSync End-to-End Operational Lifecycle & Process Data Flow",
        "From Inbound Quality Gates to Sub-2.0s POS Checkouts, Blind Audits, and AI Demand-Driven Replenishment"
    )

    steps = [
        ("STAGE 1: DOCK RECEIVING", CLR_CYAN_BG, CLR_CYAN, 80, 200, 510, 1280),
        ("STAGE 2: SPATIAL PUTAWAY", CLR_PURPLE_BG, CLR_PURPLE, 540, 200, 970, 1280),
        ("STAGE 3: POS CHECKOUT SYNC", CLR_EMERALD_BG, CLR_EMERALD, 1000, 200, 1430, 1280),
        ("STAGE 4: CYCLE COUNT AUDIT", CLR_AMBER_BG, CLR_AMBER, 1460, 200, 1890, 1280),
        ("STAGE 5: AI REPLENISHMENT", CLR_ROSE_BG, CLR_ROSE, 1920, 200, 2350, 1280)
    ]

    for title, bg_col, border_col, x0, y0, x1, y1 in steps:
        draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=bg_col, outline=border_col, width=2)
        draw.text((x0 + 16, y0 + 16), title, font=get_font(20, bold=True), fill=border_col)

    # Stage 1 Sub-cards
    s1_cards = [
        ("Supplier Arrival", "Delivery truck reaches dock.\nManifest presented to clerk.", 270),
        ("PO Barcode Scan", "Clerk scans PO barcode;\nsystem loads line-item items.", 440),
        ("Shelf-Life Verification", "Mandatory check: batch must\nhave >= 75% shelf-life left.", 610),
        ("Damage Quarantine", "Damaged units isolated to\nquarantine bin with photos.", 780),
        ("Digital GRN Commit", "Immutable GRN issued;\nvendor credit note advisory.", 950),
    ]
    for title, desc, y_pos in s1_cards:
        draw_rounded_card(draw, [100, y_pos, 490, y_pos + 130], fill=CLR_WHITE, outline=CLR_CYAN)
        draw.text((116, y_pos + 14), title, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((116, y_pos + 46), desc, font=get_font(15), fill=CLR_DARK_TEXT)
        if y_pos < 950:
            draw_arrow(draw, (295, y_pos + 130), (295, y_pos + 170), color=CLR_CYAN, width=3)

    # Stage 2 Sub-cards
    s2_cards = [
        ("Putaway Engine Trigger", "New stock triggers spatial\nrouting algorithm in backend.", 270),
        ("ABC Velocity Check", "Fast-moving (Class A) near\ndispatch dock; Class C higher.", 440),
        ("Climate Zone Match", "Chilled dairy -> Cold Zone\nAmbient staples -> Dry Aisle", 610),
        ("Bin Suggestion", "System allocates exact coordinate:\nZone-Aisle-Rack-Shelf-Bin", 780),
        ("Mobile Scan Verify", "Operator scans physical bin\nbarcode to confirm placement.", 950),
    ]
    for title, desc, y_pos in s2_cards:
        draw_rounded_card(draw, [560, y_pos, 950, y_pos + 130], fill=CLR_WHITE, outline=CLR_PURPLE)
        draw.text((576, y_pos + 14), title, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((576, y_pos + 46), desc, font=get_font(15), fill=CLR_DARK_TEXT)
        if y_pos < 950:
            draw_arrow(draw, (755, y_pos + 130), (755, y_pos + 170), color=CLR_PURPLE, width=3)

    # Stage 3 Sub-cards
    s3_cards = [
        ("POS Barcode Scan", "Cashier scans SKU at checkout;\nPOST /api/v1/pos/sync.", 270),
        ("SELECT ... FOR UPDATE", "Pessimistic row lock acquired\non earliest active FEFO batch.", 440),
        ("Sub-2.0s Deduction", "Atomic stock balance decrement;\nTransaction committed in <800ms.", 610),
        ("Zero Overselling", "Concurrent requests serialized;\n0 deadlocks across 10 registers.", 780),
        ("Offline IndexedDB", "If broadband drops, sales buffer\nlocally; syncs on reconnect.", 950),
    ]
    for title, desc, y_pos in s3_cards:
        draw_rounded_card(draw, [1020, y_pos, 1410, y_pos + 130], fill=CLR_WHITE, outline=CLR_EMERALD)
        draw.text((1036, y_pos + 14), title, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((1036, y_pos + 46), desc, font=get_font(15), fill=CLR_DARK_TEXT)
        if y_pos < 950:
            draw_arrow(draw, (1215, y_pos + 130), (1215, y_pos + 170), color=CLR_EMERALD, width=3)

    # Stage 4 Sub-cards
    s4_cards = [
        ("Blind Cycle Count", "System generates tally sheet;\nstock quantities strictly hidden.", 270),
        ("Physical Floor Count", "Operator scans and enters\nactual physical units in bin.", 440),
        ("Discrepancy Check", "Variance calculated in background;\nflags items diverging > 2%.", 610),
        ("Supervisor Workflow", "Adjustments > 1,000 BDT require\nphoto proof and supervisor signoff.", 780),
        ("Isolation Forest ML", "Unsupervised anomaly detection\nidentifies theft & loss clusters.", 950),
    ]
    for title, desc, y_pos in s4_cards:
        draw_rounded_card(draw, [1480, y_pos, 1870, y_pos + 130], fill=CLR_WHITE, outline=CLR_AMBER)
        draw.text((1496, y_pos + 14), title, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((1496, y_pos + 46), desc, font=get_font(15), fill=CLR_DARK_TEXT)
        if y_pos < 950:
            draw_arrow(draw, (1675, y_pos + 130), (1675, y_pos + 170), color=CLR_AMBER, width=3)

    # Stage 5 Sub-cards
    s5_cards = [
        ("Daily Sales Aggregation", "Nightly sales rollups feed\ninto feature engineering store.", 270),
        ("AI Demand Forecast", "LightGBM regressor projects\n7-day & 14-day rolling demand.", 440),
        ("Festival Embeddings", "Ramadan, Eid, and payday flags\nanticipate demand spikes.", 610),
        ("Dynamic ROP / SS", "Reorder Point adjusted dynamically\nfactoring vendor lead variance.", 780),
        ("Automated Draft PO", "When stock < ROP, draft PO\ngenerated for 1-click buyer approval.", 950),
    ]
    for title, desc, y_pos in s5_cards:
        draw_rounded_card(draw, [1940, y_pos, 2330, y_pos + 130], fill=CLR_WHITE, outline=CLR_ROSE)
        draw.text((1956, y_pos + 14), title, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((1956, y_pos + 46), desc, font=get_font(15), fill=CLR_DARK_TEXT)
        if y_pos < 950:
            draw_arrow(draw, (2135, y_pos + 130), (2135, y_pos + 170), color=CLR_ROSE, width=3)

    # Inter-stage Connectors (Left to Right flow)
    draw_arrow(draw, (490, 675), (560, 675), color=CLR_SLATE, width=4)
    draw_arrow(draw, (950, 675), (1020, 675), color=CLR_SLATE, width=4)
    draw_arrow(draw, (1410, 675), (1480, 675), color=CLR_SLATE, width=4)
    draw_arrow(draw, (1870, 675), (1940, 675), color=CLR_SLATE, width=4)

    # Feedback Loop (Bottom Stage 5 back to Stage 1)
    draw.line([(2135, 1080), (2135, 1180), (295, 1180), (295, 1080)], fill=CLR_NAVY, width=3)
    draw_arrow(draw, (295, 1180), (295, 1085), color=CLR_NAVY, width=3)
    draw.text((800, 1145), "★ REPLENISHMENT FEEDBACK LOOP: Automated Draft PO dispatches to Supplier -> Inbound Dock (Stage 1)", font=get_font(17, bold=True), fill=CLR_NAVY)

    out_file = os.path.join(ASSETS_DIR, "figure2_operational_flow.png")
    im.save(out_file, dpi=(300, 300))
    print(f"Generated: {out_file}")

# ==============================================================================
# DIAGRAM 3: AI DEMAND FORECASTING & PREDICTIVE REPLENISHMENT PIPELINE
# ==============================================================================
def generate_ai_pipeline_diagram():
    W, H = 2400, 1380
    im = Image.new("RGB", (W, H), CLR_BG)
    draw = ImageDraw.Draw(im)

    draw_header_banner(
        draw, [60, 40, W - 60, 150],
        "Figure 3: RetailSync AI Demand Forecasting & Replenishment DSS Architecture",
        "Supervised LightGBM Time-Series Regression with Bangladeshi Retail Calendar Flags & Greasley Dynamic Safety Stock"
    )

    # Columns / Blocks
    col_w = 400
    gap = 60
    left_margin = 100
    top_y = 200
    bot_y = 1280

    cols = [
        ("1. DATA INGESTION", CLR_CYAN_BG, CLR_CYAN, left_margin, left_margin + col_w),
        ("2. FEATURE STORE", CLR_PURPLE_BG, CLR_PURPLE, left_margin + (col_w + gap), left_margin + 2*col_w + gap),
        ("3. ML MODEL ENGINE", CLR_TEAL_BG, CLR_TEAL, left_margin + 2*(col_w + gap), left_margin + 3*col_w + 2*gap),
        ("4. UNCERTAINTY BANDS", CLR_AMBER_BG, CLR_AMBER, left_margin + 3*(col_w + gap), left_margin + 4*col_w + 3*gap),
        ("5. REPLENISHMENT DSS", CLR_ROSE_BG, CLR_ROSE, left_margin + 4*(col_w + gap), left_margin + 5*col_w + 4*gap),
    ]

    for title, bg_col, border_col, x0, x1 in cols:
        draw.rounded_rectangle([x0, top_y, x1, bot_y], radius=16, fill=bg_col, outline=border_col, width=2)
        draw.text((x0 + 16, top_y + 16), title, font=get_font(20, bold=True), fill=border_col)

    # Cards Col 1: Ingestion
    c1 = [
        ("POS Sales Ledger", "Real-time ticket scans\nGranularity: hourly/daily\nAtomic line-item checkout", 280),
        ("Inventory History", "Stockout event records\nDamaged write-offs\nSupplier GRN timestamps", 520),
        ("Vendor Performance", "Historical lead-times (L)\nSupplier variance (sigma_L)\nFulfillment rate history", 760),
        ("Store Demographics", "Urban cluster location\nFootfall volume indices\nStorage capacity limits", 1000)
    ]
    for t, d, y in c1:
        x0 = cols[0][3] + 20
        x1 = cols[0][4] - 20
        draw_rounded_card(draw, [x0, y, x1, y + 170], fill=CLR_WHITE, outline=CLR_CYAN)
        draw.text((x0 + 16, y + 14), t, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 16, y + 50), d, font=get_font(15), fill=CLR_DARK_TEXT)

    # Cards Col 2: Feature Store
    c2 = [
        ("Lag Features", "Lag-1, Lag-7, Lag-14 sales\nRolling 7-day mean & std\nExponential moving averages", 280),
        ("Festival Calendar Flags", "★ Ramadan Surge Flag\n★ Eid-ul-Fitr / Eid-ul-Adha\n★ Shab-e-Barat / Puja", 520),
        ("Payday Cycle Flags", "1st to 5th of Month Spike\nGovernment & Corporate cycle\nWeekend vs. Weekday bias", 760),
        ("Perishable Decay", "Days to product expiry\nTemperature sensitivity\nCategory velocity class", 1000)
    ]
    for t, d, y in c2:
        x0 = cols[1][3] + 20
        x1 = cols[1][4] - 20
        draw_rounded_card(draw, [x0, y, x1, y + 170], fill=CLR_WHITE, outline=CLR_PURPLE)
        draw.text((x0 + 16, y + 14), t, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 16, y + 50), d, font=get_font(15), fill=CLR_DARK_TEXT)

    # Cards Col 3: ML Model
    c3 = [
        ("LightGBM Regressor", "Gradient-boosted trees\nSub-50ms inference latency\nOptimized for tabular data", 280),
        ("Multi-Horizon Forecast", "Recursive 7-day rolling\nDirect 14-day reorder view\nRetrained weekly via Celery", 520),
        ("Cold-Start Strategy", "Category-level hierarchy\nFallback to Bayesian priors\nfor newly introduced SKUs", 760),
        ("Loss Function Tuning", "Asymmetric loss penalty:\nUnder-stocking penalized 2x\nmore than slight over-stocking", 1000)
    ]
    for t, d, y in c3:
        x0 = cols[2][3] + 20
        x1 = cols[2][4] - 20
        draw_rounded_card(draw, [x0, y, x1, y + 170], fill=CLR_WHITE, outline=CLR_TEAL)
        draw.text((x0 + 16, y + 14), t, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 16, y + 50), d, font=get_font(15), fill=CLR_DARK_TEXT)

    # Cards Col 4: Uncertainty
    c4 = [
        ("Expected Demand (d_hat)", "Point estimate of future\ndaily sales across horizon L\nUnits: items/day", 280),
        ("Demand Variance (sigma_d)", "Standard deviation of demand\nforecast error distribution\nMeasures forecast confidence", 520),
        ("Quantile Bands", "P10: Conservative lower bound\nP50: Median expected demand\nP90: Festival surge peak", 760),
        ("MAPE Evaluation Gate", "Model validation threshold:\nMAPE <= 15% on FMCG\nModel alerts if drift occurs", 1000)
    ]
    for t, d, y in c4:
        x0 = cols[3][3] + 20
        x1 = cols[3][4] - 20
        draw_rounded_card(draw, [x0, y, x1, y + 170], fill=CLR_WHITE, outline=CLR_AMBER)
        draw.text((x0 + 16, y + 14), t, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 16, y + 50), d, font=get_font(15), fill=CLR_DARK_TEXT)

    # Cards Col 5: Replenishment DSS
    c5 = [
        ("Dynamic Safety Stock", "Greasley Formulation:\nSS = Z * sqrt(L*sigma_d^2 +\nd_hat^2*sigma_L^2)", 280),
        ("Dynamic Reorder Point", "ROP = (d_hat * L) + SS\nAutomatically rises before\nRamadan / Weekend spikes", 520),
        ("Economic Order Qty", "EOQ = sqrt((2*D*S) / H)\nCalculates optimal batch size\nminimizing holding costs", 760),
        ("Automated Draft PO", "Net Stock < ROP triggers draft;\nSupplier auto-selected;\nOne-click approval portal", 1000)
    ]
    for t, d, y in c5:
        x0 = cols[4][3] + 20
        x1 = cols[4][4] - 20
        draw_rounded_card(draw, [x0, y, x1, y + 170], fill=CLR_WHITE, outline=CLR_ROSE)
        draw.text((x0 + 16, y + 14), t, font=get_font(18, bold=True), fill=CLR_NAVY)
        draw.text((x0 + 16, y + 50), d, font=get_font(15), fill=CLR_DARK_TEXT)

    # Arrows between columns
    for i in range(4):
        x_from = cols[i][4]
        x_to = cols[i+1][3]
        for y_mid in [365, 605, 845, 1085]:
            draw_arrow(draw, (x_from, y_mid), (x_to, y_mid), color=CLR_SLATE, width=3)

    out_file = os.path.join(ASSETS_DIR, "figure3_ai_forecasting_pipeline.png")
    im.save(out_file, dpi=(300, 300))
    print(f"Generated: {out_file}")

# ==============================================================================
# DIAGRAM 4: 14-WEEK CAPSTONE ROADMAP & SCENARIO-BASED GANTT CHART
# ==============================================================================
def generate_gantt_roadmap_diagram():
    W, H = 2400, 1480
    im = Image.new("RGB", (W, H), CLR_BG)
    draw = ImageDraw.Draw(im)

    draw_header_banner(
        draw, [60, 40, W - 60, 150],
        "Figure 4: RetailSync 14-Week Capstone Engineering Roadmap & Gantt Schedule",
        "7 Bi-Weekly Scrum Sprints Mapped to 4 Grounded Super Shop Operational Validation Scenarios"
    )

    # Timeline Grid Coordinates
    grid_left = 600
    grid_right = 2300
    grid_top = 220
    grid_bot = 980
    total_w = grid_right - grid_left
    week_w = total_w / 14.0

    # Draw Week Headers (W01 to W14)
    f_week = get_font(17, bold=True)
    for w in range(14):
        wx0 = grid_left + w * week_w
        wx1 = wx0 + week_w
        # Header block
        fill_col = CLR_WHITE if w % 2 == 0 else (241, 245, 249)
        draw.rectangle([wx0, grid_top - 40, wx1, grid_top], fill=fill_col, outline=CLR_BORDER)
        draw.text((wx0 + 20, grid_top - 32), f"W{w+1:02d}", font=f_week, fill=CLR_NAVY)
        # Vertical guide lines
        draw.line([wx0, grid_top, wx0, grid_bot], fill=(226, 232, 240), width=1)
    draw.line([grid_right, grid_top, grid_right, grid_bot], fill=(226, 232, 240), width=1)

    sprints = [
        ("Sprint 1 (W01-W02)", "Docker, 3NF Schema & JWT Auth", 0, 2, CLR_CYAN),
        ("Sprint 2 (W03-W04)", "Inbound Barcode Receiving & GRN", 2, 4, CLR_PURPLE),
        ("Sprint 3 (W05-W06)", "Directed Putaway & FEFO Ledger", 4, 6, CLR_TEAL),
        ("Sprint 4 (W07-W08)", "Sub-2.0s POS Sync & Offline PWA", 6, 8, CLR_EMERALD),
        ("Sprint 5 (W09-W10)", "AI Demand Forecast & Replenish DSS", 8, 10, CLR_ROSE),
        ("Sprint 6 (W11-W12)", "Blind Cycle Counting & Anomaly ML", 10, 12, CLR_AMBER),
        ("Sprint 7 (W13-W14)", "Locust Stress, Hardening & Defense", 12, 14, CLR_SLATE)
    ]

    row_h = 100
    f_sprint_title = get_font(19, bold=True)
    f_sprint_sub = get_font(15, bold=False)

    for idx, (s_name, s_sub, start_w, end_w, color) in enumerate(sprints):
        y0 = grid_top + idx * row_h
        y1 = y0 + row_h

        # Left label panel
        draw.rectangle([70, y0, grid_left, y1], fill=CLR_WHITE, outline=CLR_BORDER)
        draw.text((90, y0 + 16), s_name, font=f_sprint_title, fill=CLR_NAVY)
        draw.text((90, y0 + 52), s_sub, font=f_sprint_sub, fill=CLR_MUTED_TEXT)

        # Gantt Bar
        bar_x0 = grid_left + start_w * week_w + 6
        bar_x1 = grid_left + end_w * week_w - 6
        bar_y0 = y0 + 18
        bar_y1 = y1 - 18
        draw.rounded_rectangle([bar_x0, bar_y0, bar_x1, bar_y1], radius=12, fill=color)

        # Milestone Marker / Text on bar
        f_bar = get_font(16, bold=True)
        draw.text((bar_x0 + 16, bar_y0 + 18), f"{s_name.split()[0]} Deliverable", font=f_bar, fill=CLR_WHITE)

    # --- Scenario-Based Validation Section (Bottom of Diagram) ---
    draw.rounded_rectangle([70, 1030, W - 70, 1430], radius=16, fill=CLR_WHITE, outline=CLR_NAVY, width=2)
    draw.text((100, 1048), "★ CORE CAPSTONE VALIDATION SCENARIOS (Operational Acceptance Gates)", font=get_font(22, bold=True), fill=CLR_NAVY)

    scenarios = [
        ("SCENARIO A: DOCK QUALITY GATE", "Perishable Milk Intake Test\nSupplier delivers 100 crates; 10 have < 75% shelf-life.\nResult: PWA scanner rejects with audible tone; creates supplier credit note.\nValidated In: Sprint 2 (Week 4)", 100, 1100, 610, 1400, CLR_CYAN_BG, CLR_CYAN),
        ("SCENARIO B: RUSH-HOUR CONCURRENCY", "10-Cashier POS Contention Test\n10 registers bill final 5 units of soybean oil at 8 PM.\nResult: Row lock serializes; 5 succeed in <800ms; 5 get instant OOS; 0 deadlocks.\nValidated In: Sprint 4 (Week 8)", 640, 1100, 1160, 1400, CLR_EMERALD_BG, CLR_EMERALD),
        ("SCENARIO C: NETWORK BLACKOUT REPLAY", "Wi-Fi Outage Checkout Test\nBroadband drops during 50 customer checkout scans.\nResult: PWA buffers locally in IndexedDB; auto-syncs idempotently on reconnect.\nValidated In: Sprint 4 (Week 8)", 1190, 1100, 1710, 1400, CLR_AMBER_BG, CLR_AMBER),
        ("SCENARIO D: FESTIVAL AI DEMAND SURGE", "Pre-Ramadan Surge Prediction Test\nBaseline demand is 50 units/day; Ramadan surges to 220.\nResult: AI detects festival flag; raises ROP 10 days ahead; prevents stockout.\nValidated In: Sprint 5 (Week 10)", 1740, 1100, 2260, 1400, CLR_ROSE_BG, CLR_ROSE)
    ]

    for title, desc, x0, y0, x1, y1, bg_col, border_col in scenarios:
        draw_rounded_card(draw, [x0, y0, x1, y1], fill=bg_col, outline=border_col)
        draw.text((x0 + 16, y0 + 16), title, font=get_font(18, bold=True), fill=border_col)
        draw.text((x0 + 16, y0 + 56), desc, font=get_font(15), fill=CLR_DARK_TEXT)

    out_file = os.path.join(ASSETS_DIR, "figure4_gantt_roadmap.png")
    im.save(out_file, dpi=(300, 300))
    print(f"Generated: {out_file}")

if __name__ == "__main__":
    print("Generating High-Resolution Diagram Assets for RetailSync...")
    generate_architecture_diagram()
    generate_operational_flow_diagram()
    generate_ai_pipeline_diagram()
    generate_gantt_roadmap_diagram()
    print("All 4 Diagram Assets Successfully Generated in proposal/assets/")
