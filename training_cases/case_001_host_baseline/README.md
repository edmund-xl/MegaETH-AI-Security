# Case 001：Host Baseline
<!-- security-log-analysis mainline -->

## 中文

### 1. 案例目的

本案例用于训练系统理解主机基线材料、风险评分与整改建议之间的关系，并稳定输出 Host baseline 分析结果。

它的核心作用不是“把一份基线结果跑通”，而是帮助系统学会：

- 识别主机基线类输入
- 正确路由到 Host 模块
- 区分配置缺口、完整性问题与服务面风险
- 输出结构一致、适合复核的中文报告

### 2. 适用范围

本案例适用于：

- 主机基线检查输出
- 合规扫描结果
- 基础安全配置核查材料

不适用于：

- 应用层白盒材料
- 多文件综合审计输入
- 外部攻击面数据

### 3. 分类目标

- `source_type = host`
- `event_type = host_baseline_assessment`

### 4. 对应 Skill

- `megaeth.host.baseline_compliance_analysis`
- `megaeth.host.integrity_monitor`

### 5. 样本应训练系统学会什么

本案例的重点不在复杂聚合，而在单文件主机材料的稳定识别与分层判断。系统应学会：

- 识别高风险基线缺口
- 区分配置类问题和完整性类问题
- 判断问题是否影响到暴露面或基础防护能力
- 输出优先整改顺序

### 6. 目标输出特征

一份合格输出应具备以下特点：

- 分类正确
- Skill 路由正确
- 中文报告结构稳定
- 风险标签与建议动作互相一致
- 页面和导出报告结构一致

### 7. 训练重点

- 正确识别高风险基线缺口
- 区分配置缺口、完整性问题与服务面风险
- 输出中文合规分析结论与优先整改建议

### 8. 常见失败模式

本案例常见失败模式包括：

- 误判为通用文本或其它域输入
- 只输出问题清单，不形成优先级
- 把完整性问题和暴露面风险混为一类
- 页面与导出报告结构不一致

### 9. 完成标准

本案例只有在以下条件都满足时才算训练完成：

- 分类与路由正确
- 输出结论与建议有清晰分层
- 页面和下载结果一致
- 测试与文档同步更新

---

## English

### 1. Case Purpose

This case trains the system to understand host baseline material, risk scoring, and remediation guidance, and to produce stable Host baseline outputs.

It is not just about “processing a baseline file.” It teaches the system to:

- recognize Host-baseline inputs
- route them into the Host module correctly
- distinguish configuration gaps, integrity issues, and service-surface risk
- produce a stable, reviewable Chinese report

### 2. Scope

This case applies to:

- host baseline check outputs
- compliance scan results
- foundational host-security configuration materials

It does not apply to:

- whitebox application-security materials
- composite audit inputs
- external attack-surface datasets

### 3. Target Classification

- `source_type = host`
- `event_type = host_baseline_assessment`

### 4. Owning Skills

- `megaeth.host.baseline_compliance_analysis`
- `megaeth.host.integrity_monitor`

### 5. What the System Should Learn

The emphasis here is stable single-file Host analysis, not cross-file correlation. The system should learn to:

- identify high-risk baseline gaps
- separate configuration issues from integrity issues
- reason about exposure relevance where appropriate
- produce prioritized remediation advice

### 6. Target Output Characteristics

A correct output should have:

- correct classification
- correct Skill routing
- stable Chinese report structure
- consistent risk labels and recommendations
- matching page and export behavior

### 7. Training Focus

- correctly identify high-risk baseline gaps
- distinguish configuration gaps, integrity issues, and service-surface risk
- produce Chinese compliance conclusions and prioritized remediation advice

### 8. Common Failure Modes

Typical failures include:

- misclassifying the file into another domain
- listing issues without prioritization
- collapsing integrity and exposure problems into one bucket
- page/export structure drift

### 9. Completion Criteria

This case is complete only when:

- classification and routing are correct
- conclusions and actions are clearly layered
- page and export outputs match
- tests and docs are updated together
