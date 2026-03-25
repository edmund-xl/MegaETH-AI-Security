# 功能快照
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档提供当前主线的能力快照，用于快速回答：

- 系统目前支持什么输入
- 页面上能做什么
- 已经落地哪些分析域
- 当前不应该误解成什么

### 2. 当前输入源

当前系统已支持以下输入源：

- 本地文件上传
- 文本输入
- Bitdefender 材料
- Whitebox AppSec 材料
- EASM CSV 材料

### 3. 当前页面能力

五个页面分别承担以下职责：

- `概览`
  - 平台总览
  - 最近报告
  - 当前状态信号
- `输入`
  - 文件上传
  - 文本输入
  - 归一化后分析
- `技能`
  - 能力目录
  - 模块分布
  - 训练覆盖
- `连接`
  - 外部平台接入入口
  - 导入动作入口
- `学习`
  - 学习反馈
  - 最近训练沉淀

### 4. 当前分析域

当前已覆盖的分析域包括：

- Host
- Endpoint
- Identity / JumpServer
- AppSec
- Cloud
- CI/CD
- EASM
- Key Security

### 5. 当前已落地训练资产

当前正式落地的案例包括：

- Host baseline
- JumpServer 多源综合审计
- EASM 多层综合评估

当前模板型资产包括：

- Whitebox AppSec 模板

### 6. EASM 当前状态

EASM 当前已经不是骨架状态，而是：

- 单一样本可独立分析
- 多样本可综合分析
- 可生成 `easm_asset_assessment`
- 综合报告中的 `综合结论 / 专业判断` 可由 Gemini 增强

### 7. 当前限制

当前系统更适合：

- 材料分析
- 报告生成
- 训练与校准

当前系统不应被误解为：

- 自动攻击平台
- 自动处置中心
- 大规模任务编排系统

## English

### 1. Purpose

This document provides a capability snapshot of the current mainline and answers:

- what inputs the system supports
- what each page is meant to do
- which analysis domains are currently landed
- what the system should not be mistaken for

### 2. Current Input Sources

The system currently supports:

- local file upload
- text input
- Bitdefender materials
- Whitebox AppSec materials
- EASM CSV materials

### 3. Current UI Capabilities

The five pages currently serve these roles:

- `概览`
  - platform overview
  - recent reports
  - current status signals
- `输入`
  - file upload
  - text input
  - normalize-and-analyze trigger
- `技能`
  - capability catalog
  - module distribution
  - training coverage
- `连接`
  - external integration entry points
  - import actions
- `学习`
  - learning feedback
  - recent training retention

### 4. Current Analysis Domains

The current analysis domains include:

- Host
- Endpoint
- Identity / JumpServer
- AppSec
- Cloud
- CI/CD
- EASM
- Key Security

### 5. Current Landed Training Assets

The formally landed cases are:

- Host baseline
- JumpServer multi-source audit review
- EASM multi-layer composite assessment

Template assets currently include:

- the Whitebox AppSec template

### 6. Current EASM Status

EASM is no longer only a scaffold. It currently supports:

- single-source analysis
- composite multi-file analysis
- generation of `easm_asset_assessment`
- Gemini enhancement for composite `assessment` and `professional_judgment`

### 7. Current Limits

The system is currently best suited for:

- material analysis
- report generation
- training and calibration

It should not be mistaken for:

- an automated attack platform
- an auto-remediation center
- a large-scale orchestration system
