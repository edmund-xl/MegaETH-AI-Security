# `megaeth.cloud.config_audit`

## 中文

### 基本信息

- 中文名称：MegaETH 云配置风险能力
- 模块：Cloud
- 当前状态：已接入，启发式实现

### 作用

识别 bucket、security group、cloudtrail 等云配置弱点。

### 典型输入

- Cloud config JSON
- Cloud posture 导出
- 审计清单

### 当前触发线索

- `public bucket`
- `security group`
- `cloudtrail`
- `bucket`

### 当前输出重点

- 配置错误
- 缺失控制
- 云风险修复建议

### 当前限制

- 触发面还很窄
- 尚未覆盖 CSPM 常见资源类型全量规则

### 迭代方向

- 引入真实 CSPM 规则集
- 扩展到 IAM、KMS、网络边界等更多云资源

## English

### Basics

- Name: MegaETH Cloud Configuration Risk
- Module: Cloud
- Status: Active, heuristic implementation

### Purpose

Detects configuration weaknesses around buckets, security groups, CloudTrail, and other cloud controls.

### Typical Inputs

- cloud config JSON
- cloud posture exports
- audit checklists

### Current Triggers

- `public bucket`
- `security group`
- `cloudtrail`
- `bucket`

### Current Outputs

- misconfigurations
- missing controls
- remediation guidance

### Current Limits

- current trigger surface is narrow
- not yet a full CSPM-style ruleset

### Iteration Direction

- bring in stronger CSPM rules
- expand to IAM, KMS, and network boundary resources
