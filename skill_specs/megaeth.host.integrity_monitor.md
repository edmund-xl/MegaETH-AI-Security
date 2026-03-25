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

它是 Host 模块中的“完整性与控制状态” Skill，负责把主机治理中的结构性风险从纯基线合规结果里进一步拆分出来。

### 3. 典型输入

- 主机完整性材料、控制状态材料、基线缺口材料
- 与文件、服务、账号或关键控制缺失相关的记录

常见输入形态包括：

- 控制状态记录
- 主机完整性摘要
- 关键服务、文件或账号相关的控制缺失线索

### 4. 输出契约

- 完整性风险摘要
- 关键控制缺失
- 后续复核建议
- 不越界的完整性判断

### 5. 触发与路由

当材料更偏控制完整性和主机稳定性，而不是单一二进制事件时命中本 Skill。

它与 `baseline_compliance_analysis` 同属 Host 域，但更强调控制状态和完整性，而不是合规差距总览。

### 6. 判断边界

- 侧重控制完整性，不直接认定恶意篡改。
- 需要与其他主机侧证据联合判断。
- 不能因为完整性缺失就直接写成主机已失陷。
- 不能替代真正的篡改取证或异常行为分析。

### 7. 训练与参考资产

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。
- 当前它与 Host baseline 一起构成主机治理分析，但二者不应混成同一种报告语义。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。
- 若完整性缺失分类、关键控制集合或报告结构变化，必须同步检查：
  - Host 相关案例
  - 页面摘要
  - 导出报告

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

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
