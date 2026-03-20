# `megaeth.easm.tls_analysis`

## 中文

### 基本信息

- 中文名称：MegaETH TLS 姿态分析能力
- 模块：EASM
- 当前状态：已接入，当前偏骨架

### 作用

针对外部服务中的 TLS / 证书问题做专门分析。

### 典型输入

- TLS 扫描结果
- 证书检查结果

### 当前输出重点

- 证书异常
- TLS 配置问题

### 当前限制

- 目前尚无独立强执行逻辑
- 更多体现为规划覆盖与后续扩展点

### 迭代方向

- 增加证书过期、弱套件、主机名不匹配等专门判断

## English

### Basics

- Name: MegaETH TLS Posture Analysis
- Module: EASM
- Status: Active, currently closer to a scaffold

### Purpose

Provides a dedicated analysis path for TLS and certificate posture issues in exposed services.

### Typical Inputs

- TLS scan results
- certificate check results

### Current Outputs

- certificate anomalies
- TLS configuration issues

### Current Limits

- no strong dedicated execution branch yet
- mainly exists as planning coverage and an expansion point

### Iteration Direction

- add checks for expiry, weak ciphers, and hostname mismatch
