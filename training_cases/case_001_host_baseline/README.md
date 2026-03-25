# Case 001：Host Baseline
<!-- security-log-analysis mainline -->

## 中文

### 1. 说明

本案例用于训练系统理解主机基线材料、风险评分与整改建议之间的关系，形成稳定的 Host 分析输出。

### 2. 分类目标

- `source_type = host`
- `event_type = host_baseline_assessment`

### 3. 对应 Skill

- `megaeth.host.baseline_compliance_analysis`
- `megaeth.host.integrity_monitor`

### 4. 训练重点

- 正确识别高风险基线缺口
- 区分配置缺口、完整性问题与服务面风险
- 输出中文合规分析结论与优先整改建议


## English

### 1. Description

This case trains the system to understand host baseline material, risk scoring, and remediation guidance, and to produce stable Host analysis outputs.

### 2. Target Classification

- `source_type = host`
- `event_type = host_baseline_assessment`

### 3. Owning Skills

- `megaeth.host.baseline_compliance_analysis`
- `megaeth.host.integrity_monitor`

### 4. Training Focus

- correctly identify high-risk baseline gaps
- distinguish configuration gaps, integrity issues, and service-surface risk
- produce Chinese compliance conclusions and prioritized remediation advice
