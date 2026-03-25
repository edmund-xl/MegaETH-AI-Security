# Skill Specification: `megaeth.cicd.pr_security_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.cicd.pr_security_review`
- 所属模块：`CI/CD`
- 适用产品域：`安全日志分析`
- 对应事件类型：`github_pr`
- 当前执行模式：规则主链

### 2. 能力目的

审查 Pull Request 或代码 diff 中可能引入的危险执行路径、敏感操作和供应链风险。该 Skill 的职责是把“代码改动风险”写成可复核的发布前判断，而不是简单列出 diff 片段；它需要说明哪些改动改变了执行边界、凭据边界或供应链边界，以及为什么需要人工复核。

### 3. 典型输入

- PR 描述、代码 diff 和关键文件上下文
- 构建、部署、脚本或配置改动
- 与依赖、命令执行相关的变更
- GitHub PR 导出、补丁文本、关键文件前后对比、CI 配置改动
- 工作流文件、构建脚本、部署脚本、敏感配置、依赖锁文件的变更
- 与 secret detection、cloud config audit、whitebox report synthesis 联合引用的审查材料

### 4. 输出契约

- 高风险代码片段
- 危险执行链摘要
- 人工复核建议
- 应明确指出改动位置、潜在影响面、风险类型和建议复核动作
- 若材料足够，应区分“可疑但需上下文验证”“明显危险路径”“配置/供应链风险”
- 不应在缺少关键代码上下文时虚构应用行为或数据流

### 5. 触发与路由

当输入被识别为 PR 文本、代码 diff 或审查上下文时命中本 Skill，重点用于发布前安全复核。若输入已经是完整代码仓审计材料或白盒综合报告，则应交由 AppSec 白盒链处理，而不是让本 Skill 承担端到端设计分析。

### 6. 判断边界

- 不替代人工 Code Review。
- 未提供关键代码上下文时，不应虚构仓库行为。
- 不能仅凭敏感关键字就判定高危，必须结合改动位置、调用路径和运行边界。
- 对依赖升级、流程改名、模板更新等常见 CI 变更，应优先解释影响面，而不是直接写成供应链事件。

### 7. 上下游关系

- 上游常来自 GitHub PR、代码补丁或发布前审查工单。
- 下游可能进入发布门禁总结，也可能成为白盒综合报告中的“变更风险旁证”。
- 若未来引入 Gemini 增强，只允许增强摘要和专业判断，不得改写实际 diff 事实。

### 8. 训练与参考资产

- 暂无正式案例。

### 9. 常见失败模式

- 只抓危险关键字，不解释影响面和真实执行边界。
- 把正常依赖升级或 CI 模板更新写成已确认供应链事件。
- 忽略关键文件上下文，导致风险摘要和改动事实不一致。

### 10. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 11. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.cicd.pr_security_review`
- Module: `CI/CD`
- Product Surface: `Security Log Analysis`
- Event Type: `github_pr`
- Execution Mode: rule-first

### 2. Purpose

Review pull requests or code diffs for dangerous execution paths, sensitive operations, and supply-chain risk. The purpose of this Skill is to turn change risk into a release-gating security judgment, not to simply echo diff fragments; it should explain which edits alter execution boundaries, secret boundaries, or supply-chain boundaries and why they require manual review.

### 3. Typical Inputs

- PR descriptions, code diffs, and key file context
- build, deploy, script, or configuration changes
- dependency and command-execution changes
- GitHub PR exports, patch text, before/after file context, and CI config changes
- workflow files, build scripts, deploy scripts, sensitive configs, and lockfile changes
- review material that may later be cited by secret detection, cloud config audit, or whitebox synthesis

### 4. Output Contract

- high-risk code segments
- dangerous execution-chain summaries
- manual review recommendations
- it should clearly identify changed locations, likely blast radius, risk type, and recommended review action
- when input is sufficient, it should distinguish suspicious-but-context-dependent changes from clearly dangerous paths or supply-chain/config risk
- it must not invent application behavior or data flow when critical code context is missing

### 5. Trigger and Routing

This Skill is selected for PR text, code diffs, and review context, especially for release-gating security review. If the input is already a full codebase audit or whitebox synthesis package, the dedicated AppSec whitebox chain should take over instead of this Skill expanding beyond change review.

### 6. Decision Boundaries

- It does not replace human code review.
- When critical code context is missing, the Skill must not invent repository behavior.
- A sensitive keyword alone is not enough to declare high risk; the location, execution path, and runtime boundary must also be considered.
- Common CI changes such as dependency upgrades, workflow renames, or template refreshes should first be interpreted in context instead of being labeled as supply-chain incidents.

### 7. Upstream and Downstream Relationships

- Upstream commonly comes from GitHub PRs, patch exports, or release review work items.
- Downstream it may feed release-gating summaries or be quoted by whitebox synthesis as change-risk evidence.
- If Gemini enhancement is introduced later, it must remain limited to summary/judgment prose and never rewrite actual diff facts.

### 8. Training and Reference Assets

- No formal case yet.

### 9. Common Failure Modes

- Extracting scary keywords without explaining blast radius or actual execution boundary.
- Treating routine dependency upgrades or CI template changes as confirmed supply-chain events.
- Ignoring critical file context, which causes the summary to diverge from the actual diff.

### 10. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 11. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
