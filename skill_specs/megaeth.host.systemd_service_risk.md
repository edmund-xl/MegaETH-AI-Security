# Skill Specification: `megaeth.host.systemd_service_risk`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.systemd_service_risk`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`systemd_service_change / host_integrity`
- 当前执行模式：规则主链

### 2. 能力目的

审查 systemd 服务、开放服务和运维侧服务变更风险，解释服务层暴露与控制问题。

### 3. 典型输入

- 服务列表、systemd 配置、端口与暴露材料
- 服务变更记录和运维动作相关材料

### 4. 输出契约

- 高风险服务项
- 服务暴露面说明
- 治理建议与复核重点

### 5. 触发与路由

当输入重心是服务清单、systemd、服务变更或端口暴露时命中本 Skill。

### 6. 判断边界

- 不对单个服务名直接给出入侵结论。
- 需要结合端口、资产角色和变更背景解释风险。

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

- Skill ID: `megaeth.host.systemd_service_risk`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `systemd_service_change / host_integrity`
- Execution Mode: rule-first

### 2. Purpose

Review systemd services, exposed services, and operational service-change risk to explain service-layer exposure and control issues.

### 3. Typical Inputs

- service inventories, systemd configurations, and exposure material
- service-change records and operational action material

### 4. Output Contract

- high-risk service items
- service exposure explanations
- governance recommendations and review focus

### 5. Trigger and Routing

This Skill is selected when the input centers on service lists, systemd configuration, service changes, or port exposure.

### 6. Decision Boundaries

- A single service name must not be treated as proof of compromise.
- Risk must be explained using port exposure, asset role, and change background.

### 7. Training and Reference Assets

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
