# Skill Specification: `megaeth.identity.jumpserver_operation_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.identity.jumpserver_operation_review`
- 所属模块：`Identity`
- 适用产品域：`安全日志分析`
- 对应事件类型：`jumpserver_operation_review`
- 当前执行模式：规则主链，必要时可增强 control-plane judgment

### 2. 能力目的

分析 JumpServer 管理平面操作，如导出、授权、主机和账号变更，形成控制平面风险视图。

### 3. 典型输入

- JumpServer 操作记录导出
- 导出、授权、主机、账号、节点相关控制平面材料

### 4. 输出契约

- 管理平面摘要
- 关键控制动作与时间线
- 需要与主机侧联合复核的背景证据

### 5. 触发与路由

当输入来源于 JumpServer 操作记录导出或被识别为管理平面单文件样本时命中本 Skill。

### 6. 判断边界

- 管理平面动作只能作为背景证据，不能替代主机执行证据。
- 导出、授权和创建行为需要结合业务背景解释。

### 7. 训练与参考资产

- [Case 002 - JumpServer 多源综合审计](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.identity.jumpserver_operation_review`
- Module: `Identity`
- Product Surface: `Security Log Analysis`
- Event Type: `jumpserver_operation_review`
- Execution Mode: rule-first, with optional enhancement for control-plane judgment

### 2. Purpose

Analyze JumpServer control-plane operations such as exports, authorization changes, host creation, and account changes to form a control-plane risk view.

### 3. Typical Inputs

- JumpServer operation-audit exports
- control-plane material covering exports, authorization, hosts, accounts, and nodes

### 4. Output Contract

- control-plane summary
- key administrative actions and timeline
- background evidence that should be reviewed together with host-side activity

### 5. Trigger and Routing

This Skill is selected for JumpServer operation-audit exports or other material classified as a control-plane single-source sample.

### 6. Decision Boundaries

- Control-plane operations are background evidence and must not replace host-execution evidence.
- Export, authorization, and creation actions should be interpreted with operational context.

### 7. Training and Reference Assets

- [Case 002 - JumpServer Multi-Source Audit](../training_cases/case_002_jumpserver_multisource/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
