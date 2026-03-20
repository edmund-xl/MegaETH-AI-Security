# `megaeth.identity.jumpserver_transfer_review`

## 中文

### 基本信息

- 中文名称：MegaETH JumpServer 文件传输审计能力
- 模块：Identity
- 当前状态：已接入，负责 JumpServer 单文件传输侧审计
- 执行方式：`规则版`

### 作用

这条 Skill 专门处理 JumpServer 的文件传输审计单文件，重点不是“有没有上传文件”，而是有没有出现 /tmp 投放、root 账号上传、二进制落地，以及是否能继续和命令侧拼出放权与执行链。

### 典型输入

- `ftplog.xlsx`
- JumpServer 导出的文件传输审计 xlsx

### 当前触发线索

- `文件名`
- `操作`
- `/tmp/`
- `root`
- 可执行二进制名称
- 上传 / 下载方向

### 当前输出重点

- 文件传输总量
- 高风险上传数量
- 重点上传文件
- `/tmp -> 落地 -> 放权 -> 执行` 的候选链条

### 当前规则边界

- 单独的上传记录不能自动等于恶意载荷
- 需要继续结合命令侧确认是否被移动、放权和执行

### 当前限制

- 传输日志和命令会话还不能总是自动一一对应
- 还需要更多真实样本去稳定高风险上传画像

### 迭代方向

- 增加按文件名、时间窗和资产的自动串联
- 提升对工具投放、补丁分发和异常二进制投放的区分能力

## English

### Basics

- Name: MegaETH JumpServer Transfer Review
- Module: Identity
- Status: Active, for single-source JumpServer transfer audit
- Execution mode: `Rule only`

### Purpose

This Skill handles standalone JumpServer file-transfer audit inputs. It focuses on /tmp delivery, root uploads, binary drops, and whether those transfers can later be correlated with chmod or execution on the command side.

### Typical inputs

- `ftplog.xlsx`
- JumpServer exported file-transfer audit xlsx files

### Current outputs

- total transfer volume
- count of high-risk uploads
- top uploaded files
- candidate `/tmp -> drop -> permission -> execution` chains
