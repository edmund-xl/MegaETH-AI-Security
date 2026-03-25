# Host Baseline 系统规则
<!-- security-log-analysis mainline -->

## 1. 分类规则

- Host baseline 材料应优先进入 `host_baseline_assessment`
- 不应误分为通用主机入侵事件

## 2. 报告规则

- 以合规缺口、控制完整性和优先整改为主要输出
- 对风险评分较高的缺口进行主题归并
- 不将基线缺口直接写成攻击结论

## 3. 技能规则

- 主 Skill：`megaeth.host.baseline_compliance_analysis`
- 支撑 Skill：`megaeth.host.integrity_monitor`
