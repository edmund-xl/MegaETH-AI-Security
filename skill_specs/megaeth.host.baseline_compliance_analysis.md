# Skill Specification: `megaeth.host.baseline_compliance_analysis`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.baseline_compliance_analysis`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`host_baseline_assessment`
- 当前执行模式：规则主链

### 2. 能力目的

分析主机基线检查结果，输出合规缺口、风险分层和整改重点。

### 3. 典型输入

- 主机基线报表、检查项结果、风险评分与发现名称
- 描述控制缺失、配置偏离和账户策略问题的材料

### 4. 输出契约

- 基线缺口摘要
- 风险主题与优先整改项
- 适合治理场景的整改建议

### 5. 触发与路由

当输入被识别为主机基线报表、基线检查结果或合规差距材料时命中本 Skill。

### 6. 判断边界

- 属于基线治理分析，不等同于入侵事件判断。
- 优先级需要结合资产重要性和控制覆盖解释。

### 7. 训练与参考资产

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.host.baseline_compliance_analysis`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `host_baseline_assessment`
- Execution Mode: rule-first

### 2. Purpose

Analyze host baseline results and produce compliance gaps, risk tiers, and remediation priorities.

### 3. Typical Inputs

- host baseline reports, check results, risk scores, and finding names
- materials describing missing controls, configuration drift, and account-policy issues

### 4. Output Contract

- baseline-gap summary
- risk themes and remediation priorities
- governance-oriented remediation recommendations

### 5. Trigger and Routing

This Skill is selected when the input is recognized as a host baseline report, baseline check result, or compliance-gap material.

### 6. Decision Boundaries

- This is baseline-governance analysis and is not equivalent to intrusion attribution.
- Priority should be explained with asset criticality and control coverage.

### 7. Training and Reference Assets

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
