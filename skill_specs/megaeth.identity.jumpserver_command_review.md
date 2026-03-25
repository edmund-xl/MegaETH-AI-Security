# Skill 规格说明：`megaeth.identity.jumpserver_command_review`
<!-- security-log-analysis mainline -->

## 1. 基本信息

- Skill ID：`megaeth.identity.jumpserver_command_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`jumpserver_command_review`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

## 2. 能力目的

分析 JumpServer 命令审计日志，识别高风险命令语义与操作链线索。

## 3. 典型输入

- JumpServer 命令审计导出

## 4. 主要输出

- 高风险命令摘要
- 操作账户与资产
- 复核建议

## 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

## 6. 判断边界

- 单条 sudo 或 systemctl 不是最终结论
- 命令噪声需要去噪处理

## 7. 训练与参考资产

- [Case 002 - JumpServer Multi-Source](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md)

## 8. 当前限制

- 当前实现以本地规则与样本驱动为主
- 输出质量受输入材料完整度影响
- 重要边界应优先由案例和目标输出驱动收敛

## 9. 维护要求

- 当分类、输出结构或风险语义发生变化时，必须同步更新本文件
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档
