# `megaeth.host.baseline_compliance_analysis`

## 中文

### 基本信息

- 中文名称：MegaETH 主机基线合规分析能力
- 模块：Host
- 当前状态：已接入，已完成 `training_case_001_host_baseline`

### 作用

这是主机基线配置风险分析的核心 Skill。它把 `riskanalytics` 类材料从泛化主机完整性分析提升为专门的主机基线配置风险判断。

### 典型输入

- Host Risk Analytics CSV
- 主机安全基线评估结果
- `riskanalytics` 类导出

### 当前触发线索

- `发现名称`
- `风险评分`
- `/var/log/audit`
- `/var/tmp`
- `未安装 auditd`
- `cramfs`
- `udf`

### 当前输出重点

- 文件系统隔离配置问题
- 临时目录配置问题
- 日志权限与审计配置问题
- 不必要文件系统模块

### 当前训练结果

- 分类：
  - `host_risk_analytics`
  - `host_baseline_assessment`
- 风险语义：
  - 默认中风险
  - 配置弱点，不等于正在遭受攻击
- 当前报告以中文为主，并贴合 case 001 样本风格

### 已同步训练案例

- 案例：
  [training_case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- 样本解读：
  [training_case_001_host_baseline.md](../training_cases/case_001_host_baseline/training_case_001_host_baseline.md)
- 目标报告样本：
  [host_baseline_analysis_report.md](../training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- 系统规则样本：
  [host_baseline_system_rules.md](../training_cases/case_001_host_baseline/host_baseline_system_rules.md)

### Case 001 映射要求

- Primary Skill：
  - `megaeth.host.baseline_compliance_analysis`
- Secondary Skill：
  - `megaeth.host.integrity_monitor`
- Optional Skill：
  - `megaeth.host.systemd_service_risk`

### Case 001 Finding 聚合要求

- CSV 每一行不能直接作为最终 finding
- 必须聚合成以下关键问题类型：
  - `filesystem isolation issues`
  - `temporary directory configuration`
  - `log permission configuration`
  - `unused filesystem modules`

### Case 001 风险提升条件

- 默认风险等级：`medium`
- 当满足以下任一条件时提升优先级：
  - `environment = production`
  - `asset_role = sequencer`
  - `asset_role = signer`

### Case 001 报告要求

- 报告语言：中文优先
- 报告语义：
  - 主机安全基线配置风险
  - 不描述成实时入侵事件
- 报告结构应贴近样本：
  - 结论判断
  - 关键安全发现
  - 综合风险评估
  - 建议行动

### 当前限制

- 仍然主要覆盖 Unix / Linux 基线类问题
- 对更复杂的角色上下文和资产重要性提升逻辑还可继续细化

### 迭代方向

- 增加更多基线类别
- 加强“关键生产角色”与“普通资产”的风险分层

## English

### Basics

- Name: MegaETH Baseline Compliance Analysis
- Module: Host
- Status: Active, trained with `training_case_001_host_baseline`

### Purpose

This is the primary Skill for host baseline configuration risk. It upgrades `riskanalytics` materials from generic host integrity review into dedicated host baseline posture assessment.

### Typical Inputs

- Host Risk Analytics CSV
- host security baseline assessment output
- `riskanalytics`-style exports

### Current Triggers

- `发现名称`
- `风险评分`
- `/var/log/audit`
- `/var/tmp`
- `未安装 auditd`
- `cramfs`
- `udf`

### Current Outputs

- filesystem isolation issues
- temporary directory configuration issues
- logging and audit control issues
- unnecessary filesystem modules

### Current Training Outcome

- classification:
  - `host_risk_analytics`
  - `host_baseline_assessment`
- risk semantics:
  - default medium
  - configuration weakness, not active compromise
- current report style is Chinese-first and aligned to case 001

### Synced Training Case

- Case:
  [training_case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- Sample interpretation:
  [training_case_001_host_baseline.md](../training_cases/case_001_host_baseline/training_case_001_host_baseline.md)
- Target report sample:
  [host_baseline_analysis_report.md](../training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- System rules sample:
  [host_baseline_system_rules.md](../training_cases/case_001_host_baseline/host_baseline_system_rules.md)

### Case 001 Mapping Requirements

- Primary Skill:
  - `megaeth.host.baseline_compliance_analysis`
- Secondary Skill:
  - `megaeth.host.integrity_monitor`
- Optional Skill:
  - `megaeth.host.systemd_service_risk`

### Case 001 Finding Aggregation Rules

- CSV rows should not become findings directly
- they should be grouped into:
  - `filesystem isolation issues`
  - `temporary directory configuration`
  - `log permission configuration`
  - `unused filesystem modules`

### Case 001 Risk Escalation Conditions

- default risk: `medium`
- raise priority when any of these is true:
  - `environment = production`
  - `asset_role = sequencer`
  - `asset_role = signer`

### Case 001 Reporting Requirements

- report language: Chinese first
- report semantics:
  - host baseline configuration risk
  - not a live intrusion event
- report shape should follow the sample:
  - assessment
  - key findings
  - overall risk evaluation
  - recommended actions

### Current Limits

- focused mainly on Unix / Linux baseline issues today
- role-aware prioritization can still be refined

### Iteration Direction

- add more baseline categories
- improve prioritization for critical production roles versus normal assets
