# Skill Specification: `megaeth.identity.jumpserver_multi_source_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.jumpserver_multi_source_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`jumpserver_multi_source_audit`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

### 2. 能力目的

将登录、命令、文件传输和操作记录合并为跨源操作链，输出固定结构的综合审计报告。

### 3. 典型输入

- 同批次 JumpServer 多文件样本

### 4. 主要输出

- 固定结构综合报告
- 重点账户与高风险链
- 综合判断

### 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

### 6. 判断边界

- 不直接默认外部入侵已成立
- 必须保留模板结构与判断边界

### 7. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md)

### 8. 当前限制

- 当前实现以本地规则与样本驱动为主
- 输出质量受输入材料完整度影响
- 重要边界应优先由案例和目标输出驱动收敛

### 9. 维护要求

- 当分类、输出结构或风险语义发生变化时，必须同步更新本文件
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档

## English

### 1. Basics

- Skill ID: `megaeth.identity.jumpserver_multi_source_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `jumpserver_multi_source_audit`
- Execution Mode: rule-first, with controlled augmentation only where explicitly allowed

### 2. Purpose

Merge login, command, file-transfer, and operation-audit sources into a cross-source operations chain and output a fixed-format composite audit report.

### 3. Typical Inputs

- JumpServer multi-file batches from the same upload

### 4. Primary Outputs

- fixed-structure composite report
- key accounts and high-risk chains
- overall judgment

### 5. Trigger and Routing

This Skill is routed by the Planner using `event_type` and `source_type`. When a case or learning rule requires routing changes, update all of the following together:

- `app/core/planner.py`
- `app/skills/implementations.py`
- this Skill specification
- the linked training-case document

### 6. Decision Boundaries

- does not default to confirmed external intrusion
- must preserve the report template and judgment boundary

### 7. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md)

### 8. Current Limits

- the current implementation is primarily rule- and sample-driven
- output quality depends on the completeness of the supplied material
- important boundaries should be converged through cases and target outputs

### 9. Maintenance Requirements

- update this file whenever classification, output structure, or risk semantics change
- create or update a matching document under `training_cases/` when new real samples are introduced
