# `megaeth.cloud.identity_surface`

## 中文

### 基本信息

- 中文名称：MegaETH 云身份面分析能力
- 模块：Cloud
- 当前状态：已接入，当前偏辅助

### 作用

用于观察云身份和访问面，帮助后续做权限、身份与访问风险分析。

### 典型输入

- IAM / 身份导出
- 云身份清单
- 权限关系材料

### 当前输出重点

- 身份暴露面
- 权限风险分析入口

### 当前限制

- 目前尚未形成独立强 finding 分支
- 与策略分析能力的边界还可继续细化

### 迭代方向

- 增加身份关系图
- 补充跨账号、跨角色的权限链路分析

## English

### Basics

- Name: MegaETH Cloud Identity Surface Analysis
- Module: Cloud
- Status: Active, currently more of a supporting capability

### Purpose

Observes cloud identity and access surface so later steps can reason about privilege and identity risk.

### Typical Inputs

- IAM / identity exports
- cloud identity inventories
- privilege relationship materials

### Current Outputs

- identity surface view
- entry point for privilege risk analysis

### Current Limits

- does not yet produce a strong dedicated finding branch
- boundary with policy-analysis skills can be refined further

### Iteration Direction

- add identity relationship graphs
- analyze cross-account and cross-role privilege chains
