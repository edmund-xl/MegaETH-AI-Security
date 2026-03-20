# `megaeth.key.private_key_exposure`

## 中文

### 基本信息

- 中文名称：MegaETH 私钥暴露检测能力
- 模块：Key
- 当前状态：已接入，当前偏基础

### 作用

识别私钥、助记词和敏感密钥材料泄露线索。

### 典型输入

- 文本
- 配置
- 代码
- 事件导出

### 当前输出重点

- 私钥暴露
- 需要轮换的高风险凭据

### 当前限制

- 目前主要与通用 secret detection 协同
- 尚未针对链上钱包格式和更多密钥家族做细分

### 迭代方向

- 增加链上钱包、助记词、keystore 等专门规则

## English

### Basics

- Name: MegaETH Private Key Exposure Detection
- Module: Key
- Status: Active, currently basic

### Purpose

Detects leaked private keys, seed phrases, and sensitive key material.

### Typical Inputs

- text
- configuration
- code
- exported event material

### Current Outputs

- private key exposure
- high-risk credentials that require rotation

### Current Limits

- currently works alongside general secret detection
- not yet specialized across more wallet formats or key families

### Iteration Direction

- add dedicated rules for wallets, seed phrases, and keystore formats
