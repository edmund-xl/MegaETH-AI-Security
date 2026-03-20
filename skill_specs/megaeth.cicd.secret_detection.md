# `megaeth.cicd.secret_detection`

## 中文

### 基本信息

- 中文名称：MegaETH 密钥与敏感信息检测能力
- 模块：CI/CD
- 当前状态：已接入，启发式实现

### 作用

识别代码、配置、日志或文本中可能暴露的 AKIA、API key、private key、secret 等敏感凭据。

### 典型输入

- 源码
- 配置文件
- CI/CD 输出
- 文本型报告

### 当前触发线索

- `akia`
- `private key`
- `api_key`
- `secret`

### 当前输出重点

- 潜在密钥暴露
- 敏感凭据片段
- 轮换与清理建议

### 当前限制

- 目前主要依赖关键词
- 还没有接入更强的 secret scanner 或模式库

### 迭代方向

- 对接真实 secret scanner
- 支持按凭据类型区分严重度和轮换优先级

## English

### Basics

- Name: MegaETH Secret Detection
- Module: CI/CD
- Status: Active, heuristic implementation

### Purpose

Detects potential AKIA strings, API keys, private keys, and other secret material in code, configs, logs, or free text.

### Typical Inputs

- source code
- configuration files
- CI/CD output
- text reports

### Current Triggers

- `akia`
- `private key`
- `api_key`
- `secret`

### Current Outputs

- potential secret exposure
- credential fragments
- rotation and cleanup suggestions

### Current Limits

- mostly keyword-based today
- no stronger scanner or pattern library integrated yet

### Iteration Direction

- connect a real secret scanner
- differentiate severity and rotation priority by credential type
