# Skill Specification: `megaeth.host.integrity_monitor`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.integrity_monitor`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`host_integrity / host_baseline_assessment`
- 当前执行模式：规则主链

### 2. 能力目的

识别主机完整性、关键控制缺失和高风险变更迹象，补充主机治理视图。

### 3. 典型输入

- 主机完整性材料、控制状态材料、基线缺口材料
- 与文件、服务、账号或关键控制缺失相关的记录

### 4. 输出契约

- 完整性风险摘要
- 关键控制缺失
- 后续复核建议

### 5. 触发与路由

当材料更偏控制完整性和主机稳定性，而不是单一二进制事件时命中本 Skill。

### 6. 判断边界

- 侧重控制完整性，不直接认定恶意篡改。
- 需要与其他主机侧证据联合判断。

### 7. 训练与参考资产

- [Case 001 - Host Baseline](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.host.integrity_monitor`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `host_integrity / host_baseline_assessment`
- Execution Mode: rule-first

### 2. Purpose

Identify host integrity gaps, missing critical controls, and high-risk change indicators to enrich host-governance analysis.

### 3. Typical Inputs

- host integrity material, control-state material, and baseline-gap evidence
- records related to files, services, accounts, or missing critical controls

### 4. Output Contract

- integrity-risk summary
- missing critical controls
- follow-up review recommendations

### 5. Trigger and Routing

This Skill is selected when the material is more about control integrity and host stability than a single binary event.

### 6. Decision Boundaries

- It focuses on control integrity and must not directly conclude malicious tampering.
- It should be interpreted together with other host-side evidence.

### 7. Training and Reference Assets

- [Case 001 - Host Baseline](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
