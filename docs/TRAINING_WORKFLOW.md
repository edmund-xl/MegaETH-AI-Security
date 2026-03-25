# 训练工作流
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档说明如何用真实样本持续训练和校准安全日志分析主线。

### 2. 训练输入要求

一轮有效训练至少应包含：

- 原始样本
- 目标输出
- 分类边界要求
- 报告结构要求

如果缺少目标输出，训练只能做基础识别，不能完成高质量校准。

### 3. 标准训练流程

推荐流程如下：

1. 接收样本
2. 识别输入源和文件层次
3. 校准分类与 Skill 路由
4. 校准报告结构与语言
5. 回归页面与下载结果
6. 沉淀到训练案例与学习反馈
7. 同步文档与 GitHub

### 4. 当前重点训练主题

当前重点训练主题包括：

- Host baseline
- JumpServer 多源审计
- Whitebox AppSec
- EASM 单样本分析
- EASM 多样本综合分析

### 5. 训练时必须验证的事项

不能只验证“解析成功”，还必须验证：

- 表头是否正确归一化
- 行数是否被裁剪
- 聚合是否基于完整数据
- 页面展示是否正确
- 下载报告是否正确
- 旧数据对象是否兼容

### 6. 当前常见失败模式

当前已知高风险失败模式包括：

- 大文件只分析前几百行
- 表头带特殊字符导致聚合字段取空
- 单文件与旧输入串线
- 页面和下载报告结构不一致
- 只改代码不改文档

### 7. 训练完成标准

一轮训练只有在以下条件都成立时，才算完成：

- 分类正确
- Skill 路由正确
- 页面输出正确
- 下载输出正确
- 测试通过
- 文档同步
- GitHub 同步

## English

### 1. Purpose

This document explains how to continuously train and calibrate the security-log-analysis mainline using real samples.

### 2. Required Training Inputs

A meaningful training cycle should include:

- raw samples
- target outputs
- classification boundaries
- report-structure expectations

Without target outputs, training can only calibrate basic recognition, not high-quality reporting.

### 3. Standard Training Flow

The recommended flow is:

1. receive samples
2. identify input source and file layers
3. calibrate classification and Skill routing
4. calibrate report structure and language
5. regress page and export outputs
6. retain case and learning feedback
7. sync docs and GitHub

### 4. Current Training Priorities

Current priorities include:

- Host baseline
- JumpServer multi-source auditing
- Whitebox AppSec
- EASM single-source analysis
- EASM composite multi-file analysis

### 5. What Must Be Verified

Do not stop at “the parser succeeded.” Also verify:

- header normalization
- row-count integrity
- full-data aggregation
- page rendering correctness
- export-report correctness
- compatibility with older stored objects

### 6. Common Failure Modes

Known high-risk failure modes include:

- only the first few hundred rows being analyzed
- special characters in headers breaking aggregation
- single-file runs mixing with stale intake state
- page and export structures drifting apart
- code updates landing without doc updates

### 7. Completion Criteria

A training cycle is complete only when all of the following hold:

- classification is correct
- Skill routing is correct
- page output is correct
- export output is correct
- tests pass
- docs are updated
- GitHub is synchronized
