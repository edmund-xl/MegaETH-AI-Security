# Skill 能力库
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档说明当前 Skill 体系如何组织、如何阅读，以及如何与训练案例对应。

### 2. 当前模块划分

当前 Skill 按以下模块组织：

- CI/CD
- Endpoint
- Host
- Cloud
- AppSec
- EASM
- Identity
- Key Security

### 3. 当前重点 Skill 方向

当前主线中最值得优先理解的 Skill 方向包括：

- Host baseline
- JumpServer 单文件与多源审计
- Whitebox AppSec 三段式分析
- EASM 单样本与多样本综合评估

### 4. Skill 与案例的关系

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

### 5. 当前阅读建议

建议按以下顺序阅读：

1. Host baseline
2. JumpServer
3. Whitebox AppSec
4. EASM
5. 其余模块

### 6. 当前治理原则

Skill 管理遵循以下原则：

- Skill ID 稳定
- 规格说明是行为边界来源
- 训练案例是能力落地佐证
- 新增 Skill 必须同步：
  - spec
  - case 或模板
  - 页面显示
  - 文档说明

## English

### 1. Purpose

This document explains how the current Skill system is organized, how it should be read, and how it maps to training cases.

### 2. Current Module Structure

Skills are currently grouped into:

- CI/CD
- Endpoint
- Host
- Cloud
- AppSec
- EASM
- Identity
- Key Security

### 3. Primary Skill Areas

The most important landed Skill areas currently include:

- Host baseline
- JumpServer single-source and multi-source audit analysis
- Whitebox AppSec three-stage analysis
- EASM single-source and composite assessment

### 4. Relationship Between Skills and Cases

Skill specifications define:

- behavioral boundaries
- input and output expectations
- applicable scenarios

Training cases define:

- real samples
- target outputs
- calibration rules
- implementation evidence for the Skill

In short:

- Skills are the specification
- Cases are the evidence

### 5. Recommended Reading Order

Suggested order:

1. Host baseline
2. JumpServer
3. Whitebox AppSec
4. EASM
5. the remaining modules

### 6. Governance

Skill management follows these rules:

- Skill IDs remain stable
- specs define behavior boundaries
- training cases prove capability landing
- any new Skill must land together with:
  - a spec
  - a case or template
  - UI visibility
  - supporting documentation
