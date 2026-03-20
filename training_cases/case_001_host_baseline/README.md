# Case 001 - Host Baseline Assessment

## 中文版

### 案例定位

这是当前系统已正式落地的第一个训练案例。

目标是把 `riskanalytics` 类主机基线扫描材料，从泛化的主机完整性分析，稳定映射到专门的主机基线安全评估链路。

### 原始材料

- 文件名：
  `megalabs_2026-03-15_riskanalytics.csv`
- 材料类型：
  Host / Baseline / Risk Analytics
- 当前系统目标分类：
  - `source_type = host_risk_analytics`
  - `event_type = host_baseline_assessment`

### 案例资产

- 样本解读：
  [training_case_001_host_baseline.md](./training_case_001_host_baseline.md)
- 目标报告样本：
  [host_baseline_analysis_report.md](./host_baseline_analysis_report.md)
- 系统规则样本：
  [host_baseline_system_rules.md](./host_baseline_system_rules.md)

### 当前系统目标输出

- 主 Skill：
  - `megaeth.host.baseline_compliance_analysis`
  - `megaeth.host.integrity_monitor`
- 风险等级：
  - 默认 `medium`
  - 关键生产角色继续提升
- 报告语言：
  - 中文
- 报告语义：
  - 主机安全基线配置风险
  - 非实时入侵事件

### 当前重点提炼方向

- 文件系统隔离
- 临时目录配置
- 日志权限配置
- 不必要文件系统模块

---

## English Version

### Positioning

This is the first fully landed training case in the system.

Its goal is to turn `riskanalytics`-style host baseline scan material from a generic host integrity path into a dedicated host baseline security assessment path.

### Raw Material

- Filename:
  `megalabs_2026-03-15_riskanalytics.csv`
- Material type:
  Host / Baseline / Risk Analytics
- Current target classification:
  - `source_type = host_risk_analytics`
  - `event_type = host_baseline_assessment`

### Case Assets

- Sample interpretation:
  [training_case_001_host_baseline.md](./training_case_001_host_baseline.md)
- Target report sample:
  [host_baseline_analysis_report.md](./host_baseline_analysis_report.md)
- System rules sample:
  [host_baseline_system_rules.md](./host_baseline_system_rules.md)

### Current Target System Output

- Primary Skills:
  - `megaeth.host.baseline_compliance_analysis`
  - `megaeth.host.integrity_monitor`
- Risk level:
  - `medium` by default
  - higher for critical production roles
- Report language:
  - Chinese
- Report semantics:
  - host security baseline configuration risk
  - not a live intrusion event

### Current Focus Areas

- filesystem isolation
- temporary directory configuration
- log permission configuration
- unnecessary filesystem modules
