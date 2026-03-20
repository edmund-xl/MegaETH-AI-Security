from __future__ import annotations

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from app.appa.service import AppaService
from app.models.appa import AppaCreateEngagementRequest, AppaLaunchRunRequest


router = APIRouter(prefix="/appa", tags=["appa"])
service = AppaService()


@router.get("/overview")
def appa_overview():
    return service.overview()


@router.get("/dashboard")
def appa_dashboard():
    return service.dashboard()


@router.get("/engagements")
def appa_engagements():
    return service.list_engagements()


@router.post("/engagements")
def appa_create_engagement(payload: AppaCreateEngagementRequest):
    return service.create_engagement(payload)


@router.get("/runs")
def appa_runs():
    return service.list_runs()


@router.post("/runs")
def appa_launch_run(payload: AppaLaunchRunRequest):
    return service.launch_run(payload)


@router.get("/findings")
def appa_findings():
    return service.list_findings()


@router.get("/reports")
def appa_reports():
    return service.list_reports()


@router.get("/reports/latest/download", response_class=PlainTextResponse)
def appa_latest_report_download():
    return service.latest_report_markdown()
