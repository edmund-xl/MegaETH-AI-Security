# Skill Specification: `megaeth.appsec.whitebox_recon`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.appsec.whitebox_recon`
- 所属模块：`AppSec`
- 适用产品域：`安全日志分析`
- 对应事件类型：`whitebox_recon_assessment`
- 当前执行模式：规则主链，必要时可增强侦察结论文案

### 2. 能力目的

对白盒侦察材料做结构化解读，形成可供后续验证的候选问题、攻击面摘要和验证方向。

### 3. 典型输入

- 代码片段、目录树、配置文件或接口定义
- 侦察记录、模块说明、架构草图
- 与业务逻辑相关的关键路径说明

### 4. 输出契约

- 侦察结论与候选问题列表
- 需要进入验证阶段的关键路径
- 针对验证阶段的优先检查建议

### 5. 触发与路由

当输入被归类为白盒侦察材料，且核心信息仍处于“待验证”状态时命中本 Skill。它不负责生成最终交付报告，而是为验证和综合报告提供上游结论。

### 6. 判断边界

- 侦察阶段不直接确认最终漏洞成立。
- 没有证据的推断只能作为候选线索，不能直接升级为 confirmed finding。

### 7. 训练与参考资产

- [Whitebox AppSec 模板](../training_cases/templates/appsec_whitebox_case_template/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.appsec.whitebox_recon`
- Module: `AppSec`
- Product Surface: `Security Log Analysis`
- Event Type: `whitebox_recon_assessment`
- Execution Mode: rule-first, with optional enhancement for reconnaissance narrative only

### 2. Purpose

Interpret whitebox reconnaissance material into candidate issues, attack-surface summaries, and follow-up validation directions.

### 3. Typical Inputs

- code snippets, directory trees, configuration files, or API definitions
- recon notes, module descriptions, and architecture sketches
- business-logic path explanations

### 4. Output Contract

- recon conclusions and candidate issues
- priority paths that should move into validation
- recommended next checks for the validation stage

### 5. Trigger and Routing

This Skill is selected when the input is classified as whitebox reconnaissance and the core findings are still in a pre-validation state. It does not generate the final delivery report; it feeds validation and synthesis stages.

### 6. Decision Boundaries

- The reconnaissance stage must not confirm final vulnerabilities on its own.
- Unverified reasoning may remain as candidate signals but must not be upgraded into confirmed findings.

### 7. Training and Reference Assets

- [Whitebox AppSec template](../training_cases/templates/appsec_whitebox_case_template/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
