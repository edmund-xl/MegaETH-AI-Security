# Skill Specification: `megaeth.identity.policy_risk_analysis`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.policy_risk_analysis`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`login_auth_review / policy context`
- 当前执行模式：规则主链

### 2. 能力目的

分析授权策略、账号边界和访问控制风险，解释策略层面的边界问题。

### 3. 典型输入

- 策略配置、授权清单、身份边界材料
- 能描述账号、角色和授权关系的策略上下文

### 4. 输出契约

- 策略风险摘要
- 边界问题
- 治理建议

### 5. 触发与路由

当材料核心重心是账号策略、授权边界或身份控制面，而不是单一登录记录时命中本 Skill。

### 6. 判断边界

- 属于授权面分析，不替代主机执行证据。
- 策略风险必须与实际使用场景一起解释。

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

- Skill ID: `megaeth.identity.policy_risk_analysis`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `login_auth_review / policy context`
- Execution Mode: rule-first

### 2. Purpose

Analyze authorization policies, account boundaries, and access-control risk to explain policy-layer boundary issues.

### 3. Typical Inputs

- policy configurations, authorization inventories, and identity-boundary material
- policy context describing accounts, roles, and authorization relationships

### 4. Output Contract

- policy-risk summary
- boundary issues
- governance recommendations

### 5. Trigger and Routing

This Skill is selected when the material centers on account policy, authorization boundary, or identity control planes rather than a single login record.

### 6. Decision Boundaries

- It belongs to authorization-surface analysis and does not replace host-execution evidence.
- Policy risk must be interpreted with actual usage context.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
