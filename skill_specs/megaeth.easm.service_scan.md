# Skill Specification: `megaeth.easm.service_scan`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.easm.service_scan`
- 所属模块：`EASM`
- 适用产品域：`安全日志分析`
- 对应事件类型：`service_exposure`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

### 2. 能力目的

分析开放端口、服务暴露和网络层可访问面。

### 3. 典型输入

- 服务扫描结果
- 端口与协议信息

### 4. 主要输出

- 服务暴露摘要
- 可达性风险
- 下一步检查建议

### 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

### 6. 判断边界

- 不直接代表漏洞成立
- 需与 TLS、漏洞、资产语义联合判断

### 7. 训练与参考资产

- 当前暂无正式案例，后续新增样本时应同步建立案例文档。

### 8. 当前限制

- 当前实现以本地规则与样本驱动为主
- 输出质量受输入材料完整度影响
- 重要边界应优先由案例和目标输出驱动收敛

### 9. 维护要求

- 当分类、输出结构或风险语义发生变化时，必须同步更新本文件
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档

## English

### 1. Basics

- Skill ID: `megaeth.easm.service_scan`
- Module: `EASM`
- Product Surface: `Security Log Analysis`
- Event Type: `service_exposure`
- Execution Mode: rule-first, with controlled augmentation only where explicitly allowed

### 2. Purpose

Analyze open ports, service exposure, and network-layer reachability.

### 3. Typical Inputs

- service scan results
- port and protocol information

### 4. Primary Outputs

- service-exposure summary
- reachability risk
- next-step checks

### 5. Trigger and Routing

This Skill is routed by the Planner using `event_type` and `source_type`. When a case or learning rule requires routing changes, update all of the following together:

- `app/core/planner.py`
- `app/skills/implementations.py`
- this Skill specification
- the linked training-case document

### 6. Decision Boundaries

- does not directly confirm a vulnerability and should be correlated with TLS, vulnerability, and asset context

### 7. Training and Reference Assets

- No formal case is linked yet. Future real samples should create or update a case document.

### 8. Current Limits

- the current implementation is primarily rule- and sample-driven
- output quality depends on the completeness of the supplied material
- important boundaries should be converged through cases and target outputs

### 9. Maintenance Requirements

- update this file whenever classification, output structure, or risk semantics change
- create or update a matching document under `training_cases/` when new real samples are introduced
