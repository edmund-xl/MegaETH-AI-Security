# Case 003：EASM 多层资产综合评估
<!-- security-log-analysis mainline -->

## 中文

### 1. 案例目的

本案例用于训练系统把 EASM 的服务/端口、DNS、IP 段、证书和 ASN 材料做跨文件关联，输出按资产组织的外部攻击面综合评估结果。

它是当前主线里最重要的 EASM 综合案例，用来验证：

- 单文件 EASM 分析是否可独立工作
- 多文件是否能正确聚合成综合事件
- `easm_asset_assessment` 是否按统一 schema 输出
- Gemini 是否只增强允许增强的综合判断段落

### 2. 适用范围

本案例适用于：

- 服务面 CSV
- DNS CSV
- TLS / 证书 CSV
- ASN CSV
- IP 段 CSV

同批次多文件输入时，应同时验证单文件结果和综合结果。

### 3. 分类目标

- `source_type = easm`
- `event_type = easm_asset_assessment`

### 4. 对应 Skill

- `megaeth.easm.asset_discovery`
- `megaeth.easm.service_scan`
- `megaeth.easm.tls_analysis`
- `megaeth.easm.vulnerability_scan`
- `megaeth.easm.external_intelligence`

### 5. 样本应训练系统学会什么

本案例要让系统学会：

- 正确识别服务层、DNS 层、证书层、ASN/IP 层
- 在单文件模式下给出独立判断
- 在多文件模式下形成综合事件
- 区分事实、推断、标签、评分与建议动作
- 按资产输出统一 schema 的综合评估

### 6. 目标输出特征

合格输出应具备：

- 单文件可分析
- 多文件可综合
- 综合结果为 `easm_asset_assessment`
- 中文综合报告结构稳定
- `assessment / professional_judgment` 可由 Gemini 受控增强

### 7. 训练重点

- 正确识别 CDN 与直连源站并存
- 识别第三方委派、历史资产线索和功能面资产
- 统一资产视角，不把每个文件都当独立世界
- 保持事实层与高层判断层分离

### 8. 常见失败模式

当前 EASM 容易出错的地方包括：

- 真实文件名没有正确触发对应 event hint
- 中文表头/BOM 导致字段识别失败
- 单文件都被误判成同一种类型
- 多文件没有正确生成 `easm_asset_assessment`
- Gemini 直接参与事实抽取而不是综合判断

### 9. 完成标准

本案例训练完成的最低标准是：

- 单文件分析可用
- 多文件综合分析可用
- 资产级综合评估结构稳定
- 页面和下载报告一致
- 文档、Skill、训练案例和实现同步更新

---

## English

### 1. Case Purpose

This case trains the system to correlate EASM service/port, DNS, IP-range, certificate, and ASN material across files and produce asset-centric external attack-surface assessments.

It is the primary EASM composite case in the current mainline and validates:

- whether single-file EASM analysis works independently
- whether multi-file aggregation produces the correct composite event
- whether `easm_asset_assessment` follows a unified schema
- whether Gemini only enhances explicitly allowed composite-judgment sections

### 2. Scope

This case applies to:

- service CSV
- DNS CSV
- TLS / certificate CSV
- ASN CSV
- IP-range CSV

When these files are uploaded together, both the single-file outputs and the composite output should be validated.

### 3. Target Classification

- `source_type = easm`
- `event_type = easm_asset_assessment`

### 4. Owning Skills

- `megaeth.easm.asset_discovery`
- `megaeth.easm.service_scan`
- `megaeth.easm.tls_analysis`
- `megaeth.easm.vulnerability_scan`
- `megaeth.easm.external_intelligence`

### 5. What the System Should Learn

This case should teach the system to:

- recognize service, DNS, certificate, and ASN/IP layers correctly
- produce valid single-file assessments
- form a composite event from multi-file batches
- separate facts, inferences, tags, scoring, and recommended actions
- output unified asset-centric assessments

### 6. Target Output Characteristics

A correct output should support:

- usable single-file analysis
- usable multi-file composite analysis
- composite output as `easm_asset_assessment`
- a stable Chinese composite report
- controlled Gemini enhancement for `assessment / professional_judgment`

### 7. Training Focus

- identify CDN-plus-origin coexistence correctly
- recognize third-party delegation, historical asset hints, and functional surfaces
- unify around the asset view rather than treating each file as a separate world
- keep the fact layer separate from the judgment layer

### 8. Common Failure Modes

Common EASM failures include:

- real filenames not triggering the right event hints
- Chinese headers or BOM breaking field recognition
- all single files collapsing into one type
- failure to generate `easm_asset_assessment`
- Gemini being allowed to act on the fact layer instead of the judgment layer

### 9. Completion Criteria

This case is complete only when:

- single-file analysis works
- multi-file composite analysis works
- asset-centric composite output is stable
- page and export reports match
- docs, Skills, cases, and implementation are updated together
