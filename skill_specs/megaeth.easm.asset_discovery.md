# `megaeth.easm.asset_discovery`

## 中文

### 基本信息

- 中文名称：MegaETH 外部资产发现能力
- 模块：EASM
- 当前状态：已接入

### 作用

处理外部攻击面资产清单、IP 清单、域名清单，建立外部资产画像。

### 典型输入

- EASM CSV
- 资产导出
- IP / 域名清单

### 当前输出重点

- 资产存在性
- 外部资产范围
- 后续扫描目标

### 当前限制

- 对资产真实性和归属关系的判断还不够深
- 还没有自动把资产与漏洞、服务、证书视图打通

### 迭代方向

- 增加去重、归属和关键资产识别
- 与后续服务扫描、TLS、漏洞验证链路联动

## English

### Basics

- Name: MegaETH External Asset Discovery
- Module: EASM
- Status: Active

### Purpose

Processes external attack surface inventories, IP lists, and domain lists to build an external asset picture.

### Typical Inputs

- EASM CSV
- asset exports
- IP / domain inventories

### Current Outputs

- asset existence
- scope of external exposure
- targets for follow-on scanning

### Current Limits

- ownership and asset-truth validation are still shallow
- not yet tightly linked to vulnerability, service, or certificate views

### Iteration Direction

- add deduplication, ownership, and critical-asset recognition
- connect with service scan, TLS, and exposure verification
