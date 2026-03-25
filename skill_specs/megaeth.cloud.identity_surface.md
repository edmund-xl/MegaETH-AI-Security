# Skill Specification: `megaeth.cloud.identity_surface`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.cloud.identity_surface`
- 所属模块：`Cloud`
- 适用产品域：`安全日志分析`
- 对应事件类型：`cloud_config_change / kms_access`
- 当前执行模式：规则主链

### 2. 能力目的

识别云身份暴露、权限边界、服务账号风险以及跨云身份控制面问题。

### 3. 典型输入

- IAM 配置、账号授权清单、角色绑定材料
- 服务账号访问材料和身份面相关日志

### 4. 输出契约

- 身份暴露风险
- 权限边界问题
- 治理建议与复核重点

### 5. 触发与路由

当材料核心重心是 IAM、授权边界、服务账号或云身份控制面时命中本 Skill。

### 6. 判断边界

- 重点解释身份面与授权面，不替代完整 IAM 审计。
- 需要与主机、网络或密钥侧证据联合解释风险。

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

- Skill ID: `megaeth.cloud.identity_surface`
- Module: `Cloud`
- Product Surface: `Security Log Analysis`
- Event Type: `cloud_config_change / kms_access`
- Execution Mode: rule-first

### 2. Purpose

Identify cloud identity exposure, privilege-boundary issues, service-account risk, and cloud identity-control-plane problems.

### 3. Typical Inputs

- IAM configurations, role bindings, and account-authorization inventories
- service-account access material and identity-surface logs

### 4. Output Contract

- identity-exposure risk
- privilege-boundary issues
- governance recommendations and review focus

### 5. Trigger and Routing

This Skill is selected when the material centers on IAM, authorization boundaries, service accounts, or cloud identity control planes.

### 6. Decision Boundaries

- It explains the identity and authorization surface, but does not replace a full IAM audit.
- Risk should be interpreted together with host, network, or key-related evidence where available.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
