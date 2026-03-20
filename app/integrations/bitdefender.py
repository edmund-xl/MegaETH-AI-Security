from __future__ import annotations

import base64
import collections
import csv
import io
import re
import zipfile
from datetime import datetime, timezone
from typing import Any

import httpx

from app.models.event import RawEvent


BITDEFENDER_CACHE_TTL_SECONDS = 300
_BITDEFENDER_CACHE: dict[tuple[str, str, str], tuple[float, dict[str, Any]]] = {}


class BitdefenderClient:
    def __init__(self, api_key: str, base_url: str = "https://cloud.gravityzone.bitdefender.com/api/v1.0/jsonrpc") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _headers(self) -> dict[str, str]:
        token = base64.b64encode(f"{self.api_key}:".encode("utf-8")).decode("utf-8")
        return {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
        }

    def _post(self, service: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
        cache_key = (service, method, repr(sorted(params.items())))
        cached = _BITDEFENDER_CACHE.get(cache_key)
        now_ts = datetime.now(timezone.utc).timestamp()
        if cached and now_ts - cached[0] < BITDEFENDER_CACHE_TTL_SECONDS:
            return cached[1]
        url = f"{self.base_url}/{service}"
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": "1",
        }
        with httpx.Client(timeout=20.0) as client:
            response = client.post(url, headers=self._headers(), json=payload)
            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as exc:
                message = f"HTTP {exc.response.status_code} when calling {method}"
                try:
                    data = exc.response.json()
                    error = data.get("error") or {}
                    detail = error.get("data", {}).get("details") or error.get("message")
                    if detail:
                        message = f"{message}: {detail}"
                except Exception:
                    pass
                raise ValueError(message) from exc
            data = response.json()
        if "error" in data:
            error = data["error"]
            raise ValueError(error.get("data", {}).get("details") or error.get("message") or "Bitdefender API error")
        result = data.get("result", {})
        _BITDEFENDER_CACHE[cache_key] = (now_ts, result)
        return result

    def get_network_inventory(self, page: int = 1, per_page: int = 30) -> dict[str, Any]:
        return self._post("network", "getNetworkInventoryItems", {"page": page, "perPage": per_page})

    def get_all_network_inventory(self, per_page: int = 100) -> dict[str, Any]:
        first = self.get_network_inventory(page=1, per_page=per_page)
        pages = int(first.get("pagesCount", 1) or 1)
        items = list(first.get("items", []))
        total = int(first.get("total", len(items)) or len(items))
        for page in range(2, pages + 1):
            batch = self.get_network_inventory(page=page, per_page=per_page)
            items.extend(batch.get("items", []))
        return {
            "total": total,
            "page": 1,
            "perPage": per_page,
            "pagesCount": pages,
            "items": items,
        }

    def get_network_inventory_children(self, parent_id: str, page: int = 1, per_page: int = 100) -> dict[str, Any]:
        return self._post("network", "getNetworkInventoryItems", {"page": page, "perPage": per_page, "parentId": parent_id})

    def get_all_network_inventory_children(self, parent_id: str, per_page: int = 100) -> dict[str, Any]:
        first = self.get_network_inventory_children(parent_id, page=1, per_page=per_page)
        pages = int(first.get("pagesCount", 1) or 1)
        items = list(first.get("items", []))
        total = int(first.get("total", len(items)) or len(items))
        for page in range(2, pages + 1):
            batch = self.get_network_inventory_children(parent_id, page=page, per_page=per_page)
            items.extend(batch.get("items", []))
        return {
            "total": total,
            "page": 1,
            "perPage": per_page,
            "pagesCount": pages,
            "items": items,
        }

    def get_endpoints(self, page: int = 1, per_page: int = 100) -> dict[str, Any]:
        return self._post("network", "getEndpointsList", {"page": page, "perPage": per_page})

    def get_companies(self, page: int = 1, per_page: int = 100) -> dict[str, Any]:
        return self._post("network", "getCompaniesList", {"page": page, "perPage": per_page})

    def get_all_companies(self, per_page: int = 100) -> dict[str, Any]:
        first = self.get_companies(page=1, per_page=per_page)
        pages = int(first.get("pagesCount", 1) or 1)
        items = list(first.get("items", []))
        total = int(first.get("total", len(items)) or len(items))
        for page in range(2, pages + 1):
            batch = self.get_companies(page=page, per_page=per_page)
            items.extend(batch.get("items", []))
        return {
            "total": total,
            "page": 1,
            "perPage": per_page,
            "pagesCount": pages,
            "items": items,
        }

    def get_custom_groups(self) -> dict[str, Any]:
        return self._post("network", "getCustomGroupsList", {})

    def get_all_custom_groups(self) -> dict[str, Any]:
        result = self.get_custom_groups()
        if isinstance(result, list):
            items = list(result)
            return {
                "total": len(items),
                "items": items,
            }
        items = list(result.get("items", []))
        return {
            "total": int(result.get("total", len(items)) or len(items)),
            "items": items,
        }

    def get_managed_endpoint_details(self, endpoint_id: str) -> dict[str, Any]:
        return self._post("network", "getManagedEndpointDetails", {"endpointId": endpoint_id})

    def get_incidents(self, parent_id: str, page: int = 1, per_page: int = 500) -> dict[str, Any]:
        return self._post("incidents", "getIncidentsList", {"parentId": parent_id, "page": page, "perPage": per_page})

    def get_reports(self, page: int = 1, per_page: int = 30) -> dict[str, Any]:
        return self._post("reports", "getReportsList", {"page": page, "perPage": per_page})

    def get_report_download_links(self, report_id: str) -> dict[str, Any]:
        return self._post("reports", "getDownloadLinks", {"reportId": report_id})

    def download_report_zip(self, download_url: str) -> bytes:
        with httpx.Client(timeout=30.0, follow_redirects=True) as client:
            response = client.get(download_url, headers={"Authorization": self._headers()["Authorization"]})
            response.raise_for_status()
            return response.content

    def discover_company_id(self) -> str | None:
        inventory = self.get_network_inventory(page=1, per_page=30)
        items = inventory.get("items", [])
        for item in items:
            company_id = item.get("companyId")
            if company_id:
                return str(company_id)
        return None

    def discover_inventory_endpoints(self, company_id: str | None = None) -> dict[str, Any]:
        company = company_id or self.discover_company_id()
        if not company:
            return {"total": 0, "managed_total": 0, "unmanaged_total": 0, "items": [], "groups_traversed": 0}
        top = self.get_all_network_inventory_children(company, per_page=100)
        queue: collections.deque[str] = collections.deque()
        seen_groups: set[str] = set()
        endpoints: list[dict[str, Any]] = []
        for item in top.get("items", []):
            if item.get("type") == 4:
                group_id = str(item.get("id"))
                queue.append(group_id)
                seen_groups.add(group_id)
            elif item.get("type") == 5:
                endpoints.append(item)
        while queue:
            group_id = queue.popleft()
            result = self.get_all_network_inventory_children(group_id, per_page=100)
            for item in result.get("items", []):
                item_type = item.get("type")
                if item_type == 4:
                    child_group_id = str(item.get("id"))
                    if child_group_id not in seen_groups:
                        seen_groups.add(child_group_id)
                        queue.append(child_group_id)
                elif item_type == 5:
                    endpoints.append(item)
        unique: dict[str, dict[str, Any]] = {}
        managed_total = 0
        unmanaged_total = 0
        for item in endpoints:
            endpoint_id = str(item.get("id"))
            unique[endpoint_id] = item
        deduped = list(unique.values())
        for item in deduped:
            managed = bool(item.get("details", {}).get("isManaged"))
            if managed:
                managed_total += 1
            else:
                unmanaged_total += 1
        return {
            "total": len(deduped),
            "managed_total": managed_total,
            "unmanaged_total": unmanaged_total,
            "items": deduped,
            "groups_traversed": len(seen_groups),
        }

    def discover_inventory_hierarchy(self) -> dict[str, Any]:
        root = self.get_all_network_inventory(per_page=100)
        queue: collections.deque[str] = collections.deque()
        traversed_nodes: set[str] = set()
        groups: dict[str, dict[str, Any]] = {}
        companies: dict[str, dict[str, Any]] = {}
        endpoints: dict[str, dict[str, Any]] = {}
        node_types: collections.Counter[str] = collections.Counter()
        os_counter: collections.Counter[str] = collections.Counter()
        policy_counter: collections.Counter[str] = collections.Counter()

        def register_item(item: dict[str, Any]) -> None:
            item_type = int(item.get("type") or 0)
            item_id = str(item.get("id") or "")
            node_types[str(item_type)] += 1
            if item_type == 5 and item_id:
                endpoints[item_id] = item
                return
            if item_type in {2, 3} and item_id:
                companies[item_id] = item
            if item_type == 4 and item_id:
                groups[item_id] = item
            if item_id and item_type in {2, 3, 4} and item_id not in traversed_nodes:
                traversed_nodes.add(item_id)
                queue.append(item_id)

        for item in root.get("items", []):
            register_item(item)

        while queue:
            parent_id = queue.popleft()
            result = self.get_all_network_inventory_children(parent_id, per_page=100)
            for item in result.get("items", []):
                register_item(item)

        managed_total = 0
        unmanaged_total = 0
        for item in endpoints.values():
            details = item.get("details", {}) or {}
            managed = bool(details.get("isManaged"))
            if managed:
                managed_total += 1
            else:
                unmanaged_total += 1
            os_label = normalize_os_family(str(details.get("operatingSystemVersion") or "Unknown"))
            os_counter[os_label] += 1
            policy_name = str((details.get("policy") or {}).get("name") or "Unassigned")
            policy_counter[policy_name] += 1

        return {
            "total": len(endpoints),
            "managed_total": managed_total,
            "unmanaged_total": unmanaged_total,
            "items": list(endpoints.values()),
            "groups_traversed": len(groups),
            "companies_traversed": len(companies),
            "root_items_total": root.get("total", 0),
            "root_items": root.get("items", []),
            "groups": list(groups.values()),
            "companies": list(companies.values()),
            "node_type_counts": dict(node_types),
            "os_families": [{"name": name, "count": count} for name, count in os_counter.most_common(8)],
            "policies": [{"name": name, "count": count} for name, count in policy_counter.most_common(8)],
        }

    def test_connection(self) -> dict[str, Any]:
        inventory = self.get_network_inventory(page=1, per_page=30)
        company_id = self.discover_company_id()
        endpoints = self.get_endpoints(page=1, per_page=100)
        inventory_endpoints = self.discover_inventory_endpoints(company_id=company_id) if company_id else {"total": 0, "managed_total": 0, "unmanaged_total": 0, "items": [], "groups_traversed": 0}
        inventory_hierarchy = self.discover_inventory_hierarchy()
        managed_details_preview = []
        for item in inventory_hierarchy.get("items", [])[:30]:
            details = item.get("details", {})
            if details.get("isManaged"):
                try:
                    managed_details_preview.append(self.get_managed_endpoint_details(str(item.get("id"))))
                except ValueError:
                    pass
            if len(managed_details_preview) >= 5:
                break
        companies = None
        companies_error = None
        custom_groups = None
        custom_groups_error = None
        try:
            companies = self.get_all_companies(per_page=100)
        except ValueError as exc:
            companies_error = str(exc)
        try:
            custom_groups = self.get_all_custom_groups()
        except ValueError as exc:
            custom_groups_error = str(exc)
        reports = None
        reports_error = None
        report_download_links = None
        latest_report_summary = None
        try:
            reports = self.get_reports(page=1, per_page=30)
            report_items = reports.get("items", [])
            if report_items:
                report_id = report_items[0].get("id")
                if report_id:
                    try:
                        report_download_links = self.get_report_download_links(str(report_id))
                        download_url = report_download_links.get("lastInstanceUrl") or report_download_links.get("lastInstanceDownloadLink")
                        if download_url:
                            latest_report_summary = parse_report_zip_bundle(self.download_report_zip(str(download_url)))
                    except ValueError:
                        report_download_links = None
        except ValueError as exc:
            reports_error = str(exc)
        incidents = None
        incident_error = None
        if company_id:
            try:
                incidents = self.get_incidents(parent_id=company_id, page=1, per_page=500)
            except ValueError as exc:
                incident_error = str(exc)
        return {
            "base_url": self.base_url,
            "company_id": company_id,
            "inventory_total": inventory.get("total", 0),
            "endpoint_total": endpoints.get("total", 0),
            "inventory_endpoint_total": inventory_endpoints.get("total", 0),
            "inventory_managed_endpoint_total": inventory_endpoints.get("managed_total", 0),
            "inventory_unmanaged_endpoint_total": inventory_endpoints.get("unmanaged_total", 0),
            "inventory_groups_traversed": inventory_endpoints.get("groups_traversed", 0),
            "hierarchy_endpoint_total": inventory_hierarchy.get("total", 0),
            "hierarchy_managed_endpoint_total": inventory_hierarchy.get("managed_total", 0),
            "hierarchy_unmanaged_endpoint_total": inventory_hierarchy.get("unmanaged_total", 0),
            "hierarchy_groups_traversed": inventory_hierarchy.get("groups_traversed", 0),
            "hierarchy_companies_traversed": inventory_hierarchy.get("companies_traversed", 0),
            "hierarchy_os_families": inventory_hierarchy.get("os_families", []),
            "hierarchy_policies": inventory_hierarchy.get("policies", []),
            "companies_total": None if companies is None else companies.get("total", 0),
            "companies_error": companies_error,
            "custom_groups_total": None if custom_groups is None else custom_groups.get("total", 0),
            "custom_groups_error": custom_groups_error,
            "incident_total": None if incidents is None else incidents.get("total", 0),
            "incident_error": incident_error,
            "report_total": None if reports is None else reports.get("total", 0),
            "report_error": reports_error,
            "report_download_links": report_download_links,
            "latest_report_summary": None
            if latest_report_summary is None
            else {
                "row_count": latest_report_summary.get("row_count", 0),
                "unique_host_count": latest_report_summary.get("unique_host_count", 0),
                "malware_count": latest_report_summary.get("malware_count", 0),
                "attack_count": latest_report_summary.get("attack_count", 0),
                "blocked_count": latest_report_summary.get("blocked_count", 0),
                "top_hosts": latest_report_summary.get("top_hosts", []),
                "top_event_types": latest_report_summary.get("top_event_types", []),
                "top_modules": latest_report_summary.get("top_modules", []),
            },
            "inventory_items": items_preview(inventory.get("items", [])),
            "endpoint_items": items_preview(endpoints.get("items", [])),
            "inventory_endpoint_items": items_preview(inventory_endpoints.get("items", [])),
            "hierarchy_endpoint_items": items_preview(inventory_hierarchy.get("items", [])),
            "company_items": items_preview([] if companies is None else companies.get("items", [])),
            "custom_group_items": items_preview([] if custom_groups is None else custom_groups.get("items", [])),
            "managed_endpoint_details_preview": managed_endpoint_preview(managed_details_preview),
            "incident_items": items_preview([] if incidents is None else incidents.get("items", [])),
            "report_items": items_preview([] if reports is None else reports.get("items", [])),
        }


def normalize_os_family(value: str) -> str:
    text = value.strip()
    if not text:
        return "Unknown"
    lowered = text.lower()
    if "macos" in lowered:
        return "macOS"
    if "windows" in lowered:
        return "Windows"
    if "ubuntu" in lowered:
        return "Linux Ubuntu"
    if "linux" in lowered:
        return "Linux"
    cleaned = re.split(r"\\s+\\d", text, maxsplit=1)[0].strip()
    return cleaned or text


def items_preview(items: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    preview: list[dict[str, Any]] = []
    for item in items[:limit]:
        preview.append(
            {
                "id": item.get("id"),
                "name": item.get("name") or item.get("displayName") or item.get("machineName"),
                "type": item.get("type"),
                "companyId": item.get("companyId"),
                "severity": item.get("severity"),
                "status": item.get("status"),
                "createdAt": item.get("createdAt") or item.get("created"),
            }
        )
    return preview


def managed_endpoint_preview(items: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    preview: list[dict[str, Any]] = []
    for item in items[:limit]:
        preview.append(
            {
                "id": item.get("id"),
                "name": item.get("name"),
                "operatingSystem": item.get("operatingSystem"),
                "ip": item.get("ip"),
                "lastSeen": item.get("lastSeen"),
                "policy": (item.get("policy") or {}).get("name"),
                "managedWithBest": item.get("managedWithBest"),
                "riskScore": (item.get("riskScore") or {}).get("value"),
            }
        )
    return preview


def network_inventory_to_raw_event(inventory: dict[str, Any], company_id: str | None = None) -> RawEvent:
    return RawEvent(
        source_type="easm",
        event_hint="external_asset",
        timestamp=datetime.now(timezone.utc),
        asset_context={
            "asset_id": company_id or "bitdefender-network",
            "asset_name": "Bitdefender Network Inventory",
            "environment": "production",
            "criticality": 3,
            "source_file": "bitdefender-network-inventory",
            "integration": "bitdefender",
        },
        payload={
            "parser_profile": "bitdefender-network",
            "target": "bitdefender-network-inventory",
            "row_count": len(inventory.get("items", [])),
            "headers": ["id", "name", "type", "parentId", "companyId"],
            "rows": inventory.get("items", []),
        },
    )


def inventory_endpoints_to_raw_event(inventory_endpoints: dict[str, Any], company_id: str | None = None) -> RawEvent:
    return RawEvent(
        source_type="bitdefender",
        event_hint="endpoint_inventory",
        timestamp=datetime.now(timezone.utc),
        asset_context={
            "asset_id": company_id or "bitdefender-endpoint-inventory",
            "asset_name": "Bitdefender Endpoint Inventory",
            "environment": "production",
            "criticality": 3,
            "source_file": "bitdefender-endpoint-inventory",
            "integration": "bitdefender",
        },
        payload={
            "parser_profile": "bitdefender-endpoint-inventory",
            "target": "bitdefender-endpoint-inventory",
            "row_count": len(inventory_endpoints.get("items", [])),
            "managed_total": inventory_endpoints.get("managed_total", 0),
            "unmanaged_total": inventory_endpoints.get("unmanaged_total", 0),
            "groups_traversed": inventory_endpoints.get("groups_traversed", 0),
            "headers": ["name", "fqdn", "ip", "operatingSystemVersion", "isManaged", "policy"],
            "rows": inventory_endpoints.get("items", []),
        },
    )


def reports_catalog_to_raw_event(reports: dict[str, Any]) -> RawEvent:
    return RawEvent(
        source_type="bitdefender",
        event_hint="integration_catalog",
        timestamp=datetime.now(timezone.utc),
        asset_context={
            "asset_id": "bitdefender-reports",
            "asset_name": "Bitdefender Report Catalog",
            "environment": "production",
            "criticality": 3,
            "source_file": "bitdefender-report-catalog",
            "integration": "bitdefender",
        },
        payload={
            "parser_profile": "bitdefender-reports",
            "target": "bitdefender-report-catalog",
            "row_count": len(reports.get("items", [])),
            "headers": ["id", "name", "type", "occurrence"],
            "rows": reports.get("items", []),
            "content": " ".join(str(item.get("name", "")) for item in reports.get("items", [])),
        },
    )


def parse_report_zip_bundle(bundle: bytes) -> dict[str, Any]:
    with zipfile.ZipFile(io.BytesIO(bundle)) as archive:
        names = archive.namelist()
        csv_name = next((name for name in names if name.lower().endswith(".csv")), None)
        pdf_name = next((name for name in names if name.lower().endswith(".pdf")), None)
        if not csv_name:
            raise ValueError("The downloaded Bitdefender report bundle does not contain a CSV file.")
        text = archive.read(csv_name).decode("utf-8-sig", errors="replace")
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
    headers = reader.fieldnames or []
    content_fragments: list[str] = []
    host_names: set[str] = set()
    malware_count = 0
    blocked_count = 0
    attack_count = 0
    host_counter: collections.Counter[str] = collections.Counter()
    event_counter: collections.Counter[str] = collections.Counter()
    module_counter: collections.Counter[str] = collections.Counter()
    for row in rows[:20]:
        content_fragments.append(" ".join(str(value) for value in row.values() if value))
    for row in rows:
        if not isinstance(row, dict):
            continue
        host = str(row.get("端点名称") or row.get("endpoint_name") or row.get("端点 FQDN") or "").strip()
        if host:
            host_names.add(host)
            host_counter[host] += 1
        event_type = str(row.get("事件类型") or row.get("event_type") or "")
        module = str(row.get("模块") or row.get("module") or "")
        if event_type:
            event_counter[event_type] += 1
        if module:
            module_counter[module] += 1
        if "恶意软件检测" in event_type or "反恶意软件" in module:
            malware_count += 1
        if "阻止的网站" in event_type or "反钓鱼" in module:
            blocked_count += 1
        if "网络攻击" in event_type or "网络攻击防护" in module:
            attack_count += 1
    return {
        "zip_entries": names,
        "csv_name": csv_name,
        "pdf_name": pdf_name,
        "headers": headers,
        "rows": rows,
        "row_count": len(rows),
        "unique_host_count": len(host_names),
        "unique_hosts": sorted(host_names),
        "malware_count": malware_count,
        "blocked_count": blocked_count,
        "attack_count": attack_count,
        "top_hosts": [{"name": name, "count": count} for name, count in host_counter.most_common(5)],
        "top_event_types": [{"name": name, "count": count} for name, count in event_counter.most_common(5)],
        "top_modules": [{"name": name, "count": count} for name, count in module_counter.most_common(5)],
        "content": "\n".join(content_fragments),
    }


def latest_report_bundle_to_raw_event(report_meta: dict[str, Any], parsed_bundle: dict[str, Any]) -> RawEvent:
    report_name = str(report_meta.get("name") or "Bitdefender Latest Security Report")
    return RawEvent(
        source_type="endpoint",
        event_hint="endpoint_process",
        timestamp=datetime.now(timezone.utc),
        asset_context={
            "asset_id": str(report_meta.get("id") or "bitdefender-latest-report"),
            "asset_name": report_name,
            "environment": "production",
            "criticality": 4,
            "source_file": parsed_bundle.get("csv_name") or "bitdefender-latest-report.csv",
            "integration": "bitdefender",
        },
        payload={
            "parser_profile": "bitdefender-report-csv",
            "target": report_name,
            "report_name": report_name,
            "report_type": report_meta.get("type"),
            "occurrence": report_meta.get("occurrence"),
            "row_count": parsed_bundle.get("row_count", 0),
            "headers": parsed_bundle.get("headers", []),
            "rows": parsed_bundle.get("rows", []),
            "zip_entries": parsed_bundle.get("zip_entries", []),
            "content": parsed_bundle.get("content", ""),
        },
    )
