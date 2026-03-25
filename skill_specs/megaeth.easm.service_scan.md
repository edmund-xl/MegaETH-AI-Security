# Skill Specification: `megaeth.easm.service_scan`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.easm.service_scan`
- 所属模块：`EASM`
- 适用产品域：`安全日志分析`
- 对应事件类型：`service_exposure`
- 当前执行模式：规则主链

### 2. 能力目的

分析开放端口、服务暴露和网络层可达性，形成外部服务面风险摘要。

### 3. 典型输入

- 服务扫描结果、端口清单、协议识别结果
- 与公网服务暴露直接相关的导出材料

### 4. 输出契约

- 服务暴露摘要
- 可达性与暴露面风险
- 后续 TLS 或漏洞复核建议

### 5. 触发与路由

当输入以端口、协议、服务可达性为主时命中本 Skill。

### 6. 判断边界

- 服务暴露不直接代表漏洞成立。
- 需要与 TLS、漏洞和资产语义联合判断。

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

- Skill ID: `megaeth.easm.service_scan`
- Module: `EASM`
- Product Surface: `Security Log Analysis`
- Event Type: `service_exposure`
- Execution Mode: rule-first

### 2. Purpose

Analyze open ports, service exposure, and network-layer reachability to summarize external service-surface risk.

### 3. Typical Inputs

- service-scan outputs, port inventories, and protocol-identification results
- exports directly related to public service exposure

### 4. Output Contract

- service-exposure summary
- reachability and exposure-surface risk
- next-step TLS or vulnerability review suggestions

### 5. Trigger and Routing

This Skill is selected when the material is primarily about ports, protocols, and reachable services.

### 6. Decision Boundaries

- Service exposure does not directly prove a vulnerability.
- It should be interpreted together with TLS, vulnerability, and asset context.

### 7. Training and Reference Assets

- [Case 003 - EASM Multi-Layer Composite Assessment](../training_cases/case_003_easm_multilayer/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
