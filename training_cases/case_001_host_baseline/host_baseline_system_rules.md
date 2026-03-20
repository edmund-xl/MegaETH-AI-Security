# AI Security System Rules
## Host Baseline Assessment 规则

## 1 Parser 规则

文件识别规则：

如果文件名包含：
riskanalytics

或者 CSV 字段包含：
发现名称
风险评分
合规标准

则分类为：

source_type = host_risk_analytics
event_type = host_baseline_assessment

---

## 2 Parser 字段映射

CSV字段 → 系统字段

发现名称 → finding_name
风险评分 → risk_score
受影响的资源 → affected_asset
平台 → platform
区域 → environment
发现类型 → finding_type
缓解措施类型 → remediation_type
状态 → status
合规标准 → compliance

---

## 3 Skill Mapping

当 event_type = host_baseline_assessment 时调用：

Primary Skill
megaeth.host.baseline_compliance_analysis

Secondary Skill
megaeth.host.integrity_monitor

Optional Skill
megaeth.host.systemd_service_risk

---

## 4 Risk 评分规则

filesystem isolation issue → Medium
temporary directory configuration → Medium
log permission issue → Medium
unused filesystem modules → Low

若满足以下条件风险提升：

environment = production
asset_role = sequencer
asset_role = signer

风险 +1 级

---

## 5 Finding 提炼规则

CSV每一行不直接作为Finding。

必须聚合为关键问题：

filesystem isolation issues
temporary directory configuration
log permission configuration
unused filesystem modules

---

## 6 Report Template

Material Type
Host Baseline Security Assessment

Executive Summary
Configuration weaknesses detected.

Risk Level
Medium

Key Findings
filesystem isolation issues
log permission configuration
unused filesystem modules

Security Impact
Potential privilege abuse and log exhaustion.

Recommended Actions
isolate audit logs
disable unused filesystem modules
enforce logging permissions

---

## 7 Graph Extraction

生成实体：

host_asset
filesystem
log_directory

关系：

host → has_configuration_issue → filesystem
host → has_configuration_issue → log_directory
