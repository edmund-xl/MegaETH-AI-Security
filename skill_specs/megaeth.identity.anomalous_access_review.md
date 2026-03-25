# Skill Specification: `megaeth.identity.anomalous_access_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.anomalous_access_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`login_auth_review`
- 当前执行模式：规则主链，必要时可增强登录侧总结和专业判断

### 2. 能力目的

分析登录结果、失败模式和异常访问行为，形成登录侧风险判断。

### 3. 典型输入

- 登录日志、认证事件、失败原因和结果状态
- 与账号、OTP、来源地址和时间窗相关的材料

### 4. 输出契约

- 登录侧摘要
- 失败模式与重点账户
- 登录异常的复核建议

### 5. 触发与路由

当输入属于登录、认证、OTP 或访问结果材料时命中本 Skill，也可作为 JumpServer 多源综合的单源子能力。

### 6. 判断边界

- 不能把代理地址直接当攻击源。
- 不因单次失败直接认定爆破或外部入侵。

### 7. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计（登录侧子能力）](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.identity.anomalous_access_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `login_auth_review`
- Execution Mode: rule-first, with optional enhancement for login-side summary and professional judgment

### 2. Purpose

Analyze login outcomes, failure patterns, and anomalous access behavior to produce login-side risk judgments.

### 3. Typical Inputs

- login logs, authentication events, failure reasons, and result states
- materials related to accounts, OTP, source addresses, and time windows

### 4. Output Contract

- login-side summary
- failure patterns and focus accounts
- review guidance for anomalous access

### 5. Trigger and Routing

This Skill is selected for login, authentication, OTP, or access-result material, and also serves as a single-source component for JumpServer composite review.

### 6. Decision Boundaries

- Proxy addresses must not be treated directly as attack origin.
- A single failure must not be treated as proof of brute force or external intrusion.

### 7. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit (login-side sub-capability)](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
