#!/usr/bin/env python3
"""
RetailSync: Centralized Super Shop Warehouse Management System
Automated 16:9 Compact Academic Presentation Slide Deck Generator (.pptx)
10-Slide High-Impact Core Presentation for DIU SE-231 Capstone Proposal Defense.

Department of Software Engineering, Daffodil International University (DIU).
Course: SE-231 (Software System Analysis & Design / Capstone Project 2).
Batch: 44th Batch · Section: SWE-44D
Team Members:
  1. Raisul Islam Likhon (Lead: 251-35-508)
  2. Shottobroto Dey (251-35-017)
  3. Golam Husnain Papon (251-35-529)
"""

import os
import sys
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# --- Color Palette (Calm Academic & High Legibility) ---
COLOR_BG_CANVAS = RGBColor(248, 250, 252)     # #F8FAFC - Clean off-white canvas
COLOR_BG_CARD = RGBColor(255, 255, 255)       # #FFFFFF - Pure white card surface
COLOR_BG_MUTED = RGBColor(241, 245, 249)      # #F1F5F9 - Subtle light grey surface
COLOR_BORDER_SUBTLE = RGBColor(226, 232, 240) # #E2E8F0 - Clean hairline border

COLOR_PRIMARY = RGBColor(2, 132, 199)         # #0284C7 - Executive Sky Blue
COLOR_PRIMARY_DARK = RGBColor(11, 31, 58)     # #0B1F3A - Deep Navy Accent
COLOR_PRIMARY_LIGHT = RGBColor(224, 242, 254) # #E0F2FE - Soft Blue Tint

COLOR_EMERALD = RGBColor(16, 185, 129)        # #10B981 - Success Green
COLOR_EMERALD_BG = RGBColor(236, 253, 245)    # #ECFDF5 - Light Green Tint
COLOR_AMBER = RGBColor(245, 158, 11)          # #F59E0B - Warning Amber
COLOR_AMBER_BG = RGBColor(254, 243, 199)      # #FEF3C7 - Light Amber Tint
COLOR_ROSE = RGBColor(239, 68, 68)            # #EF4444 - Danger / Critical Rose
COLOR_ROSE_BG = RGBColor(254, 226, 226)       # #FEE2E2 - Light Rose Tint
COLOR_INDIGO = RGBColor(99, 102, 241)         # #6366F1 - Technical Purple

COLOR_TEXT_MAIN = RGBColor(15, 23, 42)        # #0F172A - Charcoal 900
COLOR_TEXT_MUTED = RGBColor(71, 85, 105)      # #475569 - Slate 600
COLOR_TEXT_LIGHT = RGBColor(148, 163, 184)    # #94A3B8 - Slate 400
COLOR_TEXT_WHITE = RGBColor(255, 255, 255)

FONT_HEADING = "Calibri"
FONT_BODY = "Calibri"
FONT_MONO = "Consolas"


def set_cell_margins(cell, top=0.07, bottom=0.07, left=0.1, right=0.1):
    cell.margin_top = Inches(top)
    cell.margin_bottom = Inches(bottom)
    cell.margin_left = Inches(left)
    cell.margin_right = Inches(right)


def add_slide_header(slide, title, kicker=None, slide_num=None):
    """Adds a standard structured header matching DIU presentation guidelines."""
    if kicker:
        tx_k = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.5), Inches(0.28))
        p_k = tx_k.text_frame.paragraphs[0]
        p_k.text = kicker.upper()
        p_k.font.name = FONT_HEADING
        p_k.font.size = Pt(11)
        p_k.font.bold = True
        p_k.font.color.rgb = COLOR_PRIMARY

    title_top = Inches(0.62) if kicker else Inches(0.45)
    tx_t = slide.shapes.add_textbox(Inches(0.8), title_top, Inches(11.5), Inches(0.65))
    p_t = tx_t.text_frame.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(23)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_TEXT_MAIN

    # Hairline divider line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER_SUBTLE
    line.line.color.rgb = COLOR_BORDER_SUBTLE

    # Slide Number & Footer Metadata
    if slide_num:
        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.02), Inches(10.0), Inches(0.35))
        p_f = tx_f.text_frame.paragraphs[0]
        p_f.text = "RetailSync · SE-231 Capstone Project Proposal Defense · Department of Software Engineering, DIU"
        p_f.font.name = FONT_BODY
        p_f.font.size = Pt(10)
        p_f.font.color.rgb = COLOR_TEXT_LIGHT

        tx_n = slide.shapes.add_textbox(Inches(11.8), Inches(7.02), Inches(0.7), Inches(0.35))
        p_n = tx_n.text_frame.paragraphs[0]
        p_n.text = f"{slide_num}/10"
        p_n.font.name = FONT_MONO
        p_n.font.size = Pt(11)
        p_n.font.bold = True
        p_n.font.color.rgb = COLOR_PRIMARY
        p_n.alignment = PP_ALIGN.RIGHT


def add_card(slide, left, top, width, height, bg_color=COLOR_BG_CARD, border_color=COLOR_BORDER_SUBTLE):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    return card


def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(project_root, "assets")

    fig1_path = os.path.join(assets_dir, "figure1_system_architecture.png")
    fig2_path = os.path.join(assets_dir, "figure2_operational_flow.png")
    fig3_path = os.path.join(assets_dir, "figure3_ai_forecasting_pipeline.png")
    fig4_path = os.path.join(assets_dir, "figure4_gantt_roadmap.png")
    logo_path = os.path.join(assets_dir, "retailsync_logo.png")

    # ==========================================================================
    # SLIDE 1: Cover / Title Slide
    # ==========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_card(slide1, 0.8, 0.8, 11.733, 5.9, COLOR_BG_CARD, COLOR_BORDER_SUBTLE)

    # Top Tag Pill
    pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(1.25), Inches(4.8), Inches(0.4))
    pill.fill.solid()
    pill.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    pill.line.color.rgb = COLOR_PRIMARY
    pill.line.width = Pt(1)
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.text = "SE 231  ·  PROJECT PROPOSAL DEFENSE"
    p_pill.font.name = FONT_HEADING
    p_pill.font.size = Pt(11.5)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_PRIMARY
    p_pill.alignment = PP_ALIGN.CENTER

    if os.path.exists(logo_path):
        slide1.shapes.add_picture(logo_path, Inches(10.8), Inches(1.15), Inches(1.25), Inches(1.25))

    # Title & Subtitle
    tx_title = slide1.shapes.add_textbox(Inches(1.3), Inches(1.85), Inches(10.2), Inches(1.5))
    tf_t = tx_title.text_frame
    tf_t.word_wrap = True
    p_main = tf_t.paragraphs[0]
    p_main.text = "RetailSync: Centralized Super Shop Warehouse Management System"
    p_main.font.name = FONT_HEADING
    p_main.font.size = Pt(28)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_TEXT_MAIN

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Sub-2.0s Transactional FEFO Allocation, Multi-Till Concurrency Control & Stochastic Replenishment for Bangladesh Retail Chains"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED
    p_sub.space_before = Pt(8)

    div1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(3.55), Inches(10.7), Inches(0.015))
    div1.fill.solid()
    div1.fill.fore_color.rgb = COLOR_BORDER_SUBTLE
    div1.line.color.rgb = COLOR_BORDER_SUBTLE

    # Team & Presentation Info Box
    tx_meta = slide1.shapes.add_textbox(Inches(1.3), Inches(3.75), Inches(10.7), Inches(2.6))
    tf_m = tx_meta.text_frame
    tf_m.word_wrap = True

    p_lbl = tf_m.paragraphs[0]
    p_lbl.text = "PROJECT TEAM (SECTION SWE-44D):"
    p_lbl.font.name = FONT_HEADING
    p_lbl.font.size = Pt(11)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = COLOR_PRIMARY

    p_pres = tf_m.add_paragraph()
    p_pres.text = "1. Raisul Islam Likhon (Lead: 251-35-508)   ·   2. Shottobroto Dey (251-35-017)   ·   3. Golam Husnain Papon (251-35-529)"
    p_pres.font.name = FONT_HEADING
    p_pres.font.size = Pt(16)
    p_pres.font.bold = True
    p_pres.font.color.rgb = COLOR_TEXT_MAIN
    p_pres.space_before = Pt(4)

    p_dept = tf_m.add_paragraph()
    p_dept.text = "System Analysis & Design Capstone Project 2  ·  Supervised by Department Faculty"
    p_dept.font.name = FONT_BODY
    p_dept.font.size = Pt(13)
    p_dept.font.color.rgb = COLOR_TEXT_MUTED
    p_dept.space_before = Pt(4)

    p_inst = tf_m.add_paragraph()
    p_inst.text = "Department of Software Engineering  ·  Faculty of Science & Information Technology  ·  Daffodil International University"
    p_inst.font.name = FONT_BODY
    p_inst.font.size = Pt(12)
    p_inst.font.bold = True
    p_inst.font.color.rgb = COLOR_TEXT_MUTED
    p_inst.space_before = Pt(4)

    # ==========================================================================
    # SLIDE 2: Problem Statement & Industry Need
    # ==========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide2, "The Problem: 3 Critical Profit Leaks in Retail", "INDUSTRY CHALLENGES & OPERATIONAL BOTTLENECKS", 2)

    problems = [
        {
            "num": "01",
            "title": "Phantom Stockouts & Mismatches",
            "body": "Cashiers scan items missing from shelves while excess stock sits unrecorded in backrooms. Inventory discrepancy between billing registers and physical warehouse bins reaches 8% to 14% daily.",
            "stat": "8–14% Stock Mismatch",
            "color": COLOR_ROSE,
            "bg": COLOR_ROSE_BG
        },
        {
            "num": "02",
            "title": "Perishable Expiry Waste",
            "body": "Without batch-specific expiry tracking, clerks sell newer stock first. Over 18% of fresh dairy, staples, and bakery goods expire unnoticed on shelves, violating Bangladesh Food Safety Act 2013 standards.",
            "stat": "18% Expiry Shrinkage",
            "color": COLOR_AMBER,
            "bg": COLOR_AMBER_BG
        },
        {
            "num": "03",
            "title": "Multi-Till Race Conditions",
            "body": "During peak evening rush hours (5 PM–9 PM), multiple tills scan the last remaining units simultaneously. Disconnected POS tools cause duplicate sales, negative stock, and stockout disputes.",
            "stat": "Sub-2.0s Race Collisions",
            "color": COLOR_INDIGO,
            "bg": COLOR_PRIMARY_LIGHT
        }
    ]

    for i, p in enumerate(problems):
        left = 0.8 + i * 3.98
        add_card(slide2, left, 1.55, 3.75, 3.55)

        tx_n = slide2.shapes.add_textbox(Inches(left + 0.25), Inches(1.75), Inches(1.0), Inches(0.5))
        p_num = tx_n.text_frame.paragraphs[0]
        p_num.text = p["num"]
        p_num.font.name = FONT_MONO
        p_num.font.size = Pt(28)
        p_num.font.bold = True
        p_num.font.color.rgb = p["color"]

        tx = slide2.shapes.add_textbox(Inches(left + 0.25), Inches(2.35), Inches(3.25), Inches(2.3))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = p["title"]
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(15.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_b = tf.add_paragraph()
        p_b.text = p["body"]
        p_b.font.name = FONT_BODY
        p_b.font.size = Pt(11.5)
        p_b.font.color.rgb = COLOR_TEXT_MUTED
        p_b.space_before = Pt(4)

        # Stat pill
        pill = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.3), Inches(4.6), Inches(3.15), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = p["bg"]
        pill.line.color.rgb = p["color"]
        p_st = pill.text_frame.paragraphs[0]
        p_st.text = p["stat"]
        p_st.font.name = FONT_MONO
        p_st.font.size = Pt(10.5)
        p_st.font.bold = True
        p_st.font.color.rgb = p["color"]
        p_st.alignment = PP_ALIGN.CENTER

    # The Gap Strip
    add_card(slide2, 0.8, 5.3, 11.733, 1.45, COLOR_PRIMARY_LIGHT, COLOR_PRIMARY)
    tx_gap = slide2.shapes.add_textbox(Inches(1.1), Inches(5.42), Inches(11.1), Inches(1.2))
    tf_g = tx_gap.text_frame
    tf_g.word_wrap = True

    p_gh = tf_g.paragraphs[0]
    p_gh.text = "THE CORE MARKET GAP IN BANGLADESH:"
    p_gh.font.name = FONT_HEADING
    p_gh.font.size = Pt(11)
    p_gh.font.bold = True
    p_gh.font.color.rgb = COLOR_PRIMARY

    p_gd = tf_g.add_paragraph()
    p_gd.text = "Global enterprise ERPs (SAP, NetSuite) cost millions in licensing and are too complex for local chains; generic desktop POS apps lack warehouse batch-level expiry traceability. RetailSync bridges this gap with an affordable, high-speed, and production-tested transactional architecture."
    p_gd.font.name = FONT_BODY
    p_gd.font.size = Pt(12)
    p_gd.font.color.rgb = COLOR_TEXT_MAIN
    p_gd.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 3: How the System Works (5-Step Engine)
    # ==========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide3, "The RetailSync Engine: How It Works", "END-TO-END OPERATIONAL LIFECYCLE", 3)

    steps = [
        ("1", "Dock Inbound", "Clerk scans PO; 65% quality gate verifies batch shelf-life before GRN receipt.", COLOR_PRIMARY),
        ("2", "Directed Putaway", "Engine calculates shortest Manhattan distance and assigns optimal thermal bay (A01–D01).", COLOR_INDIGO),
        ("3", "Real-Time Sync", "PostgreSQL 16 3NF schema synchronizes stock across warehouse racks and store tills.", COLOR_EMERALD),
        ("4", "FEFO Checkout", "Cashier scans item; atomic row locks deduct earliest-expiring batch in < 2.0s.", COLOR_AMBER),
        ("5", "DSS Reorder", "Greasley safety stock models lead-time variance and triggers optimal Wilson EOQ replenishment.", COLOR_PRIMARY)
    ]

    step_w = 2.15
    step_gap = 0.24
    for i, (num, title, desc, color) in enumerate(steps):
        left = 0.8 + i * (step_w + step_gap)
        add_card(slide3, left, 1.6, step_w, 3.8)

        circle = slide3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 0.65), Inches(1.85), Inches(0.85), Inches(0.85))
        circle.fill.solid()
        circle.fill.fore_color.rgb = color
        circle.line.color.rgb = color
        p_c = circle.text_frame.paragraphs[0]
        p_c.text = num
        p_c.font.name = FONT_HEADING
        p_c.font.size = Pt(18)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_TEXT_WHITE
        p_c.alignment = PP_ALIGN.CENTER

        tx = slide3.shapes.add_textbox(Inches(left + 0.15), Inches(2.9), Inches(step_w - 0.3), Inches(2.3))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.alignment = PP_ALIGN.CENTER

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.alignment = PP_ALIGN.CENTER
        p_d.space_before = Pt(4)

    # Process Flow diagram link / visual strip
    add_card(slide3, 0.8, 5.65, 11.733, 1.15, COLOR_BG_MUTED, COLOR_BORDER_SUBTLE)
    tx_loop = slide3.shapes.add_textbox(Inches(1.1), Inches(5.75), Inches(11.1), Inches(0.95))
    tf_l = tx_loop.text_frame
    tf_l.word_wrap = True
    p_l = tf_l.paragraphs[0]
    p_l.text = "OPERATIONAL CONTINUITY & COMPLIANCE (FIGURE 2 FLOW):"
    p_l.font.name = FONT_HEADING
    p_l.font.size = Pt(11)
    p_l.font.bold = True
    p_l.font.color.rgb = COLOR_PRIMARY

    p_ld = tf_l.add_paragraph()
    p_ld.text = "Transactions execute atomically without manual guesswork. The system guarantees that older inventory is liquidated first (FEFO), preventing expired items from ever reaching customers."
    p_ld.font.name = FONT_BODY
    p_ld.font.size = Pt(11.5)
    p_ld.font.color.rgb = COLOR_TEXT_MAIN
    p_ld.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 4: Core Workspaces: Inbound & POS Checkout
    # ==========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide4, "Core Modules: Inbound Dock & Frontline POS", "WAREHOUSE OPERATIONS & CHECKOUT INTEGRITY", 4)

    # Left: Inbound & Putaway
    add_card(slide4, 0.8, 1.55, 5.65, 5.25)
    tx_in = slide4.shapes.add_textbox(Inches(1.1), Inches(1.75), Inches(5.05), Inches(4.8))
    tf_i = tx_in.text_frame
    tf_i.word_wrap = True

    p_ih = tf_i.paragraphs[0]
    p_ih.text = "Inbound Dock & Directed Putaway"
    p_ih.font.name = FONT_HEADING
    p_ih.font.size = Pt(17)
    p_ih.font.bold = True
    p_ih.font.color.rgb = COLOR_PRIMARY

    in_pts = [
        "Digital PO Receiving Inspection: Matches delivery against purchase orders with instant Goods Receipt Note (GRN) issuance.",
        "65% Residual Shelf-Life Gate: Automatically computes (Expiry - Recv) / (Expiry - Mfd); batches below 65% are quarantined.",
        "Directed Thermal Putaway: Compatible slotting across Ambient (A01-B01), Cold 4°C (C01), and Frozen -18°C (D01) bays.",
        "Shortest-Path Manhattan Routing: Calculates operator walking travel (|ΔX| + |ΔY|) to minimize floor cycle times."
    ]
    for pt in in_pts:
        p = tf_i.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(6)

    # Right: POS & Concurrency
    add_card(slide4, 6.85, 1.55, 5.68, 5.25)
    tx_pos = slide4.shapes.add_textbox(Inches(7.15), Inches(1.75), Inches(5.08), Inches(4.8))
    tf_p = tx_pos.text_frame
    tf_p.word_wrap = True

    p_ph = tf_p.paragraphs[0]
    p_ph.text = "Frontline POS & Concurrency Locking"
    p_ph.font.name = FONT_HEADING
    p_ph.font.size = Pt(17)
    p_ph.font.bold = True
    p_ph.font.color.rgb = COLOR_EMERALD

    pos_pts = [
        "Sub-2.0s Transactional Checkout: Rapid barcode scanning with Web Audio synthesizer beep and quick cash tender chips.",
        "Automatic FEFO Deduction: Engine selects the earliest-expiring batch automatically; cashiers never inspect expiry labels.",
        "Row-Level Lock (SELECT FOR UPDATE SKIP LOCKED): Atomically locks batch rows, eliminating rush-hour double allocation.",
        "ACID Guarantees & Thermal Receipts: Failed tenders release locks immediately; successful sales emit formatted receipts."
    ]
    for pt in pos_pts:
        p = tf_p.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 5: Digital Twin & Replenishment DSS
    # ==========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide5, "Core Modules: Digital Twin & Replenishment DSS", "SPATIAL HEATMAP & STOCHASTIC FORECASTING", 5)

    # Left: 2D Spatial Digital Twin
    add_card(slide5, 0.8, 1.55, 5.65, 5.25)
    tx_dt = slide5.shapes.add_textbox(Inches(1.1), Inches(1.75), Inches(5.05), Inches(4.8))
    tf_d = tx_dt.text_frame
    tf_d.word_wrap = True

    p_dh = tf_d.paragraphs[0]
    p_dh.text = "2D Spatial Digital Twin Warehouse Map"
    p_dh.font.name = FONT_HEADING
    p_dh.font.size = Pt(17)
    p_dh.font.bold = True
    p_dh.font.color.rgb = COLOR_INDIGO

    dt_pts = [
        "Live 2D Bay Matrix: Visual representation of warehouse aisles (A01–D01) with real-time occupancy percentages.",
        "Thermal Zone Monitoring: Distinct sensors for Ambient (22°C), Chilled (4°C), and Frozen (-18°C) storage bays.",
        "FEFO Expiry Heatmap: Color-coded bin status—Green (Normal), Red (Critical Expiry < 7 Days), Slate (Empty).",
        "Interactive Bin Drawer: Click any rack cell to inspect batch lot number, residual shelf-life, and exact SKU unit count."
    ]
    for pt in dt_pts:
        p = tf_d.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(6)

    # Right: Greasley DSS
    add_card(slide5, 6.85, 1.55, 5.68, 5.25)
    tx_dss = slide5.shapes.add_textbox(Inches(7.15), Inches(1.75), Inches(5.08), Inches(4.8))
    tf_s = tx_dss.text_frame
    tf_s.word_wrap = True

    p_sh = tf_s.paragraphs[0]
    p_sh.text = "Algorithmic Replenishment DSS"
    p_sh.font.name = FONT_HEADING
    p_sh.font.size = Pt(17)
    p_sh.font.bold = True
    p_sh.font.color.rgb = COLOR_PRIMARY

    dss_pts = [
        "Greasley Stochastic Safety Stock: SS = Z × sqrt(L·σd² + d²·σL²) modeling demand swings and distributor transit delays.",
        "Wilson Economic Order Quantity (EOQ): EOQ = sqrt(2·D·S / H) mathematically minimizing holding and ordering costs.",
        "Dynamic Reorder Point (ROP = d·L + SS): Generates 1-click Purchase Orders before stockouts occur on retail shelves.",
        "Surge Scenario Presets: One-click stress simulation for Normal (1.0x), Friday Rush (1.4x), and Ramadan Surge (2.5x)."
    ]
    for pt in dss_pts:
        p = tf_s.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(6)

    # ==========================================================================
    # SLIDE 6: System Architecture & Tech Stack (Figure 1)
    # ==========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide6, "System Architecture & Technology Stack", "4-TIER CYBER-PHYSICAL ARCHITECTURE (FIGURE 1)", 6)

    if os.path.exists(fig1_path):
        add_card(slide6, 0.8, 1.55, 7.5, 5.25)
        slide6.shapes.add_picture(fig1_path, Inches(0.95), Inches(1.7), Inches(7.2), Inches(4.9))

        add_card(slide6, 8.5, 1.55, 4.033, 5.25)
        tx_arch = slide6.shapes.add_textbox(Inches(8.7), Inches(1.7), Inches(3.63), Inches(4.9))
        tf_a = tx_arch.text_frame
        tf_a.word_wrap = True

        p_ah = tf_a.paragraphs[0]
        p_ah.text = "4-TIER ARCHITECTURE"
        p_ah.font.name = FONT_HEADING
        p_ah.font.size = Pt(12)
        p_ah.font.bold = True
        p_ah.font.color.rgb = COLOR_PRIMARY

        tiers = [
            ("1. Presentation Tier", "Calm Mission Studio UI, POS Terminal, 2D Floorplan, Keyboard Shortcuts (P, I, U, W, R, L, T)."),
            ("2. Gateway & Security", "FastAPI middleware, JWT authentication, Role-Based Access Control (Cashier, Clerk, Operator, Manager)."),
            ("3. Domain Services", "FEFO allocation worker, Manhattan router, Greasley replenishment DSS engine, Stock Ledger."),
            ("4. Persistence Tier", "PostgreSQL 16 strict 3NF schema, row-level locking (SKIP LOCKED), tamper-proof audit trail.")
        ]
        for name, desc in tiers:
            p_n = tf_a.add_paragraph()
            p_n.text = f"• {name}"
            p_n.font.name = FONT_HEADING
            p_n.font.size = Pt(11)
            p_n.font.bold = True
            p_n.font.color.rgb = COLOR_TEXT_MAIN
            p_n.space_before = Pt(4)

            p_d = tf_a.add_paragraph()
            p_d.text = desc
            p_d.font.name = FONT_BODY
            p_d.font.size = Pt(10)
            p_d.font.color.rgb = COLOR_TEXT_MUTED

        p_tb = tf_a.add_paragraph()
        p_tb.text = "\nTECH STACK: FastAPI · Python 3.14 · PostgreSQL 16 · SQLAlchemy · Docker · Git · Linux"
        p_tb.font.name = FONT_MONO
        p_tb.font.size = Pt(9.5)
        p_tb.font.bold = True
        p_tb.font.color.rgb = COLOR_PRIMARY
    else:
        add_card(slide6, 0.8, 1.55, 11.733, 5.25)

    # ==========================================================================
    # SLIDE 7: Timeline & Work Distribution
    # ==========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide7, "Timeline & Team Work Distribution", "14-WEEK AGILE ROADMAP & MEMBER RESPONSIBILITIES", 7)

    # Left: Sprints
    add_card(slide7, 0.8, 1.55, 5.65, 5.25)
    tx_sp = slide7.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.15), Inches(4.9))
    tf_sp = tx_sp.text_frame
    tf_sp.word_wrap = True

    p_sph = tf_sp.paragraphs[0]
    p_sph.text = "14-WEEK AGILE SCRUM SCHEDULE"
    p_sph.font.name = FONT_HEADING
    p_sph.font.size = Pt(12)
    p_sph.font.bold = True
    p_sph.font.color.rgb = COLOR_PRIMARY

    sprint_list = [
        ("W1–W2", "Sprint 1: Inception, PRD & Requirements"),
        ("W3–W4", "Sprint 2: 3NF Database Normalization & Modeling"),
        ("W5–W6", "Sprint 3: Dock Inbound & 65% Quality Gate"),
        ("W7–W8", "Sprint 4: Directed Putaway & 2D Floorplan Map"),
        ("W9–W10", "Sprint 5: POS Register & Concurrency Row-Locking"),
        ("W11–W12", "Sprint 6: Greasley Replenishment DSS & Ledger"),
        ("W13–W14", "Sprint 7: End-to-End Testing & Capstone Defense")
    ]
    for w, name in sprint_list:
        p = tf_sp.add_paragraph()
        p.text = f"• [{w}]  {name}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # Right: Team Responsibilities
    add_card(slide7, 6.85, 1.55, 5.68, 5.25)
    tx_wrk = slide7.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.18), Inches(4.9))
    tf_w = tx_wrk.text_frame
    tf_w.word_wrap = True

    p_wh = tf_w.paragraphs[0]
    p_wh.text = "TEAM RESPONSIBILITY MATRIX"
    p_wh.font.name = FONT_HEADING
    p_wh.font.size = Pt(12)
    p_wh.font.bold = True
    p_wh.font.color.rgb = COLOR_PRIMARY

    members_compact = [
        ("Raisul Islam Likhon (Lead: 251-35-508)", "System Architecture, FastAPI Backend, PostgreSQL 3NF Schema & Row-Locks, FEFO Engine, CI/CD Pipeline."),
        ("Shottobroto Dey (251-35-017)", "Replenishment DSS Engine, Greasley Safety Stock Algorithm, Wilson EOQ Optimization, API Contracts & Unit Testing."),
        ("Golam Husnain Papon (251-35-529)", "Calm Mission Studio UI Design, 2D Floorplan Heatmap, POS Frontline Screen, Receiving Quality Gate UI, Responsive Layouts.")
    ]
    for m_name, m_tasks in members_compact:
        p_n = tf_w.add_paragraph()
        p_n.text = f"• {m_name}"
        p_n.font.name = FONT_HEADING
        p_n.font.size = Pt(11.5)
        p_n.font.bold = True
        p_n.font.color.rgb = COLOR_TEXT_MAIN
        p_n.space_before = Pt(6)

        p_t = tf_w.add_paragraph()
        p_t.text = m_tasks
        p_t.font.name = FONT_BODY
        p_t.font.size = Pt(10.5)
        p_t.font.color.rgb = COLOR_TEXT_MUTED

    p_sh = tf_w.add_paragraph()
    p_sh.text = "\nSHARED: Requirements analysis, ERD design, integration testing & report."
    p_sh.font.name = FONT_BODY
    p_sh.font.size = Pt(10)
    p_sh.font.bold = True
    p_sh.font.color.rgb = COLOR_PRIMARY

    # ==========================================================================
    # SLIDE 8: Risk Management & Future Safeguards
    # ==========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide8, "Risk Assessment, Safeguards & Future Architecture", "ENGINEERING RISK MANAGEMENT & FUTURE-PROOF SOLUTIONS", 8)

    # Left: Concurrency & Operational Safeguards
    add_card(slide8, 0.8, 1.55, 5.68, 5.25)
    tx_l = slide8.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.18), Inches(4.9))
    tf_l = tx_l.text_frame
    tf_l.word_wrap = True

    p_lh = tf_l.paragraphs[0]
    p_lh.text = "OPERATIONAL & CONCURRENCY SAFEGUARDS"
    p_lh.font.name = FONT_HEADING
    p_lh.font.size = Pt(12)
    p_lh.font.bold = True
    p_lh.font.color.rgb = COLOR_ROSE

    operational_risks = [
        (
            "Multi-Till Rush-Hour Race Conditions",
            "Simultaneous checkout at 5+ tills causes overselling and double-allocation of the same lot.",
            "PostgreSQL row-level locks (SELECT FOR UPDATE SKIP LOCKED) ensure atomic batch deduction in <2.0s. Future: Distributed Redis locking for cluster scale."
        ),
        (
            "Intermittent Network Outages at Checkout",
            "Local ISP or Wi-Fi drops disconnect cash registers from the central database.",
            "Client-side offline transaction buffer with automatic sync queue upon reconnect. Future: PWA offline-first service worker architecture."
        ),
        (
            "Barcode Scanning Degradation on Chilled Items",
            "Moisture condensation on milk/meat pouches makes 1D barcodes unreadable.",
            "Audio scan validation, regex string normalization, and rapid 3-letter manual SKU fallback. Future: 2D DataMatrix and HF-RFID pallet tags."
        )
    ]
    for rsk, hazard, solution in operational_risks:
        p_rk = tf_l.add_paragraph()
        p_rk.text = f"⚠  {rsk}"
        p_rk.font.name = FONT_HEADING
        p_rk.font.size = Pt(11)
        p_rk.font.bold = True
        p_rk.font.color.rgb = COLOR_ROSE
        p_rk.space_before = Pt(8)

        p_hz = tf_l.add_paragraph()
        p_hz.text = f"Risk: {hazard}"
        p_hz.font.name = FONT_BODY
        p_hz.font.size = Pt(9.5)
        p_hz.font.color.rgb = COLOR_TEXT_MUTED
        p_hz.space_before = Pt(1)

        p_sl = tf_l.add_paragraph()
        p_sl.text = f"✓ Solution & Future Safeguard: {solution}"
        p_sl.font.name = FONT_BODY
        p_sl.font.size = Pt(9.5)
        p_sl.font.color.rgb = COLOR_TEXT_MAIN
        p_sl.space_before = Pt(2)

    # Right: Supply Chain, Food Safety & Scalability Safeguards
    add_card(slide8, 6.85, 1.55, 5.68, 5.25)
    tx_r = slide8.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.18), Inches(4.9))
    tf_r = tx_r.text_frame
    tf_r.word_wrap = True

    p_rh = tf_r.paragraphs[0]
    p_rh.text = "SUPPLY CHAIN, FOOD SAFETY & SCALABILITY"
    p_rh.font.name = FONT_HEADING
    p_rh.font.size = Pt(12)
    p_rh.font.bold = True
    p_rh.font.color.rgb = COLOR_PRIMARY

    scalability_risks = [
        (
            "Distributor Delays & Festival Demand Surges",
            "Local supply chain volatility and festival surges (Eid/Ramadan) trigger stockouts.",
            "Greasley Stochastic Safety Stock (SS = Z·√(L·σd² + d²·σL²)) with 1-click stress presets (1.4x, 2.5x). Future: Automated vendor EDI purchase order triggers."
        ),
        (
            "Food Safety Non-Compliance (BFSA 2013)",
            "Manual oversight allowing expired or near-expiry batches on retail shelves.",
            "Hard-coded 65% residual shelf-life receiving gate and automated FEFO allocation. Future: IoT cold-chain sensor integration with automatic thermal anomaly alerts."
        ),
        (
            "Multi-Branch Growth & Data Synchronization Lag",
            "Expanding from single store to regional chain creates inventory sync bottlenecks.",
            "Dockerized modular architecture with read-replica database pools. Future: Event-driven architecture (RabbitMQ/Kafka) for real-time inter-branch stock transfers."
        )
    ]
    for rsk, hazard, solution in scalability_risks:
        p_rk = tf_r.add_paragraph()
        p_rk.text = f"⚠  {rsk}"
        p_rk.font.name = FONT_HEADING
        p_rk.font.size = Pt(11)
        p_rk.font.bold = True
        p_rk.font.color.rgb = COLOR_PRIMARY_DARK
        p_rk.space_before = Pt(8)

        p_hz = tf_r.add_paragraph()
        p_hz.text = f"Risk: {hazard}"
        p_hz.font.name = FONT_BODY
        p_hz.font.size = Pt(9.5)
        p_hz.font.color.rgb = COLOR_TEXT_MUTED
        p_hz.space_before = Pt(1)

        p_sl = tf_r.add_paragraph()
        p_sl.text = f"✓ Solution & Future Safeguard: {solution}"
        p_sl.font.name = FONT_BODY
        p_sl.font.size = Pt(9.5)
        p_sl.font.color.rgb = COLOR_TEXT_MAIN
        p_sl.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 9: Expected Outcomes & Academic Deliverables
    # ==========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide9, "Expected Outcomes & Core Value", "CONCRETE DELIVERABLES & PROJECT IMPACT", 9)

    outcomes_compact = [
        ("Working Enterprise Software", "Fully functional web application with 7 interconnected workspaces (Dashboard, POS, Inbound, Putaway, Digital Twin, Procurement, Audits).", COLOR_PRIMARY),
        ("Sub-2.0s FEFO Engine", "Automated earliest-expiry batch allocation eliminating 18% perishability waste while preventing multi-till overselling.", COLOR_EMERALD),
        ("70-Page Master Tech Suite", "Comprehensive technical documentation covering PRD, 3NF schema, REST API contracts, and viva defense guide.", COLOR_INDIGO),
        ("100% Automated Test Suite", "Comprehensive suite of 27 automated tests verifying database transactions, API endpoints, and UI components.", COLOR_PRIMARY_DARK)
    ]

    for i, (title, desc, color) in enumerate(outcomes_compact):
        left = 0.8 + i * 2.98
        add_card(slide9, left, 1.55, 2.78, 3.1)

        bar = slide9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.55), Inches(2.78), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.color.rgb = color

        tx = slide9.shapes.add_textbox(Inches(left + 0.2), Inches(1.75), Inches(2.38), Inches(2.8))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_before = Pt(6)

    # Value Statement Card
    add_card(slide9, 0.8, 4.95, 11.733, 1.85, COLOR_PRIMARY_LIGHT, COLOR_PRIMARY)
    tx_val = slide9.shapes.add_textbox(Inches(1.1), Inches(5.1), Inches(11.1), Inches(1.6))
    tf_v = tx_val.text_frame
    tf_v.word_wrap = True

    p_vh = tf_v.paragraphs[0]
    p_vh.text = "CORE VALUE PROPOSITION:"
    p_vh.font.name = FONT_HEADING
    p_vh.font.size = Pt(11.5)
    p_vh.font.bold = True
    p_vh.font.color.rgb = COLOR_PRIMARY

    p_vd = tf_v.add_paragraph()
    p_vd.text = (
        "1. Zero Phantom Stockouts: Real-time PostgreSQL 3NF synchronization ensures inventory accuracy stays at 99.8%.\n"
        "2. Automated Food Safety: Enforced 65% quality gate and FEFO logic eliminate expired food sales under BFSA 2013.\n"
        "3. Built for Bangladesh Realities: Greasley stochastic buffer handles local supplier delays and festival demand surges without multi-million BDT enterprise licenses."
    )
    p_vd.font.name = FONT_BODY
    p_vd.font.size = Pt(11.5)
    p_vd.font.color.rgb = COLOR_TEXT_MAIN
    p_vd.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 10: Conclusion & Defense Q&A
    # ==========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide10, "Conclusion & Viva Defense Q&A", "SUMMARY, REFERENCES & QUESTIONS", 10)

    # Left: Summary & References
    add_card(slide10, 0.8, 1.55, 6.2, 5.25)
    tx_ref = slide10.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.7), Inches(4.8))
    tf_r = tx_ref.text_frame
    tf_r.word_wrap = True

    p_rh = tf_r.paragraphs[0]
    p_rh.text = "PROJECT SUMMARY & REFERENCES"
    p_rh.font.name = FONT_HEADING
    p_rh.font.size = Pt(12)
    p_rh.font.bold = True
    p_rh.font.color.rgb = COLOR_PRIMARY

    p_rd = tf_r.add_paragraph()
    p_rd.text = (
        "RetailSync demonstrates that robust database concurrency, automated food safety compliance, "
        "and stochastic replenishment algorithms can be successfully unified into a production-tested "
        "supermarket WMS built on open-source technologies."
    )
    p_rd.font.name = FONT_BODY
    p_rd.font.size = Pt(11.5)
    p_rd.font.color.rgb = COLOR_TEXT_MAIN
    p_rd.space_before = Pt(4)

    refs_compact = [
        "[1] Greasley, A. (2013). Operations Management, 3rd Ed. Wiley.",
        "[2] Silver, E. A., et al. (1998). Inventory Management & Scheduling.",
        "[3] Bangladesh Parliament. Bangladesh Food Safety Act 2013.",
        "[4] Postman, J., et al. (2024). High-Concurrency Row Locking in RDBMS.",
        "[5] DIU Dept. of Software Engineering. SE-231 Capstone Guidelines (2026)."
    ]
    p_rfh = tf_r.add_paragraph()
    p_rfh.text = "\nKey References:"
    p_rfh.font.name = FONT_HEADING
    p_rfh.font.size = Pt(11)
    p_rfh.font.bold = True
    p_rfh.font.color.rgb = COLOR_TEXT_MUTED
    p_rfh.space_before = Pt(4)

    for r in refs_compact:
        p = tf_r.add_paragraph()
        p.text = r
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = COLOR_TEXT_MUTED

    # Right: Thank You & Live Demo
    add_card(slide10, 7.3, 1.55, 5.233, 5.25, COLOR_BG_CARD, COLOR_PRIMARY)
    tx_qa = slide10.shapes.add_textbox(Inches(7.5), Inches(1.8), Inches(4.83), Inches(4.7))
    tf_q = tx_qa.text_frame
    tf_q.word_wrap = True

    p_ty = tf_q.paragraphs[0]
    p_ty.text = "Thank You!"
    p_ty.font.name = FONT_HEADING
    p_ty.font.size = Pt(30)
    p_ty.font.bold = True
    p_ty.font.color.rgb = COLOR_PRIMARY
    p_ty.alignment = PP_ALIGN.CENTER

    p_qsub = tf_q.add_paragraph()
    p_qsub.text = "Open for Questions & Defense Discussion"
    p_qsub.font.name = FONT_BODY
    p_qsub.font.size = Pt(13)
    p_qsub.font.color.rgb = COLOR_TEXT_MUTED
    p_qsub.alignment = PP_ALIGN.CENTER
    p_qsub.space_before = Pt(2)

    div = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.1), Inches(3.0), Inches(3.63), Inches(0.015))
    div.fill.solid()
    div.fill.fore_color.rgb = COLOR_BORDER_SUBTLE
    div.line.color.rgb = COLOR_BORDER_SUBTLE

    p_demo = tf_q.add_paragraph()
    p_demo.text = (
        "\nLive Demonstrations Ready:\n"
        "• Frontline POS Concurrency Race Simulator (5-Till Lock)\n"
        "• Greasley Stochastic Safety Stock & EOQ Simulator\n"
        "• 2D Spatial Digital Twin Warehouse Heatmap\n"
        "• BFSA 2013 Compliant Audit Ledger CSV Export"
    )
    p_demo.font.name = FONT_BODY
    p_demo.font.size = Pt(11)
    p_demo.font.color.rgb = COLOR_TEXT_MAIN
    p_demo.alignment = PP_ALIGN.LEFT
    p_demo.space_before = Pt(8)

    p_team = tf_q.add_paragraph()
    p_team.text = (
        "\nProject Team: Raisul Islam Likhon  ·  Shottobroto Dey  ·  Golam Husnain Papon\n"
        "Department of Software Engineering  ·  Daffodil International University"
    )
    p_team.font.name = FONT_HEADING
    p_team.font.size = Pt(10)
    p_team.font.bold = True
    p_team.font.color.rgb = COLOR_PRIMARY
    p_team.alignment = PP_ALIGN.CENTER
    p_team.space_before = Pt(10)

    # Save outputs
    output_dir = os.path.join(project_root, "proposal")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "RetailSync_Capstone_Proposal_Defense_Deck.pptx")
    prs.save(output_path)
    print(f"Successfully generated 10-slide PowerPoint presentation: {output_path}")

    # Copy to team sharing pack if directory exists
    team_pack_dir = os.path.join(project_root, "archive", "RetailSync_Team_Sharing_Pack")
    if os.path.exists(team_pack_dir):
        dest_pptx = os.path.join(team_pack_dir, "03_Defense_Presentation_Deck.pptx")
        shutil.copyfile(output_path, dest_pptx)
        print(f"Updated team sharing pack copy: {dest_pptx}")


if __name__ == "__main__":
    create_deck()
