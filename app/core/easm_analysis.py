from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any

from app.models.event import RawEvent


DOMAIN_RE = re.compile(r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b", re.IGNORECASE)
IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)
PORT_RE = re.compile(r"\b\d{1,5}\b")

DATASET_KEYWORDS = {
    "service": ("port", "protocol", "service", "banner", "cve"),
    "dns": ("dns", "record", "cname", "ns", "resolver", "ttl"),
    "certificate": ("certificate", "issuer", "san", "not_before", "not_after", "common_name"),
    "asn": ("asn", "autonomous", "prefix", "netblock", "organization"),
    "ip_range": ("cidr", "netblock", "ip range", "address range", "prefix"),
}

PROVIDER_PATTERNS = {
    "CloudFlare Inc": ("cloudflare", "cf-"),
    "Google LLC": ("google", "gcp", "google cloud"),
    "Amazon.com Inc.": ("amazon", "aws", "vercel"),
    "Limestone Networks Inc.": ("limestone",),
    "Vercel": ("vercel", "vercel-dns"),
}


@dataclass
class AssetAggregate:
    asset: str
    layers: set[str] = field(default_factory=set)
    providers: set[str] = field(default_factory=set)
    ips: set[str] = field(default_factory=set)
    ports: set[int] = field(default_factory=set)
    cves: set[str] = field(default_factory=set)
    dns_targets: set[str] = field(default_factory=set)
    ns_records: set[str] = field(default_factory=set)
    cert_signals: set[str] = field(default_factory=set)
    cert_statuses: set[str] = field(default_factory=set)
    evidence: list[dict[str, Any]] = field(default_factory=list)


def _clean_header(value: Any) -> str:
    return str(value or "").strip().lower().replace("_", " ")


def _clean_value(value: Any) -> str:
    return str(value or "").strip()


def _extract_domains(value: Any) -> list[str]:
    return sorted({match.lower() for match in DOMAIN_RE.findall(_clean_value(value))})


def _extract_ips(value: Any) -> list[str]:
    return sorted({match for match in IP_RE.findall(_clean_value(value))})


def _extract_ports(value: Any) -> list[int]:
    ports: list[int] = []
    for match in PORT_RE.findall(_clean_value(value)):
        port = int(match)
        if 0 < port <= 65535:
            ports.append(port)
    return sorted(set(ports))


def _extract_cves(value: Any) -> list[str]:
    return sorted({match.upper() for match in CVE_RE.findall(_clean_value(value))})


def _canonical_provider(value: str) -> str:
    lowered = value.lower()
    for provider, patterns in PROVIDER_PATTERNS.items():
        if any(pattern in lowered for pattern in patterns):
            return provider
    return value.strip()


def _collect_providers(row: dict[str, Any]) -> set[str]:
    providers: set[str] = set()
    for key, value in row.items():
        header = _clean_header(key)
        if any(token in header for token in ("provider", "org", "organization", "company", "vendor", "hosting", "cdn")):
            raw = _clean_value(value)
            if raw:
                providers.add(_canonical_provider(raw))
        else:
            lowered = _clean_value(value).lower()
            for provider, patterns in PROVIDER_PATTERNS.items():
                if any(pattern in lowered for pattern in patterns):
                    providers.add(provider)
    return providers


def detect_easm_dataset(filename: str, headers: list[str], rows: list[dict[str, Any]]) -> str:
    lowered_name = filename.lower()
    header_blob = " ".join(_clean_header(header) for header in headers)
    preview_blob = " ".join(_clean_value(value).lower() for row in rows[:5] for value in row.values())
    corpus = f"{lowered_name} {header_blob} {preview_blob}"
    if any(token in corpus for token in ("证书id", "颁发者名称", "证书过期状态", "工件类型 证书", "证书 ")):
        return "certificate"
    if any(token in corpus for token in ("dns记录类型", "域名服务器", "cname", "邮件服务器", "工件类型 dns记录")):
        return "dns"
    if any(token in corpus for token in ("asn 国家", "asn 运营商", "工件类型 asn 报告")):
        return "asn"
    if any(token in corpus for token in ("ip地址段", "工件类型 ip地址段", "相关 ip")) and "端口" not in corpus:
        return "ip_range"
    if any(token in corpus for token in ("端口", "协议", "cve", "工件类型 服务")):
        return "service"
    for dataset, keywords in (
        ("certificate", DATASET_KEYWORDS["certificate"]),
        ("dns", DATASET_KEYWORDS["dns"]),
        ("asn", DATASET_KEYWORDS["asn"]),
        ("ip_range", DATASET_KEYWORDS["ip_range"]),
        ("service", DATASET_KEYWORDS["service"]),
    ):
        if any(keyword in corpus for keyword in keywords):
            return dataset
    return "service"


def _base_domain(domain: str) -> str:
    parts = domain.lower().split(".")
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return domain.lower()


def _collect_target_roots(raw_events: list[RawEvent]) -> set[str]:
    roots: set[str] = set()
    for event in raw_events:
        rows = [row for row in event.payload.get("rows", []) if isinstance(row, dict)]
        for row in rows:
            for key, value in row.items():
                header = _clean_header(key)
                if "相关域名" in header or "related domain" in header:
                    for domain in _extract_domains(value):
                        roots.add(_base_domain(domain))
    return roots


def _row_assets(row: dict[str, Any], dataset_type: str, target_roots: set[str]) -> set[str]:
    assets: set[str] = set()
    for key, value in row.items():
        header = _clean_header(key)
        text = _clean_value(value)
        if not text:
            continue
        if dataset_type == "certificate" and header in {"issuer", "issuer cn", "颁发者名称"}:
            continue
        if any(token in header for token in ("asset", "domain", "host", "fqdn", "name", "common name", "san", "url", "subdomain", "工件名称", "相关域名")):
            assets.update(_extract_domains(text))
        elif "://" in text:
            assets.update(_extract_domains(text))
    if target_roots:
        assets = {asset for asset in assets if _base_domain(asset) in target_roots}
    return {asset for asset in assets if "." in asset}


def _record_evidence(bucket: AssetAggregate, dataset_type: str, row: dict[str, Any]) -> None:
    compact = {str(key): _clean_value(value) for key, value in row.items() if _clean_value(value)}
    if compact:
        bucket.evidence.append({"layer": dataset_type, "row": compact})


def build_easm_composite_payload(raw_events: list[RawEvent]) -> dict[str, Any]:
    asset_map: dict[str, AssetAggregate] = {}
    layer_counts: Counter[str] = Counter()
    normalized_records: list[dict[str, Any]] = []
    target_roots = _collect_target_roots(raw_events)

    for event in raw_events:
        payload = event.payload
        rows = [row for row in payload.get("rows", []) if isinstance(row, dict)]
        headers = [str(header) for header in payload.get("headers", [])]
        dataset_type = detect_easm_dataset(str(payload.get("filename") or event.asset_context.get("source_file") or ""), headers, rows)
        layer_counts[dataset_type] += 1
        for row in rows:
            assets = _row_assets(row, dataset_type, target_roots)
            ips = {ip for value in row.values() for ip in _extract_ips(value)}
            ports = {
                port
                for key, value in row.items()
                if "port" in _clean_header(key)
                for port in _extract_ports(value)
            }
            cves = {cve for value in row.values() for cve in _extract_cves(value)}
            providers = _collect_providers(row)
            if not assets:
                continue
            normalized_records.append(
                {
                    "dataset_type": dataset_type,
                    "assets": sorted(assets),
                    "ips": sorted(ips),
                    "ports": sorted(ports),
                    "providers": sorted(providers),
                    "cves": sorted(cves),
                }
            )
            for asset in assets:
                bucket = asset_map.setdefault(asset, AssetAggregate(asset=asset))
                bucket.layers.add(dataset_type)
                bucket.ips.update(ips)
                bucket.ports.update(ports)
                bucket.cves.update(cves)
                bucket.providers.update(providers)
                if dataset_type == "dns":
                    record_type = _clean_value(row.get("record_type") or row.get("type") or row.get("dns_type")).upper()
                    for key, value in row.items():
                        header = _clean_header(key)
                        text = _clean_value(value)
                        if "ns" in header or (record_type == "NS" and any(token in header for token in ("value", "target", "content"))):
                            bucket.ns_records.update(_extract_domains(text))
                        elif any(token in header for token in ("target", "value", "content", "cname")):
                            bucket.dns_targets.update(_extract_domains(text))
                if dataset_type == "certificate":
                    joined = " ".join(_clean_value(value) for value in row.values()).lower()
                    if "cloudflare origin" in joined:
                        bucket.cert_signals.add("Cloudflare Origin Certificate")
                    if "let's encrypt" in joined or "letsencrypt" in joined:
                        bucket.cert_signals.add("Let's Encrypt")
                    if any(token in joined for token in ("expired", "过期")):
                        bucket.cert_statuses.add("expired")
                    elif joined:
                        bucket.cert_statuses.add("active")
                _record_evidence(bucket, dataset_type, row)

    asset_assessments = [_build_asset_assessment(item) for item in sorted(asset_map.values(), key=lambda value: value.asset)]
    severity_distribution = Counter(str(item["scores"]["severity"]) for item in asset_assessments)
    surface_summary = {
        "asset_count": len(asset_assessments),
        "layer_counts": dict(layer_counts),
        "severity_distribution": dict(severity_distribution),
        "high_severity_assets": [item["asset"] for item in asset_assessments if item["scores"]["severity"] in {"High", "Critical"}][:10],
        "top_tags": _top_tags(asset_assessments),
    }
    layer_findings = _layer_findings(asset_assessments, layer_counts)
    training_samples = [_training_sample(item) for item in asset_assessments]
    asset_graph = {
        "assets": [
            {
                "asset": item["asset"],
                "severity": item["scores"]["severity"],
                "providers": item.get("providers", []),
                "ips": item.get("ips", []),
                "tags": item["tags"],
            }
            for item in asset_assessments
        ]
    }
    return {
        "normalized_records": normalized_records,
        "asset_graph": asset_graph,
        "layer_findings": layer_findings,
        "asset_assessments": asset_assessments,
        "surface_summary": surface_summary,
        "training_samples": training_samples,
        "row_count": sum(len(event.payload.get("rows", [])) for event in raw_events),
    }


def _top_tags(asset_assessments: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counter: Counter[str] = Counter()
    for assessment in asset_assessments:
        counter.update(assessment.get("tags", []))
    return [{"tag": tag, "count": count} for tag, count in counter.most_common(8)]


def _layer_findings(asset_assessments: list[dict[str, Any]], layer_counts: Counter[str]) -> list[str]:
    findings: list[str] = []
    if layer_counts.get("service"):
        findings.append(f"服务/端口层共接入 {layer_counts['service']} 份数据，能够识别公网服务、协议、端口与 CVE 线索。")
    if layer_counts.get("dns"):
        findings.append(f"DNS 层共接入 {layer_counts['dns']} 份数据，可用于识别委派、CNAME 与第三方边界。")
    if layer_counts.get("certificate"):
        findings.append(f"证书层共接入 {layer_counts['certificate']} 份数据，可用于识别 Origin Certificate、历史资产与证书生命周期信号。")
    high_assets = [item["asset"] for item in asset_assessments if item["scores"]["severity"] in {"High", "Critical"}]
    if high_assets:
        findings.append(f"当前至少有 {len(high_assets)} 个资产被评估为高风险，其中包括 {', '.join(high_assets[:5])}。")
    historical_assets = [item["asset"] for item in asset_assessments if "historical_asset_hint" in item.get("tags", [])]
    if historical_assets:
        findings.append(f"证书层仍揭示出 {len(historical_assets)} 个历史资产线索，需要继续确认 DNS 与托管清理状态。")
    return findings


def _functional_tag(asset: str) -> str | None:
    lowered = asset.lower()
    if "dashboard" in lowered:
        return "functional_surface_dashboard"
    if "verify" in lowered:
        return "functional_surface_verify"
    if "rpc" in lowered:
        return "functional_surface_rpc"
    if "api" in lowered:
        return "functional_surface_api"
    return None


def _severity_for_total(total_score: int) -> str:
    if total_score >= 85:
        return "Critical"
    if total_score >= 50:
        return "High"
    if total_score >= 28:
        return "Medium"
    if total_score >= 10:
        return "Low"
    return "Info"


def _confidence_for_layers(layer_count: int) -> str:
    if layer_count >= 3:
        return "high"
    if layer_count == 2:
        return "medium_high"
    return "medium"


def _build_asset_assessment(bucket: AssetAggregate) -> dict[str, Any]:
    tags: list[str] = []
    facts: list[str] = []
    inferences: list[str] = []
    actions: list[str] = []

    functional_tag = _functional_tag(bucket.asset)
    if functional_tag:
        tags.append(functional_tag)

    providers_lower = {provider.lower() for provider in bucket.providers}
    has_cloudflare = any("cloudflare" in provider for provider in providers_lower)
    non_cf_providers = [provider for provider in bucket.providers if "cloudflare" not in provider.lower()]
    if has_cloudflare:
        facts.append("Observed on Cloudflare service IPs")
    if non_cf_providers:
        facts.append("Observed on direct public IP")
    if "Cloudflare Origin Certificate" in bucket.cert_signals:
        facts.append("Certificate layer contains Cloudflare Origin Certificate")
    if "Let's Encrypt" in bucket.cert_signals:
        facts.append("Certificate layer contains active Let's Encrypt certificate")
    if bucket.ns_records and any("vercel-dns" in value for value in bucket.ns_records):
        facts.append("DNS layer shows delegated NS under vercel-dns-3.com")
    if 80 in bucket.ports:
        facts.append("HTTP and HTTPS both exposed" if 443 in bucket.ports else "Public HTTP exposed")
    elif 443 in bucket.ports:
        facts.append("Public HTTPS exposed")
    if "expired" in bucket.cert_statuses and len(bucket.layers) == 1 and bucket.layers == {"certificate"}:
        facts.append("Appears only in certificate layer as expired historical certificate hint")
    if "rpc" in bucket.asset.lower():
        facts.append("Domain name contains rpc keyword")
    if has_cloudflare and non_cf_providers:
        tags.extend(["cdn_and_direct_origin_coexist", "potential_origin_exposure"])
        inferences.append("CDN edge and direct origin appear to coexist on the same functional surface.")
        actions.extend(["Restrict origin access to CDN only", "Review direct public reachability"])
    if bucket.ns_records and any("vercel-dns" in value for value in bucket.ns_records):
        tags.append("third_party_dns_delegation")
        inferences.append("DNS delegation splits governance across a third-party boundary.")
        actions.extend(["Validate ownership and lifecycle", "Review third-party delegation necessity"])
    if 80 in bucket.ports:
        tags.append("public_http_enabled")
        actions.append("Disable unnecessary cleartext access")
    if 443 in bucket.ports:
        tags.append("public_https_enabled")
    if "expired" in bucket.cert_statuses and len(bucket.layers) == 1 and bucket.layers == {"certificate"}:
        tags.extend(["historical_asset_hint", "certificate_lifecycle_observation"])
        inferences.append("Certificate-only historical evidence suggests possible retired asset residue.")
        actions.extend(["Check retirement status", "Confirm DNS and hosting cleanup", "Track stale asset governance"])
    if any("origin certificate" in signal.lower() for signal in bucket.cert_signals):
        actions.append("Review WAF bypass path")
    if functional_tag == "functional_surface_rpc":
        actions.extend(["Review RPC public exposure necessity", "Restrict or authenticate where appropriate"])
    if functional_tag == "functional_surface_dashboard":
        actions.extend(["Verify origin isolation", "Check dashboard exposure necessity"])
    if functional_tag == "functional_surface_api":
        actions.extend(["Validate source IP exposure necessity", "Review WAF bypass path"])
    if functional_tag == "functional_surface_verify":
        actions.extend(["Track project decommission process"])

    unique_actions = []
    for action in actions:
        if action not in unique_actions:
            unique_actions.append(action)

    exposure_score = min(20, (8 if bucket.ips else 0) + (4 if 80 in bucket.ports else 0) + (4 if 443 in bucket.ports else 0) + (4 if functional_tag else 0))
    weakness_score = min(20, (10 if "cdn_and_direct_origin_coexist" in tags else 0) + (8 if "third_party_dns_delegation" in tags else 0) + (5 if "historical_asset_hint" in tags else 0))
    exploitability_score = min(20, (8 if bucket.ips else 0) + (6 if functional_tag in {"functional_surface_rpc", "functional_surface_api", "functional_surface_dashboard"} else 0) + (4 if 80 in bucket.ports and 443 in bucket.ports else 0) + (2 if bucket.cves else 0))
    business_impact_score = min(20, (10 if functional_tag in {"functional_surface_dashboard", "functional_surface_api", "functional_surface_rpc"} else 0) + (8 if functional_tag == "functional_surface_verify" else 0) + (4 if "potential_origin_exposure" in tags else 0))
    control_gap_score = min(10, (5 if "potential_origin_exposure" in tags else 0) + (4 if "third_party_dns_delegation" in tags else 0) + (3 if "historical_asset_hint" in tags else 0))
    scope_persistence_score = min(10, 3 * len(bucket.layers) + (2 if len(bucket.layers) >= 3 else 0))
    total_score = exposure_score + weakness_score + exploitability_score + business_impact_score + control_gap_score + scope_persistence_score
    severity = _severity_for_total(total_score)

    reasoning_parts = []
    if functional_tag:
        reasoning_parts.append(f"{bucket.asset} is a functional surface")
    if "cdn_and_direct_origin_coexist" in tags:
        reasoning_parts.append("it appears both behind CDN and on a direct public provider")
    if "third_party_dns_delegation" in tags:
        reasoning_parts.append("it is independently delegated to third-party DNS/hosting")
    if "historical_asset_hint" in tags:
        reasoning_parts.append("it is currently supported only by historical certificate evidence")
    if 80 in bucket.ports and functional_tag == "functional_surface_rpc":
        reasoning_parts.append("cleartext and HTTPS exposure are both present on an RPC-named asset")
    if not reasoning_parts:
        reasoning_parts.append("the asset is externally observable across one or more attack-surface layers")
    inferences.insert(0, " ".join(reasoning_parts).capitalize() + ".")

    return {
        "asset": bucket.asset,
        "asset_type": "domain",
        "providers": sorted(bucket.providers),
        "ips": sorted(bucket.ips),
        "ports": sorted(bucket.ports),
        "facts": facts,
        "inferences": inferences,
        "tags": sorted(set(tags)),
        "scores": {
            "exposure_score": exposure_score,
            "weakness_score": weakness_score,
            "exploitability_score": exploitability_score,
            "business_impact_score": business_impact_score,
            "control_gap_score": control_gap_score,
            "scope_persistence_score": scope_persistence_score,
            "total_score": total_score,
            "severity": severity,
        },
        "confidence": _confidence_for_layers(len(bucket.layers)),
        "recommended_actions": unique_actions[:6],
        "evidence": bucket.evidence[:6],
    }


def _training_sample(assessment: dict[str, Any]) -> dict[str, Any]:
    return {
        "task": "easm_asset_risk_assessment",
        "input": {
            "asset": assessment["asset"],
            "facts": assessment["facts"],
            "context": {
                "ports": assessment.get("ports", []),
                "providers": assessment.get("providers", []),
            },
        },
        "output": {
            "severity": assessment["scores"]["severity"],
            "tags": assessment["tags"],
            "reasoning": " ".join(assessment["inferences"][:2]),
            "actions": assessment["recommended_actions"],
        },
    }


def build_easm_composite_raw_event(raw_events: list[RawEvent]) -> RawEvent | None:
    easm_events = [event for event in raw_events if event.source_type == "easm"]
    if not easm_events:
        return None
    payload = build_easm_composite_payload(easm_events)
    if not payload.get("asset_assessments"):
        return None
    distinct_layers = {
        detect_easm_dataset(
            str(event.payload.get("filename") or event.asset_context.get("source_file") or ""),
            [str(header) for header in event.payload.get("headers", [])],
            [row for row in event.payload.get("rows", []) if isinstance(row, dict)],
        )
        for event in easm_events
    }
    if len(distinct_layers) < 2 and len(easm_events) < 2:
        return None
    return RawEvent(
        source_type="easm",
        event_hint="easm_asset_assessment",
        asset_context={
            "asset_id": "easm-batch",
            "asset_name": "EASM Composite Batch",
            "environment": "internet",
            "criticality": 4,
            "source_type": "easm",
            "source_file": "EASM Composite Asset Assessment Batch",
        },
        payload=payload,
    )
