# `megaeth.identity.jumpserver_command_review`

## 中文

### 基本信息

- 中文名称：MegaETH JumpServer 命令审计能力
- 模块：Identity
- 当前状态：已接入，负责 JumpServer 单文件命令侧审计
- 执行方式：`规则版`

### 作用

这条 Skill 专门处理 JumpServer 的命令审计单文件。它不负责做多源综合判断，重点是把命令侧里真正有风险价值的部分提出来，比如提权、服务启停、下载执行、跨主机操作、权限放开和敏感参数暴露。

我一般会把它当成“多源综合之前的命令侧分拣器”。如果只传了一份 `command.xlsx`，就该落这条，而不是直接挂到多源综合 Skill。

### 典型输入

- `command.xlsx`
- JumpServer 导出的命令审计 xlsx

### 当前触发线索

- `命令`
- `风险等级`
- `会话`
- `sudo`
- `systemctl`
- `chmod`
- `chown`
- `scp`
- `rsync`
- `ssh`
- `wget`
- `curl`
- `cast send --private-key`

### 当前输出重点

- 命令总量与去噪后有效命令量
- 高风险命令语义
- 重点账户与重点资产
- 提权 / 服务控制 / 下载执行 / 横向操作 / 敏感参数暴露

### 当前规则边界

- 不因为单条 `sudo` 直接判定入侵
- 命令侧结论不能替代文件传输和管理平面证据
- 去噪后的命令链比原始导出计数更重要

### 当前限制

- 还没有完整的会话级图谱
- 仍然依赖启发式去噪和命令关键词聚合

### 迭代方向

- 继续强化 tmux / 控制字符 / AI 交互噪声过滤
- 增加账户-资产-命令链的会话化表达

## English

### Basics

- Name: MegaETH JumpServer Command Review
- Module: Identity
- Status: Active, for single-source JumpServer command audit
- Execution mode: `Rule only`

### Purpose

This Skill handles JumpServer command-audit files as standalone inputs. It focuses on high-risk command semantics such as privilege escalation, service control, download-and-execute, lateral operations, permission changes, and sensitive parameter exposure.

### Typical inputs

- `command.xlsx`
- JumpServer exported command-audit xlsx files

### Current triggers

- `命令`
- `风险等级`
- `会话`
- `sudo`
- `systemctl`
- `chmod`
- `chown`
- `scp`
- `rsync`
- `ssh`
- `wget`
- `curl`
- `cast send --private-key`

### Current outputs

- total command volume and effective commands after denoising
- high-risk command semantics
- top risky accounts and assets
- escalation / service control / download-execute / lateral movement / sensitive parameter exposure

### Current limits

- no full session graph yet
- still relies on heuristic denoising and command-pattern aggregation
