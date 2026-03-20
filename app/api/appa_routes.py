from __future__ import annotations

from fastapi import APIRouter

from app.appa.service import AppaService


router = APIRouter(prefix="/appa", tags=["appa"])
service = AppaService()


@router.get("/overview")
def appa_overview():
    return service.overview()
