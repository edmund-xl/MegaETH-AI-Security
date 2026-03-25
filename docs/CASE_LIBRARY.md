# 案例库
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档列出当前已经正式落地的训练案例和模板案例，并说明它们与 Skill、页面和报告之间的关系。

### 2. 当前案例的角色

在当前主线中，训练案例不是样本仓库的简单备份，而是能力校准的证据层。一个案例至少应回答：

- 样本是什么
- 目标输出是什么
- 系统需要学会什么
- 它对应哪些 Skill

### 3. 当前已落地正式案例

#### 3.1 `case_001_host_baseline`

- 方向：Host baseline
- 用途：主机基线合规分析训练
- 主要价值：
  - 校准主机基线分类
  - 校准 Host baseline 报告结构
  - 验证 Host Skill 的稳定性

#### 3.2 `case_002_jumpserver_multisource`

- 方向：JumpServer 多源审计
- 用途：登录、命令、文件传输、管理平面综合判断训练
- 主要价值：
  - 校准单文件与综合 Skill 路由
  - 校准页面与导出一致性
  - 校准多源综合判断质量

#### 3.3 `case_003_easm_multilayer`

- 方向：EASM 多层综合评估
- 用途：单样本分析与多样本综合评估训练
- 主要价值：
  - 校准单文件 EASM 路由
  - 校准多文件综合分析
  - 校准 `easm_asset_assessment`
  - 校准综合结论与专业判断

### 4. 当前模板案例

当前模板型案例包括：

- Whitebox AppSec 模板

模板案例的作用不是替代真实案例，而是：

- 为新样本接入提供统一格式
- 为新报告结构提供约束
- 为新 Skill 训练提供起点

### 5. 案例与 Skill 的关系

案例与 Skill 的关系是：

- 案例提供真实输入和目标输出
- Skill 提供行为边界和执行契约
- 两者共同定义“系统应该学成什么样”

当前任何正式能力如果没有对应案例或模板，就不能算完全落地。

### 6. 案例与页面的关系

训练案例最终会影响以下页面：

- `技能`
  - 影响训练覆盖统计
- `学习`
  - 影响学习反馈沉淀
- `输入`
  - 影响路由与报告结果质量
- `概览`
  - 间接影响平台能力覆盖状态

### 7. 当前案例的最低组成

一份正式案例至少应包含：

- 样本解释
- 目标输出
- 系统规则
- 对应 Skill

如果是复杂案例，建议额外包含：

- 文件层次说明
- 页面预期
- 导出报告预期
- 常见失败模式

### 8. 新增案例的最低要求

新增案例至少需要同步：

- 样本解释
- 目标输出
- 系统规则
- 对应 Skill 说明
- 文档更新

如果案例涉及新分析域，还应同步：

- Planner 路由
- 页面显示
- 导出结构
- 测试

### 9. 当前案例治理原则

当前案例治理遵循以下原则：

- 真实样本优先
- 目标输出明确优先
- 案例必须可复核
- 案例必须能映射到 Skill
- 案例变更应同步文档和 GitHub

### 10. 当前高价值案例阅读顺序

建议按以下顺序阅读案例：

1. `case_001_host_baseline`
2. `case_002_jumpserver_multisource`
3. `case_003_easm_multilayer`
4. Whitebox AppSec 模板

### 11. 结论

当前案例库应被理解为：

- 主线能力的训练证据层
- Skill 与真实样本之间的桥梁
- 报告质量与分类边界持续校准的主要来源

---

## English

### 1. Purpose

This document lists the formally landed training cases and template cases, and explains how they connect to Skills, the UI, and reporting behavior.

### 2. The Role of Cases

In the current mainline, a training case is not just sample storage. It is the evidence layer for capability calibration. A case should answer:

- what the sample is
- what the target output is
- what the system must learn
- which Skills it maps to

### 3. Formally Landed Cases

The current formal cases are:

- `case_001_host_baseline`
- `case_002_jumpserver_multisource`
- `case_003_easm_multilayer`

Each case supports a different part of the active mainline and provides evidence that the related Skills have landed.

### 4. Template Cases

Current template cases include:

- the Whitebox AppSec template

Templates exist to:

- normalize onboarding for new samples
- constrain new report structures
- provide a starting point for new Skill training

### 5. Relationship Between Cases and Skills

The relationship is:

- cases provide real samples and target outputs
- Skills define behavior boundaries and execution contracts
- together they define what the system should learn

No capability should be considered fully landed without either a formal case or a template path.

### 6. Relationship Between Cases and the UI

Training cases ultimately influence:

- `技能`
- `学习`
- `输入`
- `概览`

through training coverage, learning retention, routing quality, and overall capability state.

### 7. Minimum Structure of a Formal Case

A formal case should include:

- sample interpretation
- target outputs
- system rules
- mapped Skills

For complex cases, it is also helpful to include:

- file-layer descriptions
- expected page behavior
- expected export behavior
- common failure modes

### 8. Minimum Requirements for New Cases

A new case should land together with:

- sample interpretation
- target outputs
- system rules
- mapped Skill documentation
- document updates

If the case introduces a new domain, it should also update:

- Planner routing
- UI visibility
- export structure
- tests

### 9. Governance Principles

Current case governance prefers:

- real samples
- explicit target outputs
- reviewable case content
- traceable mapping to Skills
- synchronized doc and GitHub updates

### 10. Recommended Reading Order

Suggested order:

1. `case_001_host_baseline`
2. `case_002_jumpserver_multisource`
3. `case_003_easm_multilayer`
4. the Whitebox AppSec template

### 11. Summary

The case library should be understood as:

- the training-evidence layer of the active mainline
- the bridge between Skills and real samples
- the primary source for ongoing calibration of classification boundaries and report quality
