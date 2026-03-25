# 训练工作流
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档说明如何使用真实样本持续训练和校准安全日志分析主线，重点帮助开发者回答：

- 训练输入应准备什么
- 标准训练流程应该怎么走
- 哪些检查不能省
- 一轮训练什么时候才算完成

### 2. 训练输入要求

一轮有效训练至少应包含：

- 原始样本
- 目标输出
- 分类边界要求
- 报告结构要求

如果缺少目标输出，训练只能完成基础识别，无法完成高质量报告校准。

### 3. 样本来源

当前训练样本通常来自：

- Host baseline 检查结果
- JumpServer 导出材料
- Bitdefender 平台事件
- Whitebox AppSec 材料
- EASM CSV 文件

训练时优先使用：

- 真实样本
- 有明确目标输出的样本
- 多文件能体现综合判断的样本

### 4. 标准训练流程

推荐训练流程如下：

1. 接收样本
2. 识别输入源和文件层次
3. 校准文件识别和事件提示
4. 校准分类与 Skill 路由
5. 校准结构化输出和报告结构
6. 回归页面输出与导出报告
7. 沉淀训练案例与学习反馈
8. 更新文档并同步 GitHub

### 5. 当前重点训练主题

当前重点训练主题包括：

- Host baseline
- JumpServer 多源审计
- Whitebox AppSec
- EASM 单样本分析
- EASM 多样本综合分析

### 6. 训练时必须验证的事项

不能只验证“文件能读出来”或“解析成功”，还必须验证：

- 表头是否正确归一化
- 行数是否被静默裁剪
- 聚合是否基于完整数据
- 分类是否正确
- Skill 路由是否正确
- 页面展示是否正确
- 下载报告是否正确
- 旧对象是否兼容

### 7. 当前已知高风险失败模式

当前已知高风险模式包括：

- 大文件只分析前几百行
- 表头带特殊字符导致字段取空
- 单文件和旧输入串线
- 旧报告对象与新模板不一致
- 页面与下载结构漂移
- 只改代码不改文档

### 8. 训练沉淀要求

一轮有效训练结束后，至少要沉淀到以下位置中的一部分：

- `training_cases/`
- `data/` 历史和调查记录
- `学习反馈`
- `skill_specs/`
- `docs/`

如果训练改变了能力边界或报告结构，必须同步更新相关文档。

### 9. EASM 训练说明

当前 EASM 训练分两条：

#### 9.1 单样本训练

目标是验证：

- 文件识别
- 单文件分类
- 单域 Skill 路由
- 单文件报告结构

#### 9.2 多样本综合训练

目标是验证：

- 多文件聚合
- 跨层关联
- `easm_asset_assessment` 生成
- 综合结论与专业判断质量

### 10. 模型增强训练边界

对于允许增强的综合判断段落，训练时必须遵守：

- 事实抽取由规则负责
- 模型只增强允许增强的报告段落
- 模型失败时必须能回退到规则版
- 页面与导出必须使用同一结构

### 11. 训练完成标准

一轮训练只有在以下条件全部成立时，才算完成：

- 分类正确
- Skill 路由正确
- 页面输出正确
- 导出输出正确
- 测试通过
- 文档同步
- GitHub 同步

### 12. 结论

当前主线训练的本质不是“把样本喂进去”，而是：

- 用真实样本修正系统边界
- 用目标输出校准报告质量
- 用训练案例和文档把改动沉淀成长期能力

---

## English

### 1. Purpose

This document explains how to continuously train and calibrate the security-log-analysis mainline using real samples. It answers:

- what inputs are required
- what the standard training flow looks like
- which checks are mandatory
- when a training cycle is actually complete

### 2. Required Training Inputs

A meaningful training cycle should include:

- raw samples
- target outputs
- classification boundaries
- report-structure requirements

Without target outputs, training can only improve basic recognition, not reporting quality.

### 3. Sample Sources

Training samples currently come from:

- Host baseline outputs
- JumpServer exports
- Bitdefender platform events
- Whitebox AppSec materials
- EASM CSV files

Preferred samples are:

- real samples
- samples with explicit target outputs
- multi-file samples that exercise composite judgment

### 4. Standard Training Flow

The recommended flow is:

1. receive samples
2. identify source and file layers
3. calibrate file recognition and event hints
4. calibrate classification and Skill routing
5. calibrate structured outputs and report structure
6. regress page output and exported reports
7. retain training cases and learning feedback
8. update docs and sync GitHub

### 5. Current Training Priorities

Current priorities include:

- Host baseline
- JumpServer multi-source audit analysis
- Whitebox AppSec
- EASM single-source analysis
- EASM composite multi-file analysis

### 6. What Must Be Verified

Do not stop at “the parser succeeded.” Also verify:

- header normalization
- row-count integrity
- full-data aggregation
- classification correctness
- Skill routing correctness
- page rendering correctness
- export-report correctness
- compatibility with older stored objects

### 7. Known High-Risk Failure Modes

Known high-risk failure modes include:

- only the first few hundred rows being analyzed
- special characters in headers breaking field access
- single-file runs mixing with stale intake state
- old report objects drifting from new templates
- page/export structure drift
- code changes landing without doc updates

### 8. Retention Requirements

A useful training cycle should leave retained artifacts in at least part of:

- `training_cases/`
- `data/` history and investigations
- learning feedback
- `skill_specs/`
- `docs/`

If training changes capability boundaries or report structure, the related docs must be updated too.

### 9. EASM Training Notes

Current EASM training has two tracks:

#### 9.1 Single-Source Training

Focus on:

- file recognition
- single-file classification
- single-domain Skill routing
- single-file report structure

#### 9.2 Composite Multi-File Training

Focus on:

- multi-file aggregation
- cross-layer correlation
- generation of `easm_asset_assessment`
- quality of composite judgment sections

### 10. Model-Augmentation Boundary

For composite sections that allow model enhancement:

- facts remain rule-owned
- models only enhance explicitly allowed report sections
- model failures must fall back to rule-owned output
- page and export outputs must use the same structure

### 11. Completion Criteria

A training cycle is complete only when all of the following hold:

- classification is correct
- Skill routing is correct
- page output is correct
- export output is correct
- tests pass
- docs are updated
- GitHub is synchronized

### 12. Summary

Training in this mainline is not just “feeding samples into the system.” It is:

- using real samples to correct system boundaries
- using target outputs to calibrate reporting quality
- using training cases and documentation to retain the improvement as a durable capability
