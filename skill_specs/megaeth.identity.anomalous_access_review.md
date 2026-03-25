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

分析登录结果、失败模式和异常访问行为，形成登录侧风险判断。该 Skill 要把“账号、来源、结果、时间窗、失败模式”组织成一条登录侧叙述，帮助系统解释是常见登录噪声、运维访问、异常认证行为，还是需要进一步追查的可疑登录图景。

### 3. 典型输入

- 登录日志、认证事件、失败原因和结果状态
- 与账号、OTP、来源地址和时间窗相关的材料
- 包含 `username`、`source_ip`、`result`、`failure_reason`、`otp`、`timestamp` 等字段的认证记录
- JumpServer 登录表、堡垒机登录导出、VPN/SSO/认证代理导出的访问记录
- 与命令执行、文件传输或身份策略材料联合进入综合报告前的单源登录样本

### 4. 输出契约

- 登录侧摘要
- 失败模式与重点账户
- 登录异常的复核建议
- 需要在页面与导出中保留登录总量、成功/失败模式、重点账号和关键来源说明
- 若存在明显时间窗或批量失败模式，应解释它们为何值得关注，而不是只列计数
- 不应把所有失败登录都写成暴力破解，也不应把代理地址直接当攻击源

### 5. 触发与路由

当输入属于登录、认证、OTP 或访问结果材料时命中本 Skill，也可作为 JumpServer 多源综合的单源子能力。若同批输入的核心已经转向命令、文件传输或管理平面，就应交由对应 JumpServer 子 Skill 处理，而不是继续扩张到非登录判断。

### 6. 判断边界

- 不能把代理地址直接当攻击源。
- 不因单次失败直接认定爆破或外部入侵。
- 对共享跳板机、VPN 出口、企业 NAT、代理节点，应优先保留“来源需结合网络边界复核”的描述。
- 若没有账号基线、时间窗和成功/失败比例，结论不能越界成“账号失陷已确认”。

### 7. 上下游关系

- 上游常来自登录记录、认证导出或 JumpServer 登录表。
- 下游可直接生成登录审计报告，也可作为 `jumpserver_multi_source_review` 的登录侧输入。
- 若允许 Gemini 增强，也仅限综合结论和专业判断段，不改写登录统计事实。

### 8. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计（登录侧子能力）](../training_cases/case_002_jumpserver_multisource/README.md)

### 9. 常见失败模式

- 把 NAT/代理地址直接写成攻击源。
- 只看到失败次数多就写成爆破，不结合账号分布和时间窗。
- 忽略成功登录和失败登录的关系，导致登录侧判断失真。

### 10. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 11. 维护要求

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

Analyze login outcomes, failure patterns, and anomalous access behavior to produce login-side risk judgments. This Skill should organize account, source, result, and timing evidence into a coherent login narrative that explains whether the pattern looks like routine access noise, admin activity, or genuinely suspicious authentication behavior requiring follow-up.

### 3. Typical Inputs

- login logs, authentication events, failure reasons, and result states
- materials related to accounts, OTP, source addresses, and time windows
- authentication records containing fields such as `username`, `source_ip`, `result`, `failure_reason`, `otp`, and `timestamp`
- JumpServer login tables, bastion login exports, VPN/SSO/auth-proxy access records
- single-source login samples that will later join command, transfer, or policy evidence in composite review

### 4. Output Contract

- login-side summary
- failure patterns and focus accounts
- review guidance for anomalous access
- page and export outputs should preserve login volume, success/failure patterns, focus accounts, and key source explanations
- where time-window or batch-failure patterns stand out, the Skill should explain why they matter instead of only listing counts
- it must not rewrite every failed login as brute force, nor treat proxy addresses as direct attack origin

### 5. Trigger and Routing

This Skill is selected for login, authentication, OTP, or access-result material, and also serves as a single-source component for JumpServer composite review. If the batch center shifts toward command audit, transfer audit, or control-plane events, the corresponding neighboring Skill should take over that slice.

### 6. Decision Boundaries

- Proxy addresses must not be treated directly as attack origin.
- A single failure must not be treated as proof of brute force or external intrusion.
- Shared bastions, VPN egress, enterprise NAT, and proxy nodes should be described as “source requires network-boundary review.”
- Without account baseline, time-window context, and success/failure ratio, the conclusion must not escalate to confirmed account compromise.

### 7. Upstream and Downstream Relationships

- Upstream commonly comes from login records, auth exports, or JumpServer login tables.
- Downstream it can generate standalone login audit output or feed the login-side section of `jumpserver_multi_source_review`.
- If Gemini enhancement is allowed, it must remain limited to final judgment sections and must not rewrite login statistics.

### 8. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit (login-side sub-capability)](../training_cases/case_002_jumpserver_multisource/README.md)

### 9. Common Failure Modes

- Treating NAT or proxy IPs as the definitive attack origin.
- Concluding brute force from failure count alone without checking account distribution or timing.
- Ignoring the relationship between successful and failed logins, which distorts the access judgment.

### 10. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 11. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
