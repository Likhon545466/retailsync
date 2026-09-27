#!/usr/bin/env python3
"""
RetailSync: Centralized Super Shop Warehouse Management System
Comprehensive Academic Capstone Project Proposal Document Builder
Department of Software Engineering, Daffodil International University (DIU).
Course: SE-231 (Software System Analysis & Design / Capstone Project 2).
Part 1: Project Planning and Definition.

Author: Raisul Islam Likhon (Section: SWE-44D)
Date: September 2026
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from generate_proposal_docx import (
    COLOR_PRIMARY_NAVY, COLOR_SECONDARY_SLATE, COLOR_DARK_TEXT, COLOR_MUTED_GREY,
    COLOR_HIGHLIGHT_TEAL, HEX_NAVY, HEX_LIGHT_BLUE, HEX_ALT_ROW, HEX_BORDER,
    set_cell_background, set_cell_margins, set_table_borders, make_callout,
    setup_page_layout, add_part_header, add_h1, add_h2, add_h3, add_p, add_bullet,
    build_styled_table
)

from proposal_data import (
    MARKET_INDICATORS, PROBLEMS, COMPETITOR_COMPARISON, DIFFERENTIATION_DIMENSIONS,
    SEVERITY_MODEL, TARGET_USERS, STAKEHOLDER_MATRIX, SMART_OBJECTIVES,
    MODULE_SUMMARY, NFRS, RISKS,
    RETAILSYNC_PROBLEM_MAPPING, RETAILSYNC_TECH_STACK, RETAILSYNC_CORE_PERSONAS,
    RETAILSYNC_REAL_LIFE_SCENARIOS, RETAILSYNC_CORE_FRS, RETAILSYNC_CORE_NFRS,
    RETAILSYNC_LOCAL_RISKS, RETAILSYNC_CAPSTONE_ROADMAP,
    RETAILSYNC_RACI_MATRIX, RETAILSYNC_SDLC_EVALUATION, RETAILSYNC_DDL_TABLES_SUMMARY,
    RETAILSYNC_SQL_DDL_SCRIPT, RETAILSYNC_TESTING_STRATEGY, RETAILSYNC_EDGE_IOT_EXPANSION
)

from proposal_appendices_data import (
    DETAILED_FUNCTIONAL_REQUIREMENTS, TRACEABILITY_MATRIX, GLOSSARY,
    IMPLEMENTATION_SCOPE_MATRIX, AGILE_SPRINTS, RESOURCES_PLAN
)

def add_code_snippet(doc, code_str, title=""):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="1B365D"/>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    if title:
        run_t = p.add_run(f"-- {title}\n\n")
        run_t.font.name = "Consolas"
        run_t.font.size = Pt(8.5)
        run_t.font.bold = True
        run_t.font.color.rgb = COLOR_PRIMARY_NAVY
    
    run_code = p.add_run(code_str)
    run_code.font.name = "Consolas"
    run_code.font.size = Pt(8.0)
    run_code.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

def create_cover_page(doc):
    # Cover Page without header/footer interference
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(30)
    p_inst.paragraph_format.space_after = Pt(2)
    
    run_univ = p_inst.add_run("DAFFODIL INTERNATIONAL UNIVERSITY\n")
    run_univ.font.name = "Calibri"
    run_univ.font.size = Pt(14)
    run_univ.font.bold = True
    run_univ.font.color.rgb = COLOR_PRIMARY_NAVY
    
    run_dept = p_inst.add_run("FACULTY OF SCIENCE AND INFORMATION TECHNOLOGY\nDEPARTMENT OF SOFTWARE ENGINEERING\n")
    run_dept.font.name = "Calibri"
    run_dept.font.size = Pt(11)
    run_dept.font.bold = True
    run_dept.font.color.rgb = COLOR_SECONDARY_SLATE
    
    run_course = p_inst.add_run("Course: SE-231 (Software System Analysis & Design / Capstone Project 2)\n")
    run_course.font.name = "Calibri"
    run_course.font.size = Pt(10.5)
    run_course.font.italic = True
    run_course.font.color.rgb = COLOR_MUTED_GREY
    
    # Divider line
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_before = Pt(15)
    p_div.paragraph_format.space_after = Pt(20)
    r_div = p_div.add_run("—" * 38)
    r_div.font.color.rgb = COLOR_SECONDARY_SLATE
    
    # Project Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(4)
    
    run_title = p_title.add_run("RETAILSYNC\n")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(28)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY_NAVY
    
    run_maintitle = p_title.add_run("Centralized Super Shop Warehouse Management System\n")
    run_maintitle.font.name = "Calibri"
    run_maintitle.font.size = Pt(18)
    run_maintitle.font.bold = True
    run_maintitle.font.color.rgb = COLOR_SECONDARY_SLATE
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(4)
    p_sub.paragraph_format.space_after = Pt(25)
    
    run_tag = p_sub.add_run("“Your retail inventory, synchronized and secure.”\n\n")
    run_tag.font.name = "Calibri"
    run_tag.font.size = Pt(12)
    run_tag.font.italic = True
    run_tag.font.bold = True
    run_tag.font.color.rgb = COLOR_PRIMARY_NAVY
    
    run_sub = p_sub.add_run(
        "Comprehensive Project Proposal & Operational Study\n"
        "An Automated Retail Warehouse Management & Inventory Optimization System\n"
        "with Real-Time POS Sync, FEFO/FIFO Batch Tracking, and Automated Reordering Decision Support\n\n"
        "PROJECT PROPOSAL\nPART 1: PROJECT PLANNING AND DEFINITION"
    )
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(11)
    run_sub.font.bold = True
    run_sub.font.color.rgb = COLOR_HIGHLIGHT_TEAL
    
    # Divider line
    p_div2 = doc.add_paragraph()
    p_div2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div2.paragraph_format.space_before = Pt(10)
    p_div2.paragraph_format.space_after = Pt(25)
    r_div2 = p_div2.add_run("—" * 38)
    r_div2.font.color.rgb = COLOR_SECONDARY_SLATE
    
    # Submission Metadata Table
    meta_table = doc.add_table(rows=2, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, "E2E8F0")
    
    # Left: Submitted By
    c_by = meta_table.cell(0, 0)
    set_cell_background(c_by, "F8FAFC")
    set_cell_margins(c_by, top=100, bottom=100, left=140, right=140)
    p_by = c_by.paragraphs[0]
    p_by.paragraph_format.space_before = Pt(0)
    p_by.paragraph_format.space_after = Pt(2)
    r_by_lbl = p_by.add_run("SUBMITTED BY:\n")
    r_by_lbl.font.bold = True
    r_by_lbl.font.size = Pt(9.5)
    r_by_lbl.font.color.rgb = COLOR_PRIMARY_NAVY
    r_by_txt = p_by.add_run(
        "Raisul Islam Likhon\n"
        "Section: SWE-44D\n"
        "Department of Software Engineering\n"
        "Faculty of Science and Information Technology\n"
        "Daffodil International University"
    )
    r_by_txt.font.size = Pt(9)
    r_by_txt.font.color.rgb = COLOR_DARK_TEXT
    
    # Right: Supervised By
    c_to = meta_table.cell(0, 1)
    set_cell_background(c_to, "F8FAFC")
    set_cell_margins(c_to, top=100, bottom=100, left=140, right=140)
    p_to = c_to.paragraphs[0]
    p_to.paragraph_format.space_before = Pt(0)
    p_to.paragraph_format.space_after = Pt(2)
    r_to_lbl = p_to.add_run("SUPERVISED BY:\n")
    r_to_lbl.font.bold = True
    r_to_lbl.font.size = Pt(9.5)
    r_to_lbl.font.color.rgb = COLOR_PRIMARY_NAVY
    r_to_txt = p_to.add_run(
        "Academic Supervisor / Course Teacher\n"
        "Designation: Lecturer / Assistant Professor\n"
        "Department of Software Engineering\n"
        "Faculty of Science and Information Technology\n"
        "Daffodil International University"
    )
    r_to_txt.font.size = Pt(9)
    r_to_txt.font.color.rgb = COLOR_DARK_TEXT
    
    # Date row
    c_date = meta_table.cell(1, 0)
    set_cell_background(c_date, "FFFFFF")
    set_cell_margins(c_date, top=60, bottom=60, left=140, right=140)
    p_dt = c_date.paragraphs[0]
    p_dt.paragraph_format.space_before = Pt(0)
    p_dt.paragraph_format.space_after = Pt(0)
    r_dt = p_dt.add_run("Submission Date: September 27, 2026")
    r_dt.font.size = Pt(8.5)
    r_dt.font.bold = True
    r_dt.font.color.rgb = COLOR_MUTED_GREY
    
    c_sem = meta_table.cell(1, 1)
    set_cell_background(c_sem, "FFFFFF")
    set_cell_margins(c_sem, top=60, bottom=60, left=140, right=140)
    p_sm = c_sem.paragraphs[0]
    p_sm.paragraph_format.space_before = Pt(0)
    p_sm.paragraph_format.space_after = Pt(0)
    r_sm = p_sm.add_run("Academic Term: Fall 2026 | SE-231 Capstone 2")
    r_sm.font.size = Pt(8.5)
    r_sm.font.color.rgb = COLOR_MUTED_GREY
    
    doc.add_page_break()

def create_table_of_contents(doc):
    add_h1(doc, "Table of Contents")
    add_p(doc, "This proposal follows the official System Analysis and Design Capstone Proposal structure:", space_after=8)
    
    toc_data = [
        ("PART A: THE PROBLEM & REAL-WORLD CONTEXT", "3"),
        ("  1. Project Overview & Vision", "3"),
        ("  2. Real-World Operational Study & Background", "3"),
        ("    2.1 The Bangladeshi Retail Challenge", "3"),
        ("    2.2 The Financial Impact & Three Major Financial Leaks", "4"),
        ("    2.3 Empirical Market Telemetry & BBS Indicators", "4"),
        ("  3. Problem Statement & Feature Mapping", "5"),
        ("    3.1 Core Operational Problems & Solution Mapping", "5"),
        ("    3.2 Detailed Engineering Problem Taxonomy (P-01 to P-09)", "5"),
        ("  4. Existing Solution Gap & Competitor Comparison", "6"),
        ("    4.1 Competitor Capability Comparison Matrix", "7"),
        ("PART B: PROPOSED SOLUTION & ARCHITECTURE", "8"),
        ("  5. Product Positioning and Differentiation", "8"),
        ("    5.1 Why RetailSync Is Different", "8"),
        ("    5.2 Formal Product Positioning Statement", "8"),
        ("    5.3 Phased Market Entry & Deployment Strategy", "9"),
        ("  6. Proposed Solution Architecture, Workflows & Operational Model", "9"),
        ("    6.1 Step-by-Step Physical to Digital Workflow (4 Core Steps)", "9"),
        ("    6.2 End-to-End 7-Stage Warehouse Material Flow", "10"),
        ("    6.3 Technical Architecture & Stack Recommendation", "11"),
        ("    6.4 Conceptual 4-Tier System Architecture", "11"),
        ("    6.5 Production-Ready Relational Database Schema Blueprint (DDL & ERD Design)", "12"),
        ("    6.6 Stock Alert & Severity Escalation Model", "14"),
        ("    6.7 Barcode & Handheld Data Capture Strategy", "14"),
        ("    6.8 Hybrid Enterprise Edge Expansion: Integrating WarePulse IoT Gateways into RetailSync", "15"),
        ("  7. Intelligent System Strategy & Inventory Optimization Algorithms", "16"),
        ("    7.1 Dynamic Economic Order Quantity (EOQ)", "16"),
        ("    7.2 Greasley's Statistical Safety Stock Model", "16"),
        ("    7.3 Dynamic Reorder Point (ROP)", "17"),
        ("    7.4 Concrete Super Shop Case Study: 1-Litre Fortified Soyabean Oil", "17"),
        ("    7.5 Machine Learning Anomaly & Shrinkage Detection", "18"),
        ("PART C: TARGET USERS & REAL-LIFE SCENARIOS", "19"),
        ("  8. Target Users, Personas and Stakeholder Analysis", "19"),
        ("    8.1 Target Users Identification", "19"),
        ("    8.2 Core Operational Personas (Store Manager, Cashier, Inventory Clerk)", "19"),
        ("    8.3 Detailed Field User Personas", "20"),
        ("    8.4 Stakeholder Analysis Matrix", "21"),
        ("    8.5 Stakeholder RACI Responsibility Assignment Matrix", "21"),
        ("  9. Real-Life Operational Use-Case Scenarios", "22"),
        ("    9.1 Core Real-Life Retail Scenarios (Festival Rush, Expiry Audit, Network Drop)", "22"),
        ("    9.2 Advanced Logistics & Warehouse Scenarios", "23"),
        ("PART D: GOALS, SCOPE AND REQUIREMENTS", "25"),
        ("  10. Project Objectives", "25"),
        ("    10.1 Primary (General) Objective", "25"),
        ("    10.2 S.M.A.R.T. Specific Objectives (O-01 to O-06)", "25"),
        ("  11. Scope and Boundaries", "26"),
        ("    11.1 Initial Capstone MVP (In-Scope)", "26"),
        ("    11.2 Planned Enhancements (Time Permitting)", "26"),
        ("    11.3 Future Scope (Outside Capstone Scope)", "27"),
        ("  12. Project Boundary, Safety, Security and Compliance Framework", "27"),
        ("    12.1 The System Will and Will Not", "27"),
        ("    12.2 Security, Integrity, and Audit Framework", "27"),
        ("    12.3 Regulatory and Industry Compliance in Bangladesh", "28"),
        ("  13. Requirements Analysis Summary", "28"),
        ("    13.1 Core Functional Requirements (Table 4 from Study)", "28"),
        ("    13.2 Summary of Functional Requirements by Module (M-01 to M-11)", "29"),
        ("    13.3 Non-Functional Requirements & Performance Metrics (Table 5 & NFRs)", "30"),
        ("    13.4 Feature-to-Problem Traceability Mapping", "31"),
        ("PART E: FEASIBILITY, METHODOLOGY, RESOURCES & RISKS", "32"),
        ("  14. Feasibility Analysis", "32"),
        ("    14.1 5-Dimension Feasibility Assessment", "32"),
        ("    14.2 What Is Implemented Now vs Future Scope Matrix", "33"),
        ("  15. Development Methodology (Agile Scrum Framework & Sprint Plan)", "33"),
        ("    15.1 Comparative SDLC Methodology Evaluation Matrix", "33"),
        ("    15.2 In-Depth Justification for Agile Scrum with Evolutionary Prototyping", "34"),
        ("    15.3 Capstone Sprints & Incremental Delivery Plan", "34"),
        ("  16. Resource, Time and Budget Planning", "35"),
        ("    16.1 Development & Infrastructure Resources Planning", "35"),
        ("    16.2 14-Week Capstone Implementation Roadmap", "36"),
        ("    16.3 Budget Approach & Frugal Engineering", "36"),
        ("  17. Comprehensive Risk Analysis and Proactive Mitigation", "37"),
        ("    17.1 Risk Management in the Local Retail Context (Table 6 from Study)", "37"),
        ("    17.2 Comprehensive Operational & Technical Risks (R-01 to R-12)", "37"),
        ("    17.3 Dual-Level Verification & Validation (V&V) Testing Strategy", "39"),
        ("PART F: LOOKING AHEAD", "40"),
        ("  18. Scalability, Multi-Store Architecture and Product Vision", "40"),
        ("    18.1 Architectural Provisions for High-Volume Concurrency", "40"),
        ("    18.2 Business Model Outline (Commercial SaaS Vision)", "40"),
        ("  19. Expected Value, Financial Impact and Operational ROI", "41"),
        ("  20. Part 1 Conclusion and Roadmap to Part 2 System Design", "41"),
        ("  References", "42"),
        ("PART G: APPENDICES: DETAILED SYSTEM SPECIFICATIONS", "43"),
        ("  Appendix A: Detailed Functional Requirements Table (FR-01 to FR-78)", "43"),
        ("  Appendix B: Complete Requirements Traceability Matrix", "49"),
        ("  Appendix C: Comprehensive Glossary of Terms (24 Industry Definitions)", "51")
    ]
    
    toc_table = doc.add_table(rows=len(toc_data), cols=2)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(toc_table, "FFFFFF")  # Clean borderless TOC
    
    for idx, (title, page) in enumerate(toc_data):
        row = toc_table.rows[idx]
        c_title = row.cells[0]
        c_page = row.cells[1]
        
        c_title.width = Inches(5.8)
        c_page.width = Inches(0.7)
        
        p_t = c_title.paragraphs[0]
        p_t.paragraph_format.space_before = Pt(1)
        p_t.paragraph_format.space_after = Pt(2)
        
        p_p = c_page.paragraphs[0]
        p_p.paragraph_format.space_before = Pt(1)
        p_p.paragraph_format.space_after = Pt(2)
        p_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        
        r_t = p_t.add_run(title)
        r_p = p_p.add_run(page)
        
        r_t.font.name = "Calibri"
        r_p.font.name = "Calibri"
        
        if title.startswith("PART"):
            r_t.font.bold = True
            r_t.font.size = Pt(9.5)
            r_t.font.color.rgb = COLOR_PRIMARY_NAVY
            r_p.font.bold = True
            r_p.font.size = Pt(9.5)
            r_p.font.color.rgb = COLOR_PRIMARY_NAVY
            set_cell_background(c_title, "F1F5F9")
            set_cell_background(c_page, "F1F5F9")
        elif title.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.", "13.", "14.", "15.", "16.", "17.", "18.", "19.", "20.", "Appendix", "References")):
            r_t.font.bold = True
            r_t.font.size = Pt(9)
            r_t.font.color.rgb = COLOR_SECONDARY_SLATE
            r_p.font.size = Pt(9)
            r_p.font.color.rgb = COLOR_SECONDARY_SLATE
        else:
            r_t.font.size = Pt(8.5)
            r_t.font.color.rgb = COLOR_DARK_TEXT
            r_p.font.size = Pt(8.5)
            r_p.font.color.rgb = COLOR_MUTED_GREY
            
    doc.add_page_break()

def build_proposal_document():
    doc = docx.Document()
    
    # Configure 1-inch margins and running headers/footers
    setup_page_layout(doc.sections[0])
    
    # Cover Page & Table of Contents
    create_cover_page(doc)
    create_table_of_contents(doc)
    
    # =========================================================================
    # PART A: THE PROBLEM & REAL-WORLD CONTEXT
    # =========================================================================
    add_part_header(doc, "A", "The Problem & Real-World Context")
    
    add_h1(doc, "1. Project Overview")
    add_p(doc, 
        "RetailSync is a comprehensive Warehouse Management System (WMS) engineered specifically for mid-to-large tier "
        "super shops and grocery retail chains in Bangladesh. By establishing a real-time, deterministic data bridge "
        "between the back-end warehouse operations (receiving, batching, quarantine, putaway, auditing) and the front-end "
        "Point-of-Sale (POS) registers across retail floors, RetailSync eliminates the operational blindness, phantom inventory, "
        "and perishable waste that plague modern grocery retail."
    )
    
    make_callout(doc, [
        "\"To empower retail managers with deterministic, real-time inventory data, reducing perishable waste by up to 30%, "
        "eliminating undetected stockouts, and automating supplier reordering processes through an agile, synchronized, "
        "and mathematically optimized warehouse ecosystem.\""
    ], title="Project Vision Statement")
    
    add_p(doc, 
        "The foundational philosophy of RetailSync is that warehouse inventory data must never remain a passive static record or "
        "live on isolated paper clipboards. Instead, every physical movement of goods—from dock receiving to spatial putaway, "
        "retail shelf replenishment, and cashier barcode scan—must instantly trigger active operational intelligence, autonomous "
        "stockout warnings, automated purchase requisition drafts, and strict shelf-life priority picking.",
        bold_prefix="Product Philosophy: "
    )
    
    add_p(doc, 
        "Throughout this project proposal, the following standard terminology is adopted: "
        "'Super Shop' refers to modern self-service grocery and department retail chains (e.g., Shwapno, Agora, Meena Bazar, Unimart, Daily Shopping); "
        "'Central Distribution Center (CDC)' designates the primary warehouse hub supplying retail branches; "
        "'SKU' represents a distinct Stock Keeping Unit; 'GRN' is the Goods Receipt Note validating supplier deliveries; "
        "'FEFO' denotes First-Expired, First-Out batch picking logic; 'FIFO' denotes First-In, First-Out; "
        "'EOQ' represents Economic Order Quantity; and 'ROP' indicates Dynamic Reorder Point threshold.",
        bold_prefix="Key Terminology: "
    )
    
    add_h1(doc, "2. Real-World Operational Study & Background")
    add_h2(doc, "2.1 The Bangladeshi Retail Challenge")
    add_p(doc, 
        "The urban retail landscape across Bangladesh—from Dhaka and Chittagong to major regional hubs—has shifted rapidly from "
        "traditional open-air wet markets ('Kacha Bazar') and fragmented corner grocers ('Mudir Dokan') to organized, structured super shops. "
        "However, the operational backend of many of these stores still relies on localized XAMPP/MySQL setups running isolated, "
        "standalone POS software that does not communicate with the warehouse ledger."
    )
    add_p(doc, 
        "A standard mid-sized super shop in Bangladesh routinely grapples with severe operational complexities:"
    )
    add_bullet(doc, "50+ independent suppliers delivering goods daily across varying schedules with unpredictable lead times.", bold_prefix="Supplier Volume: ")
    add_bullet(doc, "Over 5,000 unique SKUs (Stock Keeping Units) spanning dry food, household goods, chilled dairy, and fresh produce.", bold_prefix="Catalog Scale: ")
    add_bullet(doc, "Highly perishable goods (pasteurized milk, yoghurt, meat, bakery items) that mandate strict First-Expired, First-Out (FEFO) and First-In, First-Out (FIFO) handling.", bold_prefix="Perishable Sensitivity: ")
    add_bullet(doc, "High foot traffic during peak hours (weekends and religious festival seasons like Ramadan), requiring cashier checkout speeds of less than 3 seconds per item.", bold_prefix="Checkout Concurrency: ")
    
    add_h2(doc, "2.2 The Financial Impact & Three Major Financial Leaks")
    add_p(doc, 
        "Without an integrated, synchronized Warehouse Management System, super shops face three major financial leaks that heavily erode profit margins:"
    )
    add_bullet(doc, 
        "The POS system indicates that there are 10 bottles of cooking oil in stock, but they were stolen, broken, or misplaced in the warehouse. "
        "Customers looking for them in-store or placing online delivery orders are disappointed, leading to direct lost sales, cancelled orders, "
        "and severe reputational damage.",
        bold_prefix="1. Phantom Inventory: "
    )
    add_bullet(doc, 
        "Because warehouse staff manually stack shelves without systematic batch routing, older batches of dairy or packaged foods are pushed "
        "to the back of racks. They expire unnoticed, resulting in a 100% loss of capital on those expired items and risking severe food safety regulatory penalties.",
        bold_prefix="2. Expiry Shrinkage: "
    )
    add_bullet(doc, 
        "Store managers spend 3 to 4 hours every night manually walking down the aisles with a clipboard to visually inspect shelves and determine "
        "what needs to be ordered for the next day. This manual process is heavily error-prone, subjective, and creates massive operational bottlenecks.",
        bold_prefix="3. The Procurement Bottleneck: "
    )
    
    add_h2(doc, "2.3 Market Context: Empirical Telemetry & Bangladesh Market Metrics")
    add_p(doc, 
        "To ground the design of RetailSync in empirical reality, official statistical indicators from the Bangladesh Bureau of Statistics (BBS), "
        "supermarket industry reports, and retail logistics telemetry were synthesized:"
    )
    
    build_styled_table(doc, 
        ["Market & Logistics Indicator", "Empirical Baseline Metric in Bangladesh Context"],
        MARKET_INDICATORS,
        col_widths=[2.4, 4.0],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_p(doc, 
        "These empirical indicators underscore three vital conclusions: First, the rapid 16.5% CAGR in organized supermarket retail "
        "demands automated, scalable backend systems. Second, the 15% to 22% annual spoilage rate on perishables represents an unsustainable "
        "drain that can be prevented through algorithmic batch expiration tracking. Third, existing software solutions in Bangladesh are "
        "overwhelmingly front-end billing POS tools that completely ignore back-end warehouse coordination."
    )
    
    add_p(doc, 
        "The Total Addressable Market (TAM) encompasses the 65+ million urban population served by retail grocery chains across Bangladesh. "
        "The Serviceable Addressable Market (SAM) comprises approximately 450+ central distribution warehouses and regional hubs operated by "
        "supermarket chains and FMCG distributors (e.g., Shwapno, Agora, Meena Bazar, Unimart, Daily Shopping, Chaldal). The Serviceable Obtainable "
        "Market (SOM) targets 10 to 15 pilot warehouse facilities during initial capstone roll-out.",
        bold_prefix="Market Sizing (TAM/SAM/SOM): "
    )
    
    add_h1(doc, "3. Problem Statement & Feature Mapping")
    add_h2(doc, "3.1 Core Operational Problems & Solution Mapping")
    add_p(doc, 
        "The operational study identifies five foundational problems in Bangladeshi retail logistics, directly mapped to RetailSync solutions:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_PROBLEM_MAPPING[0],
        RETAILSYNC_PROBLEM_MAPPING[1:],
        col_widths=[0.6, 1.8, 2.3, 2.3],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "3.2 Detailed Engineering Problem Taxonomy (P-01 to P-09)")
    add_p(doc, 
        "To ensure comprehensive architectural coverage and academic rigor, these challenges are further decomposed into nine "
        "permanent engineering problem statements (P-01 to P-09), establishing full traceability across requirements, algorithms, and test cases:"
    )
    
    build_styled_table(doc,
        ["ID", "Problem Domain", "Operational Reality & Pain Points", "RetailSync Architectural Response"],
        PROBLEMS,
        col_widths=[0.6, 1.6, 2.3, 2.0],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h1(doc, "4. Existing Solution Gap & Competitor Comparison")
    add_p(doc, 
        "To establish the distinct necessity of RetailSync, existing software tools and operational approaches in Bangladesh were analyzed. "
        "Currently, retail enterprises resort to four unsatisfactory compromises:"
    )
    add_bullet(doc, "Fragile, prone to data corruption, zero concurrency control, lacking spatial bin indexing or automated reorder logic.", bold_prefix="Manual Spreadsheets & Paper Clipboards: ")
    add_bullet(doc, "Optimized exclusively for customer retail billing and cashier cash-drawers; completely blind to warehouse aisle/rack topology, batch expiry tracking, or supplier lead-time variance.", bold_prefix="Standalone POS Software (e.g., PrismPOS, Tally): ")
    add_bullet(doc, "Cost-prohibitive (millions of BDT in licensing and annual maintenance), multi-year deployment cycles, rigid workflows unsuited for local super shop operational realities.", bold_prefix="Legacy Tier-1 ERPs (e.g., SAP, Oracle): ")
    add_bullet(doc, "Primarily financial accounting packages with basic stock count fields; lacking mobile barcode scanning, real-time spatial putaway, or FEFO pick routing.", bold_prefix="Mid-Market Accounting Tools (e.g., PrismERP): ")
    
    add_h2(doc, "4.1 Competitor Capability Comparison Matrix")
    add_p(doc, "The comprehensive capability matrix below contrasts existing solutions against the proposed RetailSync system across ten vital operational dimensions:")
    
    build_styled_table(doc,
        COMPETITOR_COMPARISON[0],
        COMPETITOR_COMPARISON[1:],
        col_widths=[1.5, 1.2, 1.2, 1.3, 1.3],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_p(doc, 
        "The comparison illustrates that no existing solution in the Bangladeshi market provides an integrated, cost-effective, "
        "and mobile-accessible platform combining real-time POS synchronization, spatial putaway, algorithmic FEFO batch picking, "
        "and mathematical replenishment optimization. Part B details the architecture and operational models that resolve this gap."
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # PART B: PROPOSED SOLUTION & ARCHITECTURE
    # =========================================================================
    add_part_header(doc, "B", "Proposed Solution & Architecture")
    
    add_h1(doc, "5. Product Positioning and Differentiation")
    add_p(doc, 
        "RetailSync moves beyond basic inventory bookkeeping. Its superiority stems from uniting spatial warehouse intelligence, "
        "sub-second POS inventory deduction, strict perishable expiry lifecycle enforcement, and mathematical decision support into "
        "a unified, user-friendly cyber-physical architecture tailored for supermarket supply chains."
    )
    
    add_h2(doc, "5.1 Why RetailSync Is Different")
    build_styled_table(doc,
        DIFFERENTIATION_DIMENSIONS[0],
        DIFFERENTIATION_DIMENSIONS[1:],
        col_widths=[1.8, 2.3, 2.4],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "5.2 Formal Product Positioning Statement")
    make_callout(doc, [
        "\"For retail super shop chains and central grocery distribution hubs that struggle with warehouse opacity, perishable spoilage, "
        "and stockout bottlenecks, RetailSync is a centralized, mobile-ready Warehouse Management & Inventory Optimization System. "
        "Unlike generic spreadsheets, standalone POS software, or rigid multi-crore ERPs, RetailSync delivers real-time spatial bin putaway, "
        "automated FEFO expiry allocation, sub-2.0s POS inventory deduction, and mathematical replenishment decision support (EOQ, "
        "Greasley Safety Stock, ROP) within a lightweight, highly usable, and cost-effective modern web platform.\""
    ], title="Formal Product Positioning Statement")
    
    add_h2(doc, "5.3 Phased Market Entry & Deployment Strategy")
    add_p(doc, 
        "To guarantee operational feasibility and de-risk deployment, RetailSync adopts a structured 3-stage market entry strategy: "
        "Stage 1 (Capstone MVP & Pilot) deploys the core system in a central distribution warehouse serving 3 retail branch outlets, "
        "validating barcode scanning, directed putaway, and FEFO picking on high-velocity FMCG and dairy items. "
        "Stage 2 expands functionality to include multi-temperature regional distribution centers and advanced supplier scorecards. "
        "Stage 3 transitions into a commercial enterprise SaaS/On-Premise solution supporting nationwide supermarket chains."
    )
    
    add_h1(doc, "6. Proposed Solution Architecture, Workflows & Operational Model")
    add_p(doc, 
        "RetailSync operates as a multi-tier cyber-physical software platform that captures physical stock movements via handheld barcode readers, "
        "enforces ACID transactional ledger integrity in a relational database, executes optimization algorithms in real time, and renders "
        "actionable telemetry on responsive web dashboards."
    )
    
    add_h2(doc, "6.1 Step-by-Step Physical to Digital Workflow (4 Core Steps)")
    add_p(doc, 
        "To understand RetailSync, the physical operational realities of a super shop are mapped directly to digital system workflows:"
    )
    add_bullet(doc, 
        "Physical Reality: A supplier delivery truck arrives with 50 cartons of milk. The inventory clerk physically inspects and counts them.\n"
        "Digital Action: The clerk opens RetailSync on a mobile terminal, selects the active Purchase Order (PO), and generates a Goods Receipt Note (GRN). "
        "The clerk inputs the specific Expiry Date of this batch. The system updates 'Available' stock in real-time.",
        bold_prefix="Step 1: Supplier Delivery & Receiving (GRN): "
    )
    add_bullet(doc, 
        "Physical Reality: During unloading, 2 cartons are found crushed or leaking.\n"
        "Digital Action: The clerk flags these 2 cartons as 'Damaged/Quarantine' in RetailSync. They are logged for supplier credit return and "
        "are strictly NOT added to the sellable POS inventory.",
        bold_prefix="Step 2: Quarantine & Damage Handling: "
    )
    add_bullet(doc, 
        "Physical Reality: A customer purchases 3 cartons of milk at the retail checkout counter.\n"
        "Digital Action: The cashier scans the barcode. The POS sends an API request to RetailSync. The system uses FIFO/FEFO logic to deduct "
        "3 units from the OLDEST active batch of milk in the database. Latency is guaranteed under 2.0 seconds.",
        bold_prefix="Step 3: The Retail Floor & POS Sync: "
    )
    add_bullet(doc, 
        "Physical Reality: The total milk stock on shelves and in the backroom drops to 10 cartons (the minimum safe limit).\n"
        "Digital Action: RetailSync detects the Reorder Point (ROP) breach. It automatically drafts a Purchase Order for the specific dairy supplier "
        "and dispatches a dashboard notification to the Store Manager for one-click approval.",
        bold_prefix="Step 4: Automated Auditing & Reordering: "
    )
    
    add_h2(doc, "6.2 End-to-End 7-Stage Warehouse Material Flow")
    add_p(doc, 
        "Expanding upon the 4 core steps, the comprehensive material and information flow across central distribution warehouses follows seven tightly coordinated stages:"
    )
    add_bullet(doc, "Inbound supplier deliveries are validated against digital PO line items via handheld barcode interrogation; damaged items logged; internal batch labels printed; digital GRN issued.", bold_prefix="1. Inbound Receiving & Digital GRN: ")
    add_bullet(doc, "SKU velocity (ABC classification) and temperature constraints guide operators to the optimal Zone-Aisle-Rack-Shelf-Bin; shelf barcode scan commits placement.", bold_prefix="2. Directed Spatial Putaway: ")
    add_bullet(doc, "Atomic database transaction increments physical on-hand stock and registers the batch into the real-time FEFO priority queue.", bold_prefix="3. Relational Ledger Commit: ")
    add_bullet(doc, "Branch stores submit daily requisitions; RetailSync aggregates orders into picking waves, allocating stock from earliest-expiring available batches.", bold_prefix="4. Outbound Requisition & Wave Allocation: ")
    add_bullet(doc, "Warehouse operators receive digital pick lists sorted by shortest travel path; pickers scan source bins and items to verify batch accuracy.", bold_prefix="5. Shortest-Path Wave Picking: ")
    add_bullet(doc, "Picked items are sorted into store-specific rolling cages; an official Delivery Chalan / Dispatch Note is printed for delivery transit.", bold_prefix="6. Staging & Store Dispatch: ")
    add_bullet(doc, "Store receiving staff scan incoming totes against the dispatch manifest, confirming receipt and closing the requisition cycle.", bold_prefix="7. Store Receipt Reconciliation: ")
    
    add_h2(doc, "6.3 Technical Architecture & Stack Recommendation")
    add_p(doc, 
        "To ensure high performance, bulletproof concurrency, and data integrity, RetailSync relies on an industry-standard, robust technology stack:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_TECH_STACK[0],
        RETAILSYNC_TECH_STACK[1:],
        col_widths=[1.5, 1.8, 3.4],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "6.4 Conceptual 4-Tier System Architecture")
    add_p(doc, 
        "The complete RetailSync software architecture is structured across four clean, decoupled layers: "
        "1. Physical Edge & Data Capture Layer: Handheld Bluetooth/USB barcode scanners and smartphone cameras capturing 1D/2D GS1 barcodes on pallets, cartons, and shelf bins. "
        "2. API Gateway & Ingestion Service Layer: Stateless RESTful services (Node.js/Express or Python FastAPI) managing scan validation, payload parsing, and JWT authentication. "
        "3. Relational Ledger & Analytics Data Layer: PostgreSQL 16 / MySQL database enforcing strict ACID compliance, foreign key referential integrity, B-Tree indexes, and append-only audit ledgers, coupled with Redis for high-speed caching. "
        "4. Presentation & Visualization Layer: Responsive Next.js / React web portal providing live floor telemetry, 2D interactive spatial bin maps, mobile scanner views, and executive KPI analytics."
    )
    
    add_h2(doc, "6.5 Production-Ready Relational Database Schema Blueprint (DDL & ERD Design)")
    add_p(doc, 
        "To satisfy the rigorous academic data modeling standards of SE-231 (Software System Analysis & Design), "
        "RetailSync enforces strict Third Normal Form (3NF) relational integrity across eight production-grade core entities. "
        "The schema implements declarative foreign key cascading controls, domain value check constraints, timestamped audit triggers, "
        "and strategic B-Tree indexing tailored for sub-millisecond barcode scan queries and atomic POS stock deduction:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_DDL_TABLES_SUMMARY[0],
        RETAILSYNC_DDL_TABLES_SUMMARY[1:],
        col_widths=[1.2, 2.0, 1.3, 1.4, 1.3],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_p(doc, 
        "Below is the complete, executable Data Definition Language (DDL) conceptual script for PostgreSQL 16+ / MySQL 8.0+, "
        "demonstrating the exact schema definition, referential foreign key actions, and performance indexes:"
    )
    
    add_code_snippet(doc, RETAILSYNC_SQL_DDL_SCRIPT, title="RetailSync Core Relational Schema Blueprint (PostgreSQL / MySQL DDL)")
    
    add_h2(doc, "6.6 Stock Alert & Severity Escalation Model")
    add_p(doc, 
        "To prevent alert fatigue while ensuring immediate response to operational emergencies, RetailSync establishes an explainable "
        "five-level severity model governed by deterministic rules:"
    )
    
    build_styled_table(doc,
        SEVERITY_MODEL[0],
        SEVERITY_MODEL[1:],
        col_widths=[0.8, 1.4, 1.6, 1.8, 0.9],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "6.7 Barcode & Handheld Data Capture Strategy")
    add_p(doc, 
        "Recognizing that industrial rugged terminals cost upwards of 60,000 BDT per unit, RetailSync implements a highly accessible "
        "data capture strategy: the mobile scanning interface is built as a progressive web application (PWA) compatible with standard "
        "Android smartphones paired with low-cost Bluetooth barcode trigger grips (under 4,000 BDT) or direct camera-based barcode "
        "libraries (ZXing / Html5-QRCode). Auditory beeps and haptic vibration provide instantaneous feedback, enabling operators to scan "
        "items rapidly without continuously looking at the screen."
    )
    
    add_h2(doc, "6.8 Hybrid Enterprise Edge Expansion: Integrating WarePulse IoT Gateways into RetailSync")
    add_p(doc, 
        "A critical architectural insight emerged from our comparative evaluation with the WarePulse industrial IoT prototype: "
        "while handheld mobile scanning (PWA + Bluetooth trigger) is optimal for retail floor picking and store operations, "
        "central grocery distribution warehouses handling 50+ pallet deliveries daily benefit immensely from stationary automated dock gates. "
        "RetailSync provides native architectural extensibility to incorporate the WarePulse edge IoT stack as an optional high-throughput "
        "inbound dock gateway without modifying the core software platform:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_EDGE_IOT_EXPANSION[0],
        RETAILSYNC_EDGE_IOT_EXPANSION[1:],
        col_widths=[1.5, 2.3, 2.7],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_p(doc, 
        "Under this hybrid enterprise architecture, forklifts driving pallets through loading dock doors pass under an overhead ESP32 "
        "RFID/fixed-barcode scanner array. The edge node buffers the scan telemetry into non-volatile LittleFS flash memory during Wi-Fi "
        "brownouts and pushes structured JSON payloads via TLS-encrypted MQTT (QoS 1) directly to RetailSync's Inbound Worker service, "
        "instantly reconciling open Purchase Orders and generating draft GRNs with zero human manual intervention."
    )
    
    add_h1(doc, "7. Intelligent System Strategy & Inventory Optimization Algorithms")
    add_p(doc, 
        "A foundational differentiator of RetailSync is its integration of mathematical decision support models directly into the operational "
        "application layer. Rather than relying on black-box artificial intelligence where explainability is compromised, RetailSync combines "
        "rigorous operations research formulations with targeted unsupervised machine learning for anomaly detection."
    )
    
    add_h2(doc, "7.1 Dynamic Economic Order Quantity (EOQ)")
    add_p(doc, 
        "The EOQ model calculates the optimal order batch size (Q*) that minimizes total annual inventory holding and ordering costs:"
    )
    make_callout(doc, [
        "EOQ = sqrt( (2 * D * S) / H )",
        "Where:",
        "• D = Annual Demand (units/year), dynamically extracted from rolling transactional sales history.",
        "• S = Fixed Ordering Setup Cost per purchase order (administrative, documentation, transport inspection fees in BDT).",
        "• H = Unit Holding Cost per year (cost of warehouse cubic footprint, refrigeration, tied-up working capital, insurance, and obsolescence risk in BDT/unit/year)."
    ], title="Mathematical Formulation: Economic Order Quantity")
    
    add_h2(doc, "7.2 Greasley's Statistical Safety Stock Model")
    add_p(doc, 
        "Standard naive safety stock heuristics assume constant supplier lead times or static demand rates. In Bangladeshi retail, however, "
        "supplier lead times fluctuate wildly due to traffic congestion, political strikes (hartals), and distributor stockouts. RetailSync implements "
        "Greasley's advanced statistical safety stock formula, which simultaneously models independent variances in both daily consumer demand "
        "and supplier delivery lead time:"
    )
    make_callout(doc, [
        "SS = Z * sqrt( (L_avg * sigma_d^2) + (d_avg^2 * sigma_L^2) )",
        "Where:",
        "• Z = Statistical service level factor (Z = 1.28 for 90%, Z = 1.65 for 95%, Z = 1.96 for 97.5%, Z = 2.33 for 99% non-stockout probability).",
        "• L_avg = Average supplier lead time in days.",
        "• sigma_L = Standard deviation of supplier lead time in days (capturing delivery volatility).",
        "• d_avg = Average daily demand rate in units.",
        "• sigma_d = Standard deviation of daily demand in units (capturing retail sales volatility)."
    ], title="Mathematical Formulation: Greasley Statistical Safety Stock")
    
    add_h2(doc, "7.3 Dynamic Reorder Point (ROP)")
    add_p(doc, 
        "The Reorder Point establishes the precise inventory threshold that autonomously triggers replenishment purchase orders:"
    )
    make_callout(doc, [
        "ROP = (d_avg * L_avg) + SS",
        "When the net Inventory Position (On-Hand Stock + Open POs - Allocated Store Orders) drops to or below ROP, the system automatically drafts a Purchase Order for the calculated EOQ batch size."
    ], title="Mathematical Formulation: Dynamic Reorder Point")
    
    add_h2(doc, "7.4 Concrete Super Shop Case Study: 1-Litre Fortified Soyabean Oil")
    add_p(doc, 
        "To demonstrate the mathematical rigor of RetailSync, consider a high-velocity staple commodity in a Dhaka central retail warehouse "
        "(1-Litre Bottled Fortified Soyabean Oil):"
    )
    add_bullet(doc, "Annual Demand (D) = 36,500 bottles (Average daily demand d_avg = 100 bottles/day, standard deviation sigma_d = 20 bottles/day).")
    add_bullet(doc, "Order Setup Cost (S) = 1,200 BDT per purchase order (administrative processing, quality sampling, dock labor).")
    add_bullet(doc, "Unit Holding Cost (H) = 12 BDT per bottle/year (cost of warehouse racking space, capital cost at 9%, insurance).")
    add_bullet(doc, "Supplier Lead Time: Average lead time L_avg = 6 days, standard deviation sigma_L = 2 days.")
    add_bullet(doc, "Target Customer Service Level = 95% (Z = 1.65).")
    
    add_p(doc, "Step 1: Calculate Economic Order Quantity (EOQ):")
    add_p(doc, "EOQ = sqrt( (2 * 36,500 * 1,200) / 12 ) = sqrt( 87,600,000 / 12 ) = sqrt( 7,300,000 ) = 2,702 bottles.")
    
    add_p(doc, "Step 2: Calculate Greasley Statistical Safety Stock (SS):")
    add_p(doc, "Term 1 (Demand Variance) = L_avg * sigma_d^2 = 6 * (20^2) = 6 * 400 = 2,400.")
    add_p(doc, "Term 2 (Lead Time Variance) = d_avg^2 * sigma_L^2 = (100^2) * (2^2) = 10,000 * 4 = 40,000.")
    add_p(doc, "SS = 1.65 * sqrt( 2,400 + 40,000 ) = 1.65 * sqrt( 42,400 ) = 1.65 * 205.91 = 340 bottles.")
    
    add_p(doc, "Step 3: Calculate Dynamic Reorder Point (ROP):")
    add_p(doc, "ROP = (100 * 6) + 340 = 600 + 340 = 940 bottles.")
    
    make_callout(doc, [
        "Managerial Decision Rule Generated by RetailSync:",
        "\"When total net inventory position falls to 940 bottles, the system autonomously flags the SKU and generates a draft Purchase Order for 2,702 bottles, guaranteeing a 95% statistical assurance that stock will not deplete prior to supplier delivery.\""
    ], title="Automated Decision Output")
    
    add_h2(doc, "7.5 Machine Learning Inventory Anomaly & Shrinkage Detection")
    add_p(doc, 
        "In addition to mathematical replenishment, RetailSync integrates an unsupervised Machine Learning model (Isolation Forest) "
        "trained on cycle count historical variances. The algorithm flags suspicious shrinkage anomalies where stock discrepancies "
        "deviate significantly from normal baseline breakages, correlating discrepancies across specific shifts, operators, and high-value "
        "merchandise to detect pilferage clusters proactively."
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # PART C: TARGET USERS & REAL-LIFE SCENARIOS
    # =========================================================================
    add_part_header(doc, "C", "Target Users & Real-Life Scenarios")
    
    add_h1(doc, "8. Target Users, Personas and Stakeholder Analysis")
    add_p(doc, 
        "A warehouse management system succeeds only when its user interfaces are tailored to the physical environments and cognitive "
        "demands of its diverse user base. RetailSync serves primary frontline retail and warehouse management user groups:"
    )
    
    add_h2(doc, "8.1 Target Users Identification")
    build_styled_table(doc,
        TARGET_USERS[0],
        TARGET_USERS[1:],
        col_widths=[1.4, 1.2, 2.3, 1.6],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "8.2 Core Operational Personas (From Comprehensive Study)")
    add_p(doc, "The operational study defines three fundamental personas who interact daily with the core RetailSync ecosystem:")
    
    build_styled_table(doc,
        RETAILSYNC_CORE_PERSONAS[0],
        RETAILSYNC_CORE_PERSONAS[1:],
        col_widths=[1.5, 2.2, 2.8],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "8.3 Detailed Field User Personas")
    add_p(doc, "To further anchor software design decisions in genuine human context, three detailed field user personas were established:")
    
    add_bullet(doc, 
        "Age 34, manages 18 floor staff at a central grocery distribution warehouse in Tejgaon, Dhaka. "
        "Pain points: spends 2 to 3 hours daily resolving lost pallet discrepancies and paper tally errors. "
        "RetailSync Goal: Needs a real-time 2D spatial bin map and instant mobile barcode verification to eliminate physical search latency.",
        bold_prefix="Persona 1 — Tariqul Islam (Warehouse Floor Manager): "
    )
    add_bullet(doc, 
        "Age 29, manages fresh food and FMCG vendor procurement for a 14-store retail chain. "
        "Pain points: struggles with unexpected supplier delivery delays and sudden out-of-stock weekend crises on dairy products. "
        "RetailSync Goal: Needs automated EOQ/ROP replenishment triggers and supplier lead-time variance scorecards to order accurately.",
        bold_prefix="Persona 2 — Salma Akter (Senior Procurement Executive): "
    )
    add_bullet(doc, 
        "Age 41, manages a flagship super shop outlet in Dhanmondi, Dhaka. "
        "Pain points: frequently receives incorrect goods quantities or near-expiry dairy batches from the central warehouse with zero advance notice. "
        "RetailSync Goal: Needs a clean Store Requisition Portal with live central stock visibility and automated FEFO dispatch verification.",
        bold_prefix="Persona 3 — Kamal Hossain (Branch Super Shop Store Manager): "
    )
    
    add_h2(doc, "8.4 Stakeholder Analysis Matrix")
    add_p(doc, "The stakeholder matrix below outlines the interest, influence, and engagement strategy for all direct and indirect project stakeholders:")
    
    build_styled_table(doc,
        STAKEHOLDER_MATRIX[0],
        STAKEHOLDER_MATRIX[1:],
        col_widths=[1.5, 1.2, 1.8, 0.8, 1.2],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "8.5 Stakeholder RACI Responsibility Assignment Matrix")
    add_p(doc, 
        "To establish unequivocal operational ownership and cross-functional governance throughout the capstone engineering lifecycle, "
        "the formal RACI model below delineates stakeholder roles across eleven mission-critical delivery milestones:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_RACI_MATRIX[0],
        RETAILSYNC_RACI_MATRIX[1:],
        col_widths=[1.8, 0.7, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER]
    )
    
    add_p(doc, 
        "RACI Legend: Responsible (R) = Executes the delivery; Accountable (A) = Final decision and sign-off authority; "
        "Consulted (C) = Provides bi-directional domain input; Informed (I) = Kept updated on progress and outcomes."
    )
    
    add_h1(doc, "9. Real-Life Operational Use-Case Scenarios")
    add_h2(doc, "9.1 Core Real-Life Retail Scenarios")
    add_p(doc, "RetailSync is designed to withstand extreme real-world operating conditions common in Bangladeshi super shops:")
    
    build_styled_table(doc,
        RETAILSYNC_REAL_LIFE_SCENARIOS[0],
        RETAILSYNC_REAL_LIFE_SCENARIOS[1:],
        col_widths=[1.5, 2.4, 2.6],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "9.2 Advanced Logistics & Warehouse Scenarios")
    add_p(doc, "The following operational scenarios illustrate how warehouse operators and procurement officers interact with RetailSync:")
    
    add_bullet(doc, 
        "During a Ramadan promotional surge, daily demand for 1L edible oil spikes. The dynamic ROP algorithm detects that the remaining "
        "inventory position (850 units) has breached the reorder threshold (940 units). The system autonomously drafts a Purchase Order for "
        "2,702 units (EOQ) assigned to the primary supplier, incorporating the supplier's 6-day lead-time variance. The procurement officer "
        "reviews and approves the PO in one click, preventing an impending stockout.",
        bold_prefix="Scenario 1: High-Velocity FMCG Replenishment under Volatile Lead Times: "
    )
    add_bullet(doc, 
        "A supplier delivers 500 crates of pasteurized milk. The receiving clerk scans the supplier barcode, recording a manufacturing date "
        "of Sept 26 and expiration date of Oct 3. The system verifies that the remaining shelf life exceeds the 75% threshold and generates "
        "internal batch barcode labels. When two branch stores order milk three days later, the system's FEFO engine directs pickers strictly "
        "to this batch rather than a newer batch arriving on Sept 29, eliminating spoiled stock.",
        bold_prefix="Scenario 2: Perishable Dairy Expiry Management with Automated FEFO Allocation: "
    )
    add_bullet(doc, 
        "A biscuit supplier delivers 200 cartons against an open PO of 200 cartons. During dock barcode scanning, the clerk discovers that "
        "25 cartons suffered severe water and crushing damage during transit. The clerk scans the barcode, inputs 'Rejected: 25 - Damaged Packaging', "
        "and snaps a photo. The system generates a GRN for 175 accepted cartons, automatically updates the PO status to 'Partially Received', "
        "and drafts a digital credit note advisory for the 25 rejected cartons.",
        bold_prefix="Scenario 3: Receiving Dock Discrepancy, Damaged Goods, and Automated GRN: "
    )
    add_bullet(doc, 
        "Five retail branches submit morning requisitions for 40 common FMCG items. Instead of sending five pickers through the warehouse aisles "
        "independently, RetailSync consolidates the orders into a single Wave Pick. The system generates an optimized serpentine pick path guiding "
        "a single operator to collect total quantities in one pass. At the outbound staging dock, goods are sorted into branch-specific rolling "
        "cages, reducing total picker travel distance by 64%.",
        bold_prefix="Scenario 4: Multi-Store Outbound Wave Picking and Branch Staging: "
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # PART D: GOALS, SCOPE AND REQUIREMENTS
    # =========================================================================
    add_part_header(doc, "D", "Goals, Scope and Requirements")
    
    add_h1(doc, "10. Project Objectives")
    add_h2(doc, "10.1 Primary (General) Objective")
    add_p(doc, 
        "To design, architect, implement, and evaluate an automated, web-based Centralized Super Shop Warehouse Management System (RetailSync) "
        "that digitizes physical warehouse movements via handheld barcode scanning, synchronizes warehouse ledgers with frontline retail POS registers, "
        "enforces strict FEFO/FIFO batch tracking for perishable foods, optimizes inventory carrying costs and replenishment timing through mathematical "
        "decision models (EOQ/ROP), and orchestrates seamless multi-branch retail store fulfillment."
    )
    
    add_h2(doc, "10.2 S.M.A.R.T. Specific Objectives")
    add_p(doc, 
        "The project's general objective is operationalized into six Specific, Measurable, Achievable, Relevant, and Time-bound (S.M.A.R.T.) objectives:"
    )
    
    build_styled_table(doc,
        SMART_OBJECTIVES[0],
        SMART_OBJECTIVES[1:],
        col_widths=[0.6, 2.2, 2.7, 1.0],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER]
    )
    
    add_h1(doc, "11. Scope and Boundaries")
    add_p(doc, 
        "To ensure successful completion within the rigorous academic capstone semester, the project establishes explicit functional boundaries:"
    )
    
    add_h2(doc, "11.1 Initial Capstone MVP (In-Scope)")
    add_bullet(doc, "Role-Based Access Control (RBAC) with secure JWT authentication isolating Cashier, Clerk, Supervisor, and Manager views.", bold_prefix="Authentication & RBAC: ")
    add_bullet(doc, "Product Master catalog with SKU taxonomy, ABC classification, temperature classes, and barcode generation.", bold_prefix="Product Catalog: ")
    add_bullet(doc, "Supplier directory, SLA lead-time variance tracking, and digital Purchase Order workflow.", bold_prefix="Supplier & PO: ")
    add_bullet(doc, "Dock receiving, barcode PO verification, damaged item recording, and automated digital GRN generation.", bold_prefix="Inbound & GRN: ")
    add_bullet(doc, "Hierarchical Zone-Aisle-Rack-Shelf-Bin topology mapping with capacity-aware directed putaway.", bold_prefix="Spatial Bin Engine: ")
    add_bullet(doc, "ACID append-only transaction ledger, batch expiry tracking, and strict FEFO pick queue enforcement.", bold_prefix="Inventory & FEFO: ")
    add_bullet(doc, "POS Sync Simulation API executing sub-2.0s atomic stock deductions based on FIFO/FEFO batch logic.", bold_prefix="POS Synchronization: ")
    add_bullet(doc, "Dynamic Economic Order Quantity (EOQ), Greasley Statistical Safety Stock, and Dynamic ROP alert triggers.", bold_prefix="Replenishment DSS: ")
    add_bullet(doc, "Multi-branch store requisition portal, wave picking consolidation, and digital delivery chalan generation.", bold_prefix="Outbound & Store Portal: ")
    add_bullet(doc, "Continuous cycle counting schedules, blind physical count entry, discrepancy variance auditing, and write-offs.", bold_prefix="Cycle Counting & Audit: ")
    add_bullet(doc, "Real-time floor telemetry, stockout risk heatmaps, supplier SLA scorecards, and PDF/Excel reporting.", bold_prefix="Executive Analytics: ")
    
    add_h2(doc, "11.2 Planned Enhancements (Time Permitting)")
    add_bullet(doc, "Unsupervised machine learning (Isolation Forest) for automatic inventory shrinkage and pilferage cluster detection.")
    add_bullet(doc, "2D interactive visual canvas rendering real-time heatmaps of warehouse bin utilization.")
    add_bullet(doc, "SMS and WhatsApp automated alerts for high-priority stockout and expiry escalations.")
    
    add_h2(doc, "11.3 Future Scope (Outside Capstone Scope)")
    add_bullet(doc, "Physical automated guided vehicles (AGVs), robotic gantry cranes, and motorized conveyor sorters.")
    add_bullet(doc, "Ultra-High Frequency (UHF) multi-meter warehouse radar triangulation and automated drone inventory counting.")
    add_bullet(doc, "Nationwide Electronic Data Interchange (EDI) integration with enterprise legacy ERP networks.")
    
    add_h1(doc, "12. Project Boundary, Safety, Security and Compliance Framework")
    add_h2(doc, "12.1 The System Will and Will Not")
    add_bullet(doc, "The system WILL automate warehouse stock verification, track batch expiration dates, allocate pick lists via FEFO, synchronize POS stock deductions in sub-2s, calculate mathematical replenishment parameters, and manage store requisitions.")
    add_bullet(doc, "The system WILL NOT perform financial accounting general ledger balancing, process end-customer consumer retail payments, replace human physical forklift operations, or manufacture custom scanning hardware.")
    
    add_h2(doc, "12.2 Security, Integrity, and Audit Framework")
    add_p(doc, 
        "All data transmissions are encrypted using TLS 1.3. User passwords are encrypted using bcrypt / Argon2id hashing with unique salts. "
        "All inventory balance changes are enforced server-side inside atomic database transactions (ACID compliance) with row-level locking "
        "(SELECT ... FOR UPDATE) to guarantee that concurrent sales and picking operations never produce negative inventory balances. "
        "Every stock modification, write-off, and permission change is permanently logged in an immutable, tamper-evident audit ledger."
    )
    
    add_h2(doc, "12.3 Regulatory and Industry Compliance in Bangladesh")
    add_p(doc, 
        "RetailSync is explicitly architected to satisfy national legal and regulatory requirements in Bangladesh: "
        "1. Bangladesh Food Safety Act 2013: Requires strict traceability of food origins and mandates that expired food items be permanently "
        "segregated. RetailSync enforces automated quarantine locks that mechanically prevent any batch within 48 hours of expiration from being picked. "
        "2. BSTI Standards: Ensures compliance with statutory packaged food labeling and expiration date formats. "
        "3. Personal Data Protection Ordinance 2025 (Ordinance No. 61 of 2025): Ensures that employee and supplier personal contact data "
        "is encrypted, access-restricted, and strictly protected against unauthorized disclosure."
    )
    
    add_h1(doc, "13. Requirements Analysis Summary")
    add_h2(doc, "13.1 Core Functional Requirements (From Comprehensive Study)")
    add_p(doc, "The foundational functional requirements governing core supermarket operations are summarized below:")
    
    build_styled_table(doc,
        RETAILSYNC_CORE_FRS[0],
        RETAILSYNC_CORE_FRS[1:],
        col_widths=[0.8, 1.2, 3.8, 0.7],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER]
    )
    
    add_h2(doc, "13.2 Summary of Functional Requirements by Module (M-01 to M-11)")
    add_p(doc, 
        "The complete functional requirements taxonomy encompasses 11 modules and 78 detailed specifications prioritized using MoSCoW. "
        "(The exhaustive specification is presented in Appendix A):"
    )
    
    build_styled_table(doc,
        MODULE_SUMMARY[0],
        MODULE_SUMMARY[1:],
        col_widths=[1.8, 1.2, 2.5, 1.0],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "13.3 Non-Functional Requirements & Performance Metrics")
    add_p(doc, "The key quantifiable performance and security metrics established in the operational study are detailed below:")
    
    build_styled_table(doc,
        RETAILSYNC_CORE_NFRS[0],
        RETAILSYNC_CORE_NFRS[1:],
        col_widths=[1.0, 1.6, 3.9],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_p(doc, "The complete suite of fourteen Non-Functional Requirements (NFR-01 to NFR-14) governing enterprise reliability is presented below:")
    
    build_styled_table(doc,
        NFRS[0],
        NFRS[1:],
        col_widths=[0.8, 1.4, 3.4, 0.9],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "13.4 Feature-to-Problem Mapping")
    add_p(doc, "To verify complete problem coverage, every core RetailSync feature is explicitly linked back to the problems defined in Section 3:")
    
    feat_map = [
        ["Core System Feature", "Operational Real-Life Problem Resolved", "Delivered Business Value", "Problem Link"],
        ["Handheld Barcode Receiving", "Unchecked supplier errors, manual paper manifests", "Instant verification, zero PO mismatch", "P-01"],
        ["Directed Spatial Putaway", "Disorganized racks, long search times", "60% reduction in putaway and picking travel latency", "P-02"],
        ["Strict FEFO Expiry Allocation", "Severe food spoilage from picking newer stock first", "Elimination of expired stock dispatch, 65% waste cut", "P-03"],
        ["Continuous Cycle Counting", "Phantom inventory, undetected shrinkage and theft", "99.5% inventory record accuracy, early theft detection", "P-04"],
        ["Algorithmic EOQ & ROP Engine", "Overstocking capital lockup and weekend stockouts", "Balanced working capital, 80% reduction in stockouts", "P-05"],
        ["Consolidated Wave Picking", "Pickers walking aisles repeatedly for separate orders", "Doubled picking throughput, faster store dispatches", "P-06"],
        ["Supplier SLA Scorecards", "Zero visibility into supplier lead-time volatility", "Data-backed vendor negotiation and safety stock tuning", "P-07"],
        ["Store Requisition Portal", "Phone/email ordering, central warehouse stock silos", "Transparent stock allocation, zero duplicate orders", "P-08"],
        ["Immutable Audit Ledger", "Lack of accountability, food safety violations", "Complete chain-of-custody, BFSA compliance guarantee", "P-09"]
    ]
    
    build_styled_table(doc,
        feat_map[0],
        feat_map[1:],
        col_widths=[1.6, 2.0, 2.1, 0.8],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER]
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # PART E: HOW WE WILL BUILD IT
    # =========================================================================
    add_part_header(doc, "E", "How We Will Build It")
    
    add_h1(doc, "14. Feasibility Analysis")
    add_h2(doc, "14.1 5-Dimension Feasibility Assessment")
    add_p(doc, 
        "A rigorous feasibility assessment across five critical dimensions confirms that RetailSync can be delivered within the academic semester:"
    )
    add_bullet(doc, "Fully feasible utilizing mature, open-source enterprise stacks (Node.js/Next.js, Python/FastAPI, PostgreSQL 16 / MySQL, Docker). Scanning leverages ubiquitous standard barcode hardware and mobile browser APIs without requiring custom silicon or proprietary firmware.", bold_prefix="1. Technical Feasibility: ")
    add_bullet(doc, "Feasible within a 14-week academic semester by implementing a strict Agile Scrum methodology across six 2-week iterations. Core receiving, putaway, POS sync, and FEFO picking are delivered in early sprints, ensuring a working MVP is demonstrable by mid-term.", bold_prefix="2. Schedule Feasibility: ")
    add_bullet(doc, "Highly cost-effective. Built exclusively on free, open-source software, eliminating licensing fees. Development and testing utilize personal computers, smartphones, and student cloud hosting credits (Vercel, Supabase), achieving near-zero capital expenditure.", bold_prefix="3. Economic Feasibility: ")
    add_bullet(doc, "High user adoption potential. The mobile scanning UI is designed for simple, one-handed operation with high-contrast text and dual Bangla-English language support, minimizing training requirements for floor staff.", bold_prefix="4. Operational Feasibility: ")
    add_bullet(doc, "Fully compliant with the Bangladesh Food Safety Act 2013 and the Personal Data Protection Ordinance 2025. Uses synthetic inventory datasets for academic testing, avoiding sensitive real-world trade secrets.", bold_prefix="5. Legal & Ethical Feasibility: ")
    
    add_h2(doc, "14.2 What Is Implemented Now vs Future Scope Matrix")
    build_styled_table(doc,
        IMPLEMENTATION_SCOPE_MATRIX[0],
        IMPLEMENTATION_SCOPE_MATRIX[1:],
        col_widths=[1.5, 1.6, 1.8, 1.6],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h1(doc, "15. Development Methodology")
    add_h2(doc, "15.1 Comparative SDLC Methodology Evaluation Matrix")
    add_p(doc, 
        "Selecting the optimal Software Development Life Cycle (SDLC) is a foundational software engineering decision in SE-231. "
        "The candidate methodologies are rigorously evaluated below against the specific technical realities of a real-time retail WMS:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_SDLC_EVALUATION[0],
        RETAILSYNC_SDLC_EVALUATION[1:],
        col_widths=[1.3, 1.8, 2.3, 1.1],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER]
    )
    
    add_h2(doc, "15.2 In-Depth Justification for Agile Scrum with Evolutionary Prototyping")
    add_p(doc, 
        "Agile Scrum with Evolutionary Prototyping is conclusively selected based on four empirical software engineering realities:"
    )
    add_bullet(doc, 
        "Real-Time Concurrency Discovery: Transactional concurrency locks (SELECT ... FOR UPDATE) and sub-2.0s POS deduction latencies "
        "cannot be verified through abstract theoretical paperwork. Empirical stress testing across simulated multi-register checkouts in "
        "early sprints is essential to identify and eliminate database deadlocks.",
        bold_prefix="1. Empirical Concurrency Validation: "
    )
    add_bullet(doc, 
        "Early Working Core MVP: By the conclusion of Sprint 2 (Week 4), the team delivers a functioning relational database schema and "
        "working RESTful ingestion API, guaranteeing tangible software progress for academic milestones and supervisor reviews.",
        bold_prefix="2. Early Working Core Demonstration: "
    )
    add_bullet(doc, 
        "Continuous Usability & Barcode Feedback: Floor operator ergonomics (e.g. one-handed mobile scanning, high-contrast alerts in warehouse "
        "lighting, auditory scan feedback) require continuous hands-on user interface iterations rather than end-of-project testing.",
        bold_prefix="3. Rapid Ergonomic UI Adaptation: "
    )
    add_bullet(doc, 
        "Parallel Full-Stack Development: The decoupled 4-tier architecture allows backend API engineering and React frontend development "
        "to advance synchronously against pre-agreed OpenAPI/Swagger schema contracts without blocking dependencies.",
        bold_prefix="4. Decoupled Parallel Track Execution: "
    )
    
    add_h2(doc, "15.3 Capstone Sprints & Incremental Delivery Plan")
    add_p(doc, 
        "The project execution is mapped into six 2-week sprints matching the 14-week university semester timeline:"
    )
    
    build_styled_table(doc,
        AGILE_SPRINTS[0],
        AGILE_SPRINTS[1:],
        col_widths=[1.2, 1.4, 1.4, 2.5],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h1(doc, "16. Resource, Time and Budget Planning")
    add_h2(doc, "16.1 Development & Infrastructure Resources Planning")
    build_styled_table(doc,
        RESOURCES_PLAN[0],
        RESOURCES_PLAN[1:],
        col_widths=[1.5, 1.7, 2.1, 1.2],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "16.2 14-Week Capstone Implementation Roadmap")
    add_p(doc, 
        "The project schedule is rigorously mapped across 14 academic weeks according to the operational study roadmap:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_CAPSTONE_ROADMAP[0],
        RETAILSYNC_CAPSTONE_ROADMAP[1:],
        col_widths=[1.3, 2.7, 2.5],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "16.3 Budget Approach")
    add_p(doc, 
        "The project follows a frugal engineering approach: development runs entirely on student hardware and open-source stacks. "
        "Production demonstration will utilize free-tier cloud hosting (Vercel for frontend, Supabase/Render for managed PostgreSQL). "
        "Estimated out-of-pocket expenditure is limited to approximately 3,500 BDT for a handheld Bluetooth barcode scanner test unit."
    )
    
    add_h1(doc, "17. Comprehensive Risk Analysis and Proactive Mitigation")
    add_h2(doc, "17.1 Risk Management in the Local Retail Context")
    add_p(doc, "Key operational and technical risks specific to the Bangladeshi retail context are managed as follows:")
    
    build_styled_table(doc,
        RETAILSYNC_LOCAL_RISKS[0],
        RETAILSYNC_LOCAL_RISKS[1:],
        col_widths=[0.7, 1.8, 0.9, 3.1],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "17.2 Comprehensive Operational & Technical Risks (R-01 to R-12)")
    add_p(doc, 
        "Twelve specific operational, technical, and regulatory risks have been identified along with proactive mitigation strategies:"
    )
    
    build_styled_table(doc,
        RISKS[0],
        RISKS[1:],
        col_widths=[0.6, 2.1, 0.8, 0.8, 2.2],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    add_h2(doc, "17.3 Dual-Level Verification & Validation (V&V) Testing Strategy")
    add_p(doc, 
        "To satisfy the rigorous software engineering quality assurance requirements of SE-231, RetailSync enforces an exhaustive, "
        "two-tiered Verification and Validation (V&V) framework that pairs Black-Box functional evaluation with deep White-Box structural audits:"
    )
    
    build_styled_table(doc,
        RETAILSYNC_TESTING_STRATEGY[0],
        RETAILSYNC_TESTING_STRATEGY[1:],
        col_widths=[1.3, 1.4, 2.3, 1.5],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    doc.add_page_break()
    
    # =========================================================================
    # PART F: LOOKING AHEAD
    # =========================================================================
    add_part_header(doc, "F", "Looking Ahead")
    
    add_h1(doc, "18. Scalability, Multi-Store Architecture and Product Vision")
    add_p(doc, 
        "While the capstone prototype focuses on a central distribution warehouse serving 3 retail outlets, the underlying software "
        "architecture is engineered for enterprise-wide horizontal scalability:"
    )
    add_bullet(doc, "Single central warehouse supporting up to 5,000 SKUs and 3 branch stores.", bold_prefix="Stage 1 (Capstone MVP): ")
    add_bullet(doc, "Regional distribution centers in Chittagong and Bogra with inter-warehouse stock transfer routing.", bold_prefix="Stage 2 (Regional Expansion): ")
    add_bullet(doc, "Integration with external automated high-density pallet shuttles and pick-to-light cart systems.", bold_prefix="Stage 3 (Advanced Automation): ")
    add_bullet(doc, "E-grocery rapid dark-store fulfillment supporting sub-30-minute hyper-local order dispatch.", bold_prefix="Stage 4 (Omnichannel Retail): ")
    add_bullet(doc, "Nationwide supply chain network connecting FMCG manufacturers directly to retail supermarket shelves.", bold_prefix="Stage 5 (Ecosystem Integration): ")
    
    add_h2(doc, "18.1 Architectural Provisions for High-Volume Concurrency")
    add_p(doc, 
        "To handle heavy peak transaction volumes (such as morning inbound truck unloads and afternoon store dispatch rushes), "
        "the backend services are stateless and containerized via Docker, allowing horizontal scaling behind an Nginx load balancer. "
        "PostgreSQL utilizes connection pooling (PgBouncer), strategic B-Tree indexing on SKU and batch expiry dates, row-level locking "
        "(SELECT FOR UPDATE), and read-replicas to ensure read-heavy dashboard queries never lock write-heavy floor scanning transactions."
    )
    
    add_h2(doc, "18.2 Business Model Outline (Commercial SaaS Vision)")
    add_p(doc, 
        "Post-capstone commercialization follows a tiered B2B SaaS model: "
        "1. Starter Tier: Targeting independent medium-sized super shops with a single warehouse (monthly subscription of 15,000 BDT). "
        "2. Enterprise Tier: Targeting national chains (Shwapno, Agora, Meena Bazar) with multi-warehouse licensing, custom ERP API "
        "connectors, and on-premise dedicated server deployment with 24/7 SLA maintenance contracts."
    )
    
    add_h1(doc, "19. Expected Value, Financial Impact and Operational ROI")
    add_p(doc, "Deploying RetailSync delivers tangible, quantifiable value across four primary operational domains:")
    add_bullet(doc, "Eliminates paper tallying, reduces physical bin search latency by 60%, doubles picking line throughput from 40 to 95 lines/hour, and provides clear accountability.", bold_prefix="1. Warehouse Floor Productivity: ")
    add_bullet(doc, "Reduces perishable food expiry wastage by an estimated 65% through enforced FEFO batch routing, saving millions of BDT annually; cuts high-velocity stockouts by 80% using dynamic EOQ/ROP mathematical triggers.", bold_prefix="2. Supply Chain & Financial ROI: ")
    add_bullet(doc, "Ensures retail supermarket shelves remain consistently stocked with fresh goods, completely eliminating customer dissatisfaction from expired or out-of-stock items.", bold_prefix="3. Store Operations & Customer Trust: ")
    add_bullet(doc, "Demonstrates a complete, robust System Analysis & Design (SAD) implementation, bridging theoretical operations research formulas with modern cyber-physical web software engineering.", bold_prefix="4. Academic & Pedagogical Value: ")
    
    add_h1(doc, "20. Part 1 Conclusion and Roadmap to Part 2 System Design")
    add_p(doc, 
        "RetailSync moves beyond a simple CRUD application by tackling real-world operational bottlenecks: concurrency, batch expiration, "
        "and automated procurement. By grounding the project in a robust relational database architecture and strict auditability, "
        "it meets the highest standards for a System Analysis and Design capstone, offering a highly practical solution to a prominent "
        "challenge in the Bangladeshi retail sector."
    )
    add_p(doc, 
        "This project proposal (Part 1: Project Planning and Definition) establishes the rigorous operational, algorithmic, and architectural "
        "foundation for RetailSync. Grounded in empirical supermarket logistics data from Bangladesh, the proposal formulates nine critical "
        "operational problems (P-01 to P-09), establishes six measurable S.M.A.R.T. objectives (O-01 to O-06), defines 78 detailed functional "
        "requirements (FR-01 to FR-78), and outlines mathematical inventory optimization models that bridge the gap between physical warehouse "
        "floors, POS registers, and digital enterprise decision-making."
    )
    add_p(doc, 
        "Following academic committee evaluation and supervisor approval, the project will immediately transition into Part 2: System Architecture "
        "and Detailed Design, which will articulate Context Diagrams, Level-0 and Level-1 Data Flow Diagrams (DFDs), Entity-Relationship Diagrams (ERD), "
        "relational DDL database blueprints, and detailed UI/UX wireframes."
    )
    
    add_h1(doc, "References")
    references = [
        "1. Bangladesh Bureau of Statistics (BBS), 'Population and Housing Census 2022: National Report,' Statistics and Informatics Division, Ministry of Planning, Government of Bangladesh, Dhaka, 2023.",
        "2. LightCastle Partners, 'Modern Trade in Bangladesh: Navigating the Supermarket Landscape and Consumer Shift,' Industry Insights Report, Dhaka, 2024.",
        "3. Bangladesh Food Safety Authority (BFSA), 'Food Safety Act 2013 (Act No. 43 of 2013): Operational Compliance and Storage Guidelines,' Ministry of Food, Dhaka, Bangladesh.",
        "4. Legislative and Parliamentary Affairs Division, 'Personal Data Protection Ordinance 2025 (Ordinance No. 61 of 2025),' Ministry of Law, Justice and Parliamentary Affairs, Government of Bangladesh, Nov. 2025.",
        "5. M. Greasley, 'Operations Management,' 3rd ed., John Wiley & Sons, Chichester, UK, 2013 (Statistical Safety Stock Dual Variance Modeling).",
        "6. F. S. Hillier and G. J. Lieberman, 'Introduction to Operations Research,' 10th ed., McGraw-Hill Education, New York, NY, 2015 (Economic Order Quantity and Stochastic Inventory Formulations).",
        "7. J. P. Tompkins, J. A. White, Y. A. Bozer, and J. M. A. Tanchoco, 'Facilities Planning,' 4th ed., John Wiley & Sons, Hoboken, NJ, 2010 (Warehouse Spatial Layout and Wave Picking Optimizations).",
        "8. The Daily Star, 'Supermarkets expanding footprints as urban lifestyles evolve,' Business Analysis, Dhaka, Bangladesh, Oct. 2024.",
        "9. F. T. Liu, K. M. Ting, and Z. H. Zhou, 'Isolation Forest,' IEEE International Conference on Data Mining (ICDM), pp. 413-422, 2008 (Anomaly Detection for Inventory Shrinkage).",
        "10. GS1 General Specifications, 'Standard Barcoding Practices for Retail Grocery and FMCG Supply Chains,' Release 23.0, GS1 Global, 2023."
    ]
    for ref in references:
        add_p(doc, ref, space_after=3)
        
    doc.add_page_break()
    
    # =========================================================================
    # APPENDICES
    # =========================================================================
    add_part_header(doc, "G", "Appendices: Detailed System Specifications")
    
    add_h1(doc, "Appendix A: Detailed Functional Requirements Table (FR-01 to FR-78)")
    add_p(doc, 
        "Priority Key: M = Must Have (Capstone MVP Core), S = Should Have (Important Enhancement), C = Could Have (Future/Nice to Have). "
        "The Problem Link column cross-references the permanent problem identifiers established in Section 3 (P-01 to P-09)."
    )
    
    fr_headers = ["ID", "Module Name", "Detailed Functional Requirement Statement", "Priority", "Problem Link"]
    build_styled_table(doc,
        fr_headers,
        DETAILED_FUNCTIONAL_REQUIREMENTS,
        col_widths=[0.6, 1.2, 3.8, 0.5, 0.6],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER]
    )
    
    doc.add_page_break()
    
    add_h1(doc, "Appendix B: Complete Requirements Traceability Matrix")
    add_p(doc, 
        "This traceability matrix demonstrates complete, unbroken alignment between the real-world operational problems (Section 3), "
        "project objectives (Section 10), and the functional and non-functional requirements (Section 13 and Appendix A):"
    )
    
    trace_headers = ["Problem ID", "Problem Domain Description", "Addressed by Objectives", "Addressed by Functional Requirements", "Addressed by NFRs"]
    build_styled_table(doc,
        trace_headers,
        TRACEABILITY_MATRIX,
        col_widths=[0.8, 1.8, 0.8, 1.8, 1.3],
        alignment=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    doc.add_page_break()
    
    add_h1(doc, "Appendix C: Comprehensive Glossary of Terms (24 Industry Definitions)")
    add_p(doc, "Comprehensive domain definitions for technical, supply chain, and regulatory terminology utilized throughout RetailSync:")
    
    gloss_headers = ["Domain Term / Acronym", "Formal Technical & Operational Definition"]
    build_styled_table(doc,
        gloss_headers,
        GLOSSARY,
        col_widths=[1.8, 4.7],
        alignment=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    )
    
    primary_filename = "RetailSync_WMS_Comprehensive_Proposal.docx"
    doc.save(primary_filename)
    print(f"Primary Proposal successfully generated and saved to: {primary_filename}")
    
    # Also save as SHWMS_Capstone_Project_Proposal.docx for compatibility
    compat_filename = "SHWMS_Capstone_Project_Proposal.docx"
    doc.save(compat_filename)
    print(f"Compatibility Proposal successfully saved to: {compat_filename}")
    
    return primary_filename

if __name__ == "__main__":
    build_proposal_document()
