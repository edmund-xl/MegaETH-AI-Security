from __future__ import annotations

import os

from fastapi import APIRouter
from fastapi import HTTPException

from app.api.shared import pipeline
from app.integrations.bitdefender import (
    BitdefenderClient,
    inventory_endpoints_to_raw_event,
    latest_report_bundle_to_raw_event,
    parse_report_zip_bundle,
    reports_catalog_to_raw_event,
)
from app.integrations.whitebox_appsec import (
    MegaETHWhiteboxClient,
    whitebox_recon_to_raw_event,
    whitebox_report_to_raw_event,
    whitebox_validation_to_raw_event,
)
from app.models.event import EventEnvelope, RawEvent
from app.models.integration import BitdefenderConnectionRequest, WhiteboxAppSecRequest


router = APIRouter()


def _resolve_bitdefender_client(payload: BitdefenderConnectionRequest) -> BitdefenderClient:
    api_key = payload.api_key or os.getenv("BITDEFENDER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="Bitdefender API key is not configured on the server.")
    return BitdefenderClient(api_key=api_key, base_url=payload.base_url)


def _bitdefender_import_response(raw_event: RawEvent, extra: dict | None = None) -> dict:
    raw_event, memory = pipeline.memory.apply_raw_event_memory(raw_event)
    normalized = pipeline.normalizer.normalize(raw_event)
    normalized = pipeline.memory.enrich_normalized_event(normalized, memory)
    classification = pipeline.planner.classify(normalized)
    skills, reason = pipeline.planner.plan(normalized)
    envelope = EventEnvelope(
        raw_event=raw_event,
        normalized_event=normalized,
        classification=classification,
    )
    pipeline.history.save_raw_event(raw_event)
    pipeline.memory.learn_from_analysis(raw_event, normalized, skills)
    report = pipeline.run(normalized, envelope)
    payload = {
        "raw_event": raw_event.model_dump(mode="json"),
        "normalized_event": normalized.model_dump(mode="json"),
        "planner_preview": {
            "skills_to_execute": skills,
            "analysis_reason": reason,
            "classification": classification,
        },
        "report": report.model_dump(mode="json"),
    }
    if extra:
        payload.update(extra)
    return payload


def _resolve_whitebox_client() -> MegaETHWhiteboxClient:
    return MegaETHWhiteboxClient()


@router.post("/integrations/bitdefender/test")
def bitdefender_test(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    return client.test_connection()


@router.post("/integrations/bitdefender/network")
def bitdefender_network(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    inventory = client.get_network_inventory(page=1, per_page=30)
    endpoints = client.get_endpoints(page=1, per_page=100)
    company_id = client.discover_company_id()
    inventory_endpoints = (
        client.discover_inventory_endpoints(company_id=company_id)
        if company_id
        else {
            "total": 0,
            "managed_total": 0,
            "unmanaged_total": 0,
            "items": [],
            "groups_traversed": 0,
        }
    )
    inventory_hierarchy = client.discover_inventory_hierarchy()
    companies = None
    companies_error = None
    custom_groups = None
    custom_groups_error = None
    try:
        companies = client.get_all_companies(per_page=100)
    except ValueError as exc:
        companies_error = str(exc)
    try:
        custom_groups = client.get_all_custom_groups()
    except ValueError as exc:
        custom_groups_error = str(exc)
    latest_report_summary = None
    latest_report_error = None
    latest_report_meta = None
    try:
        reports = client.get_reports(page=1, per_page=30)
        report_items = reports.get("items", [])
        if report_items:
            latest_report_meta = report_items[0]
            report_id = latest_report_meta.get("id")
            if report_id:
                links = client.get_report_download_links(str(report_id))
                download_url = links.get("lastInstanceUrl") or links.get("lastInstanceDownloadLink")
                if download_url:
                    parsed = parse_report_zip_bundle(client.download_report_zip(str(download_url)))
                    latest_report_summary = {
                        "report_name": latest_report_meta.get("name"),
                        "row_count": parsed.get("row_count", 0),
                        "unique_host_count": parsed.get("unique_host_count", 0),
                        "malware_count": parsed.get("malware_count", 0),
                        "attack_count": parsed.get("attack_count", 0),
                        "blocked_count": parsed.get("blocked_count", 0),
                        "top_hosts": parsed.get("top_hosts", []),
                        "top_event_types": parsed.get("top_event_types", []),
                        "top_modules": parsed.get("top_modules", []),
                    }
    except ValueError as exc:
        latest_report_error = str(exc)
    managed_details_preview = []
    for item in inventory_hierarchy.get("items", [])[:30]:
        details = item.get("details", {})
        if details.get("isManaged"):
            try:
                managed_details_preview.append(
                    client.get_managed_endpoint_details(str(item.get("id")))
                )
            except ValueError:
                pass
        if len(managed_details_preview) >= 5:
            break
    return {
        "company_id": company_id,
        "inventory": inventory,
        "endpoints": endpoints,
        "inventory_endpoints": inventory_endpoints,
        "inventory_hierarchy": inventory_hierarchy,
        "hierarchy_policies": inventory_hierarchy.get("policies", []),
        "hierarchy_os_families": inventory_hierarchy.get("os_families", []),
        "companies": companies,
        "companies_error": companies_error,
        "custom_groups": custom_groups,
        "custom_groups_error": custom_groups_error,
        "latest_report_meta": latest_report_meta,
        "latest_report_summary": latest_report_summary,
        "latest_report_error": latest_report_error,
        "managed_endpoint_details_preview": managed_details_preview,
    }


@router.post("/integrations/bitdefender/incidents")
def bitdefender_incidents(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    parent_id = payload.parent_id or client.discover_company_id()
    if not parent_id:
        return {
            "company_id": None,
            "incidents": {"total": 0, "items": []},
            "error": "Unable to discover companyId from network inventory.",
        }
    try:
        incidents = client.get_incidents(parent_id=parent_id, page=1, per_page=500)
        return {"company_id": parent_id, "incidents": incidents, "error": None}
    except ValueError as exc:
        return {
            "company_id": parent_id,
            "incidents": {"total": 0, "items": []},
            "error": str(exc),
        }


@router.post("/integrations/bitdefender/reports")
def bitdefender_reports(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    try:
        reports = client.get_reports(page=1, per_page=30)
        return {"reports": reports, "error": None}
    except ValueError as exc:
        return {"reports": {"total": 0, "items": []}, "error": str(exc)}


@router.post("/integrations/bitdefender/reports/download-links")
def bitdefender_report_download_links(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    try:
        reports = client.get_reports(page=1, per_page=30)
        items = reports.get("items", [])
        if not items:
            return {
                "report": None,
                "download_links": None,
                "error": "No available reports in the current catalog.",
            }
        latest = items[0]
        report_id = latest.get("id")
        if not report_id:
            return {
                "report": latest,
                "download_links": None,
                "error": "The latest report does not expose a report id.",
            }
        links = client.get_report_download_links(str(report_id))
        download_url = links.get("lastInstanceUrl") or links.get(
            "lastInstanceDownloadLink"
        )
        summary = None
        if download_url:
            parsed = parse_report_zip_bundle(client.download_report_zip(str(download_url)))
            summary = {
                "row_count": parsed.get("row_count", 0),
                "unique_host_count": parsed.get("unique_host_count", 0),
                "malware_count": parsed.get("malware_count", 0),
                "attack_count": parsed.get("attack_count", 0),
                "blocked_count": parsed.get("blocked_count", 0),
                "top_hosts": parsed.get("top_hosts", []),
                "top_event_types": parsed.get("top_event_types", []),
                "top_modules": parsed.get("top_modules", []),
            }
        return {
            "report": latest,
            "download_links": links,
            "latest_report_summary": summary,
            "error": None,
        }
    except ValueError as exc:
        return {"report": None, "download_links": None, "error": str(exc)}


@router.post("/integrations/bitdefender/network/import")
def bitdefender_network_import(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    company_id = client.discover_company_id()
    inventory_hierarchy = client.discover_inventory_hierarchy()
    raw_event = inventory_endpoints_to_raw_event(
        inventory_hierarchy,
        company_id=company_id,
    )
    return _bitdefender_import_response(
        raw_event,
        {
            "company_id": company_id,
            "hierarchy_groups_traversed": inventory_hierarchy.get("groups_traversed", 0),
            "hierarchy_companies_traversed": inventory_hierarchy.get("companies_traversed", 0),
        },
    )


@router.post("/integrations/bitdefender/reports/import")
def bitdefender_reports_import(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    reports = client.get_reports(page=1, per_page=30)
    raw_event = reports_catalog_to_raw_event(reports)
    return _bitdefender_import_response(raw_event)


@router.post("/integrations/bitdefender/reports/latest/import")
def bitdefender_latest_report_import(payload: BitdefenderConnectionRequest):
    client = _resolve_bitdefender_client(payload)
    reports = client.get_reports(page=1, per_page=30)
    items = reports.get("items", [])
    if not items:
        return {
            "report_meta": None,
            "raw_event": None,
            "report": None,
            "error": "No available reports in the current catalog.",
        }
    latest = items[0]
    report_id = latest.get("id")
    if not report_id:
        return {
            "report_meta": latest,
            "raw_event": None,
            "report": None,
            "error": "The latest report does not expose a report id.",
        }
    links = client.get_report_download_links(str(report_id))
    download_url = links.get("lastInstanceUrl") or links.get("lastInstanceDownloadLink")
    if not download_url:
        return {
            "report_meta": latest,
            "raw_event": None,
            "report": None,
            "error": "No downloadable latest report instance is available.",
        }
    bundle = client.download_report_zip(str(download_url))
    parsed = parse_report_zip_bundle(bundle)
    raw_event = latest_report_bundle_to_raw_event(latest, parsed)
    return _bitdefender_import_response(
        raw_event,
        {
            "report_meta": latest,
            "download_links": links,
            "bundle_summary": {
                "csv_name": parsed.get("csv_name"),
                "pdf_name": parsed.get("pdf_name"),
                "row_count": parsed.get("row_count"),
                "headers": parsed.get("headers"),
            },
            "error": None,
        },
    )


@router.post("/integrations/whitebox/test")
def whitebox_test(payload: WhiteboxAppSecRequest):
    client = _resolve_whitebox_client()
    return client.test_connection(repo_path=payload.repo_path, target_url=payload.target_url)


@router.post("/integrations/whitebox/recon")
def whitebox_recon(payload: WhiteboxAppSecRequest):
    client = _resolve_whitebox_client()
    result = client.collect_recon(repo_path=payload.repo_path, target_url=payload.target_url, mode=payload.mode)
    return {
        "integration_summary": result,
        "import_ready": True,
    }


@router.post("/integrations/whitebox/recon/import")
def whitebox_recon_import(payload: WhiteboxAppSecRequest):
    client = _resolve_whitebox_client()
    result = client.collect_recon(repo_path=payload.repo_path, target_url=payload.target_url, mode=payload.mode)
    raw_event = whitebox_recon_to_raw_event(result)
    return _bitdefender_import_response(raw_event, {"integration_summary": result})


@router.post("/integrations/whitebox/validate")
def whitebox_validate(payload: WhiteboxAppSecRequest):
    client = _resolve_whitebox_client()
    result = client.collect_validation(repo_path=payload.repo_path, target_url=payload.target_url, mode=payload.mode)
    return {
        "integration_summary": result,
        "import_ready": True,
    }


@router.post("/integrations/whitebox/validate/import")
def whitebox_validate_import(payload: WhiteboxAppSecRequest):
    client = _resolve_whitebox_client()
    result = client.collect_validation(repo_path=payload.repo_path, target_url=payload.target_url, mode=payload.mode)
    raw_event = whitebox_validation_to_raw_event(result)
    return _bitdefender_import_response(raw_event, {"integration_summary": result})


@router.post("/integrations/whitebox/report/import")
def whitebox_report_import(payload: WhiteboxAppSecRequest):
    client = _resolve_whitebox_client()
    result = client.synthesize_report(
        repo_path=payload.repo_path,
        target_url=payload.target_url,
        config_path=payload.config_path,
        mode=payload.mode,
    )
    raw_event = whitebox_report_to_raw_event(result)
    return _bitdefender_import_response(raw_event, {"integration_summary": result})
