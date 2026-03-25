# Skill Specification: `megaeth.identity.jumpserver_transfer_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.jumpserver_transfer_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`jumpserver_transfer_review`
- 当前执行模式：规则主链，必要时可增强 transfer-chain judgment

### 2. 能力目的

分析 JumpServer 文件传输日志，识别上传、落地、放权与后续执行前链路。

### 3. 典型输入

- JumpServer 文件传输导出
- 与文件路径、账号、资产和时间相关的传输材料

### 4. 输出契约

- 传输摘要
- 高风险文件路径与文件名
- 与命令侧联动的复核建议

### 5. 触发与路由

当输入来源于 JumpServer 文件传输导出或被识别为文件传输单文件样本时命中本 Skill。

### 6. 判断边界

- 文件传输本身不等于恶意。
- 需要结合命令、时间窗和执行链判断风险。

### 7. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.identity.jumpserver_transfer_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `jumpserver_transfer_review`
- Execution Mode: rule-first, with optional enhancement for transfer-chain judgment

### 2. Purpose

Analyze JumpServer file-transfer logs to identify upload, landing, permission-change, and pre-execution chains.

### 3. Typical Inputs

- JumpServer file-transfer exports
- transfer material tied to file paths, accounts, assets, and timestamps

### 4. Output Contract

- transfer summary
- high-risk file names and paths
- review guidance linked to command-side activity

### 5. Trigger and Routing

This Skill is selected for JumpServer file-transfer exports or other material classified as a transfer-side single-source sample.

### 6. Decision Boundaries

- File transfer alone does not prove malicious behavior.
- Risk should be judged together with commands, time windows, and execution chains.

### 7. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
