# Skill Specification: `megaeth.easm.tls_analysis`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.easm.tls_analysis`
- 所属模块：`EASM`
- 适用产品域：`安全日志分析`
- 对应事件类型：`service_exposure`
- 当前执行模式：规则主链

### 2. 能力目的

分析 TLS 证书、协议版本、密码套件和证书卫生问题，解释传输安全风险。

它是 EASM 体系中的传输安全层 Skill，负责把 TLS 语义从资产层、服务层和漏洞层中拆出来单独分析。

### 3. 典型输入

- TLS 扫描结果、证书详情、协议信息
- 与传输安全直接相关的导出材料

常见输入形态包括：

- 证书导出
- TLS 握手结果
- 协议版本与密码套件清单
- 证书卫生或到期信息

### 4. 输出契约

- TLS 风险摘要
- 协议与证书问题清单
- 治理与加固建议
- 可供 EASM 综合评估复用的传输安全事实

### 5. 触发与路由

当输入包含证书、协议版本、密码套件或 TLS 配置材料时命中本 Skill。

在多文件 EASM 批次中，本 Skill 的输出应进入资产级综合评估，而不是独立漂浮。

### 6. 判断边界

- 聚焦传输安全，不覆盖应用逻辑缺陷。
- 证书异常需要结合服务暴露和资产语义解释影响。
- TLS 弱配置不直接等于业务可利用漏洞。
- 不能因为证书异常就越界推断资产归属或服务功能。

### 7. 训练与参考资产

- [Case 003 - EASM 多层综合评估](../training_cases/case_003_easm_multilayer/README.md)

### 8. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。
- 当前 TLS 层既支持单文件分析，也会进入 `easm_asset_assessment` 综合链。

### 9. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。
- 若新增 TLS 字段、协议语义或加固建议逻辑，必须同步检查：
  - 单文件 TLS 报告
  - EASM 多文件综合判断

## English

### 1. Basics

- Skill ID: `megaeth.easm.tls_analysis`
- Module: `EASM`
- Product Surface: `Security Log Analysis`
- Event Type: `service_exposure`
- Execution Mode: rule-first

### 2. Purpose

Analyze TLS certificates, protocol versions, cipher suites, and certificate hygiene issues to explain transport-security risk.

### 3. Typical Inputs

- TLS scan results, certificate details, and protocol information
- exports directly related to transport security

### 4. Output Contract

- TLS risk summary
- protocol and certificate issue list
- hardening and remediation recommendations

### 5. Trigger and Routing

This Skill is selected when the input contains certificates, protocol versions, cipher suites, or TLS configuration material.

### 6. Decision Boundaries

- It focuses on transport security and does not cover application-logic flaws.
- Certificate anomalies should be interpreted together with service exposure and asset context.

### 7. Training and Reference Assets

- [Case 003 - EASM Multi-Layer Composite Assessment](../training_cases/case_003_easm_multilayer/README.md)

### 8. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 9. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
