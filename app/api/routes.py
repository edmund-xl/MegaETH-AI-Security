from __future__ import annotations

# Security-log-analysis mainline route composition.

from fastapi import APIRouter

from app.api.core_routes import router as core_router
from app.api.integration_routes import router as integration_router
from app.api.ui_routes import router as ui_router
from app.integrations.bitdefender import BitdefenderClient, parse_report_zip_bundle


router = APIRouter()
router.include_router(core_router)
router.include_router(integration_router)
router.include_router(ui_router)
