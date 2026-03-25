# Skill 规格说明：`megaeth.easm.external_intelligence`
<!-- security-log-analysis mainline -->

## 1. 基本信息

- Skill ID：`megaeth.easm.external_intelligence`
- 所属模块：`EASM`
- 适用产品域：`安全日志分析`
- 对应事件类型：`external_asset`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

## 2. 能力目的

汇总外部情报、暴露信号和补充上下文，支撑外部面判断。

## 3. 典型输入

- 情报材料
- 开放源信息

## 4. 主要输出

- 外部情报摘要
- 风险提示
- 后续验证方向

## 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

## 6. 判断边界

- 情报质量依赖输入来源，需要人工筛选可信度

## 7. 训练与参考资产

- 当前暂无正式案例，后续新增样本时应同步建立案例文档。

## 8. 当前限制

- 当前实现以本地规则与样本驱动为主
- 输出质量受输入材料完整度影响
- 重要边界应优先由案例和目标输出驱动收敛

## 9. 维护要求

- 当分类、输出结构或风险语义发生变化时，必须同步更新本文件
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档
