# Skill 规格说明：`megaeth.host.integrity_monitor`
<!-- security-log-analysis mainline -->

## 1. 基本信息

- Skill ID：`megaeth.host.integrity_monitor`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`host_integrity / host_baseline_assessment`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

## 2. 能力目的

识别主机完整性、关键控制缺失和高风险变更迹象。

## 3. 典型输入

- 主机完整性材料
- 基线缺口材料

## 4. 主要输出

- 完整性风险摘要
- 关键控制缺失
- 复核建议

## 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

## 6. 判断边界

- 侧重控制完整性，不直接认定恶意篡改
- 需要与其他主机证据联合判断

## 7. 训练与参考资产

- [Case 001 - Host Baseline](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/README.md)

## 8. 当前限制

- 当前实现以本地规则与样本驱动为主
- 输出质量受输入材料完整度影响
- 重要边界应优先由案例和目标输出驱动收敛

## 9. 维护要求

- 当分类、输出结构或风险语义发生变化时，必须同步更新本文件
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档
