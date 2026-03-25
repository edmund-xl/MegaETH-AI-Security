# 功能快照
<!-- security-log-analysis mainline -->

## 1. 文档目的

本文档用于说明当前主线已经具备的可见能力、输入源、页面能力和实现边界。

## 2. 当前输入源盘点

### 2.1 本地输入

- 文件上传
- 文本输入
- 混合输入批次

### 2.2 外部平台接入

- Bitdefender GravityZone
- Whitebox AppSec 输入骨架

### 2.3 已覆盖的分析域

- Host
- Endpoint
- Identity / JumpServer
- AppSec Whitebox
- Cloud
- CI/CD
- EASM
- Key Security

## 3. 当前页面能力

### 3.1 概览

- 平台总览
- 近期报告
- 历史摘要
- 能力覆盖简表

### 3.2 输入

- 统一输入
- 文件上传
- 归一化后分析
- 上传执行记录

### 3.3 技能

- 模块总览
- 全部能力
- 训练情况展示

### 3.4 连接

- 平台连接状态
- Bitdefender 导入入口
- 连接健康与导入提示

### 3.5 学习

- 学习反馈摘要
- 最近学习反馈列表

## 4. 当前代表性能力

### 4.1 Host

- 基线合规分析
- 完整性监测
- systemd 服务风险
- 二进制篡改审查

### 4.2 Endpoint

- 进程异常与平台事件分析

### 4.3 Identity

- 登录异常审查
- JumpServer 命令审计
- JumpServer 文件传输审计
- JumpServer 管理平面审计
- JumpServer 多源综合审计

### 4.4 AppSec

- 白盒侦察
- 白盒验证
- 白盒综合报告

## 5. 当前训练资产

已落地或已启用模板的训练资产包括：

- Host baseline 训练案例
- JumpServer 多源训练案例
- Whitebox AppSec 案例模板

## 6. 当前限制

- 当前仍以本地单机运行为主
- 存储层仍为文件型，而非数据库
- Agent 增强仅是部分能力的辅助方式，不替代规则主链
- 平台更适合分析、审计和学习沉淀，不是自动处置平台
