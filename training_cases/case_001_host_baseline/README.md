# Case 001：Host Baseline
<!-- security-log-analysis mainline -->

## 1. 案例目的

本案例用于训练系统理解主机基线材料、风险评分与整改建议之间的关系，形成稳定的 Host 分析输出。

## 2. 分类目标

- `source_type = host`
- `event_type = host_baseline_assessment`

## 3. 对应 Skill

- `megaeth.host.baseline_compliance_analysis`
- `megaeth.host.integrity_monitor`

## 4. 训练重点

- 正确识别高风险基线缺口
- 区分配置缺口、完整性问题与服务面风险
- 输出中文合规分析结论与优先整改建议

## 5. 参考资产

- [host_baseline_analysis_report.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/host_baseline_analysis_report.md)
- [host_baseline_system_rules.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/host_baseline_system_rules.md)
- [training_case_001_host_baseline.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/training_case_001_host_baseline.md)

## 6. 使用要求

未来新增同类主机基线样本时，应优先叠加到本案例及对应 Skill，而不是散落出新的独立规则。
