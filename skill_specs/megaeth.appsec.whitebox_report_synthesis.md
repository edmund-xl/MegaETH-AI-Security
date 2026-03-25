# Skill Specification: `megaeth.appsec.whitebox_report_synthesis`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.appsec.whitebox_report_synthesis`
- 所属模块：`AppSec`
- 适用产品域：`安全日志分析`
- 对应事件类型：`whitebox_security_report`
- 当前执行模式：规则主链，必要时增强综合结论和行动建议

### 2. 能力目的

把白盒侦察与验证结果整合为交付级综合报告，形成风险优先级、整改顺序和管理可读结论。

### 3. 典型输入

- 侦察结论与验证结果
- 候选问题、已确认问题和行动建议
- 需要面向交付对象呈现的整体背景

### 4. 输出契约

- 综合判断
- 优先行动计划
- 交付摘要与章节化报告

### 5. 触发与路由

当上游已经产生足够的侦察和验证材料，需要输出完整交付报告时命中本 Skill。它是 Whitebox 链路的收口节点。

### 6. 判断边界

- 综合报告不能重新发明上游事实，必须以侦察与验证结果为准。
- 报告摘要可以增强表达，但不应改写问题状态或证据结论。

### 7. 训练与参考资产

- [Whitebox AppSec 模板](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/templates/appsec_whitebox_case_template/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.appsec.whitebox_report_synthesis`
- Module: `AppSec`
- Product Surface: `Security Log Analysis`
- Event Type: `whitebox_security_report`
- Execution Mode: rule-first, with optional enhancement for executive judgment and action narrative

### 2. Purpose

Synthesize whitebox reconnaissance and validation outputs into a delivery-grade report with risk prioritization and remediation sequencing.

### 3. Typical Inputs

- recon conclusions and validation results
- candidate issues, confirmed issues, and action items
- context that must be presented to stakeholders

### 4. Output Contract

- overall judgment
- priority action plan
- delivery summary and report sections

### 5. Trigger and Routing

This Skill is selected when recon and validation artifacts are sufficient and a final delivery-grade report is required. It is the closing step of the whitebox chain.

### 6. Decision Boundaries

- The synthesis report must not reinvent upstream facts; it must remain grounded in recon and validation outputs.
- Narrative enhancement may improve clarity but must not rewrite issue states or evidence conclusions.

### 7. Training and Reference Assets

- [Whitebox AppSec template](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/templates/appsec_whitebox_case_template/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
