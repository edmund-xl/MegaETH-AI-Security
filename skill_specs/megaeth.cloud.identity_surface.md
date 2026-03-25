# Skill 规格说明：`megaeth.cloud.identity_surface`
<!-- security-log-analysis mainline -->

## 1. 基本信息

- Skill ID：`megaeth.cloud.identity_surface`
- 所属模块：`Cloud`
- 适用产品域：`安全日志分析`
- 对应事件类型：`cloud_config_change / kms_access`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

## 2. 能力目的

识别云身份暴露、权限边界与服务账号风险。

## 3. 典型输入

- IAM 配置
- 身份访问材料

## 4. 主要输出

- 身份暴露风险
- 权限边界问题
- 建议动作

## 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

## 6. 判断边界

- 重点解释身份面和授权面，不替代完整 IAM 审计

## 7. 训练与参考资产

- 当前暂无正式案例，后续新增样本时应同步建立案例文档。

## 8. 当前限制

- 当前实现以本地规则与样本驱动为主
- 输出质量受输入材料完整度影响
- 重要边界应优先由案例和目标输出驱动收敛

## 9. 维护要求

- 当分类、输出结构或风险语义发生变化时，必须同步更新本文件
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档
