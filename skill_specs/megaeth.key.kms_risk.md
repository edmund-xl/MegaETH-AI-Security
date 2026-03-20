# `megaeth.key.kms_risk`

## 中文

### 基本信息

- 中文名称：MegaETH KMS 风险分析能力
- 模块：Key
- 当前状态：已接入，启发式实现

### 作用

分析 KMS 签名、调用者、频次和偏离基线的访问行为。

### 典型输入

- KMS 日志
- 签名调用记录
- 加密服务事件

### 当前触发线索

- `sign`
- `kms`
- `caller`

### 当前输出重点

- 异常 KMS 使用
- 偏离运维基线的签名活动

### 当前限制

- 当前对上下文理解仍较轻
- 还没有按密钥用途、调用链和频率异常做更强建模

### 迭代方向

- 增加 signer 行为基线
- 区分正常业务签名与异常调用

## English

### Basics

- Name: MegaETH KMS Risk Analysis
- Module: Key
- Status: Active, heuristic implementation

### Purpose

Analyzes KMS signing activity, callers, frequency, and deviations from expected operational baseline.

### Typical Inputs

- KMS logs
- signing call records
- crypto-service events

### Current Triggers

- `sign`
- `kms`
- `caller`

### Current Outputs

- abnormal KMS usage
- signing activity deviating from operational baseline

### Current Limits

- context understanding is still light
- no stronger model for key purpose, call chains, or rate anomalies yet

### Iteration Direction

- add signer behavior baselines
- distinguish normal service signing from suspicious calls
