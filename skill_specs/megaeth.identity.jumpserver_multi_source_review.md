# Skill Specification: `megaeth.identity.jumpserver_multi_source_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.jumpserver_multi_source_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`jumpserver_multi_source_audit`
- 当前执行模式：规则主链，必要时增强综合结论与专业判断

### 2. 能力目的

把 JumpServer 登录、命令、文件传输和管理平面记录合并成跨源操作链，输出固定结构综合审计报告。

### 3. 典型输入

- 同批次 JumpServer 多文件样本
- 登录、命令、文件传输和操作记录材料的组合

### 4. 输出契约

- 固定结构综合报告
- 重点账户与高风险链
- 综合判断与证据来源说明

### 5. 触发与路由

当 Planner 识别到同批次 JumpServer 多源材料时命中本 Skill。它负责综合，不替代各单文件 Skill 的独立分析。

### 6. 判断边界

- 不直接默认外部入侵已成立。
- 必须保留模板结构与判断边界，不能自由发挥成散文摘要。

### 7. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.identity.jumpserver_multi_source_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `jumpserver_multi_source_audit`
- Execution Mode: rule-first, with optional enhancement for composite judgment and professional narrative

### 2. Purpose

Merge JumpServer login, command, transfer, and control-plane records into cross-source operation chains and output a fixed composite audit report.

### 3. Typical Inputs

- JumpServer multi-file batches from the same upload
- combined login, command, file-transfer, and operation-audit materials

### 4. Output Contract

- fixed-structure composite report
- key accounts and high-risk chains
- overall judgment plus evidence-source explanation

### 5. Trigger and Routing

This Skill is selected when the Planner recognizes a same-batch multi-source JumpServer package. It owns the composite judgment and does not replace the single-source Skills.

### 6. Decision Boundaries

- It must not default to confirmed external intrusion.
- The fixed report structure and decision boundary must be preserved rather than turning into free-form prose.

### 7. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
