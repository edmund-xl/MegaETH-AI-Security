# `megaeth.identity.policy_risk_analysis`

## 中文

### 基本信息

- 中文名称：MegaETH 身份策略风险分析能力
- 模块：Identity
- 当前状态：已接入，当前偏骨架

### 作用

识别身份与访问策略中的提权风险、宽权限和危险策略结构。

### 典型输入

- IAM policy
- 身份策略 JSON / text

### 当前输出重点

- 提权风险
- 宽权限策略
- 策略修复建议

### 当前限制

- 当前尚无专门执行分支
- 需要进一步与真实策略引擎或规则库结合

### 迭代方向

- 对接真实 policy lint / reasoning 引擎
- 增加 privilege escalation 路径分析

## English

### Basics

- Name: MegaETH Identity Policy Risk Analysis
- Module: Identity
- Status: Active, currently closer to a scaffold

### Purpose

Detects privilege-escalation risk, overbroad permissions, and dangerous identity policy structure.

### Typical Inputs

- IAM policy
- identity policy JSON / text

### Current Outputs

- privilege-escalation risk
- broad permissions
- remediation guidance

### Current Limits

- no dedicated execution branch yet
- still needs stronger policy linting or reasoning engines

### Iteration Direction

- connect a real policy reasoning engine
- add privilege-escalation path analysis
