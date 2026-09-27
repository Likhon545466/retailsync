import os
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
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

