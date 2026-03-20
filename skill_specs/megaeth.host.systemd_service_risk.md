# `megaeth.host.systemd_service_risk`

## 中文

### 基本信息

- 中文名称：MegaETH 服务姿态分析能力
- 模块：Host
- 当前状态：已接入

### 作用

从主机风险材料中识别 SSH、telnet、rsync、ICMP、打印机服务等远程访问和服务暴露风险。

### 典型输入

- Unix / Linux 主机基线清单
- 服务暴露类主机报告

### 当前触发线索

- `ssh`
- `telnet`
- `rsync`
- `icmp`
- `openssh`
- `printer`

### 当前输出重点

- 服务暴露
- 远程访问风险
- 管理边界收敛建议

### 当前限制

- 目前主要基于标题文本关键词
- 对 systemd 单元配置本身还没有做深度解析

### 迭代方向

- 加入 systemd service 配置级审计
- 区分管理面服务与业务面服务的优先级

## English

### Basics

- Name: MegaETH Service Posture Analysis
- Module: Host
- Status: Active

### Purpose

Detects SSH, telnet, rsync, ICMP, printer, and other remote-access or service exposure risks in host posture material.

### Typical Inputs

- Unix / Linux baseline checklists
- host service posture reports

### Current Triggers

- `ssh`
- `telnet`
- `rsync`
- `icmp`
- `openssh`
- `printer`

### Current Outputs

- service exposure
- remote-access risk
- boundary-tightening guidance

### Current Limits

- currently title-keyword driven
- does not yet deeply parse systemd unit configuration

### Iteration Direction

- add service-unit-level auditing
- distinguish admin-plane services from business services
