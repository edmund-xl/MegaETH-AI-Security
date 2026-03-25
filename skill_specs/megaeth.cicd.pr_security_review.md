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

审查 Pull Request 或代码 diff 中可能引入的危险执行路径、敏感操作和供应链风险。

### 3. 典型输入

- PR 描述、代码 diff 和关键文件上下文
- 构建、部署、脚本或配置改动
- 与依赖、命令执行相关的变更

### 4. 输出契约

- 高风险代码片段
- 危险执行链摘要
- 人工复核建议

### 5. 触发与路由

当输入被识别为 PR 文本、代码 diff 或审查上下文时命中本 Skill，重点用于发布前安全复核。

### 6. 判断边界

- 不替代人工 Code Review。
- 未提供关键代码上下文时，不应虚构仓库行为。

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

- Skill ID: `megaeth.cicd.pr_security_review`
- Module: `CI/CD`
- Product Surface: `Security Log Analysis`
- Event Type: `github_pr`
- Execution Mode: rule-first

### 2. Purpose

Review pull requests or code diffs for dangerous execution paths, sensitive operations, and supply-chain risk.

### 3. Typical Inputs

- PR descriptions, code diffs, and key file context
- build, deploy, script, or configuration changes
- dependency and command-execution changes

### 4. Output Contract

- high-risk code segments
- dangerous execution-chain summaries
- manual review recommendations

### 5. Trigger and Routing

This Skill is selected for PR text, code diffs, and review context, especially for release-gating security review.

### 6. Decision Boundaries

- It does not replace human code review.
- When critical code context is missing, the Skill must not invent repository behavior.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
