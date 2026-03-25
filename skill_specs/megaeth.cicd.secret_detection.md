# Skill Specification: `megaeth.cicd.secret_detection`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.cicd.secret_detection`
- 所属模块：`CI/CD`
- 适用产品域：`安全日志分析`
- 对应事件类型：`secret_exposure`
- 当前执行模式：规则主链

### 2. 能力目的

识别代码、配置、提交内容和构建材料中的密钥、令牌与高敏感凭证暴露。

### 3. 典型输入

- 源码片段、配置文件、提交内容
- CI 日志、脚本参数、环境变量片段
- 可能包含凭证的明文材料

### 4. 输出契约

- 疑似秘密信息命中
- 暴露位置和材料来源
- 紧急处置与轮换建议

### 5. 触发与路由

当输入被识别为凭证暴露、密钥泄漏或高敏感参数暴露材料时命中本 Skill。

### 6. 判断边界

- 命中需要人工确认真实性与有效性。
- 不自动判断凭证是否仍然有效。

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

- Skill ID: `megaeth.cicd.secret_detection`
- Module: `CI/CD`
- Product Surface: `Security Log Analysis`
- Event Type: `secret_exposure`
- Execution Mode: rule-first

### 2. Purpose

Detect exposed keys, tokens, and sensitive credentials in code, configuration, commit content, and build artifacts.

### 3. Typical Inputs

- source snippets, configuration files, and commit content
- CI logs, script arguments, and environment-variable snippets
- plain-text materials that may contain credentials

### 4. Output Contract

- suspected secret hits
- exposure location and material origin
- urgent rotation and containment recommendations

### 5. Trigger and Routing

This Skill is selected when the input is recognized as credential exposure, key leakage, or high-sensitivity parameter exposure.

### 6. Decision Boundaries

- Hits require human confirmation for authenticity and validity.
- The Skill does not automatically conclude whether the credential is still active.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
