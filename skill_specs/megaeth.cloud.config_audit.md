# Skill Specification: `megaeth.cloud.config_audit`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.cloud.config_audit`
- 所属模块：`Cloud`
- 适用产品域：`安全日志分析`
- 对应事件类型：`cloud_config_change`
- 当前执行模式：规则主链

### 2. 能力目的

分析云配置变更、基线偏离和高风险安全配置问题，输出治理优先级。

### 3. 典型输入

- 云配置清单、差异快照或变更材料
- 安全控制配置、网络暴露配置、存储与身份配置

### 4. 输出契约

- 配置风险摘要
- 高风险项与影响面
- 治理建议与复核优先级

### 5. 触发与路由

当输入被识别为云配置变更、配置审计或基线对比材料时命中本 Skill。

### 6. 判断边界

- 不替代云原生取证。
- 需要结合环境角色、暴露面和资产重要性解释风险。

### 7. 训练与参考资产

- 暂无正式案例。

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.cloud.config_audit`
- Module: `Cloud`
- Product Surface: `Security Log Analysis`
- Event Type: `cloud_config_change`
- Execution Mode: rule-first

### 2. Purpose

Analyze cloud configuration changes, baseline drift, and risky security misconfigurations, producing governance priorities.

### 3. Typical Inputs

- cloud inventories, diff snapshots, or change material
- security-control, network-exposure, storage, and identity configuration

### 4. Output Contract

- configuration-risk summary
- high-risk items and impact surface
- governance recommendations and review priority

### 5. Trigger and Routing

This Skill is selected for cloud configuration changes, audit inventories, or baseline-comparison materials.

### 6. Decision Boundaries

- It does not replace cloud-native forensics.
- Risk must be interpreted together with environment role, exposure surface, and asset criticality.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
