from __future__ import annotations

# Security-log-analysis mainline learning-memory services.

from collections import Counter
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.models.event import NormalizedEvent, RawEvent
from app.models.memory import ClassificationFeedback, ClassificationMemoryRule
from app.utils.store import JsonFileStore, MEMORY_FEEDBACK_FILE, MEMORY_RULES_FILE, write_json


class MemoryService:
    def __init__(self) -> None:
        self.store = JsonFileStore()

    def list_rules(self) -> list[dict[str, Any]]:
        return self._dedupe_rules(self.store.list_records(MEMORY_RULES_FILE, limit=200))

    def list_feedback(self) -> list[dict[str, Any]]:
        return self.store.list_records(MEMORY_FEEDBACK_FILE, limit=200)

    def _tokenize(self, value: str) -> list[str]:
        token = []
        tokens: list[str] = []
        for char in value.lower():
            if char.isalnum() or char in {"_", "-", ".", "/"} or "\u4e00" <= char <= "\u9fff":
                token.append(char)
            elif token:
                tokens.append("".join(token))
                token = []
        if token:
            tokens.append("".join(token))
        return [item for item in tokens if len(item) >= 2]

    def build_signature(self, raw_event: RawEvent) -> dict[str, Any]:
        filename = str(raw_event.asset_context.get("source_file") or raw_event.asset_context.get("asset_name") or "")
        headers = [str(v) for v in raw_event.payload.get("headers", [])]
        rows = raw_event.payload.get("rows", [])
        snippets: list[str] = []
        if isinstance(rows, list):
            for row in rows[:8]:
                if isinstance(row, dict):
                    snippets.extend(str(v) for v in row.values())
        if raw_event.payload.get("content"):
            snippets.append(str(raw_event.payload["content"]))
        return {
            "filename": filename,
            "filename_tokens": self._tokenize(filename),
            "header_tokens": self._tokenize(" ".join(headers)),
            "content_tokens": self._tokenize(" ".join(snippets))[:60],
            "parser_profile": str(raw_event.payload.get("parser_profile") or ""),
        }

    def _score(self, rule: dict[str, Any], sig: dict[str, Any], raw_event: RawEvent | None = None) -> int:
        score = 0
        if raw_event is not None:
            expected_source = str(rule.get("expected_source_type") or "")
            if expected_source == raw_event.source_type:
                score += 6
            elif expected_source and raw_event.source_type and expected_source != raw_event.source_type:
                score -= 4
        for token in rule.get("filename_tokens", []):
            if token in sig["filename_tokens"]:
                score += 4
        for token in rule.get("header_tokens", []):
            if token in sig["header_tokens"]:
                score += 3
        for token in rule.get("content_tokens", []):
            if token in sig["content_tokens"]:
                score += 2
        if sig["parser_profile"] and sig["parser_profile"] in rule.get("parser_profiles", []):
            score += 2
        return score

    def _is_host_risk_analytics_signature(self, sig: dict[str, Any]) -> bool:
        filename_tokens = set(sig.get("filename_tokens", []))
        header_tokens = set(sig.get("header_tokens", []))
        content_tokens = set(sig.get("content_tokens", []))
        return (
            "riskanalytics" in filename_tokens
            or "发现名称" in header_tokens
            or "风险评分" in header_tokens
            or "合规标准" in header_tokens
            or "风险评分" in content_tokens
        )

    def _upgrade_match_for_signature(self, match: dict[str, Any], sig: dict[str, Any]) -> dict[str, Any]:
        if self._is_host_risk_analytics_signature(sig) and match.get("expected_source_type") == "host" and match.get("expected_event_type") == "host_integrity":
            upgraded = dict(match)
            upgraded["expected_source_type"] = "host_risk_analytics"
            upgraded["expected_event_type"] = "host_baseline_assessment"
            upgraded["matched_rule_name"] = "host baseline memory"
            preferred = upgraded.get("preferred_skills", [])
            upgraded["preferred_skills"] = list(
                dict.fromkeys(
                    [
                        "megaeth.host.baseline_compliance_analysis",
                        *preferred,
                    ]
                )
            )
            return upgraded
        return match

    def _rule_priority(self, rule: dict[str, Any]) -> int:
        notes = str(rule.get("notes") or "").lower()
        return 0 if "auto-generated" in notes else 1

    def _rule_key(self, rule: dict[str, Any]) -> tuple[str, str, str, str]:
        filename = ",".join(rule.get("filename_tokens", [])[:3])
        headers = ",".join(rule.get("header_tokens", [])[:4])
        return (
            str(rule.get("expected_source_type") or ""),
            str(rule.get("expected_event_type") or ""),
            str(rule.get("parser_profiles", [""])[0] if rule.get("parser_profiles") else ""),
            f"{filename}|{headers}",
        )

    def _rule_sort_key(self, rule: dict[str, Any]) -> tuple[int, int, str]:
        timestamp = str(rule.get("updated_at") or rule.get("created_at") or "")
        return (
            self._rule_priority(rule),
            int(rule.get("usage_count", 0)),
            timestamp,
        )

    def _source_match_rank(self, rule: dict[str, Any], raw_event: RawEvent) -> int:
        expected_source = str(rule.get("expected_source_type") or "")
        if not expected_source:
            return 0
        if expected_source == raw_event.source_type:
            return 2
        if self._is_host_risk_analytics_signature(self.build_signature(raw_event)) and expected_source == "host":
            return 0
        return -1

    def _event_match_rank(self, rule: dict[str, Any], raw_event: RawEvent) -> int:
        expected_event = str(rule.get("expected_event_type") or "")
        if not expected_event:
            return 0
        if raw_event.event_hint and expected_event == raw_event.event_hint:
            return 2
        if raw_event.event_hint and expected_event != raw_event.event_hint:
            return -1
        if self._is_host_risk_analytics_signature(self.build_signature(raw_event)) and expected_event == "host_integrity":
            return 0
        return 0

    def _dedupe_rules(self, rules: list[dict[str, Any]]) -> list[dict[str, Any]]:
        merged: dict[tuple[str, str, str, str], dict[str, Any]] = {}
        for rule in rules:
            key = self._rule_key(rule)
            current = merged.get(key)
            if not current:
                merged[key] = rule
                continue
            preferred, secondary = (rule, current) if self._rule_sort_key(rule) > self._rule_sort_key(current) else (current, rule)
            preferred["usage_count"] = max(int(preferred.get("usage_count", 0)), int(secondary.get("usage_count", 0)))
            preferred["last_matched_at"] = preferred.get("last_matched_at") or secondary.get("last_matched_at")
            preferred["updated_at"] = max(str(preferred.get("updated_at") or ""), str(secondary.get("updated_at") or ""))
            preferred["preferred_skills"] = list(dict.fromkeys((preferred.get("preferred_skills") or []) + (secondary.get("preferred_skills") or [])))
            preferred["filename_tokens"] = list(dict.fromkeys((preferred.get("filename_tokens") or []) + (secondary.get("filename_tokens") or [])))[:8]
            preferred["header_tokens"] = list(dict.fromkeys((preferred.get("header_tokens") or []) + (secondary.get("header_tokens") or [])))[:12]
            preferred["content_tokens"] = list(dict.fromkeys((preferred.get("content_tokens") or []) + (secondary.get("content_tokens") or [])))[:16]
            preferred["parser_profiles"] = list(dict.fromkeys((preferred.get("parser_profiles") or []) + (secondary.get("parser_profiles") or [])))
            merged[key] = preferred
        return sorted(merged.values(), key=self._rule_sort_key, reverse=True)

    def recall(self, raw_event: RawEvent) -> dict[str, Any] | None:
        sig = self.build_signature(raw_event)
        best = None
        best_rank = (-1, -1, -1, -1)
        best_score = 0
        for rule in self.list_rules():
            expected_source = str(rule.get("expected_source_type") or "")
            expected_event = str(rule.get("expected_event_type") or "")
            if raw_event.source_type and expected_source and expected_source != raw_event.source_type:
                if not (self._is_host_risk_analytics_signature(sig) and expected_source == "host"):
                    continue
            if raw_event.event_hint and expected_event and expected_event != raw_event.event_hint:
                continue
            score = self._score(rule, sig, raw_event)
            priority = self._rule_priority(rule)
            rank = (
                self._source_match_rank(rule, raw_event),
                self._event_match_rank(rule, raw_event),
                priority,
                score,
            )
            if rank > best_rank:
                best = rule
                best_rank = rank
                best_score = score
        if not best or best_score < 6:
            return None
        rules = self.store.list_records(MEMORY_RULES_FILE, limit=200)
        now = datetime.now(timezone.utc).isoformat()
        for rule in rules:
            if rule["rule_id"] == best["rule_id"]:
                rule["last_matched_at"] = now
                rule["updated_at"] = now
                rule["usage_count"] = int(rule.get("usage_count", 0)) + 1
        write_json(MEMORY_RULES_FILE, rules)
        return {
            "matched_rule_id": best["rule_id"],
            "matched_rule_name": best["name"],
            "expected_source_type": best["expected_source_type"],
            "expected_event_type": best["expected_event_type"],
            "preferred_skills": best.get("preferred_skills", []),
            "notes": best.get("notes", ""),
            "score": best_score,
        }

    def apply_raw_event_memory(self, raw_event: RawEvent) -> tuple[RawEvent, dict[str, Any] | None]:
        match = self.recall(raw_event)
        if not match:
            return raw_event, None
        sig = self.build_signature(raw_event)
        match = self._upgrade_match_for_signature(match, sig)
        adjusted = raw_event.model_copy(
            update={
                "source_type": match["expected_source_type"],
                "event_hint": match["expected_event_type"],
                "asset_context": {
                    **raw_event.asset_context,
                    "memory_rule_id": match["matched_rule_id"],
                    "memory_rule_name": match["matched_rule_name"],
                },
            }
        )
        return adjusted, match

    def enrich_normalized_event(self, event: NormalizedEvent, match: dict[str, Any] | None) -> NormalizedEvent:
        if not match:
            return event
        return event.model_copy(
            update={
                "event_type": match["expected_event_type"],
                "normalized_data": {
                    **event.normalized_data,
                    "_memory_context": match,
                },
            }
        )

    def learn_classification(
        self,
        raw_event: RawEvent,
        expected_source_type: str,
        expected_event_type: str,
        preferred_skills: list[str] | None = None,
        notes: str = "",
        name: str | None = None,
    ) -> dict[str, Any]:
        preferred_skills = preferred_skills or []
        sig = self.build_signature(raw_event)
        now = datetime.now(timezone.utc)
        feedback = ClassificationFeedback(
            feedback_id=f"fb-{uuid4().hex[:10]}",
            name=name or "classification feedback",
            filename=sig["filename"],
            expected_source_type=expected_source_type,
            expected_event_type=expected_event_type,
            preferred_skills=preferred_skills,
            notes=notes,
            created_at=now,
        )
        self.store.append(MEMORY_FEEDBACK_FILE, feedback.model_dump(mode="json"), limit=200)
        rules = self.store.list_records(MEMORY_RULES_FILE, limit=200)
        rule_name = name or f"{expected_source_type} memory"
        matched_rule = None
        best_score = 0
        for rule in rules:
            score = self._score(rule, sig, raw_event)
            if (
                rule.get("expected_source_type") == expected_source_type
                and rule.get("expected_event_type") == expected_event_type
                and self._rule_priority(rule) == 1
                and score >= best_score
            ):
                matched_rule = rule
                best_score = score

        if matched_rule and best_score >= 6:
            matched_rule["name"] = rule_name
            matched_rule["preferred_skills"] = preferred_skills
            matched_rule["notes"] = notes
            matched_rule["filename_tokens"] = [item for item, _ in Counter(sig["filename_tokens"]).most_common(8)]
            matched_rule["header_tokens"] = [item for item, _ in Counter(sig["header_tokens"]).most_common(12)]
            matched_rule["content_tokens"] = [item for item, _ in Counter(sig["content_tokens"]).most_common(16)]
            matched_rule["parser_profiles"] = [sig["parser_profile"]] if sig["parser_profile"] else []
            matched_rule["updated_at"] = now.isoformat()
            write_json(MEMORY_RULES_FILE, self._dedupe_rules(rules))
            return matched_rule

        rule = ClassificationMemoryRule(
            rule_id=f"mem-{uuid4().hex[:10]}",
            name=rule_name,
            expected_source_type=expected_source_type,
            expected_event_type=expected_event_type,
            preferred_skills=preferred_skills,
            filename_tokens=[item for item, _ in Counter(sig["filename_tokens"]).most_common(8)],
            header_tokens=[item for item, _ in Counter(sig["header_tokens"]).most_common(12)],
            content_tokens=[item for item, _ in Counter(sig["content_tokens"]).most_common(16)],
            parser_profiles=[sig["parser_profile"]] if sig["parser_profile"] else [],
            notes=notes,
            created_at=now,
            updated_at=now,
        )
        rules.insert(0, rule.model_dump(mode="json"))
        write_json(MEMORY_RULES_FILE, self._dedupe_rules(rules)[:200])
        return rule.model_dump(mode="json")

    def learn_from_analysis(
        self,
        raw_event: RawEvent,
        normalized_event: NormalizedEvent,
        preferred_skills: list[str] | None = None,
    ) -> dict[str, Any]:
        preferred_skills = preferred_skills or []
        sig = self.build_signature(raw_event)
        rules = self.store.list_records(MEMORY_RULES_FILE, limit=200)
        best_rule = None
        best_score = 0
        for rule in rules:
            score = self._score(rule, sig, raw_event)
            if (
                rule.get("expected_source_type") == normalized_event.source_type
                and rule.get("expected_event_type") == normalized_event.event_type
                and self._rule_priority(rule) == 1
                and score > best_score
            ):
                best_rule = rule
                best_score = score

        now = datetime.now(timezone.utc)
        feedback = ClassificationFeedback(
            feedback_id=f"fb-{uuid4().hex[:10]}",
            name=f"Auto observation: {normalized_event.event_type}",
            filename=sig["filename"],
            expected_source_type=normalized_event.source_type,
            expected_event_type=normalized_event.event_type,
            preferred_skills=preferred_skills,
            notes="auto-observed from successful analysis",
            created_at=now,
        )
        self.store.append(MEMORY_FEEDBACK_FILE, feedback.model_dump(mode="json"), limit=200)

        if best_rule and best_score >= 8:
            rule_rows = self.store.list_records(MEMORY_RULES_FILE, limit=200)
            for rule in rule_rows:
                if rule["rule_id"] == best_rule["rule_id"]:
                    rule["updated_at"] = now.isoformat()
                    rule["last_matched_at"] = now.isoformat()
                    rule["usage_count"] = int(rule.get("usage_count", 0)) + 1
            write_json(MEMORY_RULES_FILE, self._dedupe_rules(rule_rows))
            return {"mode": "updated", "rule_id": best_rule["rule_id"], "score": best_score}

        rule = ClassificationMemoryRule(
            rule_id=f"mem-{uuid4().hex[:10]}",
            name=f"Auto learned: {normalized_event.event_type}",
            expected_source_type=normalized_event.source_type,
            expected_event_type=normalized_event.event_type,
            preferred_skills=preferred_skills,
            filename_tokens=[item for item, _ in Counter(sig["filename_tokens"]).most_common(8)],
            header_tokens=[item for item, _ in Counter(sig["header_tokens"]).most_common(12)],
            content_tokens=[item for item, _ in Counter(sig["content_tokens"]).most_common(16)],
            parser_profiles=[sig["parser_profile"]] if sig["parser_profile"] else [],
            notes="auto-generated from successful analysis",
            created_at=now,
            updated_at=now,
            last_matched_at=now,
            usage_count=1,
        )
        rules.insert(0, rule.model_dump(mode="json"))
        write_json(MEMORY_RULES_FILE, self._dedupe_rules(rules)[:200])
        return {"mode": "created", "rule_id": rule.rule_id, "score": best_score}
