# 功能快照
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档提供当前主线能力快照，用于快速回答：

- 系统目前支持哪些输入
- 工作台各页面能做什么
- 已落地哪些分析域和训练资产
- 当前系统不应该被误解成什么

### 2. 当前输入源

当前系统已支持以下输入形式：

- 本地文件上传
- 文本输入
- Bitdefender 材料
- Whitebox AppSec 材料
- JumpServer 审计材料
- EASM CSV 材料

### 3. 当前页面能力

五个页面分别承担以下职责：

#### 3.1 `概览`

用于查看：

- 平台当前状态
- 最近报告
- 近期运行态势
- 能力覆盖概览

#### 3.2 `输入`

用于：

- 上传文件
- 输入文本
- 触发归一化后分析
- 查看当前调查批次的结果

#### 3.3 `技能`

用于：

- 浏览 Skill 目录
- 查看模块分布
- 查看训练覆盖

#### 3.4 `连接`

用于：

- 查看外部平台接入
- 触发导入动作
- 明确平台入口

#### 3.5 `学习`

用于：

- 查看最近学习反馈
- 观察训练沉淀

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

当前仍以模板方式存在的资产包括：

- Whitebox AppSec 模板

### 6. EASM 当前状态

EASM 当前已经不是骨架状态，而是：

- 单一样本可独立分析
- 多样本可综合分析
- 可生成 `easm_asset_assessment`
- 综合报告中的 `assessment / professional_judgment` 可由 Gemini 增强

### 7. Skill 与模型增强快照

当前系统以规则主链为基础，模型增强只用于允许增强的段落。典型场景包括：

- JumpServer 多源综合判断
- EASM 多文件综合专业判断
- Whitebox 综合报告高层总结

### 8. 当前系统适用范围

当前系统更适合：

- 安全材料分析
- 中文报告生成
- 样本驱动训练
- 页面与导出复核

当前系统不应被误解为：

- 自动攻击平台
- 自动处置中心
- 分布式执行编排平台

### 9. 当前快照结论

当前主线已经具备：

- 稳定的五页面工作台
- 多域安全日志分析
- 规则主链 + 受控模型增强
- 训练案例与学习反馈闭环

---

## English

### 1. Purpose

This document provides a capability snapshot of the active mainline and answers:

- what inputs the system supports
- what each page is responsible for
- which domains and training assets are already landed
- what the system should not be mistaken for

### 2. Current Input Sources

The system currently supports:

- local file upload
- text input
- Bitdefender materials
- Whitebox AppSec materials
- JumpServer audit materials
- EASM CSV materials

### 3. Current UI Capabilities

The five pages currently serve:

- `Overview`
  - platform state
  - recent reports
  - runtime signals
  - capability overview
- `Intake`
  - file upload
  - text input
  - normalize-and-analyze trigger
  - current investigation outputs
- `Skills`
  - Skill catalog
  - module distribution
  - training coverage
- `Integrations`
  - external integration entry points
  - import actions
- `Learning`
  - recent learning feedback
  - training retention

### 4. Current Analysis Domains

Current analysis domains include:

- Host
- Endpoint
- Identity / JumpServer
- AppSec
- Cloud
- CI/CD
- EASM
- Key Security

### 5. Current Landed Training Assets

Formally landed cases include:

- Host baseline
- JumpServer multi-source audit review
- EASM multi-layer composite assessment

Template assets currently include:

- Whitebox AppSec templates

### 6. Current EASM Status

EASM is no longer just a scaffold. It currently supports:

- standalone single-source analysis
- composite multi-file analysis
- generation of `easm_asset_assessment`
- Gemini enhancement for composite `assessment` and `professional_judgment`

### 7. Skill and Model-Augmentation Snapshot

The platform remains rule-first, with model augmentation only in explicitly allowed sections. Typical examples include:

- JumpServer multi-source composite judgment
- EASM multi-file composite professional judgment
- Whitebox composite report synthesis

### 8. Intended Scope

The system is currently well suited for:

- security-material analysis
- Chinese report generation
- sample-driven training
- UI/export review

It should not be mistaken for:

- an automated attack platform
- an auto-remediation center
- a distributed execution orchestrator

### 9. Snapshot Summary

The active mainline now provides:

- a stable five-page workbench
- multi-domain security log analysis
- a rule-first pipeline with controlled model augmentation
- a closed loop across training cases and learning feedback
