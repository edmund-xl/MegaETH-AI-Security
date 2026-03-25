# 接入与执行能力库
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档说明当前主线的接入面、执行面和受控增强边界。

### 2. 接入面

当前可见接入面包括：

- 文件上传
- 文本输入
- Bitdefender 输入
- Whitebox AppSec 材料输入
- EASM CSV 输入

这些接入面全部服务于安全日志分析，不构成独立产品。

### 3. 标准执行链

默认执行链为：

```text
ingest -> normalize -> plan -> skill -> risk -> report
```

各阶段作用如下：

- ingest
  - 识别文件、文本和输入形态
- normalize
  - 标准化为统一事件模型
- plan
  - 选择事件类型与 Skill
- skill
  - 产生 findings 和结构化判断
- risk
  - 给出风险等级和标签
- report
  - 生成页面与导出报告

### 4. 受控增强

部分 Skill 可接入受控模型增强，但原则是：

- 事实提取由系统完成
- 结构与 schema 由系统控制
- 模型只增强特定叙述段落

当前已接入的代表性模式包括：

- JumpServer 综合判断增强
- EASM 多文件综合 `assessment / professional_judgment` 增强

### 5. 当前可见输入到 Skill 的映射方向

典型映射包括：

- Host baseline 材料 -> Host baseline Skills
- JumpServer 单文件或多文件材料 -> JumpServer 系列 Skills
- Whitebox 材料 -> Whitebox AppSec Skills
- EASM CSV 材料 -> EASM 单样本或综合评估 Skill

### 6. 管理边界

必须遵守以下边界：

- 接入面不能扩展成第二产品域
- 模型增强不能替代结构化事实提取
- 共享执行链改动必须回归五个页面
- 新输入源接入必须同步文档、测试和训练案例

## English

### 1. Purpose

This document explains the current integration surfaces, execution surfaces, and controlled-augmentation boundaries.

### 2. Integration Surfaces

The visible intake surfaces currently include:

- file upload
- text input
- Bitdefender input
- Whitebox AppSec material input
- EASM CSV input

All of these serve the security-log-analysis mainline and do not form an independent product surface.

### 3. Standard Execution Path

The default execution chain is:

```text
ingest -> normalize -> plan -> skill -> risk -> report
```

Each phase currently serves this role:

- ingest
  - recognize file, text, and intake form
- normalize
  - convert inputs into a common event model
- plan
  - select event types and Skills
- skill
  - produce findings and structured judgments
- risk
  - assign risk labels and levels
- report
  - generate page and export reports

### 4. Controlled Augmentation

Some Skills may use controlled model augmentation, with these rules:

- factual extraction remains system-owned
- structure and schema remain system-owned
- the model only enhances specific narrative sections

Current examples include:

- JumpServer composite judgment enhancement
- EASM composite `assessment / professional_judgment` enhancement

### 5. Representative Intake-to-Skill Mapping

Typical mappings include:

- Host baseline materials -> Host baseline Skills
- JumpServer single-source or multi-source materials -> JumpServer Skills
- Whitebox materials -> Whitebox AppSec Skills
- EASM CSV materials -> EASM single-source or composite assessment Skills

### 6. Governance Boundary

The following boundaries must hold:

- integrations must not become a second product surface
- model augmentation must not replace structured factual extraction
- shared execution-chain changes must regress all five pages
- any new input source must land together with docs, tests, and training cases
