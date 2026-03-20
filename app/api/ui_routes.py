from __future__ import annotations

from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.api.shared import STATIC_DIR


router = APIRouter()


@router.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")
