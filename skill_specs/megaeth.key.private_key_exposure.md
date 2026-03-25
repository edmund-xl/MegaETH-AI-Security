# Skill Specification: `megaeth.key.private_key_exposure`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.key.private_key_exposure`
- 所属模块：`Key Security`
- 适用产品域：`安全日志分析`
- 对应事件类型：`secret_exposure`
- 当前执行模式：规则主链

### 2. 能力目的

识别明文私钥、助记词和高敏感密钥材料暴露，形成高优先级处置建议。

它是 Key Security 模块中最强调“立即响应”的 Skill，重点是快速识别高敏感密钥材料暴露并给出处置优先级，而不是判断是否已经发生链上或业务损害。

### 3. 典型输入

- 代码、配置、命令行参数、日志片段
- 任何可能包含高敏感密钥材料的明文内容

常见输入形态包括：

- 代码片段
- 配置文件
- shell 历史或命令行参数
- 日志与明文转储

### 4. 输出契约

- 高风险密钥暴露告警
- 证据位置与材料来源
- 紧急处置建议
- 不越界的高紧急性提示

### 5. 触发与路由

当输入被识别为秘密信息暴露，且命中的是高敏感密钥材料时命中本 Skill。

如果命中对象更像普通令牌、一般密码或环境变量片段，应由更通用的 secret 类 Skill 处理，而不是默认落在本 Skill。

### 6. 判断边界

- 默认按高风险处理，但仍需人工确认场景真实性。
- 不自动判断密钥是否已被利用。
- 不能把“疑似私钥暴露”直接写成“密钥已失窃并被使用”。
- 不能越界做资产归属和攻击结果判断。

### 7. 训练与参考资产

- 暂无正式案例。

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。
- 当前还没有正式案例，因此最需要通过真实样本收敛误报与处置语言。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。
- 一旦引入正式案例，必须同步更新：
  - 训练案例文档
  - 技能页训练统计
  - 相关 Key Security 文档

## English

### 1. Basics

- Skill ID: `megaeth.key.private_key_exposure`
- Module: `Key Security`
- Product Surface: `Security Log Analysis`
- Event Type: `secret_exposure`
- Execution Mode: rule-first

### 2. Purpose

Detect exposed private keys, seed phrases, and high-sensitivity key material and produce high-priority containment guidance.

### 3. Typical Inputs

- code, configuration, command-line parameters, and log snippets
- any plain-text content that may contain highly sensitive key material

### 4. Output Contract

- high-risk key-exposure alerts
- evidence location and material origin
- urgent containment recommendations

### 5. Trigger and Routing

This Skill is selected when the input is recognized as secret exposure and the hit involves highly sensitive key material.

### 6. Decision Boundaries

- Hits default to high risk but still require human confirmation of the surrounding scenario.
- It does not automatically conclude the key has already been abused.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
