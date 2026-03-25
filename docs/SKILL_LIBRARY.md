# Skill 能力库
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档说明当前 Skill 体系如何组织、如何阅读、如何治理，以及它们如何与训练案例和页面展示对应。

### 2. Skill 在当前系统中的角色

当前系统中的 Skill 不是“随便起名的能力标签”，而是主分析链中的领域边界。一个 Skill 至少要回答：

- 它分析什么
- 它接受什么输入
- 它产出什么输出
- 它不该做什么

### 3. 当前模块划分

当前 Skill 主要按以下模块组织：

- CI/CD
- Endpoint
- Host
- Cloud
- AppSec
- EASM
- Identity
- Key Security

### 4. 当前重点 Skill 方向

当前最值得优先理解的 Skill 方向包括：

- Host baseline
- JumpServer 单文件与多源审计
- Whitebox AppSec 三段式分析
- EASM 单样本与多样本综合评估

这些方向既是当前主线的重点能力，也是当前训练最活跃的域。

### 5. Skill 规格文档的标准结构

一份成熟的 Skill 规格至少应说明：

- Skill 的目的
- 典型输入
- 主要输出
- 触发与路由
- 判断边界
- 训练与参考资产
- 当前实现说明
- 维护要求

### 6. Skill 与训练案例的关系

Skill 说明的是：

- 行为边界
- 输入输出要求
- 适用场景

训练案例说明的是：

- 真实样本
- 目标输出
- 校准规则
- Skill 的落地证据

也就是说：

- Skill 是规范
- Case 是验证

### 7. Skill 与页面的关系

当前前端中的 `技能` 页应被理解为 Skill 的可视化目录，而不是独立控制面。

页面主要展示：

- 模块分布
- 能力数量
- 每个 Skill 的训练覆盖
- 重点能力摘要

### 8. 当前重点模块说明

#### 8.1 Host

主要承担：

- 主机基线合规分析

#### 8.2 Identity / JumpServer

主要承担：

- 登录审计
- 命令审计
- 文件传输审计
- 管理平面审计
- 多源综合审计

#### 8.3 AppSec

主要承担：

- Whitebox Recon
- Whitebox Exploit Validation
- Whitebox Report Synthesis

#### 8.4 EASM

主要承担：

- 单层外部资产分析
- 多层 EASM 综合评估

### 9. 当前阅读建议

建议按以下顺序阅读 Skill：

1. Host baseline
2. JumpServer
3. Whitebox AppSec
4. EASM
5. 其余模块

这样能最快理解当前主线最重要的设计边界。

### 10. 新增 Skill 的最低要求

新增 Skill 至少需要同步完成：

- Skill spec
- Planner 路由
- 实现逻辑
- 页面可见性
- 训练案例或模板
- 测试
- 文档更新

### 11. Skill 治理原则

当前 Skill 管理遵循以下原则：

- Skill ID 必须稳定
- spec 是行为边界来源
- 训练案例是能力落地佐证
- 页面展示不能替代 spec
- 模型增强只能是 Skill 的受控补充

### 12. 当前已知问题与维护重点

Skill 层当前仍要重点防止：

- 同一能力出现多个显示口径
- 单文件与综合 Skill 串线
- 新增训练案例但页面统计不更新
- 能力更新了但 spec 和文档没同步

### 13. 结论

当前 Skill 体系应被理解为：

- 当前安全日志分析主线的领域边界集合
- 连接 Planner、实现层、训练案例和报告结构的核心契约层

---

## English

### 1. Purpose

This document explains how the current Skill system is organized, how it should be read, how it is governed, and how it maps to training cases and UI presentation.

### 2. The Role of Skills in the Current System

In the current mainline, a Skill is not just a label. It is a domain boundary in the analysis pipeline. A Skill should define:

- what it analyzes
- what it accepts as input
- what it produces as output
- what it must not do

### 3. Current Module Structure

Skills are currently grouped into:

- CI/CD
- Endpoint
- Host
- Cloud
- AppSec
- EASM
- Identity
- Key Security

### 4. Primary Skill Areas

The most important areas to understand first are:

- Host baseline
- JumpServer single-source and multi-source audit analysis
- Whitebox AppSec three-stage analysis
- EASM single-source and composite assessment

### 5. Expected Skill-Spec Structure

A mature Skill spec should cover:

- purpose
- typical inputs
- primary outputs
- trigger and routing behavior
- judgment boundary
- training and reference assets
- current implementation note
- maintenance requirements

### 6. Relationship Between Skills and Cases

Skill specs define:

- behavior boundaries
- input and output expectations
- applicable scenarios

Training cases define:

- real samples
- target outputs
- calibration rules
- evidence that the Skill has landed

In short:

- Skills are the contract
- Cases are the proof

### 7. Relationship Between Skills and the UI

The `技能` page is a visualization layer for the Skill catalog, not an independent control plane.

It currently shows:

- module distribution
- capability counts
- training coverage per Skill
- summaries for key capabilities

### 8. Key Module Notes

Important current modules include:

- Host
- Identity / JumpServer
- AppSec
- EASM

### 9. Recommended Reading Order

Suggested order:

1. Host baseline
2. JumpServer
3. Whitebox AppSec
4. EASM
5. the remaining modules

### 10. Minimum Requirements for New Skills

A new Skill should land together with:

- a Skill spec
- Planner routing
- implementation logic
- UI visibility
- a case or template
- tests
- documentation updates

### 11. Governance Principles

Current Skill governance follows these rules:

- Skill IDs must remain stable
- specs are the source of behavioral boundaries
- cases are the proof of landed capability
- UI presentation must not replace the spec
- model augmentation is only a controlled supplement

### 12. Current Risks and Maintenance Priorities

The Skill layer still needs to prevent:

- multiple display names for the same capability
- single-file and composite Skills bleeding into each other
- training coverage drifting from actual cases
- capability changes landing without spec and doc updates

### 13. Summary

The Skill system should be understood as:

- the set of domain boundaries in the security-log-analysis mainline
- the core contract layer connecting Planner, implementation, training, and reporting
