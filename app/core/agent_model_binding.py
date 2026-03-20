from __future__ import annotations

import json
import os
from typing import Any

import httpx

from app.models.event import NormalizedEvent


AGENT_ID = "megaeth.agent.core"

AGENT_MODEL_BINDINGS: dict[str, dict[str, Any]] = {
    AGENT_ID: {
        "provider": "gemini",
        "api_key_env": "GEMINI_API_KEY",
        "model_env": "GEMINI_MODEL_JUMPSERVER",
        "default_model": "gemini-2.5-flash",
        "skills": [
            "megaeth.identity.jumpserver_multi_source_review",
            "megaeth.identity.anomalous_access_review",
            "megaeth.identity.jumpserver_command_review",
            "megaeth.identity.jumpserver_transfer_review",
            "megaeth.identity.jumpserver_operation_review",
        ],
    }
}


class AgentModelBindingService:
    def __init__(self) -> None:
        binding = self.binding_for_agent() or {}
        self.api_key = os.getenv(str(binding.get("api_key_env") or "GEMINI_API_KEY"), "").strip()
        self.base_url = os.getenv("GEMINI_API_BASE_URL", "https://generativelanguage.googleapis.com/v1beta").rstrip("/")

    def binding_for_agent(self, agent_id: str = AGENT_ID) -> dict[str, Any] | None:
        return AGENT_MODEL_BINDINGS.get(agent_id)

    def supports_skill(self, skill_id: str, agent_id: str = AGENT_ID) -> bool:
        binding = self.binding_for_agent(agent_id)
        if not binding:
            return False
        return skill_id in binding.get("skills", [])

    def enabled_for_skill(self, skill_id: str, agent_id: str = AGENT_ID) -> bool:
        return bool(self.api_key and self.supports_skill(skill_id, agent_id))

    def model_name(self, agent_id: str = AGENT_ID) -> str | None:
        binding = self.binding_for_agent(agent_id)
        if not binding:
            return None
        return os.getenv(binding["model_env"]) or os.getenv("OPENAI_MODEL") or binding["default_model"]

    def _generate_json(self, *, model: str, system_prompt: str, user_prompt: str) -> dict[str, Any] | None:
        payload = {
            "system_instruction": {
                "parts": [{"text": system_prompt}]
            },
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": user_prompt}],
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json",
            },
        }
        try:
            with httpx.Client(timeout=25.0) as client:
                response = client.post(
                    f"{self.base_url}/models/{model}:generateContent",
                    headers={
                        "x-goog-api-key": f"{self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json=payload,
                )
                response.raise_for_status()
                body = response.json()
        except Exception:
            return None
        try:
            parts = body["candidates"][0]["content"]["parts"]
            content = "".join(str(part.get("text") or "") for part in parts if isinstance(part, dict))
            return json.loads(content)
        except Exception:
            return None

    def generate_jumpserver_narrative(
        self,
        *,
        skill_id: str,
        event: NormalizedEvent,
        fallback_conclusion: str,
        fallback_judgment_lines: list[str],
    ) -> dict[str, Any] | None:
        if not self.enabled_for_skill(skill_id):
            return None
        model = self.model_name()
        if not model:
            return None

        data = event.normalized_data
        prompt_payload = {
            "source_type": event.source_type,
            "event_type": event.event_type,
            "asset_context": event.asset_context,
            "login_summary": data.get("login_summary", {}),
            "command_summary": data.get("command_summary", {}),
            "file_transfer_summary": data.get("file_transfer_summary", {}),
            "operation_summary": data.get("operation_summary", {}),
            "cross_source_correlations": data.get("cross_source_correlations", []),
            "high_risk_accounts": data.get("high_risk_accounts", []),
            "risk_classification": data.get("risk_classification", {}),
            "fallback_conclusion": fallback_conclusion,
            "fallback_judgment_lines": fallback_judgment_lines,
        }

        system_prompt = (
            "你是 MegaETH Agent 的安全分析模型。"
            "你只负责生成 JumpServer 综合报告中的两部分内容："
            "1) 综合结论 2) 综合判断。"
            "不要改动报告结构，不要输出 markdown，不要添加标题。"
            "语气专业、克制、中文输出。"
            "不要出现训练说明或教学口吻。"
            "综合结论允许根据真实数据动态生成，但判断边界必须保持审慎。"
            "综合判断必须保留重点链条列表和最终定性。"
            "输出必须是 JSON 对象，字段只有 comprehensive_conclusion 和 final_judgment_lines。"
        )
        user_prompt = (
            "请根据以下 JumpServer 多源审计结构化数据，生成综合结论与综合判断。"
            "final_judgment_lines 必须是字符串数组。"
            "如果当前数据不足，就保留保守判断，不要编造。"
            "\n\n"
            f"{json.dumps(prompt_payload, ensure_ascii=False)}"
        )

        parsed = self._generate_json(model=model, system_prompt=system_prompt, user_prompt=user_prompt)
        if not parsed:
            return None
        try:
            conclusion = str(parsed.get("comprehensive_conclusion") or "").strip()
            lines = parsed.get("final_judgment_lines") or []
            if not isinstance(lines, list):
                lines = []
            clean_lines = [str(item).strip() for item in lines if str(item).strip()]
            if not conclusion and not clean_lines:
                return None
            return {
                "comprehensive_conclusion": conclusion or fallback_conclusion,
                "final_judgment_lines": clean_lines or fallback_judgment_lines,
                "model": model,
                "provider": "gemini",
                "agent_id": AGENT_ID,
            }
        except Exception:
            return None

    def generate_jumpserver_single_source_narrative(
        self,
        *,
        skill_id: str,
        event: NormalizedEvent,
        compact_context: dict[str, Any],
        fallback_assessment: str,
        fallback_key_facts: list[str],
        fallback_professional_judgment: str,
    ) -> dict[str, Any] | None:
        if not self.enabled_for_skill(skill_id):
            return None
        model = self.model_name()
        if not model:
            return None
        data = event.normalized_data
        prompt_payload = {
            "source_type": event.source_type,
            "event_type": event.event_type,
            "asset_context": event.asset_context,
            "compact_context": compact_context,
            "fallback_assessment": fallback_assessment,
            "fallback_key_facts": fallback_key_facts,
            "fallback_professional_judgment": fallback_professional_judgment,
        }
        system_prompt = (
            "你是 MegaETH Agent 的安全分析模型。"
            "你只负责增强 JumpServer 单文件报告中的三部分内容："
            "1) assessment 2) key_facts 3) professional_judgment。"
            "不要改动报告类型，不要输出 markdown，不要添加标题。"
            "语气专业、克制、中文输出。"
            "不要编造不存在的数据，数字必须来自输入。"
            "输出必须是 JSON 对象，字段只有 assessment、key_facts、professional_judgment。"
        )
        user_prompt = (
            "请根据以下 JumpServer 单源审计结构化数据，增强报告的 assessment、key_facts、professional_judgment。"
            "key_facts 必须是字符串数组，保留 2 到 4 条。"
            "\n\n"
            f"{json.dumps(prompt_payload, ensure_ascii=False)}"
        )
        parsed = self._generate_json(model=model, system_prompt=system_prompt, user_prompt=user_prompt)
        if not parsed:
            return None
        try:
            assessment = str(parsed.get("assessment") or "").strip() or fallback_assessment
            key_facts = parsed.get("key_facts") or []
            if not isinstance(key_facts, list):
                key_facts = []
            key_facts = [str(item).strip() for item in key_facts if str(item).strip()][:4] or fallback_key_facts
            professional_judgment = str(parsed.get("professional_judgment") or "").strip() or fallback_professional_judgment
            return {
                "assessment": assessment,
                "key_facts": key_facts,
                "professional_judgment": professional_judgment,
                "model": model,
                "provider": "gemini",
                "agent_id": AGENT_ID,
            }
        except Exception:
            return None
