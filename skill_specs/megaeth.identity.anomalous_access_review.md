# Skill Specification: `megaeth.identity.anomalous_access_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.anomalous_access_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`login_auth_review`
- 当前执行模式：以规则主链为主，必要时可叠加受控增强

### 2. 能力目的

分析登录结果、认证失败模式与异常访问行为。

### 3. 典型输入

- 登录日志
- 认证事件

### 4. 主要输出

- 登录侧摘要
- 失败模式
- 账户风险提示

### 5. 触发与路由

该 Skill 由 Planner 根据 `event_type` 与 `source_type` 路由命中。若训练案例或学习规则要求对路由进行校准，应同时更新：

- `app/core/planner.py`
- `app/skills/implementations.py`
- 本 Skill 规格说明
- 对应训练案例文档

### 6. 判断边界

- 不把代理地址直接当攻击源
- 不因单次失败直接认定爆破

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

- Skill ID: `megaeth.identity.anomalous_access_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `login_auth_review`
- Execution Mode: rule-first, with controlled augmentation only where explicitly allowed

### 2. Purpose

Analyze login outcomes, authentication-failure patterns, and anomalous access behavior.

### 3. Typical Inputs

- login logs
- authentication events

### 4. Primary Outputs

- login-side summary
- failure patterns
- account-risk notes

### 5. Trigger and Routing

This Skill is routed by the Planner using `event_type` and `source_type`. When a case or learning rule requires routing changes, update all of the following together:

- `app/core/planner.py`
- `app/skills/implementations.py`
- this Skill specification
- the linked training-case document

### 6. Decision Boundaries

- does not treat proxy addresses as the real attack source
- does not classify brute force from a single failed event

### 7. Training and Reference Assets

- No formal case is linked yet. Future real samples should create or update a case document.

### 8. Current Limits

- the current implementation is primarily rule- and sample-driven
- output quality depends on the completeness of the supplied material
- important boundaries should be converged through cases and target outputs

### 9. Maintenance Requirements

- update this file whenever classification, output structure, or risk semantics change
- create or update a matching document under `training_cases/` when new real samples are introduced
