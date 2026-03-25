# Skill Specification: `megaeth.key.kms_risk`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.key.kms_risk`
- 所属模块：`Key Security`
- 适用产品域：`安全日志分析`
- 对应事件类型：`kms_access`
- 当前执行模式：规则主链

### 2. 能力目的

分析 KMS 访问行为、密钥使用模式与授权异常，输出密钥控制面风险判断。

### 3. 典型输入

- KMS 访问记录、密钥使用日志、授权材料
- 与密钥调用和授权边界相关的上下文

### 4. 输出契约

- 密钥风险摘要
- 访问模式异常
- 治理建议

### 5. 触发与路由

当输入属于 KMS 访问、密钥使用或授权边界材料时命中本 Skill。

### 6. 判断边界

- 不直接推断密钥泄露，需要更多访问上下文。
- 需要结合资产角色和调用背景解释风险。

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

- Skill ID: `megaeth.key.kms_risk`
- Module: `Key Security`
- Product Surface: `Security Log Analysis`
- Event Type: `kms_access`
- Execution Mode: rule-first

### 2. Purpose

Analyze KMS access behavior, key-usage patterns, and authorization anomalies to produce key-control-plane risk judgments.

### 3. Typical Inputs

- KMS access records, key-usage logs, and authorization materials
- context related to key invocation and authorization boundaries

### 4. Output Contract

- key-risk summary
- abnormal access patterns
- governance recommendations

### 5. Trigger and Routing

This Skill is selected when the input belongs to KMS access, key usage, or authorization-boundary material.

### 6. Decision Boundaries

- It must not directly conclude key leakage without broader access context.
- Risk should be interpreted with asset role and invocation background.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
