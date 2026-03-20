# AppSec Whitebox Case Template

## 中文版

### 作用

这是一份用于后续白盒应用安全训练的标准案例模板。

每当你给我一个新的白盒应用安全案例时，建议都按这个目录结构整理。这样训练完成后，可以稳定同步到：
- 对应的 AppSec Skill
- 对应测试
- 对应案例索引
- 对应报告风格要求

### 建议目录内容

- `sample_interpretation.md`
  - 你对原始材料的解读
- `target_report.md`
  - 你认可的目标报告样式
- `system_rules.md`
  - 你希望系统遵守的分类、风险和报告规则
- `notes.md`
  - 额外补充说明，可选

### 训练时要明确的内容

- 材料属于哪一阶段
  - `whitebox_recon_assessment`
  - `whitebox_exploit_validation`
  - `whitebox_security_report`
- 正确的 Skill
  - `megaeth.appsec.whitebox_recon`
  - `megaeth.appsec.whitebox_exploit_validation`
  - `megaeth.appsec.whitebox_report_synthesis`
- 正确风险语义
  - 侦察线索
  - 已确认问题
  - 候选问题
  - 综合治理报告

### 推荐命名方式

- `case_101_appsec_recon_<topic>`
- `case_102_appsec_validation_<topic>`
- `case_103_appsec_report_<topic>`

这样后面 EASM、Host、Endpoint、AppSec 各类训练案例都可以并行演进，同时保持清晰。

---

## English Version

### Purpose

This is the standard template for future whitebox application security training cases.

When you provide a new whitebox AppSec case, it should ideally follow this structure so the result can be synced into:
- the matching AppSec Skill
- the matching tests
- the case index
- the target report style

### Suggested Directory Contents

- `sample_interpretation.md`
  - your interpretation of the raw material
- `target_report.md`
  - the report style you want the system to match
- `system_rules.md`
  - the classification, risk, and reporting rules the system should follow
- `notes.md`
  - optional extra notes

### What To Define During Training

- which stage the material belongs to
  - `whitebox_recon_assessment`
  - `whitebox_exploit_validation`
  - `whitebox_security_report`
- which Skill should own it
  - `megaeth.appsec.whitebox_recon`
  - `megaeth.appsec.whitebox_exploit_validation`
  - `megaeth.appsec.whitebox_report_synthesis`
- the correct risk semantics
  - recon lead
  - confirmed issue
  - candidate issue
  - synthesis / governance report

### Suggested Naming Pattern

- `case_101_appsec_recon_<topic>`
- `case_102_appsec_validation_<topic>`
- `case_103_appsec_report_<topic>`

This keeps AppSec training compatible with the rest of the MegaETH case library.
