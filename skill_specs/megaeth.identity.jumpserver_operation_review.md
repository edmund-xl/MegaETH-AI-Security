# `megaeth.identity.jumpserver_operation_review`

## 中文

### 基本信息

- 中文名称：MegaETH JumpServer 管理平面审计能力
- 模块：Identity
- 当前状态：已接入，负责 JumpServer 单文件操作记录审计
- 执行方式：`规则版`

### 作用

这条 Skill 专门处理 JumpServer 的管理平面操作记录。它的重点不是主机侧执行，而是导出、授权、主机/账号创建、节点更新和会话建立这些高影响控制平面动作。

### 典型输入

- `operatelog.xlsx`
- JumpServer 导出的操作记录审计 xlsx

### 当前触发线索

- `动作`
- `资源类型`
- `组织名称`
- `create`
- `update`
- `export`
- 主机 / 账号 / 授权 / 会话

### 当前输出重点

- 导出动作
- 授权与更新
- 主机/账号创建
- 会话创建
- 主要操作者与资源类型分布

### 当前规则边界

- 管理平面动作是背景证据，不替代主机侧执行证据
- 不能把日志导出、资产授权直接当成入侵动作

### 当前限制

- 仍然缺少和主机命令侧的强会话绑定
- 需要更多真实样本来稳定“高影响管理平面操作”的判断边界

### 迭代方向

- 强化导出来源链和资产授权变更链
- 更好地区分正常运维管理和异常高影响变更

## English

### Basics

- Name: MegaETH JumpServer Operation Review
- Module: Identity
- Status: Active, for single-source JumpServer operation-audit inputs
- Execution mode: `Rule only`

### Purpose

This Skill handles JumpServer control-plane operation logs. It focuses on export actions, authorization changes, host/account creation, node updates, and session creation rather than host-side execution.

### Typical inputs

- `operatelog.xlsx`
- JumpServer exported operation-audit xlsx files

### Current outputs

- export actions
- authorization and update activity
- host/account creation
- session creation
- top operators and resource-type distribution
