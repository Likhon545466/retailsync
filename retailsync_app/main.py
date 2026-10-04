import os
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from retailsync_app.config import settings
from retailsync_app.database import engine, Base, SessionLocal, get_db
from retailsync_app import models, auth
from retailsync_app.seed_data import seed_database
from retailsync_app.api import (
    auth_routes,
    pos_routes,
    inbound_routes,
    putaway_routes,
    procurement_routes,
    warehouse_routes,
)

# Initialize database schema tables
Base.metadata.create_all(bind=engine)

# Seed initial database records
with SessionLocal() as db:
    seed_database(db)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Centralized Super Shop Warehouse Management System. Developed for Daffodil International University (DIU).",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Mount Static Assets
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "static")), name="static")

assets_dir = os.path.join(root_dir, "assets")
if os.path.exists(assets_dir):
    app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

# Jinja2 Templates
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

# Register API Routers under /api/v1
api_prefix = "/api/v1"
app.include_router(auth_routes.router, prefix=api_prefix)
app.include_router(pos_routes.router, prefix=api_prefix)
app.include_router(inbound_routes.router, prefix=api_prefix)
app.include_router(putaway_routes.router, prefix=api_prefix)
app.include_router(procurement_routes.router, prefix=api_prefix)
app.include_router(warehouse_routes.router, prefix=api_prefix)


# ==============================================================================
# HTML Web Application Routes (Jinja2 Rendered)
# ==============================================================================

@app.get("/", response_class=HTMLResponse)
def index_route(request: Request):
    return RedirectResponse(url="/dashboard")

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_view(request: Request, user: models.User = Depends(auth.get_current_user_optional), db: Session = Depends(get_db)):
    stats = warehouse_routes.get_operational_stats(db)
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"active_page": "dashboard", "current_user": user, "stats": stats}
    )

@app.get("/pos", response_class=HTMLResponse)
def pos_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    return templates.TemplateResponse(
        request=request,
        name="pos.html",
        context={"active_page": "pos", "current_user": user}
    )

@app.get("/inbound", response_class=HTMLResponse)
def inbound_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    return templates.TemplateResponse(
        request=request,
        name="inbound.html",
        context={"active_page": "inbound", "current_user": user}
    )

@app.get("/putaway", response_class=HTMLResponse)
def putaway_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    return templates.TemplateResponse(
        request=request,
        name="putaway.html",
        context={"active_page": "putaway", "current_user": user}
    )

@app.get("/warehouse", response_class=HTMLResponse)
def warehouse_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    return templates.TemplateResponse(
        request=request,
        name="warehouse.html",
        context={"active_page": "warehouse", "current_user": user}
    )

@app.get("/procurement", response_class=HTMLResponse)
def procurement_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    return templates.TemplateResponse(
        request=request,
        name="procurement.html",
        context={"active_page": "procurement", "current_user": user}
    )

@app.get("/audits", response_class=HTMLResponse)
def audits_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    return templates.TemplateResponse(
        request=request,
        name="audits.html",
        context={"active_page": "audits", "current_user": user}
    )

@app.get("/showcase", response_class=HTMLResponse)
def showcase_view():
    showcase_path = os.path.join(root_dir, "proposal", "interactive_showcase.html")
    if os.path.exists(showcase_path):
        return FileResponse(showcase_path)
    return HTMLResponse("<h1>Proposal Showcase</h1><p>File not found.</p>", status_code=404)

@app.get("/slides", response_class=HTMLResponse)
@app.get("/presentation", response_class=HTMLResponse)
@app.get("/presentation_deck.html", response_class=HTMLResponse)
def slides_view():
    slides_path = os.path.join(root_dir, "proposal", "presentation_deck.html")
    if os.path.exists(slides_path):
        return FileResponse(slides_path)
    return HTMLResponse("<h1>Defense Slides</h1><p>File not found.</p>", status_code=404)

# ==============================================================================
# Official Document Downloads & View Endpoints
# ==============================================================================

# --- 1. Capstone Project Proposal (PDF) ---
@app.get("/proposal", response_class=FileResponse)
@app.get("/proposal/pdf", response_class=FileResponse)
@app.get("/proposal.pdf", response_class=FileResponse)
@app.get("/RetailSync_WMS_Project_Proposal.pdf", response_class=FileResponse)
def proposal_pdf_download():
    pdf_path = os.path.join(root_dir, "proposal", "RetailSync_WMS_Project_Proposal.pdf")
    if os.path.exists(pdf_path):
        return FileResponse(
            pdf_path,
            filename="RetailSync_WMS_Project_Proposal.pdf",
            media_type="application/pdf"
        )
    return HTMLResponse("<h1>Proposal PDF Not Found</h1>", status_code=404)

# --- 2. Capstone Project Proposal (Word .docx) ---
@app.get("/proposal/docx", response_class=FileResponse)
@app.get("/proposal.docx", response_class=FileResponse)
@app.get("/RetailSync_WMS_Project_Proposal.docx", response_class=FileResponse)
def proposal_docx_download():
    docx_path = os.path.join(root_dir, "proposal", "RetailSync_WMS_Project_Proposal.docx")
    if os.path.exists(docx_path):
        return FileResponse(
            docx_path,
            filename="RetailSync_WMS_Project_Proposal.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    return HTMLResponse("<h1>Proposal DOCX Not Found</h1>", status_code=404)

# --- 3. PowerPoint Slide Deck (.pptx) ---
@app.get("/deck", response_class=FileResponse)
@app.get("/deck/pptx", response_class=FileResponse)
@app.get("/slides/pptx", response_class=FileResponse)
@app.get("/RetailSync_Capstone_Proposal_Defense_Deck.pptx", response_class=FileResponse)
def deck_download():
    deck_path = os.path.join(root_dir, "proposal", "RetailSync_Capstone_Proposal_Defense_Deck.pptx")
    if os.path.exists(deck_path):
        return FileResponse(
            deck_path,
            filename="RetailSync_Capstone_Proposal_Defense_Deck.pptx",
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
    return HTMLResponse("<h1>Deck Not Found</h1>", status_code=404)

# --- 4. 70-Page Master Technical Engineering Specification Suite (PDF) ---
@app.get("/engineering-suite", response_class=FileResponse)
@app.get("/engineering-suite/pdf", response_class=FileResponse)
@app.get("/engineering-suite.pdf", response_class=FileResponse)
@app.get("/docs/master-suite.pdf", response_class=FileResponse)
@app.get("/RetailSync_Master_Engineering_Suite.pdf", response_class=FileResponse)
def engineering_suite_pdf_download():
    pdf_path = os.path.join(root_dir, "docs", "RetailSync_Master_Engineering_Suite.pdf")
    if os.path.exists(pdf_path):
        return FileResponse(
            pdf_path,
            filename="RetailSync_Master_Engineering_Suite.pdf",
            media_type="application/pdf"
        )
    return HTMLResponse("<h1>Master Engineering Suite PDF Not Found</h1>", status_code=404)

# --- 5. 70-Page Master Technical Engineering Specification Suite (Word .docx) ---
@app.get("/engineering-suite/docx", response_class=FileResponse)
@app.get("/engineering-suite.docx", response_class=FileResponse)
@app.get("/docs/master-suite.docx", response_class=FileResponse)
@app.get("/RetailSync_Master_Engineering_Suite.docx", response_class=FileResponse)
def engineering_suite_docx_download():
    docx_path = os.path.join(root_dir, "docs", "RetailSync_Master_Engineering_Suite.docx")
    if os.path.exists(docx_path):
        return FileResponse(
            docx_path,
            filename="RetailSync_Master_Engineering_Suite.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    return HTMLResponse("<h1>Master Engineering Suite DOCX Not Found</h1>", status_code=404)

# --- 6. Master Technical Stack, Architecture Decisions & Viva Defense Guide (Interactive Web Page) ---
@app.get("/technical-guide", response_class=HTMLResponse)
@app.get("/tech-guide", response_class=HTMLResponse)
@app.get("/viva", response_class=HTMLResponse)
@app.get("/viva-guide", response_class=HTMLResponse)
def technical_guide_view(request: Request, user: models.User = Depends(auth.get_current_user_optional)):
    guide_path = os.path.join(root_dir, "TECHNICAL_STACK_AND_DEFENSE_GUIDE.md")
    content = ""
    if os.path.exists(guide_path):
        with open(guide_path, "r", encoding="utf-8") as f:
            content = f.read()
    return templates.TemplateResponse(
        request=request,
        name="technical_guide.html",
        context={
            "active_page": "technical_guide",
            "current_user": user,
            "markdown_content": content
        }
    )

# --- 6b. Raw Markdown File Download for Offline/Editors ---
@app.get("/technical-guide/raw", response_class=FileResponse)
@app.get("/technical-guide/download", response_class=FileResponse)
@app.get("/technical-guide.md", response_class=FileResponse)
@app.get("/TECHNICAL_STACK_AND_DEFENSE_GUIDE.md", response_class=FileResponse)
def technical_guide_raw_download():
    guide_path = os.path.join(root_dir, "TECHNICAL_STACK_AND_DEFENSE_GUIDE.md")
    if os.path.exists(guide_path):
        return FileResponse(
            guide_path,
            filename="TECHNICAL_STACK_AND_DEFENSE_GUIDE.md",
            media_type="text/markdown; charset=utf-8"
        )
    return HTMLResponse("<h1>Technical Guide Not Found</h1>", status_code=404)

# --- 7. Complete Team Sharing Dossier Archive (ZIP) ---
@app.get("/team-pack", response_class=FileResponse)
@app.get("/team-pack.zip", response_class=FileResponse)
@app.get("/RetailSync_Team_Sharing_Pack.zip", response_class=FileResponse)
def team_pack_download():
    zip_path = os.path.join(root_dir, "RetailSync_Team_Sharing_Pack.zip")
    if os.path.exists(zip_path):
        return FileResponse(
            zip_path,
            filename="RetailSync_Team_Sharing_Pack.zip",
            media_type="application/zip"
        )
    return HTMLResponse("<h1>Team Sharing Pack Not Found</h1>", status_code=404)

@app.get("/api")
def api_root():
    return {
        "status": "online",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "institution": settings.INSTITUTION,
        "team": settings.TEAM_MEMBERS,
        "documentation": "/api/docs",
        "routes": {
            "dashboard": "/dashboard",
            "pos": "/pos",
            "inbound": "/inbound",
            "putaway": "/putaway",
            "warehouse": "/warehouse",
            "procurement": "/procurement",
            "audits": "/audits",
            "showcase": "/showcase",
            "slides": "/slides",
            "deck_pptx": "/deck",
            "proposal_pdf": "/proposal/pdf",
            "proposal_docx": "/proposal/docx",
            "master_engineering_suite_pdf": "/engineering-suite/pdf",
            "master_engineering_suite_docx": "/engineering-suite/docx",
            "technical_defense_guide": "/technical-guide",
            "team_pack_zip": "/team-pack.zip"
        }
    }


