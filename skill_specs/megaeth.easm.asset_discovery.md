# Skill Specification: `megaeth.easm.asset_discovery`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.easm.asset_discovery`
- 所属模块：`EASM`
- 适用产品域：`安全日志分析`
- 对应事件类型：`external_asset`
- 当前执行模式：规则主链

### 2. 能力目的

整理外部暴露资产、域名、IP、ASN 和入口面，为后续外部攻击面评估提供资产基础。

### 3. 典型输入

- 资产清单、DNS、IP 段、ASN 或基础发现材料
- 能够描述外部归属关系和暴露范围的原始导出

### 4. 输出契约

- 资产范围摘要
- 待关注目标与可疑归属关系
- 后续服务、TLS 或漏洞检查建议

### 5. 触发与路由

当输入以外部资产盘点为主，尚未进入服务、TLS 或漏洞结论时命中本 Skill。

### 6. 判断边界

- 属于暴露面盘点，不直接下漏洞结论。
- 资产归属与暴露范围应基于材料事实，不应超范围外推。

### 7. 训练与参考资产

- [Case 003 - EASM 多层综合评估](../training_cases/case_003_easm_multilayer/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.easm.asset_discovery`
- Module: `EASM`
- Product Surface: `Security Log Analysis`
- Event Type: `external_asset`
- Execution Mode: rule-first

### 2. Purpose

Organize externally exposed assets, domains, IPs, ASNs, and entry surfaces to provide the asset foundation for EASM assessment.

### 3. Typical Inputs

- asset inventories, DNS, IP ranges, ASN, or foundational discovery material
- raw exports that describe external ownership and exposure scope

### 4. Output Contract

- asset-scope summary
- targets of interest and suspicious ownership relations
- recommended next checks for services, TLS, or vulnerabilities

### 5. Trigger and Routing

This Skill is selected when the input is primarily an external asset inventory and has not yet moved into service, TLS, or vulnerability interpretation.

### 6. Decision Boundaries

- It belongs to exposure inventory and must not conclude vulnerabilities directly.
- Ownership and exposure scope must stay grounded in supplied material without over-expansion.

### 7. Training and Reference Assets

- [Case 003 - EASM Multi-Layer Composite Assessment](../training_cases/case_003_easm_multilayer/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
