# Skill Specification: `megaeth.identity.jumpserver_command_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.jumpserver_command_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`jumpserver_command_review`
- 当前执行模式：规则主链，必要时可增强 assessment 与 professional judgment

### 2. 能力目的

分析 JumpServer 命令审计日志，识别高风险命令语义、关键账户和操作链线索。

它是 JumpServer 单文件链里最容易被误读的 Skill，重点不是统计命令数量，而是从命令事实中提取需要会话级复核的危险操作语义。

### 3. 典型输入

- JumpServer 命令审计导出
- 包含命令、账号、资产、会话和时间信息的审计材料

常见输入形态包括：

- `command_*.xlsx`
- 带账号、资产、命令、会话、时间字段的导出

### 4. 输出契约

- 高风险命令摘要
- 重点账户与资产
- 需要会话级复核的操作链
- 去噪后的有效命令视角

### 5. 触发与路由

当材料来源于 JumpServer 命令审计导出，或被识别为命令侧单文件样本时命中本 Skill。

当同批次同时存在登录、命令、文件传输和管理平面材料时，本 Skill 仍应先独立产出结果，再交由多源综合 Skill 收口。

### 6. 判断边界

- 单条 sudo、systemctl、curl|bash 不是最终结论。
- 必须先去噪，再解释风险语义。
- 命令危险性需要结合账号、资产和上下文解释。
- 单文件命令判断不能替代多源综合判断。

### 7. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。
- 当前它既用于单文件报告，也作为 JumpServer 多源综合链的重要事实输入。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。
- 若命令去噪、危险命令识别或上下文字段变化，必须同步检查：
  - 单文件命令报告
  - 多源综合报告中的命令链摘要

## English

### 1. Basics

- Skill ID: `megaeth.identity.jumpserver_command_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `jumpserver_command_review`
- Execution Mode: rule-first, with optional enhancement for assessment and professional judgment

### 2. Purpose

Analyze JumpServer command-audit logs to identify risky command semantics, key operators, and operation-chain clues.

### 3. Typical Inputs

- JumpServer command-audit exports
- audit material containing commands, accounts, assets, sessions, and timestamps

### 4. Output Contract

- high-risk command summary
- focus accounts and assets
- operation chains that require session-level review

### 5. Trigger and Routing

This Skill is selected for JumpServer command-audit exports or other materials classified as command-side single-source samples.

### 6. Decision Boundaries

- A single sudo, systemctl, or curl|bash line is not a final conclusion.
- Noise reduction must happen before risk semantics are interpreted.

### 7. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
