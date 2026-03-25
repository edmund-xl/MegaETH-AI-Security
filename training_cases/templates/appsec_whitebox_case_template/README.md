# Whitebox AppSec 案例模板
<!-- security-log-analysis mainline -->

## 中文

### 1. 模板目的

本模板用于承接未来的白盒应用安全样本，使 AppSec 训练案例保持统一目录结构、统一目标输出约束和统一规则沉淀方式。

### 2. 适用场景

本模板适用于：

- 源码审计样本
- 白盒验证样本
- 白盒综合报告样本

### 3. 对应 Skill

- `megaeth.appsec.whitebox_recon`
- `megaeth.appsec.whitebox_exploit_validation`
- `megaeth.appsec.whitebox_report_synthesis`

### 4. 模板至少应包含的内容

建议每个基于模板创建的新案例至少包含：

- 样本解释
- 目标输出
- 系统规则
- 路由边界
- 对应 Skill

### 5. 使用要求

新案例不应只复制模板标题。创建时应补齐：

- 该白盒样本属于哪个阶段
- 应路由到哪个 Skill
- 输出报告结构是什么
- 哪些判断必须保持证据边界

---

## English

### 1. Template Purpose

This template exists to onboard future whitebox application-security samples with a consistent directory structure, output contract, and rule-retention model.

### 2. Applicable Scenarios

This template applies to:

- source-review samples
- whitebox validation samples
- whitebox composite report samples

### 3. Owning Skills

- `megaeth.appsec.whitebox_recon`
- `megaeth.appsec.whitebox_exploit_validation`
- `megaeth.appsec.whitebox_report_synthesis`

### 4. Minimum Contents

Each case created from this template should include:

- sample interpretation
- target outputs
- system rules
- routing boundaries
- mapped Skills

### 5. Usage Rules

Do not create a new whitebox case by copying only the title. Each new case should explain:

- which whitebox stage it belongs to
- which Skill should own it
- what report structure is expected
- which judgments must remain evidence-bounded
