# Skill Specification: `megaeth.host.binary_tamper_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.binary_tamper_review`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`host_integrity`
- 当前执行模式：规则主链

### 2. 能力目的

分析二进制替换、文件篡改和高风险落地行为，解释主机完整性破坏风险。

### 3. 典型输入

- 主机完整性记录、文件校验差异、二进制替换线索
- 涉及落地文件、替换路径和发布时间的材料

### 4. 输出契约

- 篡改风险摘要
- 可疑文件与路径
- 复核动作与时间窗说明

### 5. 触发与路由

当材料核心重心是文件替换、二进制落地、路径变更或完整性校验异常时命中本 Skill。

### 6. 判断边界

- 需要结合文件来源、发布时间和宿主环境复核。
- 不自动判定攻击成功。

### 7. 训练与参考资产

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.host.binary_tamper_review`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `host_integrity`
- Execution Mode: rule-first

### 2. Purpose

Analyze binary replacement, file tampering, and risky dropped-artifact behavior to explain host-integrity compromise risk.

### 3. Typical Inputs

- host integrity records, checksum drift, and binary-replacement clues
- materials covering dropped files, replacement paths, and release timing

### 4. Output Contract

- tamper-risk summary
- suspicious files and paths
- review actions and time-window explanations

### 5. Trigger and Routing

This Skill is selected when the material centers on file replacement, dropped binaries, path changes, or integrity-check anomalies.

### 6. Decision Boundaries

- The interpretation must be reviewed against file origin, release timing, and host context.
- It must not automatically conclude successful compromise.

### 7. Training and Reference Assets

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
