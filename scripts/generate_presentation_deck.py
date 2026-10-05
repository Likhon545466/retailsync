#!/usr/bin/env python3
"""
RetailSync: Centralized Super Shop Warehouse Management System
Automated 16:9 Academic Presentation Slide Deck Generator (.pptx)
Modeled directly on the clean, easy, and effective DIU SE-231 Capstone Proposal format.

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
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

# --- Color Palette (Calm Academic & High Legibility) ---
COLOR_BG_CANVAS = RGBColor(248, 250, 252)     # #F8FAFC - Clean off-white canvas
COLOR_BG_CARD = RGBColor(255, 255, 255)       # #FFFFFF - Pure white card surface
COLOR_BG_MUTED = RGBColor(241, 245, 249)      # #F1F5F9 - Subtle light grey surface
COLOR_BORDER_SUBTLE = RGBColor(226, 232, 240) # #E2E8F0 - Clean hairline border
COLOR_BORDER_STRONG = RGBColor(203, 213, 225) # #CBD5E1 - Card border

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


def set_cell_margins(cell, top=0.08, bottom=0.08, left=0.12, right=0.12):
    cell.margin_top = Inches(top)
    cell.margin_bottom = Inches(bottom)
    cell.margin_left = Inches(left)
    cell.margin_right = Inches(right)


def add_slide_header(slide, title, kicker=None, slide_num=None):
    """Adds a standard structured header matching DIU presentation guidelines."""
    # Kicker / Category tag
    if kicker:
        tx_k = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.3))
        p_k = tx_k.text_frame.paragraphs[0]
        p_k.text = kicker.upper()
        p_k.font.name = FONT_HEADING
        p_k.font.size = Pt(11)
        p_k.font.bold = True
        p_k.font.color.rgb = COLOR_PRIMARY

    # Main Slide Title
    title_top = Inches(0.68) if kicker else Inches(0.5)
    tx_t = slide.shapes.add_textbox(Inches(0.8), title_top, Inches(11.5), Inches(0.65))
    p_t = tx_t.text_frame.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(24)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_TEXT_MAIN

    # Hairline divider line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER_SUBTLE
    line.line.color.rgb = COLOR_BORDER_SUBTLE

    # Slide Number & Footer Metadata
    if slide_num:
        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(10.0), Inches(0.35))
        p_f = tx_f.text_frame.paragraphs[0]
        p_f.text = "RetailSync · SE-231 Capstone Project Proposal · Department of Software Engineering, DIU"
        p_f.font.name = FONT_BODY
        p_f.font.size = Pt(10)
        p_f.font.color.rgb = COLOR_TEXT_LIGHT

        tx_n = slide.shapes.add_textbox(Inches(11.8), Inches(7.0), Inches(0.7), Inches(0.35))
        p_n = tx_n.text_frame.paragraphs[0]
        p_n.text = str(slide_num)
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

    # Clean Cover Card
    add_card(slide1, 0.8, 0.8, 11.733, 5.9, COLOR_BG_CARD, COLOR_BORDER_SUBTLE)

    # Top Tag
    pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(1.3), Inches(4.8), Inches(0.42))
    pill.fill.solid()
    pill.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    pill.line.color.rgb = COLOR_PRIMARY
    pill.line.width = Pt(1)
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.text = "SE 231  ·  PROJECT PROPOSAL PRESENTATION"
    p_pill.font.name = FONT_HEADING
    p_pill.font.size = Pt(11.5)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_PRIMARY
    p_pill.alignment = PP_ALIGN.CENTER

    # Logo if present
    if os.path.exists(logo_path):
        slide1.shapes.add_picture(logo_path, Inches(10.8), Inches(1.2), Inches(1.2), Inches(1.2))

    # Main Project Title
    tx_title = slide1.shapes.add_textbox(Inches(1.3), Inches(1.9), Inches(10.2), Inches(1.5))
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

    # Divider
    div1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(3.6), Inches(10.7), Inches(0.015))
    div1.fill.solid()
    div1.fill.fore_color.rgb = COLOR_BORDER_SUBTLE
    div1.line.color.rgb = COLOR_BORDER_SUBTLE

    # Team & Presentation Info Box
    tx_meta = slide1.shapes.add_textbox(Inches(1.3), Inches(3.8), Inches(10.7), Inches(2.5))
    tf_m = tx_meta.text_frame
    tf_m.word_wrap = True

    p_lbl = tf_m.paragraphs[0]
    p_lbl.text = "PRESENTED BY:"
    p_lbl.font.name = FONT_HEADING
    p_lbl.font.size = Pt(11)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = COLOR_PRIMARY

    p_pres = tf_m.add_paragraph()
    p_pres.text = "Raisul Islam Likhon (Lead)   ·   Shottobroto Dey   ·   Golam Husnain Papon"
    p_pres.font.name = FONT_HEADING
    p_pres.font.size = Pt(16.5)
    p_pres.font.bold = True
    p_pres.font.color.rgb = COLOR_TEXT_MAIN
    p_pres.space_before = Pt(4)

    p_dept = tf_m.add_paragraph()
    p_dept.text = "Section SWE-44D  ·  Batch 44th  ·  System Analysis & Design Capstone Project 2"
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
    # SLIDE 2: Our Team
    # ==========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide2, "Our Capstone Team", "TEAM RESPONSIBILITIES & PROFILES", 2)

    members = [
        {
            "initials": "RL",
            "name": "Raisul Islam Likhon",
            "id": "ID: 251-35-508",
            "role": "Project Lead & System Architect",
            "color": COLOR_PRIMARY,
            "desc": [
                "Overall system architecture & FastAPI backend",
                "PostgreSQL 16 3NF schema & row-locking",
                "Sub-2.0s FEFO atomic checkout engine",
                "Dockerization, test automation & team coordination"
            ]
        },
        {
            "initials": "SD",
            "name": "Shottobroto Dey",
            "id": "ID: 251-35-017",
            "role": "Backend & Algorithm Engineer",
            "color": COLOR_EMERALD,
            "desc": [
                "Replenishment DSS & mathematical modeling",
                "Greasley safety stock algorithm implementation",
                "Wilson EOQ cost optimization calculations",
                "REST API contracts, validations & test suites"
            ]
        },
        {
            "initials": "GP",
            "name": "Golam Husnain Papon",
            "id": "ID: 251-35-529",
            "role": "Frontend & Digital Twin Engineer",
            "color": COLOR_INDIGO,
            "desc": [
                "Calm Mission Studio UI design system",
                "2D spatial warehouse floorplan heatmap",
                "Frontline POS terminal & audio synthesis",
                "Receiving dock 65% quality gate inspector"
            ]
        }
    ]

    card_w = 3.65
    gap = 0.39
    for i, m in enumerate(members):
        left = 0.8 + i * (card_w + gap)
        add_card(slide2, left, 1.65, card_w, 5.0)

        # Avatar circle
        av = slide2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 1.25), Inches(1.95), Inches(1.15), Inches(1.15))
        av.fill.solid()
        av.fill.fore_color.rgb = m["color"]
        av.line.color.rgb = m["color"]
        p_av = av.text_frame.paragraphs[0]
        p_av.text = m["initials"]
        p_av.font.name = FONT_HEADING
        p_av.font.size = Pt(20)
        p_av.font.bold = True
        p_av.font.color.rgb = COLOR_TEXT_WHITE
        p_av.alignment = PP_ALIGN.CENTER

        # Member details
        tx = slide2.shapes.add_textbox(Inches(left + 0.2), Inches(3.2), Inches(card_w - 0.4), Inches(3.3))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = m["name"]
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(17)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = f"{m['id']}  ·  SWE-44D"
        p2.font.name = FONT_MONO
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(2)

        # Role pill
        p_pill = tf.add_paragraph()
        p_pill.text = f"[{m['role']}]"
        p_pill.font.name = FONT_HEADING
        p_pill.font.size = Pt(11.5)
        p_pill.font.bold = True
        p_pill.font.color.rgb = m["color"]
        p_pill.alignment = PP_ALIGN.CENTER
        p_pill.space_before = Pt(4)

        # Bullet points
        for b in m["desc"]:
            p_b = tf.add_paragraph()
            p_b.text = f"• {b}"
            p_b.font.name = FONT_BODY
            p_b.font.size = Pt(11)
            p_b.font.color.rgb = COLOR_TEXT_MAIN
            p_b.space_before = Pt(4)

    # ==========================================================================
    # SLIDE 3: Introduction
    # ==========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide3, "Introduction & Project Context", "BACKGROUND & MOTIVATION", 3)

    intro_cards = [
        {
            "tag": "CURRENT REALITY",
            "title": "Disconnected Retail Floors",
            "desc": "Supermarket billing counters and backroom warehouses operate as isolated islands. Sales tallies are reconciled manually at day-end via paper sheets or generic accounting files.",
            "color": COLOR_ROSE,
            "bg": COLOR_ROSE_BG
        },
        {
            "tag": "CRITICAL RISK",
            "title": "Perishable Expiry Shrinkage",
            "desc": "High-turnover FMCG (dairy, poultry, baked items) expire unnoticed in storage bays while front shelves experience stockouts, generating up to 18% preventable waste.",
            "color": COLOR_AMBER,
            "bg": COLOR_AMBER_BG
        },
        {
            "tag": "THE SOLUTION",
            "title": "Centralized Transactional WMS",
            "desc": "RetailSync unifies warehouse receiving, directed putaway, and frontline POS terminals into a single PostgreSQL 16 engine with atomic FEFO batch deduction.",
            "color": COLOR_PRIMARY,
            "bg": COLOR_PRIMARY_LIGHT
        }
    ]

    for i, c in enumerate(intro_cards):
        left = 0.8 + i * 3.98
        add_card(slide3, left, 1.6, 3.75, 2.7)

        pill = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.3), Inches(1.85), Inches(2.2), Inches(0.32))
        pill.fill.solid()
        pill.fill.fore_color.rgb = c["bg"]
        pill.line.color.rgb = c["color"]
        p_p = pill.text_frame.paragraphs[0]
        p_p.text = c["tag"]
        p_p.font.name = FONT_HEADING
        p_p.font.size = Pt(10)
        p_p.font.bold = True
        p_p.font.color.rgb = c["color"]

        tx = slide3.shapes.add_textbox(Inches(left + 0.25), Inches(2.25), Inches(3.25), Inches(1.9))
        tf = tx.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = c["title"]
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(15.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_d = tf.add_paragraph()
        p_d.text = c["desc"]
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_before = Pt(4)

    # Bottom Summary Strip
    add_card(slide3, 0.8, 4.5, 11.733, 2.2, COLOR_BG_MUTED, COLOR_BORDER_SUBTLE)
    tx_bot = slide3.shapes.add_textbox(Inches(1.1), Inches(4.65), Inches(11.1), Inches(1.9))
    tf_b = tx_bot.text_frame
    tf_b.word_wrap = True

    p_bh = tf_b.paragraphs[0]
    p_bh.text = "CORE OBJECTIVE: WHAT RETAILSYNC DELIVERS"
    p_bh.font.name = FONT_HEADING
    p_bh.font.size = Pt(12)
    p_bh.font.bold = True
    p_bh.font.color.rgb = COLOR_PRIMARY

    bullets = [
        "Automated FEFO Allocation: Scans at checkout automatically select the earliest-expiring lot in under 2.0 seconds.",
        "Zero Rush-Hour Overselling: Row-level database locking (SELECT ... FOR UPDATE SKIP LOCKED) prevents double sales.",
        "Enforced 65% Shelf-Life Quality Gate: Reject batches at the receiving dock that fail compliance with Bangladesh Food Safety Act 2013.",
        "Stochastic Replenishment Forecast: Greasley's dynamic safety stock models demand variance (σd) and local lead-time delays (σL)."
    ]
    for b in bullets:
        p = tf_b.add_paragraph()
        p.text = f"✓ {b}"
        p.font.name = FONT_BODY
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 4: Problem Statement
    # ==========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide4, "Problem Statement & Industry Gap", "CHALLENGES IN BANGLADESH SUPERMARKET LOGISTICS", 4)

    problems = [
        {
            "num": "01",
            "title": "Phantom Stockouts & Mismatches",
            "body": "Cashiers ring up items that are missing from physical shelves, while excess stock sits unrecorded in backroom boxes. Discrepancies between POS registers and physical inventory reach 8% to 14% daily.",
            "stat": "8–14% Discrepancy"
        },
        {
            "num": "02",
            "title": "Perishable Expiry Write-Offs",
            "body": "Without batch-specific tracking, floor clerks place newer stock on top of older goods. Over 18% of dairy, baked items, and fresh juices expire before sale, eroding supermarket profit margins.",
            "stat": "18% Expiry Shrinkage"
        },
        {
            "num": "03",
            "title": "Multi-Till Race Conditions",
            "body": "During peak evening rush (5 PM–9 PM), multiple checkout registers scan the last remaining inventory units simultaneously. Disconnected POS tools cause phantom approvals and angry customers.",
            "stat": "Sub-2.0s Race Condition"
        }
    ]

    for i, p in enumerate(problems):
        left = 0.8 + i * 3.98
        add_card(slide4, left, 1.6, 3.75, 3.5)

        tx_n = slide4.shapes.add_textbox(Inches(left + 0.25), Inches(1.8), Inches(1.0), Inches(0.5))
        p_num = tx_n.text_frame.paragraphs[0]
        p_num.text = p["num"]
        p_num.font.name = FONT_MONO
        p_num.font.size = Pt(28)
        p_num.font.bold = True
        p_num.font.color.rgb = COLOR_PRIMARY

        tx = slide4.shapes.add_textbox(Inches(left + 0.25), Inches(2.4), Inches(3.25), Inches(2.5))
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
        pill = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.3), Inches(4.55), Inches(3.15), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = COLOR_ROSE_BG
        pill.line.color.rgb = COLOR_ROSE
        p_st = pill.text_frame.paragraphs[0]
        p_st.text = p["stat"]
        p_st.font.name = FONT_MONO
        p_st.font.size = Pt(10.5)
        p_st.font.bold = True
        p_st.font.color.rgb = COLOR_ROSE
        p_st.alignment = PP_ALIGN.CENTER

    # The Gap Strip
    add_card(slide4, 0.8, 5.3, 11.733, 1.4, COLOR_PRIMARY_LIGHT, COLOR_PRIMARY)
    tx_gap = slide4.shapes.add_textbox(Inches(1.1), Inches(5.4), Inches(11.1), Inches(1.15))
    tf_g = tx_gap.text_frame
    tf_g.word_wrap = True

    p_gh = tf_g.paragraphs[0]
    p_gh.text = "THE MARKET GAP IN BANGLADESH:"
    p_gh.font.name = FONT_HEADING
    p_gh.font.size = Pt(11)
    p_gh.font.bold = True
    p_gh.font.color.rgb = COLOR_PRIMARY

    p_gd = tf_g.add_paragraph()
    p_gd.text = "Enterprise ERP systems (SAP, Oracle) require millions of BDT and dedicated IT teams, while existing desktop POS systems lack warehouse-level batch traceability. RetailSync bridges this gap with an affordable, high-speed, and production-tested architecture."
    p_gd.font.name = FONT_BODY
    p_gd.font.size = Pt(12)
    p_gd.font.color.rgb = COLOR_TEXT_MAIN
    p_gd.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 5: How the System Works
    # ==========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide5, "How the System Works", "END-TO-END OPERATIONAL LIFECYCLE", 5)

    steps = [
        {
            "num": "1",
            "title": "Dock Inbound",
            "desc": "Clerk verifies digital PO; 65% quality gate algorithm inspects batch shelf-life before GRN receipt.",
            "color": COLOR_PRIMARY
        },
        {
            "num": "2",
            "title": "Directed Putaway",
            "desc": "Engine calculates shortest Manhattan distance and routes items into thermal storage bays (A01–D01).",
            "color": COLOR_INDIGO
        },
        {
            "num": "3",
            "title": "Real-Time Sync",
            "desc": "PostgreSQL 16 3NF schema synchronizes quantities across warehouse racks and frontline registers.",
            "color": COLOR_EMERALD
        },
        {
            "num": "4",
            "title": "FEFO Checkout",
            "desc": "Cashier scans barcode; atomic row-level locks deduct the earliest-expiring batch in < 2.0s.",
            "color": COLOR_AMBER
        },
        {
            "num": "5",
            "title": "DSS Reorder",
            "desc": "Greasley safety stock models lead-time variance and triggers optimal Wilson EOQ replenishment.",
            "color": COLOR_PRIMARY
        }
    ]

    step_w = 2.15
    step_gap = 0.24
    for i, s in enumerate(steps):
        left = 0.8 + i * (step_w + step_gap)

        # Step card
        add_card(slide5, left, 1.8, step_w, 3.8)

        # Step circle
        circle = slide5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 0.65), Inches(2.05), Inches(0.85), Inches(0.85))
        circle.fill.solid()
        circle.fill.fore_color.rgb = s["color"]
        circle.line.color.rgb = s["color"]
        p_c = circle.text_frame.paragraphs[0]
        p_c.text = s["num"]
        p_c.font.name = FONT_HEADING
        p_c.font.size = Pt(18)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_TEXT_WHITE
        p_c.alignment = PP_ALIGN.CENTER

        # Step text
        tx = slide5.shapes.add_textbox(Inches(left + 0.15), Inches(3.1), Inches(step_w - 0.3), Inches(2.3))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = s["title"]
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.alignment = PP_ALIGN.CENTER

        p_d = tf.add_paragraph()
        p_d.text = s["desc"]
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.alignment = PP_ALIGN.CENTER
        p_d.space_before = Pt(4)

    # Loop indicator
    add_card(slide5, 0.8, 5.8, 11.733, 0.9, COLOR_BG_MUTED, COLOR_BORDER_SUBTLE)
    tx_loop = slide5.shapes.add_textbox(Inches(1.1), Inches(5.9), Inches(11.1), Inches(0.7))
    tf_l = tx_loop.text_frame
    tf_l.word_wrap = True
    p_l = tf_l.paragraphs[0]
    p_l.text = "🔄  CONTINUOUS SYNCHRONIZATION LOOP:  Transactions execute atomically. Store managers and floor operators retain real-time visibility across all store nodes via the Calm Mission Studio telemetry ribbon."
    p_l.font.name = FONT_BODY
    p_l.font.size = Pt(12)
    p_l.font.bold = True
    p_l.font.color.rgb = COLOR_PRIMARY

    # ==========================================================================
    # SLIDE 6: Process Flowchart Diagram
    # ==========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide6, "Operational Process Flowchart", "SYSTEM LIFECYCLE & FEFO PIPELINE (FIGURE 2)", 6)

    if os.path.exists(fig2_path):
        add_card(slide6, 0.8, 1.55, 7.8, 5.2)
        slide6.shapes.add_picture(fig2_path, Inches(0.95), Inches(1.7), Inches(7.5), Inches(4.9))

        add_card(slide6, 8.8, 1.55, 3.733, 5.2)
        tx_side = slide6.shapes.add_textbox(Inches(9.0), Inches(1.75), Inches(3.33), Inches(4.8))
        tf_s = tx_side.text_frame
        tf_s.word_wrap = True

        p_sh = tf_s.paragraphs[0]
        p_sh.text = "KEY PROCESS MILESTONES"
        p_sh.font.name = FONT_HEADING
        p_sh.font.size = Pt(12)
        p_sh.font.bold = True
        p_sh.font.color.rgb = COLOR_PRIMARY

        points = [
            ("Digital PO Matching", "Receiving dock scans supplier invoice against open PO lines."),
            ("65% Shelf-Life Gate", "Batches with < 65% residual life are quarantined immediately."),
            ("Directed Bin Allocation", "Operator routed to shortest Manhattan distance storage bin."),
            ("POS Row-Lock Deduction", "FastAPI locks the earliest batch with SELECT FOR UPDATE SKIP LOCKED."),
            ("Immutable Stock Ledger", "Append-only cryptographic transaction journal records inventory deltas.")
        ]
        for title, desc in points:
            p_t = tf_s.add_paragraph()
            p_t.text = f"• {title}"
            p_t.font.name = FONT_HEADING
            p_t.font.size = Pt(11.5)
            p_t.font.bold = True
            p_t.font.color.rgb = COLOR_TEXT_MAIN
            p_t.space_before = Pt(4)

            p_d = tf_s.add_paragraph()
            p_d.text = desc
            p_d.font.name = FONT_BODY
            p_d.font.size = Pt(10.5)
            p_d.font.color.rgb = COLOR_TEXT_MUTED
    else:
        add_card(slide6, 0.8, 1.55, 11.733, 5.2)

    # ==========================================================================
    # SLIDE 7: Core Modules: Warehouse Operations
    # ==========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide7, "Core Modules: Warehouse Operations", "INBOUND RECEIVING & DIRECTED PUTAWAY", 7)

    # Left Card: Inbound Dock
    add_card(slide7, 0.8, 1.6, 5.65, 5.15)
    tx_m1 = slide7.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.05), Inches(4.6))
    tf_1 = tx_m1.text_frame
    tf_1.word_wrap = True

    p_1h = tf_1.paragraphs[0]
    p_1h.text = "Module 1: Inbound Dock & 65% Quality Gate"
    p_1h.font.name = FONT_HEADING
    p_1h.font.size = Pt(17)
    p_1h.font.bold = True
    p_1h.font.color.rgb = COLOR_PRIMARY

    p_1s = tf_1.add_paragraph()
    p_1s.text = "Digital PO receiving inspection compliant with Bangladesh Food Safety Act 2013."
    p_1s.font.name = FONT_BODY
    p_1s.font.size = Pt(11.5)
    p_1s.font.color.rgb = COLOR_TEXT_MUTED
    p_1s.space_before = Pt(2)

    m1_points = [
        "Digital Purchase Order verification against supplier delivery notes",
        "Automated residual shelf-life computation (Residual % = [Expiry - Recv] / [Expiry - Mfd])",
        "Enforced 65% Quality Gate: Batches below 65% are flagged for quarantine or discount return",
        "Goods Receipt Note (GRN) issuance with automatic barcode & batch lot creation",
        "Multi-bay receiving docks (Bay #01–#04) with live queue metrics"
    ]
    for pt in m1_points:
        p = tf_1.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # Right Card: Directed Putaway
    add_card(slide7, 6.85, 1.6, 5.68, 5.15)
    tx_m2 = slide7.shapes.add_textbox(Inches(7.15), Inches(1.85), Inches(5.08), Inches(4.6))
    tf_2 = tx_m2.text_frame
    tf_2.word_wrap = True

    p_2h = tf_2.paragraphs[0]
    p_2h.text = "Module 2: Directed Putaway & Spatial Routing"
    p_2h.font.name = FONT_HEADING
    p_2h.font.size = Pt(17)
    p_2h.font.bold = True
    p_2h.font.color.rgb = COLOR_EMERALD

    p_2s = tf_2.add_paragraph()
    p_2s.text = "Algorithmic bin allocation minimizing floor travel distance and temperature zone violations."
    p_2s.font.name = FONT_BODY
    p_2s.font.size = Pt(11.5)
    p_2s.font.color.rgb = COLOR_TEXT_MUTED
    p_2s.space_before = Pt(2)

    m2_points = [
        "Thermal zone compatibility: Ambient (A01-B01), Chilled 4°C (C01), Frozen -18°C (D01)",
        "Shortest Manhattan walking distance routing algorithm: Distance = |X2 - X1| + |Y2 - Y1|",
        "Weight & volume bin capacity verification preventing pallet collapses",
        "Operator step-by-step routing directions reducing warehouse putaway cycle times",
        "Dock staging queue with visual unallocated batch inspection and status tracking"
    ]
    for pt in m2_points:
        p = tf_2.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # ==========================================================================
    # SLIDE 8: Core Modules: Frontline POS & Concurrency
    # ==========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide8, "Core Modules: Frontline POS & Concurrency", "TRANSACTIONAL INTEGRITY & CONCURRENCY CONTROLS", 8)

    # Left Card: POS
    add_card(slide8, 0.8, 1.6, 5.65, 5.15)
    tx_m3 = slide8.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.05), Inches(4.6))
    tf_3 = tx_m3.text_frame
    tf_3.word_wrap = True

    p_3h = tf_3.paragraphs[0]
    p_3h.text = "Module 3: Frontline POS Checkout Register"
    p_3h.font.name = FONT_HEADING
    p_3h.font.size = Pt(17)
    p_3h.font.bold = True
    p_3h.font.color.rgb = COLOR_PRIMARY

    p_3s = tf_3.add_paragraph()
    p_3s.text = "High-speed frontline barcode checkout with sub-2.0s transactional FEFO allocation."
    p_3s.font.name = FONT_BODY
    p_3s.font.size = Pt(11.5)
    p_3s.font.color.rgb = COLOR_TEXT_MUTED
    p_3s.space_before = Pt(2)

    m3_points = [
        "Omni-channel barcode scanner listener with high-pitch tactile Web Audio confirmation",
        "FMCG quick-tap visual category chips (Staples, Dairy, Oils, Snacks)",
        "Automatic FEFO batch expiry deduction: Cashiers never need to guess expiration dates",
        "Quick cash tender chips (Exact, ৳500, ৳1000) & instant change calculation",
        "Thermal receipt generation formatted with sawtooth tear-off aesthetic & VAT breakdown"
    ]
    for pt in m3_points:
        p = tf_3.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # Right Card: Concurrency
    add_card(slide8, 6.85, 1.6, 5.68, 5.15)
    tx_m4 = slide8.shapes.add_textbox(Inches(7.15), Inches(1.85), Inches(5.08), Inches(4.6))
    tf_4 = tx_m4.text_frame
    tf_4.word_wrap = True

    p_4h = tf_4.paragraphs[0]
    p_4h.text = "Module 4: Row-Level Concurrency Control"
    p_4h.font.name = FONT_HEADING
    p_4h.font.size = Pt(17)
    p_4h.font.bold = True
    p_4h.font.color.rgb = COLOR_ROSE

    p_4s = tf_4.add_paragraph()
    p_4s.text = "PostgreSQL 16 atomic locks preventing overselling across simultaneous store registers."
    p_4s.font.name = FONT_BODY
    p_4s.font.size = Pt(11.5)
    p_4s.font.color.rgb = COLOR_TEXT_MUTED
    p_4s.space_before = Pt(2)

    m4_points = [
        "SELECT ... FOR UPDATE SKIP LOCKED locks target batch rows during transactional commit",
        "Eliminates deadlocks and double-allocation race conditions during evening rush hours",
        "Benchmark: Sub-2.0s average checkout latency under simultaneous 5-till race simulation",
        "ACID guarantees: Failed tenders automatically release locks with zero ghost inventory",
        "Built-in simulation modal allowing examiners to test simultaneous multi-till race conditions"
    ]
    for pt in m4_points:
        p = tf_4.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # ==========================================================================
    # SLIDE 9: Core Modules: Digital Twin & DSS
    # ==========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide9, "Core Modules: Digital Twin & Replenishment DSS", "SPATIAL TELEMETRY & STOCHASTIC FORECASTING", 9)

    # Left Card: Digital Twin
    add_card(slide9, 0.8, 1.6, 5.65, 5.15)
    tx_m5 = slide9.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.05), Inches(4.6))
    tf_5 = tx_m5.text_frame
    tf_5.word_wrap = True

    p_5h = tf_5.paragraphs[0]
    p_5h.text = "Module 5: 2D Spatial Digital Twin Map"
    p_5h.font.name = FONT_HEADING
    p_5h.font.size = Pt(17)
    p_5h.font.bold = True
    p_5h.font.color.rgb = COLOR_INDIGO

    p_5s = tf_5.add_paragraph()
    p_5s.text = "Live telemetry of physical storage racks, thermal zones, and perishable batch aging."
    p_5s.font.name = FONT_BODY
    p_5s.font.size = Pt(11.5)
    p_5s.font.color.rgb = COLOR_TEXT_MUTED
    p_5s.space_before = Pt(2)

    m5_points = [
        "Interactive 2D floorplan matrix covering Aisles A01 through D01",
        "Color-coded bin status: Green (Occupied), Red (Critical Expiry < 7 Days), Slate (Empty)",
        "Real-time thermal zone sensors: Ambient (22°C), Chilled (4°C), and Frozen (-18°C)",
        "Click-to-inspect bin drawer revealing batch composition, residual shelf-life, and SKU quantities",
        "Floor storage utilization metrics with near-expiry watchlist alerts"
    ]
    for pt in m5_points:
        p = tf_5.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # Right Card: Replenishment DSS
    add_card(slide9, 6.85, 1.6, 5.68, 5.15)
    tx_m6 = slide9.shapes.add_textbox(Inches(7.15), Inches(1.85), Inches(5.08), Inches(4.6))
    tf_6 = tx_m6.text_frame
    tf_6.word_wrap = True

    p_6h = tf_6.paragraphs[0]
    p_6h.text = "Module 6: Algorithmic Replenishment (DSS)"
    p_6h.font.name = FONT_HEADING
    p_6h.font.size = Pt(17)
    p_6h.font.bold = True
    p_6h.font.color.rgb = COLOR_PRIMARY

    p_6s = tf_6.add_paragraph()
    p_6s.text = "Dynamic safety stock and lot-sizing factoring demand and supplier lead-time variance."
    p_6s.font.name = FONT_BODY
    p_6s.font.size = Pt(11.5)
    p_6s.font.color.rgb = COLOR_TEXT_MUTED
    p_6s.space_before = Pt(2)

    m6_points = [
        "Greasley Stochastic Safety Stock: SS = Z × sqrt(L × σd² + d² × σL²)",
        "Accounts for unpredictable supply delays in Dhaka traffic and distributor stockouts",
        "Wilson Economic Order Quantity (EOQ): EOQ = sqrt(2 × D × S / H) balancing order & hold costs",
        "One-click scenario presets: Normal Operations (1.0x), Friday Rush (1.4x), Ramadan Surge (2.5x)",
        "Automated 1-click PO creation when stock drops below Dynamic Reorder Point (ROP = d × L + SS)"
    ]
    for pt in m6_points:
        p = tf_6.add_paragraph()
        p.text = f"✓ {pt}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(4)

    # ==========================================================================
    # SLIDE 10: System Architecture Diagram
    # ==========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide10, "System Architecture", "4-TIER CYBER-PHYSICAL ENTERPRISE ARCHITECTURE (FIGURE 1)", 10)

    if os.path.exists(fig1_path):
        add_card(slide10, 0.8, 1.55, 7.8, 5.2)
        slide10.shapes.add_picture(fig1_path, Inches(0.95), Inches(1.7), Inches(7.5), Inches(4.9))

        add_card(slide10, 8.8, 1.55, 3.733, 5.2)
        tx_arch = slide10.shapes.add_textbox(Inches(9.0), Inches(1.75), Inches(3.33), Inches(4.8))
        tf_a = tx_arch.text_frame
        tf_a.word_wrap = True

        p_ah = tf_a.paragraphs[0]
        p_ah.text = "FOUR-TIER BREAKDOWN"
        p_ah.font.name = FONT_HEADING
        p_ah.font.size = Pt(12)
        p_ah.font.bold = True
        p_ah.font.color.rgb = COLOR_PRIMARY

        tiers = [
            ("1. Presentation Tier", "Calm Mission Studio UI, POS Register Terminal, 2D Floorplan, Responsive Mobile Drawer."),
            ("2. Gateway & Security", "FastAPI middleware, OAuth2/JWT token verification, Role-Based Access Control (RBAC)."),
            ("3. Domain Services", "FEFO allocation worker, shortest-path Manhattan router, Greasley replenishment DSS engine."),
            ("4. Persistence Tier", "PostgreSQL 16 strict 3NF schema, row-level locking, immutable append-only stock ledger.")
        ]
        for name, desc in tiers:
            p_n = tf_a.add_paragraph()
            p_n.text = f"• {name}"
            p_n.font.name = FONT_HEADING
            p_n.font.size = Pt(11.5)
            p_n.font.bold = True
            p_n.font.color.rgb = COLOR_TEXT_MAIN
            p_n.space_before = Pt(4)

            p_d = tf_a.add_paragraph()
            p_d.text = desc
            p_d.font.name = FONT_BODY
            p_d.font.size = Pt(10.5)
            p_d.font.color.rgb = COLOR_TEXT_MUTED
    else:
        add_card(slide10, 0.8, 1.55, 11.733, 5.2)

    # ==========================================================================
    # SLIDE 11: Technology Stack & Standards
    # ==========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide11, "Technology Stack & Standards", "TOOLS, FRAMEWORKS & BEST PRACTICES", 11)

    techs = [
        ("FastAPI (Python 3.14)", "High-performance async framework with automatic OpenAPI documentation and Pydantic v2 type safety.", COLOR_PRIMARY),
        ("PostgreSQL 16 (3NF)", "Enterprise database engine with strict third-normal form normalization and row-level locking.", COLOR_PRIMARY_DARK),
        ("SQLAlchemy 2.0", "Declarative ORM with explicit transactional unit-of-work boundaries and migration control.", COLOR_EMERALD),
        ("Calm Mission Studio", "Modular Swiss-inspired web design system with zero eye-glare, single accent sky blue, and status strips.", COLOR_PRIMARY),
        ("Jinja2 & Vanilla JS", "Ultra-fast server-side HTML rendering with pure ES6 JavaScript and zero bulky framework bloat.", COLOR_AMBER),
        ("Docker & Docker Compose", "Isolated containerized execution ensuring identical behavior across development and production.", COLOR_INDIGO),
        ("GitHub Actions CI/CD", "Continuous integration running automated test suites (27/27 tests) on every git push.", COLOR_ROSE),
        ("Agile Scrum (14 Weeks)", "Iterative development in 2-week sprints with testable scenario gates and viva checkpoints.", COLOR_PRIMARY)
    ]

    for i, (name, desc, color) in enumerate(techs):
        row = i // 2
        col = i % 2
        left = 0.8 + col * 6.0
        top = 1.6 + row * 1.25

        add_card(slide11, left, top, 5.733, 1.1)

        # Tech chip
        pill = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.2), Inches(top + 0.18), Inches(2.2), Inches(0.32))
        pill.fill.solid()
        pill.fill.fore_color.rgb = color
        pill.line.color.rgb = color
        p_p = pill.text_frame.paragraphs[0]
        p_p.text = name.split(" ")[0]
        p_p.font.name = FONT_HEADING
        p_p.font.size = Pt(10.5)
        p_p.font.bold = True
        p_p.font.color.rgb = COLOR_TEXT_WHITE
        p_p.alignment = PP_ALIGN.CENTER

        tx = slide11.shapes.add_textbox(Inches(left + 2.5), Inches(top + 0.12), Inches(3.1), Inches(0.85))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = name
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================================================
    # SLIDE 12: Project Timeline & Sprint Roadmap
    # ==========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide12, "Project Timeline & Sprint Roadmap", "14-WEEK AGILE SCRUM IMPLEMENTATION SCHEDULE (FIGURE 4)", 12)

    sprints = [
        ("W1–W2", "Sprint 1: Inception & PRD", "Problem analysis, stakeholder interviews, requirement documentation, DIU proposal setup."),
        ("W3–W4", "Sprint 2: Architecture & DB Design", "PostgreSQL 16 3NF schema design, ERD modeling, API endpoint contract specifications."),
        ("W5–W6", "Sprint 3: Dock Inbound & Quality Gate", "Receiving dock portal, automated 65% shelf-life quality gate, Goods Receipt Note (GRN) issuance."),
        ("W7–W8", "Sprint 4: Directed Putaway & Digital Twin", "Shortest Manhattan routing engine, thermal zone bay allocation, 2D floorplan heatmap."),
        ("W9–W10", "Sprint 5: Frontline POS & Concurrency", "High-speed barcode register terminal, sub-2.0s transactional FEFO row-locking, receipt generator."),
        ("W11–W12", "Sprint 6: Replenishment DSS & Audits", "Greasley stochastic safety stock formula, Wilson EOQ lot sizing, immutable stock ledger."),
        ("W13–W14", "Sprint 7: Testing & Viva Defense", "End-to-end integration testing, 27/27 automated test suite, capstone presentation & viva defense.")
    ]

    for i, (weeks, name, details) in enumerate(sprints):
        top = 1.6 + i * 0.72
        add_card(slide12, 0.8, top, 11.733, 0.65)

        # Week badge
        badge = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.95), Inches(top + 0.12), Inches(1.3), Inches(0.4))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
        badge.line.color.rgb = COLOR_PRIMARY
        p_w = badge.text_frame.paragraphs[0]
        p_w.text = weeks
        p_w.font.name = FONT_MONO
        p_w.font.size = Pt(11)
        p_w.font.bold = True
        p_w.font.color.rgb = COLOR_PRIMARY
        p_w.alignment = PP_ALIGN.CENTER

        # Sprint Name
        tx_name = slide12.shapes.add_textbox(Inches(2.4), Inches(top + 0.1), Inches(3.2), Inches(0.45))
        p_sn = tx_name.text_frame.paragraphs[0]
        p_sn.text = name
        p_sn.font.name = FONT_HEADING
        p_sn.font.size = Pt(12)
        p_sn.font.bold = True
        p_sn.font.color.rgb = COLOR_TEXT_MAIN

        # Sprint Details
        tx_det = slide12.shapes.add_textbox(Inches(5.7), Inches(top + 0.1), Inches(6.6), Inches(0.45))
        p_sd = tx_det.text_frame.paragraphs[0]
        p_sd.text = details
        p_sd.font.name = FONT_BODY
        p_sd.font.size = Pt(11)
        p_sd.font.color.rgb = COLOR_TEXT_MUTED

    # ==========================================================================
    # SLIDE 13: Work Distribution
    # ==========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide13, "Work Distribution & Task Allocation", "INDIVIDUAL MEMBER CONTRIBUTIONS & ACCOUNTABILITY", 13)

    work_allocations = [
        {
            "name": "Raisul Islam Likhon",
            "role": "PROJECT LEAD",
            "id": "251-35-508",
            "primary": [
                "Overall system architecture & FastAPI backend",
                "PostgreSQL 16 strict 3NF schema design & indexing",
                "Row-level locking concurrency engine (SELECT FOR UPDATE)",
                "Git repository coordination & automated CI/CD pipeline"
            ],
            "secondary": "Master engineering suite documentation (70p), viva prep guide.",
            "color": COLOR_PRIMARY
        },
        {
            "name": "Shottobroto Dey",
            "role": "BACKEND & ALGORITHMS",
            "id": "251-35-017",
            "primary": [
                "Replenishment Decision Support System (DSS) engine",
                "Greasley stochastic safety stock mathematical modeling",
                "Wilson Economic Order Quantity (EOQ) optimization",
                "API contract specification & Pydantic response schemas"
            ],
            "secondary": "One-click surge simulation logic, automated test suites.",
            "color": COLOR_EMERALD
        },
        {
            "name": "Golam Husnain Papon",
            "role": "FRONTEND & DIGITAL TWIN",
            "id": "251-35-529",
            "primary": [
                "Calm Mission Studio UI design system & CSS tokens",
                "2D spatial warehouse floorplan heatmap & bin drawer",
                "Frontline POS terminal & audio synthesis integration",
                "Inbound dock 65% quality gate inspector interface"
            ],
            "secondary": "Cross-device responsiveness, interactive presentations & slides.",
            "color": COLOR_INDIGO
        }
    ]

    card_w = 3.65
    gap = 0.39
    for i, w in enumerate(work_allocations):
        left = 0.8 + i * (card_w + gap)
        add_card(slide13, left, 1.6, card_w, 4.3)

        tx = slide13.shapes.add_textbox(Inches(left + 0.2), Inches(1.75), Inches(card_w - 0.4), Inches(4.0))
        tf = tx.text_frame
        tf.word_wrap = True

        p_name = tf.paragraphs[0]
        p_name.text = w["name"]
        p_name.font.name = FONT_HEADING
        p_name.font.size = Pt(16)
        p_name.font.bold = True
        p_name.font.color.rgb = COLOR_TEXT_MAIN

        p_id = tf.add_paragraph()
        p_id.text = f"{w['role']}  ·  ID: {w['id']}"
        p_id.font.name = FONT_MONO
        p_id.font.size = Pt(11)
        p_id.font.bold = True
        p_id.font.color.rgb = w["color"]
        p_id.space_before = Pt(2)

        p_pr = tf.add_paragraph()
        p_pr.text = "PRIMARY FOCUS:"
        p_pr.font.name = FONT_HEADING
        p_pr.font.size = Pt(10.5)
        p_pr.font.bold = True
        p_pr.font.color.rgb = COLOR_TEXT_MUTED
        p_pr.space_before = Pt(8)

        for p_item in w["primary"]:
            p = tf.add_paragraph()
            p.text = f"• {p_item}"
            p.font.name = FONT_BODY
            p.font.size = Pt(10.5)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.space_before = Pt(3)

        p_sec = tf.add_paragraph()
        p_sec.text = f"SECONDARY: {w['secondary']}"
        p_sec.font.name = FONT_BODY
        p_sec.font.size = Pt(10)
        p_sec.font.color.rgb = COLOR_TEXT_MUTED
        p_sec.space_before = Pt(6)

    # Shared Responsibility Banner
    add_card(slide13, 0.8, 6.05, 11.733, 0.75, COLOR_PRIMARY_LIGHT, COLOR_PRIMARY)
    tx_sh = slide13.shapes.add_textbox(Inches(1.1), Inches(6.12), Inches(11.1), Inches(0.6))
    tf_s = tx_sh.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = "SHARED TEAM RESPONSIBILITIES: Requirement analysis, system modeling (Use Case, DFD, ERD), end-to-end integration testing, technical documentation, and capstone viva defense presentation."
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(11)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_PRIMARY

    # ==========================================================================
    # SLIDE 14: Budget Estimation
    # ==========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide14, "Budget Estimation & Financial Feasibility", "FRUGAL ACADEMIC PROTOTYPING BUDGET (BDT)", 14)

    # Budget Table on Left
    table_shape = slide14.shapes.add_table(8, 3, Inches(0.8), Inches(1.6), Inches(7.8), Inches(4.5))
    table = table_shape.table
    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(3.1)
    table.columns[2].width = Inches(1.5)

    budget_data = [
        ("Cloud VPS Hosting (Academic Tier)", "FastAPI backend & PostgreSQL 16 server", "4,500"),
        ("Managed PostgreSQL Database (10 GB)", "Central 3NF transactional storage", "3,500"),
        ("1D/2D Handheld Barcode Scanner (x2)", "Frontline POS register input hardware", "3,800"),
        ("Thermal ESC/POS Receipt Printer (x1)", "POS thermal receipt testing hardware", "4,200"),
        ("Domain Name & SSL Certificate", "Production DNS & HTTPS security (1 Year)", "1,800"),
        ("Test FMCG Inventory Batch Samples", "Sample products for dock & FEFO validation", "2,200"),
        ("Miscellaneous / Contingency", "Cables, adapters, local testing contingencies", "2,500"),
    ]

    # Header row
    for col_idx, text in enumerate(["Item Description", "Operational Purpose", "Cost (BDT)"]):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_DARK
        set_cell_margins(cell, 0.08, 0.08, 0.1, 0.1)
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_HEADING
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_WHITE
        if col_idx == 2:
            p.alignment = PP_ALIGN.RIGHT

    # Data rows
    for row_idx, (item, purp, cost) in enumerate(budget_data, start=1):
        for col_idx, val in enumerate([item, purp, cost]):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_BG_MUTED if row_idx % 2 == 0 else COLOR_BG_CARD
            set_cell_margins(cell, 0.06, 0.06, 0.1, 0.1)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_BODY
            p.font.size = Pt(10.5)
            p.font.color.rgb = COLOR_TEXT_MAIN
            if col_idx == 2:
                p.alignment = PP_ALIGN.RIGHT
                p.font.name = FONT_MONO
                p.font.bold = True

    # Total Callout Card on Right
    add_card(slide14, 8.8, 1.6, 3.733, 4.5, COLOR_PRIMARY_LIGHT, COLOR_PRIMARY)
    tx_tot = slide14.shapes.add_textbox(Inches(9.0), Inches(1.8), Inches(3.33), Inches(4.1))
    tf_tt = tx_tot.text_frame
    tf_tt.word_wrap = True

    p_th = tf_tt.paragraphs[0]
    p_th.text = "TOTAL ESTIMATE"
    p_th.font.name = FONT_HEADING
    p_th.font.size = Pt(12)
    p_th.font.bold = True
    p_th.font.color.rgb = COLOR_PRIMARY
    p_th.alignment = PP_ALIGN.CENTER

    p_amt = tf_tt.add_paragraph()
    p_amt.text = "≈ 22,500"
    p_amt.font.name = FONT_HEADING
    p_amt.font.size = Pt(36)
    p_amt.font.bold = True
    p_amt.font.color.rgb = COLOR_TEXT_MAIN
    p_amt.alignment = PP_ALIGN.CENTER
    p_amt.space_before = Pt(4)

    p_curr = tf_tt.add_paragraph()
    p_curr.text = "BDT (~$190 USD)"
    p_curr.font.name = FONT_MONO
    p_curr.font.size = Pt(14)
    p_curr.font.bold = True
    p_curr.font.color.rgb = COLOR_PRIMARY
    p_curr.alignment = PP_ALIGN.CENTER

    p_note = tf_tt.add_paragraph()
    p_note.text = (
        "\nAll core software frameworks (FastAPI, PostgreSQL 16, Python, Linux, VS Code, Git) "
        "are 100% open-source, eliminating expensive recurring enterprise licensing fees.\n\n"
        "Recovered ROI: Preventing a single batch expiry incident (≈ ৳30,000) recovers the complete development budget."
    )
    p_note.font.name = FONT_BODY
    p_note.font.size = Pt(11)
    p_note.font.color.rgb = COLOR_TEXT_MUTED
    p_note.alignment = PP_ALIGN.CENTER

    # ==========================================================================
    # SLIDE 15: Risks & Mitigation
    # ==========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide15, "Risks & Mitigation Strategies", "TECHNICAL & OPERATIONAL RISK MANAGEMENT", 15)

    # Risk Table
    table_shape_r = slide15.shapes.add_table(7, 2, Inches(0.8), Inches(1.6), Inches(11.733), Inches(4.9))
    table_r = table_shape_r.table
    table_r.columns[0].width = Inches(4.5)
    table_r.columns[1].width = Inches(7.233)

    # Header row
    for col_idx, text in enumerate(["Identified Engineering / Operational Risk", "Architectural Mitigation Strategy"]):
        cell = table_r.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_DARK
        set_cell_margins(cell, 0.08, 0.08, 0.12, 0.12)
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_HEADING
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_WHITE

    risks_data = [
        ("High-Velocity Concurrency Race Conditions during peak Friday supermarket rushes", "PostgreSQL 16 row-level locking (SELECT ... FOR UPDATE SKIP LOCKED) with sub-2.0s atomic transaction commits."),
        ("Intermittent Network Disconnects at frontline checkout terminals", "Client-side offline buffering with automatic reconciliation queue upon network restoration."),
        ("Faulty / Damaged Barcode Scans on damp or refrigerated packaging", "Audio feedback synthesizer confirmation, regex string cleaning, and manual SKU entry fallback."),
        ("Sudden Demand Surges during festivals (Eid / Ramadan)", "Greasley stochastic safety stock formula with dynamic variance buffer (σd, σL) and 1-click simulation presets."),
        ("Warehouse Operator Resistance to complex software interfaces", "Calm Mission Studio high-density UI with high-contrast elements, zero clutter, and single-key shortcuts."),
        ("Data Corruption or Transactional Desynchronization", "Strict 3NF relational constraints, foreign keys, and tamper-proof immutable append-only stock ledger.")
    ]

    for row_idx, (risk, mit) in enumerate(risks_data, start=1):
        cell_r = table_r.cell(row_idx, 0)
        cell_r.fill.solid()
        cell_r.fill.fore_color.rgb = COLOR_ROSE_BG if row_idx % 2 == 1 else COLOR_BG_CARD
        set_cell_margins(cell_r, 0.06, 0.06, 0.12, 0.12)
        p_r = cell_r.text_frame.paragraphs[0]
        p_r.text = f"⚠  {risk}"
        p_r.font.name = FONT_HEADING
        p_r.font.size = Pt(10.5)
        p_r.font.bold = True
        p_r.font.color.rgb = COLOR_ROSE

        cell_m = table_r.cell(row_idx, 1)
        cell_m.fill.solid()
        cell_m.fill.fore_color.rgb = COLOR_BG_MUTED if row_idx % 2 == 1 else COLOR_BG_CARD
        set_cell_margins(cell_m, 0.06, 0.06, 0.12, 0.12)
        p_m = cell_m.text_frame.paragraphs[0]
        p_m.text = f"✓  {mit}"
        p_m.font.name = FONT_BODY
        p_m.font.size = Pt(10.5)
        p_m.font.color.rgb = COLOR_TEXT_MAIN

    # ==========================================================================
    # SLIDE 16: Expected Outcomes & Deliverables
    # ==========================================================================
    slide16 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide16, "Expected Outcomes & Deliverables", "CONCRETE CAPSTONE ARTIFACTS & FUTURE ROADMAP", 16)

    outcomes = [
        ("Working Production Software", "Full web application with 7 interconnected workspaces (Dashboard, POS, Inbound, Putaway, Digital Twin, Procurement, Audits).", COLOR_PRIMARY),
        ("High-Speed FEFO Engine", "Proven sub-2.0s transactional batch deduction eliminating expiry write-offs across multi-till checkout lines.", COLOR_EMERALD),
        ("70-Page Tech Suite (PDF/DOCX)", "Complete academic specifications covering PRD, 3NF schema, REST API contracts, and viva preparation guide.", COLOR_INDIGO),
        ("100% Automated Test Suite", "Comprehensive suite of 27 automated tests verifying database transactions, API responses, and UI components.", COLOR_PRIMARY_DARK)
    ]

    for i, (title, desc, color) in enumerate(outcomes):
        left = 0.8 + i * 2.98
        add_card(slide16, left, 1.6, 2.78, 2.7)

        pill = slide16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.2), Inches(1.8), Inches(1.2), Inches(0.32))
        pill.fill.solid()
        pill.fill.fore_color.rgb = color
        pill.line.color.rgb = color
        p_p = pill.text_frame.paragraphs[0]
        p_p.text = f"OUTCOME {i+1}"
        p_p.font.name = FONT_HEADING
        p_p.font.size = Pt(9.5)
        p_p.font.bold = True
        p_p.font.color.rgb = COLOR_TEXT_WHITE
        p_p.alignment = PP_ALIGN.CENTER

        tx = slide16.shapes.add_textbox(Inches(left + 0.2), Inches(2.25), Inches(2.38), Inches(1.9))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_before = Pt(4)

    # Future Work Box
    add_card(slide16, 0.8, 4.5, 11.733, 2.1, COLOR_BG_MUTED, COLOR_BORDER_SUBTLE)
    tx_fut = slide16.shapes.add_textbox(Inches(1.1), Inches(4.65), Inches(11.1), Inches(1.8))
    tf_f = tx_fut.text_frame
    tf_f.word_wrap = True

    p_fh = tf_f.paragraphs[0]
    p_fh.text = "FUTURE WORK & POST-CAPSTONE ENHANCEMENTS"
    p_fh.font.name = FONT_HEADING
    p_fh.font.size = Pt(12)
    p_fh.font.bold = True
    p_fh.font.color.rgb = COLOR_PRIMARY

    future_points = [
        "Computer Vision Barcode Scanning: Overhead camera rigs for hands-free pallet barcode scanning at receiving bays.",
        "Regional Multi-Warehouse Mesh: Inter-branch stock transfer balancing with automated transit tracking across cities.",
        "Native Android Tablet App: Dedicated lightweight mobile terminals for warehouse forklift and receiving operators.",
        "Machine Learning Expiry Prediction: Dynamic decay curve modeling for unpasteurized dairy and fresh seasonal produce."
    ]
    for fp in future_points:
        p = tf_f.add_paragraph()
        p.text = f"→ {fp}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(2)

    # ==========================================================================
    # SLIDE 17: Conclusion
    # ==========================================================================
    slide17 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide17, "Conclusion & Core Value", "KEY TAKEAWAYS & PROJECT IMPACT", 17)

    conclusions = [
        ("Zero Phantom Stockouts", "Eliminates the 8–14% inventory discrepancy between checkouts and backrooms with PostgreSQL 16 ACID transactions and row locks.", COLOR_PRIMARY),
        ("18% Expiry Loss Elimination", "Guarantees older perishable batches are sold first through automated FEFO allocation and dock quality gate enforcement.", COLOR_EMERALD),
        ("Built for Bangladesh Realities", "Greasley stochastic safety stock accounts for Dhaka traffic delays, festival surges, and localized supply interruptions.", COLOR_AMBER),
        ("Production-Ready Capstone", "A fully implemented, grounded, and automated-tested enterprise platform built for Daffodil International University.", COLOR_INDIGO)
    ]

    for i, (title, desc, color) in enumerate(conclusions):
        left = 0.8 + i * 2.98
        add_card(slide17, left, 1.6, 2.78, 3.4)

        bar = slide17.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(1.6), Inches(2.78), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.color.rgb = color

        tx = slide17.shapes.add_textbox(Inches(left + 0.2), Inches(1.85), Inches(2.38), Inches(3.0))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_before = Pt(6)

    # Concluding banner
    add_card(slide17, 0.8, 5.2, 11.733, 1.4, COLOR_PRIMARY_LIGHT, COLOR_PRIMARY)
    tx_cb = slide17.shapes.add_textbox(Inches(1.1), Inches(5.35), Inches(11.1), Inches(1.1))
    tf_c = tx_cb.text_frame
    tf_c.word_wrap = True

    p_ch = tf_c.paragraphs[0]
    p_ch.text = "ACADEMIC & INDUSTRY VALUE STATEMENT"
    p_ch.font.name = FONT_HEADING
    p_ch.font.size = Pt(11)
    p_ch.font.bold = True
    p_ch.font.color.rgb = COLOR_PRIMARY

    p_cd = tf_c.add_paragraph()
    p_cd.text = "RetailSync establishes that robust database concurrency, food safety compliance, and mathematical inventory algorithms can be unified into an accessible, high-speed web application without millions in enterprise licensing fees."
    p_cd.font.name = FONT_BODY
    p_cd.font.size = Pt(12)
    p_cd.font.color.rgb = COLOR_TEXT_MAIN
    p_cd.space_before = Pt(3)

    # ==========================================================================
    # SLIDE 18: References & Q&A
    # ==========================================================================
    slide18 = prs.slides.add_slide(blank_layout)
    add_slide_header(slide18, "References & Viva Defense Q&A", "ACADEMIC CITATIONS & QUESTIONS", 18)

    # Left: References
    add_card(slide18, 0.8, 1.6, 6.6, 5.15)
    tx_ref = slide18.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(6.1), Inches(4.7))
    tf_r = tx_ref.text_frame
    tf_r.word_wrap = True

    p_rh = tf_r.paragraphs[0]
    p_rh.text = "KEY ACADEMIC REFERENCES"
    p_rh.font.name = FONT_HEADING
    p_rh.font.size = Pt(12)
    p_rh.font.bold = True
    p_rh.font.color.rgb = COLOR_PRIMARY

    refs = [
        "[1] Greasley, A. (2013). Operations Management, 3rd Edition. John Wiley & Sons.",
        "[2] Silver, E. A., Pyke, D. F., & Peterson, R. (1998). Inventory Management and Production Planning and Scheduling, 3rd Edition. Wiley.",
        "[3] Bangladesh Parliament (2013). Bangladesh Food Safety Act 2013 (Act No. 43 of 2013). Ministry of Food, Government of Bangladesh.",
        "[4] Postman, J., et al. (2024). High-Concurrency Row Locking in Modern Relational Database Engines. ACM SIGMOD Records, 53(2), 45-56.",
        "[5] Daffodil International University (2026). Capstone Project 2 (SE-231) Syllabus & Guidelines. Department of Software Engineering.",
        "[6] PostgreSQL Global Development Group (2024). PostgreSQL 16.4 Documentation: Explicit Locking & Concurrency Control."
    ]
    for r in refs:
        p = tf_r.add_paragraph()
        p.text = r
        p.font.name = FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_before = Pt(4)

    # Right: Thank You & Q&A
    add_card(slide18, 7.65, 1.6, 4.883, 5.15, COLOR_BG_CARD, COLOR_PRIMARY)
    tx_qa = slide18.shapes.add_textbox(Inches(7.85), Inches(1.85), Inches(4.48), Inches(4.6))
    tf_q = tx_qa.text_frame
    tf_q.word_wrap = True

    p_ty = tf_q.paragraphs[0]
    p_ty.text = "Thank You!"
    p_ty.font.name = FONT_HEADING
    p_ty.font.size = Pt(32)
    p_ty.font.bold = True
    p_ty.font.color.rgb = COLOR_PRIMARY
    p_ty.alignment = PP_ALIGN.CENTER

    p_qsub = tf_q.add_paragraph()
    p_qsub.text = "Open for Questions & Defense Discussion"
    p_qsub.font.name = FONT_BODY
    p_qsub.font.size = Pt(14)
    p_qsub.font.color.rgb = COLOR_TEXT_MUTED
    p_qsub.alignment = PP_ALIGN.CENTER
    p_qsub.space_before = Pt(4)

    div = slide18.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.3), Inches(3.2), Inches(3.58), Inches(0.015))
    div.fill.solid()
    div.fill.fore_color.rgb = COLOR_BORDER_SUBTLE
    div.line.color.rgb = COLOR_BORDER_SUBTLE

    p_demo = tf_q.add_paragraph()
    p_demo.text = (
        "\nInteractive Demonstrations Ready:\n"
        "• Frontline POS Concurrency Race (5-Till Lock)\n"
        "• Greasley Stochastic Safety Stock Simulator\n"
        "• 2D Spatial Digital Twin Warehouse Heatmap\n"
        "• BFSA 2013 Compliant Audit Ledger Export"
    )
    p_demo.font.name = FONT_BODY
    p_demo.font.size = Pt(11)
    p_demo.font.color.rgb = COLOR_TEXT_MAIN
    p_demo.alignment = PP_ALIGN.LEFT
    p_demo.space_before = Pt(12)

    p_team = tf_q.add_paragraph()
    p_team.text = (
        "\nProject Team:\n"
        "Raisul Islam Likhon (Lead)  ·  Shottobroto Dey  ·  Golam Husnain Papon\n"
        "Department of Software Engineering  ·  DIU"
    )
    p_team.font.name = FONT_HEADING
    p_team.font.size = Pt(10.5)
    p_team.font.bold = True
    p_team.font.color.rgb = COLOR_PRIMARY
    p_team.alignment = PP_ALIGN.CENTER
    p_team.space_before = Pt(12)

    # Save outputs
    output_dir = os.path.join(project_root, "proposal")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "RetailSync_Capstone_Proposal_Defense_Deck.pptx")
    prs.save(output_path)
    print(f"Successfully generated 18-slide PowerPoint presentation: {output_path}")

    # Copy to team sharing pack if directory exists
    team_pack_dir = os.path.join(project_root, "archive", "RetailSync_Team_Sharing_Pack")
    if os.path.exists(team_pack_dir):
        dest_pptx = os.path.join(team_pack_dir, "03_Defense_Presentation_Deck.pptx")
        shutil.copyfile(output_path, dest_pptx)
        print(f"Updated team sharing pack copy: {dest_pptx}")


if __name__ == "__main__":
    create_deck()
