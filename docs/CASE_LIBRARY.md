# Case Library / 案例库

## 中文版

这份文档不是“案例列表展示墙”，而是给你快速判断两件事：
- 现在系统到底已经被哪些真实案例训过
- 后面新 case 应该按什么结构落进去

我一般会先看这里，再决定某个问题应该继续训老 Skill，还是该新开 case。

### 现在已经正式落地的案例

#### Case 001 - Host Baseline Assessment

这条 case 目前是最成熟的一条，也是后面训练风格的基线。

你如果要理解“一个 case 真正训进系统”是什么意思，就先看它：

- 案例目录：
  [training_cases/case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- 样本解读：
  [training_cases/case_001_host_baseline/training_case_001_host_baseline.md](../training_cases/case_001_host_baseline/training_case_001_host_baseline.md)
- 目标报告样本：
  [training_cases/case_001_host_baseline/host_baseline_analysis_report.md](../training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- 系统规则样本：
  [training_cases/case_001_host_baseline/host_baseline_system_rules.md](../training_cases/case_001_host_baseline/host_baseline_system_rules.md)
- 对应主 Skill：
  [megaeth.host.baseline_compliance_analysis.md](../skill_specs/megaeth.host.baseline_compliance_analysis.md)

这条 case 现在已经稳定带来这些结果：
- `riskanalytics` 类文件不再被泛化成普通 host integrity
- 会稳定命中：
  - `host_risk_analytics`
  - `host_baseline_assessment`
- 报告默认中文
- 风险语义是“配置弱点 / 基线缺口”，不是“实时入侵”
- finding 会聚合，而不是逐行抛原始记录

#### Case 002 - JumpServer Multi-Source Audit Review

这条 case 是 JumpServer 方向的第一个正式落点。

它的重点不是“看见危险命令就告警”，而是把登录、命令、文件传输、操作记录几类日志拼成一条会话级判断链。

- 案例目录：
  [training_cases/case_002_jumpserver_multisource/README.md](../training_cases/case_002_jumpserver_multisource/README.md)
- 核心训练模板：
  [jumpserver_training_template_and_enhanced_conclusion.md](../training_cases/case_002_jumpserver_multisource/jumpserver_training_template_and_enhanced_conclusion.md)
- 对应主 Skill：
  [megaeth.identity.jumpserver_multi_source_review.md](../skill_specs/megaeth.identity.jumpserver_multi_source_review.md)

这条 case 当前已经把系统拉到这一步：
- 支持 `xlsx` 类型的 JumpServer 审计文件
- 能识别：
  - `login_auth`
  - `command_audit`
  - `file_transfer_audit`
  - `operation_audit`
- 较早登录快照只作为补充样本，不再作为独立证据源重复计数
- 同一批上传时会额外生成：
  - `source_type = jumpserver`
  - `event_type = jumpserver_multi_source_audit`
- 报告默认不直接判定外部入侵，而是优先输出：
  - 高风险运维 / 调试链
  - 高风险待复核
  - 判断边界与后续动作
- 报告结构也已经固定成专属模板：
  - `综合结论`
  - `主要依据如下`
  - `重点高危操作账户与命令汇总`
  - `证据来源与导出链`
  - `综合判断`

### 怎么判断一个 case 算不算落地

我现在的标准很简单，不满足就不算：

1. 代码已经改了
2. 测试已经补了
3. 对应 Skill spec 已经更新
4. 案例目录里有样本、规则和目标输出
5. GitHub 已同步

这个顺序是前面踩坑之后定下来的。只改代码不补文档，后面一定会忘；只补文档不补测试，后面一定会退化。

### 后面新 case 我建议怎么放

如果你后面继续给我材料，最稳的结构还是：

```text
training_cases/
  case_xxx/
    README.md
    sample_interpretation.md
    target_report.md
    system_rules.md
    optional_raw_examples/
```

这样后面看一个 case，不用在聊天记录里翻来翻去。

### AppSec 这条线准备怎么进

AppSec 我已经预留了模板，不建议一上来就训“总报告”。更稳的顺序是：

1. Recon
2. Validation
3. Synthesis report

模板目录在这里：
- [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)

模板文件：
- [sample_interpretation.md](../training_cases/templates/appsec_whitebox_case_template/sample_interpretation.md)
- [target_report.md](../training_cases/templates/appsec_whitebox_case_template/target_report.md)
- [system_rules.md](../training_cases/templates/appsec_whitebox_case_template/system_rules.md)

我推荐这么做的原因很简单：如果前面两个子能力没训准，综合报告一定会漂。

---

## English Version

This file is not meant to be a decorative case catalog. It is here to answer two practical questions:
- which real cases have actually been trained into the system
- how new cases should be structured when they land

I usually check this file before deciding whether a problem should extend an existing Skill or become a new case.

### Landed case right now

#### Case 001 - Host Baseline Assessment

This is currently the most mature case and the best reference for how a case should be absorbed into the platform.

Start here if you want to see what “a case is truly landed” means:

- Case directory:
  [training_cases/case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- Sample interpretation:
  [training_cases/case_001_host_baseline/training_case_001_host_baseline.md](../training_cases/case_001_host_baseline/training_case_001_host_baseline.md)
- Target report sample:
  [training_cases/case_001_host_baseline/host_baseline_analysis_report.md](../training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- System rules sample:
  [training_cases/case_001_host_baseline/host_baseline_system_rules.md](../training_cases/case_001_host_baseline/host_baseline_system_rules.md)
- Primary Skill:
  [megaeth.host.baseline_compliance_analysis.md](../skill_specs/megaeth.host.baseline_compliance_analysis.md)

This case now gives the system a stable behavior:
- `riskanalytics` materials no longer fall back to generic host integrity handling
- they route to:
  - `host_risk_analytics`
  - `host_baseline_assessment`
- reports default to Chinese
- the conclusion is about configuration weakness / baseline gap, not active intrusion
- findings are aggregated instead of dumped row by row

### What counts as a landed case

My rule is simple. It does not count unless all of these are true:

1. the code changed
2. tests were added or updated
3. the matching Skill spec was updated
4. the case directory contains sample, rules, and target output
5. GitHub is synced

That rule exists because we already learned what happens when only one of those layers is updated.

### Recommended case structure for future work

The cleanest shape is still:

```text
training_cases/
  case_xxx/
    README.md
    sample_interpretation.md
    target_report.md
    system_rules.md
    optional_raw_examples/
```

This keeps training knowledge in the repository instead of scattering it across chat history.

### How AppSec cases should land

For AppSec, I do not recommend starting with the final synthesis report.

The more reliable order is:
1. Recon
2. Validation
3. Synthesis report

Template directory:
- [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)

Template files:
- [sample_interpretation.md](../training_cases/templates/appsec_whitebox_case_template/sample_interpretation.md)
- [target_report.md](../training_cases/templates/appsec_whitebox_case_template/target_report.md)
- [system_rules.md](../training_cases/templates/appsec_whitebox_case_template/system_rules.md)

The reason is straightforward: if the earlier sub-capabilities are still weak, the composite report will drift.
