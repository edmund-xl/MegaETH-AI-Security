# 案例库
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档列出当前已经正式落地的训练案例与模板案例，并说明它们和 Skill 的关系。

### 2. 已落地案例

当前正式案例包括：

- `case_001_host_baseline`
  - 方向：Host baseline
  - 用途：主机基线合规分析训练
- `case_002_jumpserver_multisource`
  - 方向：JumpServer 多源审计
  - 用途：登录、命令、文件传输、管理平面综合判断训练
- `case_003_easm_multilayer`
  - 方向：EASM 多层综合评估
  - 用途：单样本分析与多样本综合评估训练

### 3. 模板案例

当前模板型案例包括：

- Whitebox AppSec 模板

模板用于：

- 新样本规范化接入
- 新报告结构定义
- 新 Skill 训练对齐

### 4. 案例与 Skill 的关系

案例与 Skill 的关系是：

- 案例提供真实样本和目标输出
- Skill 提供行为边界和执行规范
- 两者共同定义“系统应该学成什么样”

### 5. 新增案例的最低要求

新增案例至少需要同步：

- 样本解释
- 目标输出
- 系统规则
- 对应 Skill 说明

## English

### 1. Purpose

This document lists the formally landed training cases and template cases, and explains how they map to Skills.

### 2. Landed Cases

The current formal cases are:

- `case_001_host_baseline`
  - domain: Host baseline
  - purpose: host baseline compliance training
- `case_002_jumpserver_multisource`
  - domain: JumpServer multi-source auditing
  - purpose: training across login, command, transfer, and control-plane evidence
- `case_003_easm_multilayer`
  - domain: EASM multi-layer assessment
  - purpose: single-source and composite external attack-surface training

### 3. Template Cases

Current template cases include:

- the Whitebox AppSec template

Templates are used for:

- normalized onboarding of new samples
- defining new report structures
- aligning new Skill training

### 4. Relationship Between Cases and Skills

The relationship is:

- cases provide real samples and target outputs
- Skills define behavior boundaries and execution rules
- together they define what the system should learn

### 5. Minimum Requirements for New Cases

Any new case should include:

- sample interpretation
- target outputs
- system rules
- mapped Skill documentation
