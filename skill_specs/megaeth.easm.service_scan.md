# `megaeth.easm.service_scan`

## 中文

### 基本信息

- 中文名称：MegaETH 服务暴露分析能力
- 模块：EASM
- 当前状态：已接入，启发式实现

### 作用

识别端口、协议、HTTP/SSH 等服务暴露情况。

### 典型输入

- 端口扫描 CSV
- 服务暴露导出
- Nmap / service 枚举结果

### 当前触发线索

- `port`
- `service`
- `ssh`
- `http`

### 当前输出重点

- 服务暴露
- 协议与端口风险

### 当前限制

- 仍是轻量级触发
- 没有做 banner、版本、默认口令或弱协议深度判断

### 迭代方向

- 增加服务版本画像
- 增加高危端口与弱协议专项规则

## English

### Basics

- Name: MegaETH Service Exposure Analysis
- Module: EASM
- Status: Active, heuristic implementation

### Purpose

Detects exposed services, ports, and protocols such as HTTP and SSH.

### Typical Inputs

- port-scan CSV
- service exposure exports
- Nmap or service enumeration results

### Current Triggers

- `port`
- `service`
- `ssh`
- `http`

### Current Outputs

- service exposure
- protocol and port risk

### Current Limits

- still lightweight and trigger-based
- no deep judgment on banners, versions, default credentials, or weak protocols yet

### Iteration Direction

- add service version profiling
- add dedicated rules for dangerous ports and weak protocols
