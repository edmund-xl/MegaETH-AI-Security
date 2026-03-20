# `megaeth.host.integrity_monitor`

## 中文

### 基本信息

- 中文名称：MegaETH 主机完整性分析能力
- 模块：Host
- 当前状态：已接入

### 作用

识别主机高分风险项和整体完整性缺口，帮助平台形成主机级风险概览。

### 典型输入

- 主机基线风险清单
- 完整性检查导出
- 系统风险分析 CSV

### 当前触发线索

- 高分风险项
- 大量主机控制缺口

### 当前输出重点

- 高风险完整性缺口
- 主机基线总体风险

### 当前限制

- 在 `host_baseline_assessment` 场景下，它更多作为辅助 Skill
- 还没有覆盖文件级篡改证据链

### 迭代方向

- 补充文件完整性、AIDE、二进制偏移等更细粒度线索

## English

### Basics

- Name: MegaETH Host Integrity Analysis
- Module: Host
- Status: Active

### Purpose

Identifies high-risk host control gaps and provides an overall host integrity posture summary.

### Typical Inputs

- host baseline risk lists
- integrity exports
- system risk analytics CSVs

### Current Triggers

- very high score findings
- clusters of host control gaps

### Current Outputs

- high-risk integrity gaps
- overall host baseline posture

### Current Limits

- acts mostly as a supporting Skill in `host_baseline_assessment`
- does not yet reconstruct file-level tampering evidence

### Iteration Direction

- add deeper file integrity, AIDE, and binary-drift evidence
