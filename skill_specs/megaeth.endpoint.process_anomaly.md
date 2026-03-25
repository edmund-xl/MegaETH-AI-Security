# Skill Specification: `megaeth.endpoint.process_anomaly`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.endpoint.process_anomaly`
- 所属模块：`Endpoint`
- 适用产品域：`安全日志分析`
- 对应事件类型：`process_alert`
- 当前执行模式：规则主链

### 2. 能力目的

分析进程异常、端点告警和可疑执行行为，输出可复核的主机侧风险判断。

### 3. 典型输入

- 端点平台告警、进程树、命令行与父子进程信息
- 与主机可疑执行行为相关的事件材料

### 4. 输出契约

- 异常进程摘要
- 高风险执行线索
- 复核和处置建议

### 5. 触发与路由

当材料核心重心是进程行为、执行链、父子进程或端点异常告警时命中本 Skill。

### 6. 判断边界

- 异常进程不自动等于入侵成立。
- 需要结合宿主机角色、时间窗和其他证据解释异常性。

### 7. 训练与参考资产

- 暂无正式案例。

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.endpoint.process_anomaly`
- Module: `Endpoint`
- Product Surface: `Security Log Analysis`
- Event Type: `process_alert`
- Execution Mode: rule-first

### 2. Purpose

Analyze process anomalies, endpoint alerts, and suspicious execution behavior to produce reviewable host-side risk judgments.

### 3. Typical Inputs

- endpoint alerts, process trees, command lines, and parent-child process data
- event material related to suspicious execution behavior on endpoints

### 4. Output Contract

- anomalous-process summary
- high-risk execution signals
- review and containment recommendations

### 5. Trigger and Routing

This Skill is selected when the material centers on process behavior, execution chains, parent-child process relations, or endpoint anomaly alerts.

### 6. Decision Boundaries

- An anomalous process does not automatically prove a confirmed intrusion.
- The anomaly should be interpreted together with host role, time window, and corroborating evidence.

### 7. Training and Reference Assets

- No formal case yet.

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
