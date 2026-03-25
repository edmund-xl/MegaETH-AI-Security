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

分析授权策略、账号边界和访问控制风险，解释策略层面的边界问题。该 Skill 的价值在于把“权限事实”翻译成“边界风险”：它要说明哪些策略、角色或授权方式扩大了访问面，为什么这些配置对资产控制或审计边界有影响，以及后续应如何收口。

### 3. 典型输入

- 策略配置、授权清单、身份边界材料
- 能描述账号、角色和授权关系的策略上下文
- IAM 策略导出、角色绑定、组成员、AssumeRole/委派配置、权限矩阵
- JumpServer、云身份平台或企业权限系统的策略截图、导出表、文本配置
- 与高危账号、管理平面、云资源暴露需要联合解释的身份控制材料

### 4. 输出契约

- 策略风险摘要
- 边界问题
- 治理建议
- 应保留高风险主体、策略范围、资源范围和影响边界
- 若材料足够，应指出“横向越权”“管理员面扩大”“默认授权过宽”属于哪一种风险
- 不应在没有完整策略上下文时虚构真实可利用路径

### 5. 触发与路由

当材料核心重心是账号策略、授权边界或身份控制面，而不是单一登录记录时命中本 Skill。若输入更偏登录异常、命令执行或管理操作审计，则应由 Identity/JumpServer 其它 Skill 负责。

### 6. 判断边界

- 属于授权面分析，不替代主机执行证据。
- 策略风险必须与实际使用场景一起解释。
- 仅凭管理员角色名或大权限标签，不足以证明风险成立，必须结合资源范围和主体职责。
- 没有策略上下文、资源边界或角色归属时，结论应停在“高风险配置需收敛”，不能写成“已形成利用链”。

### 7. 上下游关系

- 上游常来自云 IAM、JumpServer 授权策略、企业权限系统或身份面资产梳理。
- 下游可能进入综合身份风险结论，也可能在 EASM/Cloud 报告中作为权限边界证据被引用。
- 若未来接入 Gemini，也只能增强结论表达，不能改写策略事实和权限范围。

### 8. 训练与参考资产

- 暂无正式案例。

### 9. 常见失败模式

- 只见“管理员”就直接判高危，不解释主体职责和资源范围。
- 把过宽权限直接写成“已被利用”。
- 忽略默认继承、组成员关系和角色委派，导致边界描述不完整。

### 10. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 11. 维护要求

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

Analyze authorization policies, account boundaries, and access-control risk to explain policy-layer boundary issues. The value of this Skill is to translate permission facts into boundary risk: it should explain which policies, roles, or authorization models expand the access surface, why they matter for control or audit boundaries, and what tightening action is appropriate.

### 3. Typical Inputs

- policy configurations, authorization inventories, and identity-boundary material
- policy context describing accounts, roles, and authorization relationships
- IAM policy exports, role bindings, group membership, AssumeRole/delegation settings, and permission matrices
- policy screenshots, exported tables, or text configs from JumpServer, cloud identity platforms, or enterprise access systems
- identity-control material that must later be interpreted together with high-risk accounts, control-plane audit, or cloud exposure evidence

### 4. Output Contract

- policy-risk summary
- boundary issues
- governance recommendations
- it should preserve the high-risk principal, policy scope, resource scope, and impact boundary
- when possible, it should classify the risk as lateral overreach, management-plane expansion, or overly broad default authorization
- it must not invent an exploit path when complete policy context is missing

### 5. Trigger and Routing

This Skill is selected when the material centers on account policy, authorization boundary, or identity control planes rather than a single login record. If the input is actually centered on anomalous logins, command behavior, or admin-operation audit, the neighboring Identity/JumpServer Skill should own that slice instead.

### 6. Decision Boundaries

- It belongs to authorization-surface analysis and does not replace host-execution evidence.
- Policy risk must be interpreted with actual usage context.
- An administrator role label or broad-permission tag alone is not enough; the resource scope and principal responsibility must also be considered.
- Without policy context, resource boundaries, or role ownership, the conclusion should remain at “risky configuration requiring tightening,” not “confirmed exploitable chain.”

### 7. Upstream and Downstream Relationships

- Upstream commonly comes from cloud IAM, JumpServer authorization policy, enterprise access systems, or identity-surface inventory.
- Downstream it may feed composite identity-risk conclusions or be cited by Cloud/EASM reports as access-boundary evidence.
- If Gemini is introduced later, it must stay limited to narrative conclusions and never rewrite policy facts or permission scope.

### 8. Training and Reference Assets

- No formal case yet.

### 9. Common Failure Modes

- Declaring every admin principal high-risk without describing responsibility and scope.
- Turning overbroad permissions into “already exploited.”
- Ignoring inheritance, group membership, or delegation, which leaves the boundary description incomplete.

### 10. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 11. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
