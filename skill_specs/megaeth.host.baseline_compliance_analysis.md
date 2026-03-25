# Skill Specification: `megaeth.host.baseline_compliance_analysis`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.baseline_compliance_analysis`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`host_baseline_assessment`
- 当前执行模式：规则主链

### 2. 能力目的

分析主机基线检查结果，输出合规缺口、风险分层和整改重点。

它是 Host 模块中的基线治理入口 Skill，重点是把检查结果转成可治理、可排序、可复核的合规分析结论。

### 3. 典型输入

- 主机基线报表、检查项结果、风险评分与发现名称
- 描述控制缺失、配置偏离和账户策略问题的材料

常见输入形态包括：

- 基线检查导出
- 控制项差距列表
- 账户与系统策略审计结果

### 4. 输出契约

- 基线缺口摘要
- 风险主题与优先整改项
- 适合治理场景的整改建议
- 可供治理方直接复核的结论摘要

### 5. 触发与路由

当输入被识别为主机基线报表、基线检查结果或合规差距材料时命中本 Skill。

它不应被其它 Host 风险类 Skill 替代，因为它更关注治理和控制缺口，而不是异常行为。

### 6. 判断边界

- 属于基线治理分析，不等同于入侵事件判断。
- 优先级需要结合资产重要性和控制覆盖解释。
- 不能把配置缺口直接写成“已被入侵”。
- 不能因为存在多个控制缺失就自动写成最高危事件。

### 7. 训练与参考资产

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。
- 当前它与 Host integrity 类 Skill 共同构成 Host 分析域，但职责边界不同，不应串线。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。
- 若基线分层、整改优先级或结论结构变化，必须同步检查：
  - Host case
  - 页面摘要
  - 导出报告

## English

### 1. Basics

- Skill ID: `megaeth.host.baseline_compliance_analysis`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `host_baseline_assessment`
- Execution Mode: rule-first

### 2. Purpose

Analyze host baseline results and produce compliance gaps, risk tiers, and remediation priorities.

### 3. Typical Inputs

- host baseline reports, check results, risk scores, and finding names
- materials describing missing controls, configuration drift, and account-policy issues

### 4. Output Contract

- baseline-gap summary
- risk themes and remediation priorities
- governance-oriented remediation recommendations

### 5. Trigger and Routing

This Skill is selected when the input is recognized as a host baseline report, baseline check result, or compliance-gap material.

### 6. Decision Boundaries

- This is baseline-governance analysis and is not equivalent to intrusion attribution.
- Priority should be explained with asset criticality and control coverage.

### 7. Training and Reference Assets

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
