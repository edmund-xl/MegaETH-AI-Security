# Skill Specification: `megaeth.easm.external_intelligence`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.easm.external_intelligence`
- 所属模块：`EASM`
- 适用产品域：`安全日志分析`
- 对应事件类型：`external_asset`
- 当前执行模式：规则主链

### 2. 能力目的

汇总外部情报、暴露信号与补充上下文，为外部面风险判断提供关联信息。

它是 EASM 体系中的补充语义层 Skill，负责把开放源、归属备注和外部线索转化为“背景情报”，而不是直接替代资产、服务或漏洞事实。

### 3. 典型输入

- 开放源情报、资产备注、外部关联信息
- 能补充资产上下文和可疑信号的材料

常见输入形态包括：

- 归属备注
- 外部资产说明
- 第三方托管或委派信息
- 历史线索与公开情报补充

### 4. 输出契约

- 外部情报摘要
- 风险提示与优先关注方向
- 需要进一步验证的外部线索
- 附着在资产和服务事实上的背景说明

### 5. 触发与路由

当输入以外部情报、归属关系、开放源补充信息为主时命中本 Skill。

在多文件 EASM 批次中，它通常为综合评估提供资产背景和补充线索，而不是承担事实主层。

### 6. 判断边界

- 情报质量依赖输入来源，需要说明可信度与不足。
- 外部情报不能替代资产、服务或漏洞事实本身。
- 不能把开放源备注直接写成已确认事实。
- 不能因为第三方托管或 CDN 线索就直接给出漏洞结论。

### 7. 训练与参考资产

- [Case 003 - EASM 多层综合评估](../training_cases/case_003_easm_multilayer/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。
- 当前它主要服务于 EASM 综合链中的背景解释层。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。
- 若引入新的情报来源或归属语义，必须同步检查：
  - 单文件背景情报输出
  - EASM 综合报告中的背景判断

## English

### 1. Basics

- Skill ID: `megaeth.easm.external_intelligence`
- Module: `EASM`
- Product Surface: `Security Log Analysis`
- Event Type: `external_asset`
- Execution Mode: rule-first

### 2. Purpose

Aggregate external intelligence, exposure signals, and supplementary context to support external-surface risk assessment.

### 3. Typical Inputs

- open-source intelligence, asset notes, and external correlation data
- materials that enrich asset context and suspicious signals

### 4. Output Contract

- external-intelligence summary
- risk notes and priority directions
- external leads that require further validation

### 5. Trigger and Routing

This Skill is selected when the material is centered on external intelligence, ownership context, or open-source enrichment.

### 6. Decision Boundaries

- Intelligence quality depends on the source and should state confidence and gaps.
- External intelligence must not replace asset, service, or vulnerability facts.

### 7. Training and Reference Assets

- [Case 003 - EASM Multi-Layer Composite Assessment](../training_cases/case_003_easm_multilayer/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
