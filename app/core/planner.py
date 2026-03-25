from __future__ import annotations

# Security-log-analysis mainline planner.

from app.models.event import NormalizedEvent


EVENT_SKILL_MAP = {
    "github_pr": ["megaeth.cicd.pr_security_review"],
    "secret_exposure": ["megaeth.cicd.secret_detection", "megaeth.key.private_key_exposure"],
    "endpoint_process": ["megaeth.endpoint.process_anomaly"],
    "host_baseline_assessment": [
        "megaeth.host.baseline_compliance_analysis",
        "megaeth.host.integrity_monitor",
    ],
    "host_integrity": ["megaeth.host.integrity_monitor", "megaeth.host.systemd_service_risk", "megaeth.host.binary_tamper_review"],
    "systemd_service_change": ["megaeth.host.systemd_service_risk", "megaeth.host.integrity_monitor"],
    "cloud_config_change": ["megaeth.cloud.config_audit"],
    "external_asset": ["megaeth.easm.asset_discovery"],
    "service_exposure": ["megaeth.easm.service_scan", "megaeth.easm.tls_analysis"],
    "tls_analysis": ["megaeth.easm.tls_analysis"],
    "easm_asset_assessment": [
        "megaeth.easm.asset_discovery",
        "megaeth.easm.service_scan",
        "megaeth.easm.tls_analysis",
        "megaeth.easm.vulnerability_scan",
        "megaeth.easm.external_intelligence",
    ],
    "kms_access": ["megaeth.key.kms_risk"],
    "whitebox_recon_assessment": ["megaeth.appsec.whitebox_recon"],
    "whitebox_exploit_validation": ["megaeth.appsec.whitebox_exploit_validation"],
    "whitebox_security_report": ["megaeth.appsec.whitebox_report_synthesis"],
    "jumpserver_multi_source_audit": ["megaeth.identity.jumpserver_multi_source_review"],
    "login_auth_review": ["megaeth.identity.anomalous_access_review"],
    "jumpserver_command_review": ["megaeth.identity.jumpserver_command_review"],
    "jumpserver_transfer_review": ["megaeth.identity.jumpserver_transfer_review"],
    "jumpserver_operation_review": ["megaeth.identity.jumpserver_operation_review"],
    "integration_catalog": [],
    "endpoint_inventory": [],
}


class Planner:
    def _sanitize_skills_for_event(self, event: NormalizedEvent, skills: list[str]) -> list[str]:
        sanitized = list(skills)
        if event.event_type == "login_auth_review":
            allowed = {"megaeth.identity.anomalous_access_review"}
            sanitized = [skill for skill in sanitized if skill in allowed]
        elif event.event_type == "jumpserver_command_review":
            allowed = {"megaeth.identity.jumpserver_command_review"}
            sanitized = [skill for skill in sanitized if skill in allowed]
        elif event.event_type == "jumpserver_transfer_review":
            allowed = {"megaeth.identity.jumpserver_transfer_review"}
            sanitized = [skill for skill in sanitized if skill in allowed]
        elif event.event_type == "jumpserver_operation_review":
            allowed = {"megaeth.identity.jumpserver_operation_review"}
            sanitized = [skill for skill in sanitized if skill in allowed]
        elif event.event_type == "jumpserver_multi_source_audit":
            allowed = {"megaeth.identity.jumpserver_multi_source_review"}
            sanitized = [skill for skill in sanitized if skill in allowed]
        return sanitized

    def classify(self, event: NormalizedEvent) -> dict[str, object]:
        tags: list[str] = []
        if event.source_type == "github":
            tags.append("supply_chain")
        if event.source_type in {"host", "host_risk_analytics"}:
            tags.append("host_posture")
        if event.source_type == "cloud":
            tags.append("cloud_posture")
        if event.source_type == "endpoint":
            tags.append("endpoint_incident")
        if event.source_type == "easm":
            tags.append("external_surface")
        if event.source_type == "bitdefender":
            tags.append("security_platform")
        if event.source_type in {"jumpserver", "login_auth", "command_audit", "file_transfer_audit", "operation_audit"}:
            tags.append("privileged_access_audit")
        if event.source_type == "appsec":
            tags.append("application_security")
        return {"classification": tags or ["general"], "priority": "high" if event.asset_context.get("criticality", 1) >= 4 else "normal"}

    def plan(self, event: NormalizedEvent) -> tuple[list[str], str]:
        skills = list(EVENT_SKILL_MAP.get(event.event_type, []))
        if not skills and event.event_type != "integration_catalog":
            skills = ["megaeth.easm.asset_discovery"]
        memory_context = event.normalized_data.get("_memory_context", {})
        preferred = [item for item in memory_context.get("preferred_skills", []) if item]
        if preferred:
            skills = list(dict.fromkeys([*preferred, *skills]))
        skills = self._sanitize_skills_for_event(event, skills)
        reason = (
            f"Classified event as {', '.join(self.classify(event)['classification'])}; "
            f"selected skill set for event_type={event.event_type} and source_type={event.source_type}."
        )
        matched_rule_name = str(memory_context.get("matched_rule_name") or "").strip()
        if matched_rule_name:
            if event.event_type == "host_baseline_assessment":
                reason += " 该类材料已命中主机基线学习规则。"
            elif event.event_type == "jumpserver_multi_source_audit":
                reason += " 该类材料已命中 JumpServer 多源审计学习规则。"
            elif event.event_type == "jumpserver_operation_review":
                reason += " 该类材料已命中 JumpServer 管理平面审计学习规则。"
            elif event.source_type == "endpoint":
                reason += " 该类材料已命中端点事件学习规则。"
            else:
                reason += " 系统已命中相似材料学习规则。"
        return skills, reason
