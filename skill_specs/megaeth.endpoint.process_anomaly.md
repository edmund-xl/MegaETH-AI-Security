# `megaeth.endpoint.process_anomaly`

## 中文

### 基本信息

- 中文名称：MegaETH 端点行为分析能力
- 模块：Endpoint
- 当前状态：已接入，真实案例已多轮打磨

### 作用

分析 EDR / XDR / Bitdefender 报表中的恶意软件检测、攻击行为、防钓鱼和阻断记录，并提炼出可读的端点风险结论。

### 典型输入

- Bitdefender 安全审计报表
- 端点事件 CSV / PDF / JSON
- 端点 incident 材料

### 当前触发线索

- 报表中的 `恶意软件检测`
- `网络攻击`
- `阻止的网站`
- 兼容旧 incident 线索：
  - `Attack.LocalFileInclusion`
  - `/.env`
  - `ShellSpawned`

### 当前输出重点

- 恶意软件检测
- 网络攻击检测
- 恶意网站或钓鱼拦截
- 高频主机与重点终端

### 当前限制

- 仍以报表结构化字段和关键词为主
- 对多步攻击链、进程树和横向移动的还原还不够深

### 迭代方向

- 增加主机级聚合与优先排查列表
- 结合事件流而不是只看静态报表

## English

### Basics

- Name: MegaETH Endpoint Behavior Analysis
- Module: Endpoint
- Status: Active, refined through real report training

### Purpose

Analyzes EDR/XDR/Bitdefender materials for malware, exploit-style detections, phishing blocks, and suspicious endpoint activity.

### Typical Inputs

- Bitdefender security audit reports
- endpoint CSV / PDF / JSON exports
- endpoint incident materials

### Current Triggers

- `恶意软件检测` / malware detections
- `网络攻击` / network attacks
- `阻止的网站` / blocked sites
- legacy incident indicators such as:
  - `Attack.LocalFileInclusion`
  - `/.env`
  - `ShellSpawned`

### Current Outputs

- malware detections
- network attack detections
- phishing or malicious web activity
- top hosts and priority endpoints

### Current Limits

- still centered on structured report fields and keywords
- not yet deep on process trees, lateral movement, or multi-step attack reconstruction

### Iteration Direction

- add host-level prioritization
- move toward event-stream analysis instead of static reports only
