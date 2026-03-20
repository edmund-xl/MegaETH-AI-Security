# Training Workflow / 训练协作流程

## 中文版

### 目标

这份文档定义的是：以后你怎么给材料，我怎么把它训练进系统。目标不是一次性修一个 bug，而是让 MegaETH AI Security Platform 持续变准。

### 最佳协作方式

每次尽量围绕一类材料来训练，而不是把不同类型的文件混在一起。

推荐分类：
- EASM 类
- Endpoint / Incident 类
- Host / Baseline / Risk Analytics 类
- AppSec / Whitebox 类
- Cloud / IAM / KMS 类
- CI/CD / Repo / Secret / Dependency 类

### 每次训练最好提供什么

1. 原始材料
   - `csv / json / log / txt / md / pdf`
2. 你认为正确的分类
   - `source_type`
   - `event_type`
   - 应调用哪些 `skills`
3. 你认可的分析结论
   - 是否真实问题
   - 风险级别
   - 关键依据
   - 是否误报
   - 建议动作
4. 你不满意当前系统的地方
   - 分错类
   - skill 太浅
   - 报告抓错重点
   - 风险级别不对
- 报告太像模板

### AppSec / Whitebox 训练建议顺序

这类材料建议分三步训练，不要一上来就直接训综合报告：

1. `whitebox_recon_assessment`
   - 先训练攻击面、入口、鉴权边界、候选验证路径
2. `whitebox_exploit_validation`
   - 再训练哪些已经被确认，哪些仍是候选问题
3. `whitebox_security_report`
   - 最后再训练综合交付报告

模板目录：
- [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)

### 推荐输入模板

```text
文件：
<path>

正确分类：
source_type =
event_type =
skills =

正确结论：
- 是否真实问题：
- 风险级别：
- 关键依据：
- 是否误报：
- 建议动作：

当前系统哪里不对：
- ...
```

### 系统该怎么学习

每一轮训练，我会做四层修正：
1. 文件识别
2. 分类
3. 技能规划
4. 报告生成

报告层重点修正：
- 结论方向
- 风险级别
- 证据提炼
- 建议动作
- 输出风格

### 系统里已经支持的学习动作

- 自动学习：成功分析后写入 `memory_feedback` 和 auto-observation
- 规则沉淀：把稳定模式整理进对应 Skill spec、测试和案例文档
- 纠偏吸收：通过系统内已有纠偏流程和后续 case 训练继续修正

### 训练优先级建议

优先训练：
1. 容易误判但经常出现的文件
2. 你最常看的报告类型
3. 最难区分误报和真实问题的材料
4. 你最在意的输出风格

### 一次训练后的理想结果

- 相似材料分类更准
- 相似材料 skill 分配更准
- 报告不再跑偏到完全错误的方向
- Memory Rules / Feedback 有更干净的积累

### 当前已落地案例

#### Case 001

- 文件：`training_case_001_host_baseline`
- 案例目录：
  [training_cases/case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- 样本解读：
  [training_cases/case_001_host_baseline/training_case_001_host_baseline.md](../training_cases/case_001_host_baseline/training_case_001_host_baseline.md)
- 目标报告样本：
  [training_cases/case_001_host_baseline/host_baseline_analysis_report.md](../training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- 系统规则样本：
  [training_cases/case_001_host_baseline/host_baseline_system_rules.md](../training_cases/case_001_host_baseline/host_baseline_system_rules.md)
- 材料类型：Host / Baseline / Risk Analytics
- 当前系统目标输出：
  - `source_type = host_risk_analytics`
  - `event_type = host_baseline_assessment`
  - 主要能力：
    - `megaeth.host.baseline_compliance_analysis`
    - `megaeth.host.integrity_monitor`
  - 报告语言：中文
  - 报告结论：
    - 配置弱点 / 基线缺口
    - 默认中风险
    - 生产环境或关键角色继续升高

#### Case 002

- 文件：`jumpserver_training_template_and_enhanced_conclusion`
- 案例目录：
  [training_cases/case_002_jumpserver_multisource/README.md](../training_cases/case_002_jumpserver_multisource/README.md)
- 核心训练模板：
  [jumpserver_training_template_and_enhanced_conclusion.md](../training_cases/case_002_jumpserver_multisource/jumpserver_training_template_and_enhanced_conclusion.md)
- 当前系统目标输出：
  - `source_type = jumpserver`
  - `event_type = jumpserver_multi_source_audit`
  - 主要能力：
    - `megaeth.identity.jumpserver_multi_source_review`
    - `megaeth.identity.anomalous_access_review`
  - 支持的中间输入类型：
    - `login_auth`
    - `command_audit`
    - `file_transfer_audit`
    - `operation_audit`
  - 较早登录快照只作为补充样本，不重复计数
  - 报告语言：中文
  - 报告结论：
    - 高风险运维 / 调试链
    - 高风险待复核
    - 默认不直接确认外部入侵
  - 报告结构：
    - `综合结论`
    - `主要依据如下`
    - `重点高危操作账户与命令汇总`
    - `证据来源与导出链`
    - `综合判断`

---

## English Version

### Goal

This document defines how you provide materials and how I train them into the system. The goal is not to patch one bug at a time, but to continuously improve the platform’s accuracy.

### Best Collaboration Pattern

Train around one material family at a time rather than mixing unrelated file types.

Recommended buckets:
- EASM
- Endpoint / Incident
- Host / Baseline / Risk Analytics
- AppSec / Whitebox
- Cloud / IAM / KMS
- CI/CD / Repo / Secret / Dependency

### What To Provide Each Time

1. Raw material
   - `csv / json / log / txt / md / pdf`
2. Expected classification
   - `source_type`
   - `event_type`
   - expected `skills`
3. Expected conclusion
   - real issue or not
   - risk level
   - key evidence
   - false positive or not
   - recommended actions
4. What is wrong in the current system output

### Recommended AppSec / Whitebox Training Order

For AppSec whitebox material, it is better to train in three stages instead of starting with the final report:

1. `whitebox_recon_assessment`
   - attack surface, entry points, auth boundaries, and candidate validation paths
2. `whitebox_exploit_validation`
   - what is confirmed vs. what remains a candidate
3. `whitebox_security_report`
   - the final delivery-grade synthesis report

Template directory:
- [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)

### Recommended Template

```text
File:
<path>

Expected classification:
source_type =
event_type =
skills =

Expected conclusion:
- Real issue or not:
- Risk level:
- Key evidence:
- False positive or not:
- Recommended action:

What is wrong in the current system:
- ...
```

### How The System Should Learn

Each training round applies four layers of correction:
1. file recognition
2. classification
3. skill planning
4. report generation

The reporting layer focuses on:
- conclusion direction
- risk level
- evidence extraction
- recommended actions
- output style

### Learning Actions Already Supported

- Automatic learning through `memory_feedback` and auto-observation
- Rule consolidation into the matching Skill spec, tests, and case docs
- Ongoing correction through the current system workflow and later case training

### Training Priority

Prioritize:
1. frequently appearing files that are easy to misclassify
2. report types you review most often
3. materials where false positives and real issues are hardest to separate
4. the output style you care about most

### Ideal Result After One Training Round

- better classification for similar material
- better skill planning for similar material
- reports no longer drift into completely wrong directions
- cleaner accumulation in Memory Rules / Feedback

### Currently Landed Case

#### Case 001

- File: `training_case_001_host_baseline`
- Case directory:
  [training_cases/case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- Sample interpretation:
  [training_cases/case_001_host_baseline/training_case_001_host_baseline.md](../training_cases/case_001_host_baseline/training_case_001_host_baseline.md)
- Target report sample:
  [training_cases/case_001_host_baseline/host_baseline_analysis_report.md](../training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- System rules sample:
  [training_cases/case_001_host_baseline/host_baseline_system_rules.md](../training_cases/case_001_host_baseline/host_baseline_system_rules.md)
- Type: Host / Baseline / Risk Analytics
- Current target output:
  - `source_type = host_risk_analytics`
  - `event_type = host_baseline_assessment`
  - Primary skills:
    - `megaeth.host.baseline_compliance_analysis`
    - `megaeth.host.integrity_monitor`
  - Report language: Chinese
  - Report conclusion:
    - configuration weakness / baseline gap
    - medium risk by default
    - escalate further for production or critical roles
