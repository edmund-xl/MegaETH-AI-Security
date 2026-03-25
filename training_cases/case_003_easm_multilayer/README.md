# Case 003：EASM 多层资产综合评估
<!-- security-log-analysis mainline -->

## 中文

### 1. 说明

本案例用于训练系统把 EASM 的服务/端口、DNS、IP 段、证书和 ASN 材料做跨文件关联，输出按资产组织的外部攻击面综合评估结果。

### 2. 分类目标

- `source_type = easm`
- `event_type = easm_asset_assessment`

### 3. 对应 Skill

- `megaeth.easm.asset_discovery`
- `megaeth.easm.service_scan`
- `megaeth.easm.tls_analysis`
- `megaeth.easm.vulnerability_scan`
- `megaeth.easm.external_intelligence`

### 4. 训练重点

- 正确识别服务层、DNS 层、证书层、ASN/IP 层并完成多文件关联
- 区分事实、推断、标签、评分与建议动作
- 识别 CDN 与直连源站并存、第三方委派、历史资产线索和功能面资产
- 按资产输出统一 schema 的风险评估结果与中文综合报告


## English

### 1. Description

This case trains the system to correlate EASM service/port, DNS, IP-range, certificate, and ASN material across files and produce asset-centric external attack-surface assessments.

### 2. Target Classification

- `source_type = easm`
- `event_type = easm_asset_assessment`

### 3. Owning Skills

- `megaeth.easm.asset_discovery`
- `megaeth.easm.service_scan`
- `megaeth.easm.tls_analysis`
- `megaeth.easm.vulnerability_scan`
- `megaeth.easm.external_intelligence`

### 4. Training Focus

- correctly identify service, DNS, certificate, and ASN/IP layers and correlate them across files
- separate facts, inferences, tags, scores, and recommended actions
- recognize CDN-plus-origin coexistence, third-party delegation, historical asset hints, and functional surfaces
- output asset assessments in a unified schema plus a Chinese composite report
