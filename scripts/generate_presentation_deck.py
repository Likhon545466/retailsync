#!/usr/bin/env python3
"""
RetailSync: Centralized Super Shop Warehouse Management System
Automated 16:9 Academic Presentation Slide Deck Generator (.pptx)
Department of Software Engineering, Daffodil International University (DIU).
Course: SE-231 (Software System Analysis & Design / Capstone Project 2).
Author: Raisul Islam Likhon (Section: SWE-44D)
Date: September 2026 | Version: 2.0.0-RELEASE
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# --- Color Palette ---
COLOR_NAVY_DARK = RGBColor(15, 23, 42)       # #0F172A - Deep Background
COLOR_NAVY_PRIMARY = RGBColor(27, 54, 93)    # #1B365D - Brand Navy
COLOR_SLATE_BLUE = RGBColor(43, 76, 126)     # #2B4C7E - Slate Accent
COLOR_CARD_DARK = RGBColor(30, 41, 59)       # #1E293B - Card Surface Dark
COLOR_CARD_LIGHT = RGBColor(248, 250, 252)   # #F8FAFC - Card Surface Light
COLOR_BORDER = RGBColor(51, 65, 85)          # #334155 - Subtle Border
COLOR_BORDER_LIGHT = RGBColor(203, 213, 225) # #CBD5E1 - Light Border

COLOR_CYAN = RGBColor(14, 165, 233)          # #0EA5E9 - Primary Accent
COLOR_CYAN_LIGHT = RGBColor(56, 189, 248)    # #38BDF8 - Bright Cyan
COLOR_EMERALD = RGBColor(16, 185, 129)       # #10B981 - Success Green
COLOR_AMBER = RGBColor(245, 158, 11)         # #F59E0B - Warning Amber
COLOR_ROSE = RGBColor(244, 63, 94)           # #F43F5E - Danger / Leak Rose
COLOR_PURPLE = RGBColor(168, 85, 247)        # #A855F7 - AI / ML Purple

COLOR_TEXT_WHITE = RGBColor(255, 255, 255)
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8
COLOR_TEXT_DARK = RGBColor(30, 41, 59)       # #1E293B

FONT_HEADING = "Calibri"
FONT_BODY = "Calibri"

def create_slide_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(project_root, "proposal", "assets")
    
    fig1_path = os.path.join(assets_dir, "figure1_system_architecture.png")
    fig2_path = os.path.join(assets_dir, "figure2_operational_flow.png")
    fig3_path = os.path.join(assets_dir, "figure3_ai_forecasting_pipeline.png")
    fig4_path = os.path.join(assets_dir, "figure4_gantt_roadmap.png")

    def add_slide_background(slide, color=COLOR_NAVY_DARK):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_slide_header(slide, title, category="CAPSTONE PROPOSAL DEFENSE", dark_mode=True):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.733), Inches(1.15))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Category Badge
        p_cat = tf.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.name = FONT_HEADING
        p_cat.font.size = Pt(14)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_CYAN if dark_mode else COLOR_SLATE_BLUE
        p_cat.space_after = Pt(2)
        
        # Title
        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(30)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT_WHITE if dark_mode else COLOR_NAVY_PRIMARY

    def add_slide_footer(slide, current_slide, total_slides=12, dark_mode=True):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.4))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"RetailSync (SE-231 Capstone Project 2) • Department of Software Engineering, Daffodil International University | Slide {current_slide} of {total_slides}"
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_TEXT_MUTED if dark_mode else COLOR_MUTED_GREY

    def add_card(slide, left, top, width, height, bg_color=COLOR_CARD_DARK, border_color=COLOR_BORDER):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        if border_color:
            shape.line.color.rgb = border_color
            shape.line.width = Pt(1)
        else:
            shape.line.fill.background()
        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Pt(7)
        tf.margin_right = Pt(7)
        tf.margin_top = Pt(7)
        tf.margin_bottom = Pt(7)
        return shape

    # =========================================================================
    # SLIDE 1: Title & Academic Credentials (Dark Cover)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide1, COLOR_NAVY_DARK)
    
    # Institution Badge Box
    inst_card = add_card(slide1, 0.8, 0.65, 11.733, 1.05, bg_color=RGBColor(24, 34, 53), border_color=COLOR_CYAN)
    tf_inst = inst_card.text_frame
    tf_inst.word_wrap = True
    p1 = tf_inst.paragraphs[0]
    p1.text = "DAFFODIL INTERNATIONAL UNIVERSITY • FACULTY OF SCIENCE & INFORMATION TECHNOLOGY"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(15.5)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_CYAN
    p1.alignment = PP_ALIGN.CENTER
    p2 = tf_inst.add_paragraph()
    p2.text = "Department of Software Engineering | Course: SE-231 (Software System Analysis & Design / Capstone Project 2)"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(13)
    p2.font.color.rgb = COLOR_TEXT_MUTED
    p2.alignment = PP_ALIGN.CENTER

    # Add Logo Picture if present
    logo_path = os.path.join(assets_dir, "retailsync_logo.png")
    if os.path.exists(logo_path):
        slide1.shapes.add_picture(logo_path, Inches(10.7), Inches(1.9), Inches(1.8), Inches(1.8))
        title_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(9.6), Inches(2.3))
    else:
        title_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(11.733), Inches(2.3))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    
    p_sub_tag = tf_t.paragraphs[0]
    p_sub_tag.text = "CAPSTONE PROJECT PROPOSAL DEFENSE • FALL 2026"
    p_sub_tag.font.name = FONT_HEADING
    p_sub_tag.font.size = Pt(15)
    p_sub_tag.font.bold = True
    p_sub_tag.font.color.rgb = COLOR_EMERALD
    p_sub_tag.space_after = Pt(4)
    
    p_m_title = tf_t.add_paragraph()
    p_m_title.text = "RetailSync: Centralized Super Shop Warehouse Management System"
    p_m_title.font.name = FONT_HEADING
    p_m_title.font.size = Pt(32)
    p_m_title.font.bold = True
    p_m_title.font.color.rgb = COLOR_TEXT_WHITE
    p_m_title.space_after = Pt(4)
    
    p_m_sub = tf_t.add_paragraph()
    p_m_sub.text = "Real-Time POS Concurrency, Dynamic Putaway, FEFO Batch Tracking, and AI-Driven Replenishment"
    p_m_sub.font.name = FONT_BODY
    p_m_sub.font.size = Pt(17)
    p_m_sub.font.color.rgb = COLOR_CYAN_LIGHT

    # 3 Stat Highlight Badges
    stats = [
        ("Sub-2.0s POS Latency", "p95 ≤ 800ms • Zero Oversell", COLOR_CYAN),
        ("< 16,000 BDT Hardware", "90% Capex Cut vs Zebra TC52", COLOR_EMERALD),
        ("14-Week Scrum Plan", "6 Sprints • 4 Validation Scenarios", COLOR_AMBER)
    ]
    for idx, (s_title, s_sub, s_col) in enumerate(stats):
        bx = add_card(slide1, 0.8 + idx * 4.0, 4.35, 3.733, 1.15, bg_color=COLOR_CARD_DARK, border_color=s_col)
        tf_s = bx.text_frame
        tf_s.word_wrap = True
        ps1 = tf_s.paragraphs[0]
        ps1.text = s_title
        ps1.font.name = FONT_HEADING
        ps1.font.size = Pt(18)
        ps1.font.bold = True
        ps1.font.color.rgb = s_col
        ps2 = tf_s.add_paragraph()
        ps2.text = s_sub
        ps2.font.name = FONT_BODY
        ps2.font.size = Pt(14)
        ps2.font.color.rgb = COLOR_TEXT_WHITE

    # Author Credentials Footer Card
    cred_card = add_card(slide1, 0.8, 5.65, 11.733, 1.25, bg_color=RGBColor(24, 34, 53), border_color=COLOR_BORDER)
    tf_cred = cred_card.text_frame
    tf_cred.word_wrap = True
    pc1 = tf_cred.paragraphs[0]
    pc1.text = "Project Team: Raisul Islam Likhon (Lead: 251-35-508)  •  Shottobroto Dey (251-35-017)  •  Golam Husnain Papon (251-35-529)"
    pc1.font.name = FONT_HEADING
    pc1.font.size = Pt(16)
    pc1.font.bold = True
    pc1.font.color.rgb = COLOR_CYAN
    pc2 = tf_cred.add_paragraph()
    pc2.text = "Section: SWE-44D (44th Batch)  •  Department of Software Engineering  •  Daffodil International University (DIU)"
    pc2.font.name = FONT_BODY
    pc2.font.size = Pt(13.5)
    pc2.font.color.rgb = COLOR_TEXT_WHITE

    slide1.notes_slide.notes_text_frame.text = (
        "Opening Script: Good morning, respected course instructors and evaluation committee members. "
        "On behalf of my project team members Shottobroto Dey, Golam Husnain Papon, and myself Raisul Islam Likhon from Section SWE-44D, "
        "today I am proud to present our Capstone Project 2 proposal: 'RetailSync: Centralized Super Shop Warehouse Management System'. "
        "RetailSync addresses a critical engineering problem in the modern trade grocery sector of Bangladesh: the destructive "
        "disconnect between frontline retail checkout counters and central distribution warehouses. Over the next 10 minutes, "
        "we will demonstrate our problem formulation, grounded objectives, 4-tier architecture, AI replenishment algorithms, and 14-week execution roadmap."
    )

    # =========================================================================
    # SLIDE 2: Industry Background & The 3 Critical Profit Leaks
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide2)
    add_slide_header(slide2, "Industry Problem: Disconnected Supermarkets & 3 Critical Profit Leaks", "PROBLEM STATEMENT & CONTEXT")
    add_slide_footer(slide2, 2)

    # Left: Operational Context
    ctx_card = add_card(slide2, 0.8, 1.6, 5.2, 5.1, bg_color=COLOR_CARD_DARK)
    tf_ctx = ctx_card.text_frame
    tf_ctx.word_wrap = True
    p = tf_ctx.paragraphs[0]
    p.text = "The Modern Retail Landscape in Bangladesh"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(8)

    bullets = [
        "Rapid Urban Expansion: ~65.2M urban citizens (39.7% national share, BBS 2022) increasingly rely on modern supermarkets like Shwapno (450+ outlets), Agora, Meena Bazar, and Unimart.",
        "Frontline vs Back-office Chasm: POS billing counters have modernized, but back-of-house warehouses still operate on paper manifests, pen-and-paper clipboards, and delayed manual Excel sheets.",
        "Batch Blindness: Standard POS software tracks only bulk SKU numbers. When shelves are restocked, newer milk or oil cartons are stacked in front, leaving older batches rotting at the back.",
        "Delayed Replenishment: Reorder decisions take 6 to 12 hours to reach central warehouses, causing severe stockouts during peak Friday and Ramadan shopping rushes."
    ]
    for b in bullets:
        pb = tf_ctx.add_paragraph()
        pb.text = "• " + b
        pb.font.name = FONT_BODY
        pb.font.size = Pt(13.5)
        pb.font.color.rgb = COLOR_TEXT_WHITE
        pb.space_after = Pt(4)

    # Right: 3 Profit Leaks Cards
    leaks = [
        ("15% to 22% Perishable Food & Dairy Spoilage",
         "Older batches rot unnoticed at the rear of shelves due to lack of FEFO batch tracking. Selling expired milk violates the Bangladesh Food Safety Act 2013 and causes millions in losses.",
         COLOR_ROSE, "LEAK 1: EXPIRY WASTE"),
        ("1.8% to 2.4% Phantom Shrinkage & Unrecorded Damage",
         "A severe disconnect between database records and physical shelf reality caused by unrecorded carton tears, internal theft, and delayed reconciliations.",
         COLOR_AMBER, "LEAK 2: PHANTOM INVENTORY"),
        ("7.5% to 11.2% Peak-Hour Stockout Revenue Losses",
         "Cooking oil, sugar, and milk run out within minutes during Friday evenings and Ramadan rushes. Non-atomic POS deductions delay warehouse replenishment by hours.",
         COLOR_CYAN, "LEAK 3: LOST SALES SURGE")
    ]
    for idx, (l_title, l_desc, l_col, l_tag) in enumerate(leaks):
        l_card = add_card(slide2, 6.3, 1.6 + idx * 1.75, 6.2, 1.6, bg_color=COLOR_CARD_DARK, border_color=l_col)
        tf_l = l_card.text_frame
        tf_l.word_wrap = True
        pt = tf_l.paragraphs[0]
        pt.text = l_tag
        pt.font.name = FONT_HEADING
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = l_col
        
        ph = tf_l.add_paragraph()
        ph.text = l_title
        ph.font.name = FONT_HEADING
        ph.font.size = Pt(17.5)
        ph.font.bold = True
        ph.font.color.rgb = COLOR_TEXT_WHITE
        
        pd = tf_l.add_paragraph()
        pd.text = l_desc
        pd.font.name = FONT_BODY
        pd.font.size = Pt(13.5)
        pd.font.color.rgb = COLOR_TEXT_MUTED

    slide2.notes_slide.notes_text_frame.text = (
        "Slide 2 Script: In Bangladesh, modern grocery chains are growing rapidly, but behind the shiny checkout counters, "
        "warehouse operations are fragile. The primary problem is the disconnect between front-of-house POS registers and back-of-house warehouses. "
        "This disconnect causes three crippling profit leaks: First, 15% to 22% perishable food and dairy spoilage because staff don't have batch-level "
        "expiry tracking. Second, 1.8% to 2.4% phantom shrinkage where the system claims stock exists but the shelf is empty. "
        "And third, 7.5% to 11.2% lost sales when high-velocity items sell out during evening and festival rushes. RetailSync directly solves all three."
    )

    # =========================================================================
    # SLIDE 3: Grounded Epistemological Taxonomy
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide3)
    add_slide_header(slide3, "Defending Proposal Claims: Grounded Epistemological Taxonomy", "ACADEMIC RIGOR & GROUNDING")
    add_slide_footer(slide3, 3)

    # Left Intro Card
    tax_intro = add_card(slide3, 0.8, 1.6, 3.8, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_CYAN)
    tf_ti = tax_intro.text_frame
    tf_ti.word_wrap = True
    p = tf_ti.paragraphs[0]
    p.text = "Why We Ground Every Value"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(8)

    tax_bullets = [
        "Eliminating Arbitrary Figures: In capstone defenses, student proposals are often challenged if numbers appear fabricated. We explicitly categorize every single claim.",
        "Three Strict Epistemological Classes:\n1. Literature Baselines: Published field research (BSOA, FAO, NRSS).\n2. Engineering SLOs: Testable benchmarks verified with Locust.\n3. Simulation Assumptions: Controlled pilot mathematical models.",
        "Zero Hand-Waving: Every percentage, latency threshold, and cost savings target is tied directly to a verifiable test protocol."
    ]
    for b in tax_bullets:
        pb = tf_ti.add_paragraph()
        pb.text = "• " + b
        pb.font.name = FONT_BODY
        pb.font.size = Pt(13.5)
        pb.font.color.rgb = COLOR_TEXT_WHITE
        pb.space_after = Pt(5)

    # Right: Taxonomy Table
    table_shape = slide3.shapes.add_table(8, 4, Inches(4.8), Inches(1.6), Inches(7.7), Inches(5.1))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(1.8)
    tbl.columns[1].width = Inches(1.6)
    tbl.columns[2].width = Inches(1.8)
    tbl.columns[3].width = Inches(2.5)

    headers = ["Metric / Parameter", "Claimed Value", "Classification", "Source & Verification Protocol"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_HEADING
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_WHITE

    taxonomy_rows = [
        ("Perishable Spoilage", "15% to 22% annual loss", "Literature Baseline", "BSOA 2024 Report & FAO Post-Harvest Study"),
        ("Phantom Shrinkage", "1.8% to 2.4% loss", "Industry Baseline", "NRSS Supermarket Shrinkage Survey"),
        ("Peak Stockout Losses", "7.5% to 11.2% lost sales", "Industry Baseline", "IHL Group Retail Out-of-Stock Index"),
        ("POS Checkout Latency", "≤ 2.0s (p95 ≤ 800ms)", "Engineering SLO", "Locust load test with PostgreSQL row locks"),
        ("Barcode Scan Latency", "≤ 350ms visual decode", "Hardware SLO", "Android camera/Bluetooth trigger test"),
        ("Post-Launch Spoilage", "< 6% annual wastage", "Simulation Target", "Modeled FEFO queue + automated quarantine"),
        ("Hardware Station Cost", "< 16,000 BDT (90% cut)", "Budget Benchmark", "Android phone + Bluetooth trigger vs Zebra")
    ]
    for r_idx, row in enumerate(taxonomy_rows):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(24, 34, 53) if r_idx % 2 == 1 else COLOR_CARD_DARK
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_BODY
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_TEXT_WHITE

    slide3.notes_slide.notes_text_frame.text = (
        "Slide 3 Script: To ensure our proposal has defense-grade academic rigor, we did not pick numbers out of thin air. "
        "We classified every single claimed metric into three epistemological tiers: First, published literature baselines like the "
        "15% to 22% spoilage reported by the Bangladesh Supermarket Owners Association and UN FAO. Second, empirical engineering SLOs "
        "that we will benchmark directly using automated Locust tests—such as our sub-2.0s POS deduction latency and sub-350ms barcode decode. "
        "And third, modeled simulation targets like reducing spoilage to under 6% through strict FEFO rotation."
    )

    # =========================================================================
    # SLIDE 4: SMART Project Objectives (O-01 to O-05)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide4)
    add_slide_header(slide4, "Quantitative SMART Project Objectives (O-01 to O-05)", "OBJECTIVES & EVALUATION CRITERIA")
    add_slide_footer(slide4, 4)

    smart_objs = [
        ("O-01: Sub-Second POS Concurrency & ACID Integrity",
         "Execute atomic stock deductions from retail cash registers via PostgreSQL row-level locks (SELECT ... FOR UPDATE), achieving p95 latency ≤ 800ms and p99 ≤ 1.5s with zero deadlocks across 10 concurrent registers.",
         "Gate: Locust load test simulating 10 concurrent cashiers competing for the last inventory batch.",
         "Sprint 4 (Weeks 7–8)", COLOR_CYAN),
        ("O-02: Automated FEFO Priority & Food Safety Quarantine",
         "Enforce database-level First-Expired, First-Out allocation ensuring 100% of store replenishment orders pick earliest expiring batches; automatically quarantine stock reaching ≤ 3 days to expiry, reducing spoilage from 22% to < 6% in pilot simulations.",
         "Gate: Automated Pytest batch sorting assertions & Celery quarantine triggers.",
         "Sprint 3 (Weeks 5–6)", COLOR_EMERALD),
        ("O-03: AI-Driven Demand Forecasting & Dynamic Replenishment",
         "Deploy a CatBoost Machine Learning Time-Series Forecasting engine achieving MAPE ≤ 15% on high-velocity FMCG items; dynamically compute Reorder Points (ROP) using Greasley's Safety Stock with native calendar festival embeddings (LightGBM deferred to roadmap).",
         "Gate: 12-month walk-forward backtesting against historical FMCG sales series.",
         "Sprint 5 (Weeks 9–10)", COLOR_PURPLE),
        ("O-04: Frugal Hardware Architecture & Sub-350ms Scanning",
         "Engineer a mobile Progressive Web Application (PWA) running on consumer Android smartphones paired with Bluetooth HID trigger grips (< 4,000 BDT), achieving barcode decode-to-render latency ≤ 350ms and cutting terminal capex by 90%.",
         "Gate: Physical hardware testing on Android 13 with EAN-13 and Code-128 labels.",
         "Sprint 2 (Weeks 3–4)", COLOR_AMBER),
        ("O-05: Offline Network Resilience & Idempotent Replay",
         "Implement Service Worker background sync and encrypted IndexedDB client storage to buffer ≥ 200 sales transactions during warehouse broadband outages, replaying idempotently via Redis X-Idempotency-Key upon connection restoration.",
         "Gate: Network blackout drill with Wi-Fi severance during peak scanning.",
         "Sprint 4 (Weeks 7–8)", COLOR_ROSE)
    ]

    col_w = 5.7
    coords = [
        (0.8, 1.6, col_w, 2.4),
        (6.8, 1.6, col_w, 2.4),
        (0.8, 4.2, 3.7, 2.5),
        (4.8, 4.2, 3.7, 2.5),
        (8.8, 4.2, 3.7, 2.5)
    ]
    for idx, (title, desc, gate, sprint, col) in enumerate(smart_objs):
        x, y, w, h = coords[idx]
        cd = add_card(slide4, x, y, w, h, bg_color=COLOR_CARD_DARK, border_color=col)
        tf = cd.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.space_after = Pt(2)
        
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(13)
        p2.font.color.rgb = COLOR_TEXT_WHITE
        p2.space_after = Pt(3)
        
        p3 = tf.add_paragraph()
        p3.text = f"Verification: {gate}  [{sprint}]"
        p3.font.name = FONT_BODY
        p3.font.size = Pt(12)
        p3.font.italic = True
        p3.font.color.rgb = COLOR_CYAN_LIGHT

    slide4.notes_slide.notes_text_frame.text = (
        "Slide 4 Script: Our five SMART objectives are engineered to be verifiable: "
        "O-01 targets sub-2.0s POS concurrency with non-blocking row locks (SKIP LOCKED) and zero overselling, verified by Locust load tests in Sprint 4. "
        "O-02 enforces automated FEFO batch rotation and a 3-day food safety quarantine lock in Sprint 3. "
        "O-03 introduces our AI demand forecasting engine using CatBoost with native festival calendar embeddings in Sprint 5. "
        "O-04 proves our frugal smartphone scanning model with sub-350ms decode in Sprint 2. "
        "And O-05 delivers offline resilience by buffering up to 200 sales in client IndexedDB during broadband dropouts."
    )

    # =========================================================================
    # SLIDE 5: 4-Quadrant Scope Boundaries (Defense-Proof)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide5)
    add_slide_header(slide5, "Scope Boundaries & Operational Constraints (4-Quadrant Matrix)", "SCOPE MANAGEMENT & SAFEGUARDS")
    add_slide_footer(slide5, 5)

    quadrants = [
        ("Quadrant 1: In-Scope Functional Capabilities",
         "• Handheld barcode receiving & digital GRN generation\n• Directed spatial putaway (ABC turnover velocity)\n• Real-time FEFO batch ledger & automated quarantine\n• Sub-2.0s atomic POS inventory deduction (SELECT ... FOR UPDATE SKIP LOCKED)\n• CatBoost Demand Forecasting & Greasley dynamic safety stock\n• Blind cycle counting with supervisor discrepancy signoff\n• Rule-based shrinkage anomaly threshold alerts (>3% variance)",
         COLOR_CYAN),
        ("Quadrant 2: Pilot Operational Boundaries",
         "• Central Warehouse: 1 Central Distribution Center testbed\n• Retail Outlets: Up to 3 Retail Branch Store environments\n• Catalog Scale: 500 representative FMCG & grocery SKUs\n• Concurrency Load: 10 concurrent POS registers + 10 floor scanners\n• Pilot Duration: 4 weeks of simulated operational runs\n• Geographic Scope: Metropolitan Dhaka retail environment",
         COLOR_EMERALD),
        ("Quadrant 3: Technical & Architectural Scope",
         "• Frontend: Next.js 14 PWA (TypeScript, Tailwind CSS)\n• Backend API: FastAPI asynchronous ASGI (Python 3.11+)\n• Relational Core: PostgreSQL 16 (3NF, ACID, Non-Blocking Row Locks)\n• In-Memory Tier: Redis 7 (Client-generated Idempotency Keys, Session Tokens)\n• ML Worker: Celery + Redis with CatBoost & Daily 02:00 BST Quarantine Sweep\n• Deployment: Multi-container Docker Compose staging",
         COLOR_AMBER),
        ("Quadrant 4: Explicit Out-of-Scope (Deliberately Excluded)",
         "• NO Full Corporate Accounting: No general ledger or payroll (exports CSV/JSON audit trails to external ERPs)\n• NO Warehouse Robotics: No physical automated cranes (AGVs) or motor conveyor belts\n• NO Consumer Delivery: No B2C grocery shopping or courier app\n• NO Merchant Payment Gateways: POS billing handles credit card/bKash settlement externally",
         COLOR_ROSE)
    ]

    qw = 5.7
    qh = 2.45
    q_coords = [
        (0.8, 1.6, qw, qh),
        (6.8, 1.6, qw, qh),
        (0.8, 4.3, qw, qh),
        (6.8, 4.3, qw, qh)
    ]
    for idx, (q_title, q_body, q_col) in enumerate(quadrants):
        x, y, w, h = q_coords[idx]
        qc = add_card(slide5, x, y, w, h, bg_color=COLOR_CARD_DARK, border_color=q_col)
        tf = qc.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = q_title
        p.font.name = FONT_HEADING
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = q_col
        p.space_after = Pt(3)
        
        for line in q_body.split("\n"):
            pl = tf.add_paragraph()
            pl.text = line
            pl.font.name = FONT_BODY
            pl.font.size = Pt(13)
            pl.font.color.rgb = COLOR_TEXT_WHITE
            pl.space_after = Pt(1)

    slide5.notes_slide.notes_text_frame.text = (
        "Slide 5 Script: A major flaw in student capstone proposals is scope creep—promising to build everything from accounting to robotics. "
        "In RetailSync, we defined a strict 4-Quadrant scope matrix. In Quadrant 1 and 3, we define our core WMS features and technical stack. "
        "In Quadrant 2, we bound our pilot to 1 central warehouse, 3 branch stores, 500 SKUs, and 10 concurrent POS registers. "
        "And crucially, in Quadrant 4, we explicitly exclude full accounting ERP modules, physical AGV robotics, and merchant banking gateways. "
        "This ensures our 14-week effort is 100% focused on core warehouse operations and database concurrency."
    )

    # =========================================================================
    # SLIDE 6: 4-Tier Cyber-Physical Architecture (Figure 1)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide6)
    add_slide_header(slide6, "System Architecture: 4-Tier Cyber-Physical Design (Figure 1)", "TECHNICAL ARCHITECTURE")
    add_slide_footer(slide6, 6)

    # Left: Tier Description Cards
    left_card = add_card(slide6, 0.8, 1.6, 4.6, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_CYAN)
    tf_lc = left_card.text_frame
    tf_lc.word_wrap = True
    
    p = tf_lc.paragraphs[0]
    p.text = "Decoupled 4-Tier Stack"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(5)

    tiers = [
        ("Tier 1: Client Edge (PWA & Terminals)", "Next.js 14 PWA running on Android smartphones, tablets, and POS PCs. Pure JS barcode scanning (ZXing) with IndexedDB offline queue (< 150ms UI response)."),
        ("Tier 2: Edge Gateway & Security", "Nginx reverse proxy terminating TLS 1.3, managing JWT bearer token authentication and rate limiting (< 10ms gateway overhead)."),
        ("Tier 3: Core Application & AI Workers", "Python 3.11+ FastAPI asynchronous ASGI backend. Paired with Celery workers running CatBoost demand forecasting and scheduled quarantine sweeps (< 180ms p95 SLA)."),
        ("Tier 4: Enterprise Persistence & Cache", "PostgreSQL 16 relational database with strict 3NF schema, row-level locks, and composite B-Trees. Redis 7 for distributed locks and idempotency caching (< 50ms commit).")
    ]
    for t_name, t_desc in tiers:
        pt = tf_lc.add_paragraph()
        pt.text = t_name
        pt.font.name = FONT_HEADING
        pt.font.size = Pt(15)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_CYAN_LIGHT
        
        pd = tf_lc.add_paragraph()
        pd.text = t_desc
        pd.font.name = FONT_BODY
        pd.font.size = Pt(13)
        pd.font.color.rgb = COLOR_TEXT_WHITE
        pd.space_after = Pt(3)

    # Right: Embedded Figure 1
    if os.path.exists(fig1_path):
        slide6.shapes.add_picture(fig1_path, Inches(5.6), Inches(1.6), width=Inches(6.9))

    slide6.notes_slide.notes_text_frame.text = (
        "Slide 6 Script: Here is our Figure 1: 4-Tier Cyber-Physical System Architecture. "
        "At Tier 1, our Next.js PWA runs on warehouse smartphones and POS registers. It uses Service Workers and IndexedDB for offline buffering. "
        "At Tier 2, an Nginx reverse proxy handles TLS 1.3 termination, JWT authentication, and edge rate-limiting. "
        "At Tier 3, our asynchronous FastAPI backend processes business logic, while background Celery workers execute CatBoost forecasting. "
        "At Tier 4, PostgreSQL 16 guarantees ACID double-entry inventory transactions with non-blocking row locks (SKIP LOCKED), and Redis 7 caches client-generated idempotency keys."
    )

    # =========================================================================
    # SLIDE 7: End-to-End Operational Lifecycle & Flow (Figure 2)
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide7)
    add_slide_header(slide7, "Operational Flow: Inbound Receiving to POS Checkout (Figure 2)", "FLOOR LIFECYCLE & PROCESS FLOW")
    add_slide_footer(slide7, 7)

    # Left: 7 Operational Stages
    left_card = add_card(slide7, 0.8, 1.6, 4.6, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_EMERALD)
    tf_lc = left_card.text_frame
    tf_lc.word_wrap = True
    
    p = tf_lc.paragraphs[0]
    p.text = "7-Stage Floor Goods Journey"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(5)

    flow_steps = [
        ("1. Supplier Dock Arrival", "Cartons scanned against digital PO; expiration date and damaged units captured."),
        ("2. Inbound GRN Generation", "Digital Goods Receipt Note generated instantly; variance auto-credited."),
        ("3. Directed Spatial Putaway", "Optimal bin (Zone-Aisle-Rack-Shelf) suggested by SKU velocity & temp."),
        ("4. Real-time FEFO Ledger", "Batch added to FEFO queue; batches ≤ 3 days to expiry auto-quarantined."),
        ("5. Multi-Store Wave Picking", "Consolidated store requisitions picked via shortest-path routing."),
        ("6. Sub-2s POS Checkout", "Pessimistic row lock decrements earliest batch atomically in < 800ms."),
        ("7. Blind Cycle Count Audit", "Quantities hidden on staff sheets; discrepancy reconciliation with signoff.")
    ]
    for s_name, s_desc in flow_steps:
        pt = tf_lc.add_paragraph()
        pt.text = s_name + ": " + s_desc
        pt.font.name = FONT_BODY
        pt.font.size = Pt(13.5)
        pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(3)

    # Right: Embedded Figure 2
    if os.path.exists(fig2_path):
        slide7.shapes.add_picture(fig2_path, Inches(5.6), Inches(1.6), width=Inches(6.9))

    slide7.notes_slide.notes_text_frame.text = (
        "Slide 7 Script: Figure 2 maps the physical journey of grocery items across 7 integrated stages. "
        "When delivery trucks arrive, cartons are barcode-scanned against open POs, logging expiration dates and generating digital GRNs. "
        "The system calculates directed putaway bin locations based on temperature and SKU turnover velocity. "
        "Batches enter an active FEFO priority queue. When checkout registers ring up sales, row-level locks deduct stock from the earliest batch in under 800ms. "
        "Finally, continuous blind cycle counts catch shrinkage before quarterly audits."
    )

    # =========================================================================
    # SLIDE 8: AI Demand Forecasting & Replenishment DSS (Figure 3)
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide8)
    add_slide_header(slide8, "AI Demand Forecasting & Greasley Dynamic Safety Stock (Figure 3)", "DECISION SUPPORT SYSTEM (M-07)")
    add_slide_footer(slide8, 8)

    # Left: ML Engine Details
    left_card = add_card(slide8, 0.8, 1.6, 4.8, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_PURPLE)
    tf_lc = left_card.text_frame
    tf_lc.word_wrap = True
    
    p = tf_lc.paragraphs[0]
    p.text = "Why Static Reorder Points Fail"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_PURPLE
    p.space_after = Pt(4)

    ml_points = [
        "The Flaw of Classic EOQ: Traditional inventory models assume constant demand (d). In Bangladeshi retail, demand surges 300% during Ramadan, Eid, and payday weekends.",
        "CatBoost Multi-Horizon Predictor: Trains gradient boosted decision trees over historical POS sales. Features include 7-day lags, rolling statistics, and native categorical festival calendar embeddings.",
        "Festival Calendar Awareness: Native handling of categorical flags for Ramadan (Iftar rushes), Eid-ul-Fitr, Eid-ul-Adha, and corporate salary disbursement cycles (1st to 7th of each month) without target leakage.",
        "Greasley Dynamic Formula:\nSS = Z × √((L̄ × σ_d²) + (d_hat² × σ_L²))\nROP = (d_hat × L̄) + SS\nBy replacing static demand with AI-predicted demand (d_hat), replenishment orders trigger 10 days in advance of holiday surges."
    ]
    for mp in ml_points:
        pt = tf_lc.add_paragraph()
        pt.text = "• " + mp
        pt.font.name = FONT_BODY
        pt.font.size = Pt(13.5)
        pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(4)

    # Right: Embedded Figure 3
    if os.path.exists(fig3_path):
        slide8.shapes.add_picture(fig3_path, Inches(5.8), Inches(1.6), width=Inches(6.7))

    slide8.notes_slide.notes_text_frame.text = (
        "Slide 8 Script: Figure 3 illustrates our machine learning replenishment pipeline. "
        "Standard inventory formulas assume demand is static, which is why supermarkets run out of soybean oil during Ramadan. "
        "RetailSync deploys a CatBoost regressor trained on POS sales. We feed it lag features and native categorical embeddings for Ramadan, "
        "Eid, and payday cycles. The model outputs predicted daily demand (d_hat). We then plug d_hat directly into Greasley's statistical "
        "safety stock equation. This dynamically raises reorder points 10 days before a festival rush, preventing stockouts without over-ordering after the holiday."
    )

    # =========================================================================
    # SLIDE 9: POS Concurrency & Frugal Hardware Strategy
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide9)
    add_slide_header(slide9, "High-Velocity Concurrency & The Frugal Hardware Model", "CONCURRENCY CONTROL & HARDWARE")
    add_slide_footer(slide9, 9)

    # Left: Concurrency Control
    c_card = add_card(slide9, 0.8, 1.6, 5.7, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_CYAN)
    tf_c = c_card.text_frame
    tf_c.word_wrap = True
    
    p = tf_c.paragraphs[0]
    p.text = "Pessimistic Row-Level Locking in PostgreSQL"
    p.font.name = FONT_HEADING
    p.font.size = Pt(19.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(4)

    concurrency_text = [
        "The Rush-Hour Race Condition: At 8:45 PM on Eid Eve, 3 cashiers simultaneously scan the last carton of Aarong Milk. Without locking, all 3 transactions read stock=1 and decrement, causing negative inventory and overselling.",
        "The RetailSync Solution: Our POS sync route queries PostgreSQL 16 with exclusive row-level locking:",
        "SELECT batch_id, current_quantity\nFROM product_batches\nWHERE product_id = :p_id AND current_quantity > 0\nORDER BY expiry_date ASC LIMIT 1\nFOR UPDATE;",
        "Deterministic Serialization: Lane 1 acquires the lock, decrements stock 1 -> 0, and commits. Lane 2 and Lane 3 safely evaluate current_quantity = 0 and return clean HTTP 409 Conflict with suggested alternative batches. Zero oversell."
    ]
    for ct in concurrency_text:
        pt = tf_c.add_paragraph()
        if "SELECT" in ct:
            pt.text = ct
            pt.font.name = "Consolas"
            pt.font.size = Pt(13)
            pt.font.color.rgb = COLOR_AMBER
        else:
            pt.text = "• " + ct
            pt.font.name = FONT_BODY
            pt.font.size = Pt(13.5)
            pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(4)

    # Right: Frugal Hardware Strategy
    h_card = add_card(slide9, 6.8, 1.6, 5.7, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_EMERALD)
    tf_h = h_card.text_frame
    tf_h.word_wrap = True
    
    p = tf_h.paragraphs[0]
    p.text = "Frugal Hardware Strategy (90% Capex Cut)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(19.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(4)

    hw_text = [
        "The Enterprise ERP Trap: Traditional WMS vendors mandate industrial ruggedized scanners (e.g., Zebra TC52) costing upwards of 60,000 BDT per unit. For a chain with 20 branches, this requires over 1.2M BDT in terminal hardware alone.",
        "The RetailSync Alternative: We pair commodity Android smartphones (12,000 BDT) with ergonomic Bluetooth HID barcode trigger grips (3,800 BDT). Total station cost: ~15,800 BDT.",
        "Performance Validation: WebAssembly-accelerated ZXing decodes standard EAN-13 and Code-128 barcodes in ≤ 350ms, matching industrial hardware speeds at a fraction of the price.",
        "Audio/Haptic Feedback: Positive beep confirmation on scan ensures warehouse operators can pick rapidly without staring constantly at the screen."
    ]
    for ht in hw_text:
        pt = tf_h.add_paragraph()
        pt.text = "• " + ht
        pt.font.name = FONT_BODY
        pt.font.size = Pt(13.5)
        pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(4)

    slide9.notes_slide.notes_text_frame.text = (
        "Slide 9 Script: On this slide, we address two practical implementation realities: database concurrency and hardware affordability. "
        "On the left, we show our PostgreSQL row-level locking query using SELECT ... FOR UPDATE. When multiple cashiers scan the last milk carton, "
        "Lane 1 acquires the lock, commits, and Lanes 2 and 3 receive an immediate HTTP 409 Conflict. There are zero deadlocks and zero overselling. "
        "On the right, we highlight our frugal hardware model: instead of buying 60,000 BDT Zebra scanners, RetailSync runs on 12,000 BDT Android phones "
        "paired with 3,800 BDT Bluetooth barcode grips, cutting frontline hardware capex by nearly 90% while achieving sub-350ms scan speeds."
    )

    # =========================================================================
    # SLIDE 10: 14-Week Agile Scrum Roadmap & Scenarios (Figure 4)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide10)
    add_slide_header(slide10, "14-Week Agile Scrum Roadmap & Scenario Acceptance Gates (Figure 4)", "PROJECT EXECUTION & SCHEDULE")
    add_slide_footer(slide10, 10)

    # Left: Sprints & Scenarios
    left_card = add_card(slide10, 0.8, 1.6, 4.8, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_AMBER)
    tf_lc = left_card.text_frame
    tf_lc.word_wrap = True
    
    p = tf_lc.paragraphs[0]
    p.text = "14-Week Scrum Execution (137 pts)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_AMBER
    p.space_after = Pt(4)

    scrum_text = [
        "Sprint 1 (W1-2, 21 pts): 3NF schema, Docker Compose, JWT RBAC.",
        "Sprint 2 (W3-4, 24 pts): Inbound scanning, digital GRN. [Scenario A: Dock Expiry Rejection Gate]",
        "Sprint 3 (W5-6, 26 pts): Directed spatial putaway & FEFO expiry engine.",
        "Sprint 4 (W7-8, 22 pts): Sub-2s POS concurrency & offline sync. [Scenario B: POS Concurrency Rush & Scenario C: Network Blackout Sync]",
        "Sprint 5 (W9-10, 23 pts): AI Demand Forecasting & wave picking. [Scenario D: Pre-Ramadan Demand Surge]",
        "Sprint 6 (W11-12, 21 pts): Blind cycle counts & Locust load hardening.",
        "Hardening (W13-14): DIU staging pilot & capstone defense."
    ]
    for st in scrum_text:
        pt = tf_lc.add_paragraph()
        pt.text = "• " + st
        pt.font.name = FONT_BODY
        pt.font.size = Pt(13.5)
        pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(3)

    # Right: Embedded Figure 4
    if os.path.exists(fig4_path):
        slide10.shapes.add_picture(fig4_path, Inches(5.8), Inches(1.6), width=Inches(6.7))

    slide10.notes_slide.notes_text_frame.text = (
        "Slide 10 Script: Figure 4 presents our 14-week Agile Scrum Gantt roadmap across six 2-week sprints and a final hardening phase (137 total story points). "
        "Crucially, sprint completion is verified against four concrete, stress-injected supermarket scenarios: "
        "Scenario A in Sprint 2 tests dock rejection of short-dated milk. "
        "Scenario B and C in Sprint 4 test rush-hour POS concurrency and offline sales caching during network blackouts. "
        "And Scenario D in Sprint 5 tests advance replenishment ordering before Ramadan. Every sprint deliverable is testable."
    )

    # =========================================================================
    # SLIDE 11: Hardware Budget & Financial ROI Impact
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide11)
    add_slide_header(slide11, "Resource Allocation, Budget & Projected Financial ROI", "BUDGET & BUSINESS FEASIBILITY")
    add_slide_footer(slide11, 11)

    # Left: Student Prototype Hardware Budget
    b_card = add_card(slide11, 0.8, 1.6, 5.7, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_CYAN)
    tf_b = b_card.text_frame
    tf_b.word_wrap = True
    
    p = tf_b.paragraphs[0]
    p.text = "Capstone Prototype Hardware Budget"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(4)

    b_items = [
        ("Android Test Smartphone (Android 13, 4GB RAM)", "12,500 BDT"),
        ("Bluetooth Barcode Trigger Grips (Qty: 2)", "7,600 BDT"),
        ("4-inch Thermal Label & Receipt Printer", "6,500 BDT"),
        ("EAN-128 Adhesive Barcode Labels (3,000 labels)", "1,950 BDT"),
        ("Cloud Staging VPS Hosting (6 Months)", "5,500 BDT"),
        ("Total Prototype Investment", "34,050 BDT")
    ]
    for item, cost in b_items:
        pt = tf_b.add_paragraph()
        if "Total" in item:
            pt.text = f"{item}: {cost}"
            pt.font.name = FONT_HEADING
            pt.font.size = Pt(15.5)
            pt.font.bold = True
            pt.font.color.rgb = COLOR_EMERALD
        else:
            pt.text = f"• {item} — {cost}"
            pt.font.name = FONT_BODY
            pt.font.size = Pt(14)
            pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(4)

    # Right: Real Supermarket ROI
    r_card = add_card(slide11, 6.8, 1.6, 5.7, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_EMERALD)
    tf_r = r_card.text_frame
    tf_r.word_wrap = True
    
    p = tf_r.paragraphs[0]
    p.text = "Commercial ROI (Per 3-Store Cluster)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(4)

    roi_items = [
        ("Perishable Spoilage Savings", "Reduced from 22% down to < 6%, saving ~2.18M BDT annually in prevented waste."),
        ("Stockout Revenue Recapture", "Reduced out-of-stock from 11.2% down to < 2.5%, recapturing ~2.43M BDT in retail sales."),
        ("Net Annual Financial Gain", "~4.61M BDT net bottom-line gain across a 3-branch supermarket pilot."),
        ("Projected Capital Payback Period", "2.8 Months based on CapEx of 485,000 BDT (development, smartphones, servers) and OpEx of 14,000 BDT/month.")
    ]
    for r_title, r_desc in roi_items:
        pt = tf_r.add_paragraph()
        pt.text = r_title
        pt.font.name = FONT_HEADING
        pt.font.size = Pt(15)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_CYAN_LIGHT
        
        pd = tf_r.add_paragraph()
        pd.text = r_desc
        pd.font.name = FONT_BODY
        pd.font.size = Pt(13.5)
        pd.font.color.rgb = COLOR_TEXT_WHITE
        pd.space_after = Pt(3)

    slide11.notes_slide.notes_text_frame.text = (
        "Slide 11 Script: On this slide, we present two budgets: our student hardware prototype cost and the commercial ROI for a real retail chain. "
        "Our capstone prototype budget is realistic and self-funded at 34,050 BDT, covering an Android test smartphone, two Bluetooth trigger grips, "
        "a thermal label printer, labels, and 6 months of cloud staging. "
        "For a real 3-store supermarket cluster, RetailSync delivers 4.61M BDT in annual net benefit from prevented spoilage and recaptured stockouts, "
        "achieving a full capital payback period in just 2.8 months."
    )

    # =========================================================================
    # SLIDE 12: Summary, Academic References & Defense Q&A
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide12)
    add_slide_header(slide12, "Summary, References & Defense Q&A Session", "CONCLUSION & DEFENSE")
    add_slide_footer(slide12, 12)

    # Left: Core Takeaways & References
    sum_card = add_card(slide12, 0.8, 1.6, 5.7, 5.1, bg_color=COLOR_CARD_DARK, border_color=COLOR_CYAN)
    tf_s = sum_card.text_frame
    tf_s.word_wrap = True
    
    p = tf_s.paragraphs[0]
    p.text = "Key Engineering Contributions"
    p.font.name = FONT_HEADING
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(4)

    sum_points = [
        "1. Centralized Relational Integrity: Bridges frontline POS and warehouse bins with strict 3NF schema and sub-2.0s row locking.",
        "2. Automated FEFO Food Safety: Mechanically prevents expired product sales under Bangladesh Food Safety Act 2013.",
        "3. AI Replenishment Engine: CatBoost demand predictor with native festival embeddings coupled to Greasley's dynamic safety stock (LightGBM deferred to roadmap).",
        "4. Frugal Hardware Model: Standard Android smartphones cut deployment costs by 90% with sub-350ms scan speed."
    ]
    for sp in sum_points:
        pt = tf_s.add_paragraph()
        pt.text = sp
        pt.font.name = FONT_BODY
        pt.font.size = Pt(13.5)
        pt.font.color.rgb = COLOR_TEXT_WHITE
        pt.space_after = Pt(3)

    pr = tf_s.add_paragraph()
    pr.text = "Key Academic References:"
    pr.font.name = FONT_HEADING
    pr.font.size = Pt(15)
    pr.font.bold = True
    pr.font.color.rgb = COLOR_AMBER
    pr.space_after = Pt(2)

    refs_short = [
        "• BFSA (2013). Bangladesh Food Safety Act 2013, Ministry of Food.",
        "• BSOA (2024). Annual Report on Supermarket Operations & Wastage.",
        "• FAO (2022). Post-Harvest Losses in South Asian Retail Supply Chains.",
        "• Greasley, A. (2013). Operations Management, 3rd ed., Wiley.",
        "• Prokhorenkova, L. et al. (2018). CatBoost: Unbiased Boosting with Categorical Features.",
        "• Ke, G. et al. (2017). LightGBM: A Highly Efficient GBDT, NeurIPS (Deferred).",
        "• Kleppmann, M. (2017). Designing Data-Intensive Applications, O'Reilly."
    ]
    for r in refs_short:
        prf = tf_s.add_paragraph()
        prf.text = r
        prf.font.name = FONT_BODY
        prf.font.size = Pt(12)
        prf.font.color.rgb = COLOR_TEXT_MUTED

    # Right: Q&A and Demo Callout Box
    qa_card = add_card(slide12, 6.8, 1.6, 5.7, 5.1, bg_color=RGBColor(24, 34, 53), border_color=COLOR_EMERALD)
    tf_qa = qa_card.text_frame
    tf_qa.word_wrap = True
    
    p = tf_qa.paragraphs[0]
    p.text = "DEFENSE Q&A SESSION"
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(8)

    p_msg = tf_qa.add_paragraph()
    p_msg.text = (
        "Thank you, respected committee members.\n\n"
        "We now warmly invite your questions, feedback, and critique on the RetailSync project proposal.\n\n"
        "Interactive Demonstrations Available Live:\n"
        "• Live POS Concurrency Race Simulator (PostgreSQL 16 Lock)\n"
        "• Greasley Statistical Safety Stock & Dynamic EOQ Engine\n"
        "• 4-Tier Interactive Architecture Stack Inspector"
    )
    p_msg.font.name = FONT_BODY
    p_msg.font.size = Pt(15.5)
    p_msg.font.color.rgb = COLOR_TEXT_WHITE
    p_msg.alignment = PP_ALIGN.CENTER

    p_colophon = tf_qa.add_paragraph()
    p_colophon.text = "\nProject Team: Raisul Islam Likhon (Lead: 251-35-508)  •  Shottobroto Dey (251-35-017)  •  Golam Husnain Papon (251-35-529)\nBatch: 44th Batch  •  Section: SWE-44D  |  Department of Software Engineering, Daffodil International University"
    p_colophon.font.name = FONT_HEADING
    p_colophon.font.size = Pt(15)
    p_colophon.font.bold = True
    p_colophon.font.color.rgb = COLOR_CYAN
    p_colophon.alignment = PP_ALIGN.CENTER

    slide12.notes_slide.notes_text_frame.text = (
        "Closing Script: In conclusion, RetailSync bridges the gap between frontline checkouts and central warehouses with rigorous database concurrency, "
        "automated FEFO food safety compliance, and AI demand forecasting, all while keeping hardware costs under 16,000 BDT per station. "
        "We have established a comprehensive 14-week Agile plan with testable scenario gates. "
        "I now welcome your questions, and I am ready to demonstrate our live POS concurrency and safety stock simulator in the browser. Thank you!"
    )

    output_dir = os.path.join(project_root, "proposal")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "RetailSync_Capstone_Proposal_Defense_Deck.pptx")
    prs.save(output_path)
    print(f"Successfully generated 12-slide PowerPoint presentation: {output_path}")

if __name__ == "__main__":
    create_slide_deck()
