from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from app.models.event import NormalizedEvent, RawEvent


EVENT_TYPE_HINTS = {
    "github": {"pull_request": "github_pr", "secret": "secret_exposure"},
    "endpoint": {"incident": "endpoint_process", "shellspawned": "endpoint_process"},
    "host": {"发现名称": "host_integrity", "auditd": "host_integrity", "ssh": "systemd_service_change"},
    "host_risk_analytics": {"发现名称": "host_baseline_assessment", "风险评分": "host_baseline_assessment", "合规标准": "host_baseline_assessment"},
    "cloud": {"config": "cloud_config_change", "bucket": "cloud_config_change"},
    "easm": {"port": "service_exposure", "tls": "tls_change"},
    "kms": {"sign": "kms_access"},
    "bitdefender": {"catalog": "integration_catalog", "report": "integration_catalog", "inventory": "endpoint_inventory"},
    "jumpserver": {"jumpserver_multi_source_audit": "jumpserver_multi_source_audit"},
    "login_auth": {"登录 ip": "login_auth_review", "otp": "login_auth_review", "认证方式": "login_auth_review"},
    "command_audit": {"风险等级": "jumpserver_command_review", "会话": "jumpserver_command_review", "命令": "jumpserver_command_review"},
    "file_transfer_audit": {"文件名": "jumpserver_transfer_review", "可下载": "jumpserver_transfer_review", "操作": "jumpserver_transfer_review"},
    "operation_audit": {"资源类型": "jumpserver_operation_review", "动作": "jumpserver_operation_review", "组织名称": "jumpserver_operation_review"},
    "appsec": {
        "whitebox_recon_assessment": "whitebox_recon_assessment",
        "whitebox_exploit_validation": "whitebox_exploit_validation",
        "whitebox_security_report": "whitebox_security_report",
    },
}


class EventNormalizer:
    def infer_event_type(self, raw_event: RawEvent) -> str:
        if raw_event.event_hint:
            return raw_event.event_hint
        blob = " ".join(str(v).lower() for v in raw_event.payload.values())
        for marker, event_type in EVENT_TYPE_HINTS.get(raw_event.source_type, {}).items():
            if marker in blob:
                return event_type
        return {
            "github": "github_pr",
            "endpoint": "endpoint_process",
            "host": "host_integrity",
            "host_risk_analytics": "host_baseline_assessment",
            "cloud": "cloud_config_change",
            "easm": "external_asset",
            "kms": "kms_access",
            "identity": "anomalous_access",
            "jumpserver": "jumpserver_multi_source_audit",
            "login_auth": "login_auth_review",
            "command_audit": "jumpserver_command_review",
            "file_transfer_audit": "jumpserver_transfer_review",
            "operation_audit": "jumpserver_operation_review",
            "bitdefender": "integration_catalog",
            "appsec": "whitebox_recon_assessment",
        }.get(raw_event.source_type, "external_asset")

    def normalize(self, raw_event: RawEvent) -> NormalizedEvent:
        timestamp = raw_event.timestamp or datetime.now(timezone.utc)
        normalized = dict(raw_event.payload)
        normalized.setdefault("target", raw_event.asset_context.get("asset_name", "."))
        return NormalizedEvent(
            event_id=f"evt-{uuid4().hex[:12]}",
            event_type=self.infer_event_type(raw_event),
            source_type=raw_event.source_type,
            timestamp=timestamp,
            asset_context=raw_event.asset_context,
            normalized_data=normalized,
        )
