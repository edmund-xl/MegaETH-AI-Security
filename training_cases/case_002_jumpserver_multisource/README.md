# Case 002：JumpServer 多源综合审计
<!-- security-log-analysis mainline -->

## 中文

### 1. 说明

本案例用于训练系统将 JumpServer 的登录、命令、文件传输和操作记录联合起来，输出一份固定结构的中文综合审计报告。

### 2. 分类目标

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

### 3. 对应 Skill

- `megaeth.identity.jumpserver_multi_source_review`
- `megaeth.identity.anomalous_access_review`
- `megaeth.identity.jumpserver_command_review`
- `megaeth.identity.jumpserver_transfer_review`
- `megaeth.identity.jumpserver_operation_review`

### 4. 固定报告结构

- `综合结论`
- `主要依据如下`
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`


## English

### 1. Description

This case trains the system to combine JumpServer login, command, file-transfer, and operation logs into a fixed-structure Chinese composite audit report.

### 2. Target Classification

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

### 3. Owning Skills

- `megaeth.identity.jumpserver_multi_source_review`
- `megaeth.identity.anomalous_access_review`
- `megaeth.identity.jumpserver_command_review`
- `megaeth.identity.jumpserver_transfer_review`
- `megaeth.identity.jumpserver_operation_review`

### 4. Fixed Report Structure

- `综合结论`
- `主要依据如下`
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`
