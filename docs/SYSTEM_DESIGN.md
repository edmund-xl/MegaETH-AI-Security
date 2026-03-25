# 系统设计说明
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档说明 MegaETH AI Security Platform 当前主线的系统设计，重点回答以下问题：

- 系统到底做什么，不做什么
- 输入、分析、报告和留存如何串起来
- 核心模块分别承担什么职责
- 当前主线的主要数据对象是什么
- 现在已经实现到什么程度

本文档面向开发、维护、回归测试、交接和后续样本训练，不面向市场宣传。

### 2. 系统边界

当前仓库只服务于一个产品域：

- 安全日志分析

当前系统负责的事情包括：

- 接收安全材料和平台导入结果
- 解析并归一化原始输入
- 使用 Planner 选择事件类型与 Skill 路由
- 生成 Findings、报告、调查记录和学习反馈
- 使用真实样本持续校准分析链路

当前系统不负责：

- 自动处置
- 主机/云环境远程执行编排
- 第二产品域控制面
- 多租户 SaaS 级隔离

### 3. 设计原则

当前主线遵循以下原则：

#### 3.1 单一产品域

只保留安全日志分析一条主线。任何新能力如果无法自然落在这条主线内，就不应直接进入本仓库。

#### 3.2 规则主链优先

事实提取、字段归一化、分类、结构化输出和导出结构必须由系统控制，不能交给模型自由发挥。

#### 3.3 受控模型增强

模型只能增强允许增强的段落，例如综合结论、专业判断等，不得替代：

- 原始字段抽取
- 风险结构计算
- 报告骨架定义
- 持久化结构

#### 3.4 样本驱动迭代

系统能力的主要推进方式不是先设计大而全的平台，而是：

1. 接收真实样本
2. 对齐目标输出
3. 修正分类与 Skill 路由
4. 修正报告和导出
5. 沉淀训练案例、学习反馈与文档

### 4. 系统分层

当前系统按四层理解最清晰。

#### 4.1 输入与接入层

负责：

- 文件上传
- 文本输入
- 平台材料导入
- 文件识别和基础分流

核心位置：

- `/app/api`
- `/app/utils/file_ingest.py`

#### 4.2 归一化与规划层

负责：

- 原始事件标准化
- 表头修正、字段归并、事件提示
- Planner 分类
- Skill 路由
- 识别单文件直达链与多文件综合链

核心位置：

- `/app/core/normalizer.py`
- `/app/core/planner.py`

#### 4.3 分析与报告层

负责：

- 单文件 Skill 执行
- 多文件聚合与综合事件生成
- 风险判断
- EASM / JumpServer / Host / Whitebox 等域内分析
- SecurityReport 生成
- 受控模型增强

核心位置：

- `/app/skills`
- `/app/core/report_engine.py`
- `/app/core/agent_model_binding.py`

#### 4.4 留存与学习层

负责：

- 历史事件
- 调查批次
- 报告落库
- 学习反馈
- 训练案例

核心位置：

- `/app/core/history.py`
- `/data`
- `/training_cases`

### 5. 核心模块职责

#### 5.1 API 层

API 层负责：

- 暴露前端工作台
- 接收上传请求
- 提供概览、技能、历史、报告等读取接口
- 提供分析触发入口

#### 5.2 Planner

Planner 的职责是：

- 根据归一化结果判断事件类型
- 选择一个或多个 Skill
- 决定是否生成综合事件
- 决定当前输入是走单文件直达链还是多文件综合链

Planner 不负责：

- 最终报告撰写
- 风险分持久化
- 页面渲染

#### 5.3 Skill 层

Skill 层负责：

- 领域内分析逻辑
- 结构化 findings
- 受控判断边界
- 报告片段输入

Skill 不负责：

- 接管整个系统生命周期
- 替代持久化层
- 破坏报告骨架

#### 5.4 Report Engine

Report Engine 负责：

- 将 findings 和综合结果组织成固定报告结构
- 保证页面和导出版本结构一致
- 在允许的报告段落中接入 Gemini 等模型增强

### 5.6 聚合器 / 综合事件层

在多文件分析场景下，系统会在 Planner 与 Skill 之间插入聚合器逻辑。

聚合器负责：

- 识别同一批次中的相关文件
- 生成综合事件
- 为综合 Skill 提供跨文件上下文

当前已明确存在的综合链包括：

- JumpServer 多文件综合审计
- EASM 多文件综合评估

#### 5.5 History / Learning

History 与 Learning 负责：

- 沉淀最近运行历史
- 保存调查记录
- 提供学习反馈展示
- 与训练案例形成闭环

### 6. 主要数据对象

当前主线中的关键对象包括：

#### 6.1 RawEvent

表示原始输入材料的初始表示，通常保留：

- 来源文件
- 原始载荷
- 摄取时间
- 文件层类型提示

#### 6.2 NormalizedEvent

表示统一后的事件模型，通常保留：

- 事件类型
- 来源层次
- 统一字段
- Planner 所需的路由信息

#### 6.3 Finding

表示一条分析输出，通常保留：

- 标题
- 严重性/风险标签
- 证据事实
- 评估描述
- 建议动作
- Skill 来源

#### 6.4 SecurityReport

表示页面与导出共用的报告对象，通常保留：

- 报告类型
- 标题
- 摘要
- 分段正文
- 执行模式
- 关联 findings

#### 6.5 Investigation

表示一次样本输入和分析批次，通常保留：

- investigation_id
- 文件列表
- 事件类型
- 结果数量
- 关联报告

#### 6.6 LearningFeedback

表示最近的学习沉淀，通常保留：

- 来源样本
- 关联能力
- 学习方向
- 时间信息

### 7. 核心运行链路

标准运行链如下：

```text
原始安全材料 / 平台导入
-> 输入解析
-> 归一化
-> Planner 分类
-> 单文件 Skill 或多文件聚合
-> findings / 综合事件
-> 风险判断
-> 报告结构生成
-> 受控 Gemini 增强（可选）
-> 历史 / 调查 / 学习沉淀
```

在当前实现中，这条链是最重要的系统主轴，任何能力都必须能映射到这条路径中的某个位置。

### 8. 单文件与综合链的分流

当前系统并不是所有输入都走同一条直线链路，而是至少包含两类运行模式：

#### 8.1 单文件直达链

适用于：

- Host baseline
- JumpServer 单文件
- Whitebox 单阶段输入
- EASM 单文件

标准模式为：

```text
单文件输入 -> 归一化 -> Planner -> 对应 Skill -> findings -> report
```

#### 8.2 多文件综合链

适用于：

- JumpServer 多文件同批次输入
- EASM 多文件同批次输入

标准模式为：

```text
多文件输入 -> 归一化 -> Planner -> 聚合器 -> 综合事件 -> 综合 Skill -> report
```

### 9. 当前综合链实例

#### 9.1 JumpServer

当前 JumpServer 支持：

- 登录、命令、文件传输、管理平面单文件分析
- 多文件同批次聚合成综合审计结果
- 综合判断在固定结构下由 Gemini 增强

#### 9.2 EASM

当前 EASM 支持：

- 服务、DNS、证书、ASN、IP 等单文件分析
- 多文件同批次聚合成 `easm_asset_assessment`
- 综合报告中的 `assessment / professional_judgment` 由 Gemini 增强
### 10. 当前已落地主分析域

当前已稳定落地的域包括：

- Host baseline
- Endpoint 平台事件
- Identity / JumpServer
- Whitebox AppSec
- EASM
- Cloud
- Key Security
- CI/CD

其中 EASM 当前已完成：

- 单文件分析
- 多文件综合分析
- `easm_asset_assessment` 结果生成
- 综合报告中 `assessment / professional_judgment` 的受控 Gemini 增强

### 11. 模型增强策略

模型增强当前不是全链路默认行为，而是受控启用。

当前原则如下：

- 规则负责事实、结构和分类
- 模型负责高层语言增强
- 失败时必须能回退到规则输出

当前模型增强不应被理解为“整条链交给 Gemini”，而应被理解为：

- 规则拥有事实层
- Report Engine 拥有结构层
- Gemini 只增强允许增强的总结或专业判断段

典型适合模型增强的段落包括：

- JumpServer 多源综合结论
- EASM 多文件综合专业判断
- 白盒综合报告中的高层总结段

### 12. 运行与持久化现实

当前系统仍然是本地优先、文件驱动的实现：

- 前端为静态工作台
- 后端为 FastAPI
- 主要持久化仍为本地 JSON 和压缩归档

这意味着当前系统适合：

- 本地分析
- 样本训练
- 交互式复核

而不适合：

- 企业级高并发执行环境
- 云端多实例分布式运行

### 13. 已知高风险点

当前系统的高风险点包括：

- 大文件被静默裁剪
- 特殊表头导致字段归并失败
- 旧对象和新模板不一致
- 共享前端逻辑影响五页面工作台
- 改代码不改文档
- 综合输入没有走到综合事件链
- 模型增强段落与规则事实层边界漂移

### 14. 设计结论

当前系统的正确理解方式是：

- 一个围绕真实样本持续训练的安全日志分析平台
- 一个规则主链优先、模型受控增强的报告系统
- 一个本地优先、重视交互复核与学习沉淀的工程主线
- 一个同时支持单文件直达链与多文件综合链的分析架构

---

## English

### 1. Purpose

This document explains the current system design of MegaETH AI Security Platform and answers:

- what the system does and does not do
- how intake, analysis, reporting, and retention connect
- what each core module is responsible for
- what the main data objects are
- how far the current mainline has been implemented

### 2. System Boundary

The repository now serves only one product surface:

- security log analysis

The current system is responsible for:

- ingesting security materials and platform imports
- parsing and normalizing inputs
- selecting event types and Skills through the Planner
- generating findings, reports, investigations, and learning feedback
- continuously calibrating the pipeline with real samples

The current system does not cover:

- auto-remediation
- remote execution orchestration
- a second product surface
- multi-tenant SaaS isolation

### 3. Design Principles

The mainline follows these principles:

- single product surface
- rule-first pipeline ownership
- controlled model augmentation
- sample-driven iteration

### 4. System Layers

The current system is most clearly understood as four layers:

- intake and integration
- normalization and planning
- analysis and reporting
- retention and learning

### 5. Core Component Responsibilities

The major components are:

- API
- Planner
- Skills
- Report Engine
- History / Learning

Each has a separate ownership boundary and should not take over another layer's job.

### 6. Primary Data Objects

The main objects in the current mainline are:

- `RawEvent`
- `NormalizedEvent`
- `Finding`
- `SecurityReport`
- `Investigation`
- `LearningFeedback`

### 7. Primary Runtime Path

```text
raw security material / platform import
-> intake parsing
-> normalization
-> Planner classification
-> Skill execution
-> risk judgment
-> report generation
-> history / investigation / learning retention
```

### 8. Implemented Analysis Domains

The currently landed domains include:

- Host baseline
- Endpoint platform events
- Identity / JumpServer
- Whitebox AppSec
- EASM
- Cloud
- Key Security
- CI/CD

EASM currently supports:

- single-file analysis
- composite multi-file analysis
- generation of `easm_asset_assessment`
- controlled Gemini enhancement for composite judgment sections

### 9. Model Augmentation Strategy

Model augmentation is not the default for the whole system.

Current policy:

- rules own facts, structure, and classification
- models enhance high-level judgment language
- failures must fall back to rule-owned outputs

### 10. Runtime and Persistence Reality

The system remains local-first and file-backed:

- static frontend workbench
- FastAPI backend
- local JSON and compressed archives as the primary persistence model

It is suitable for:

- local analysis
- sample-driven training
- interactive review

It is not yet suitable for:

- enterprise-scale high-concurrency environments
- distributed cloud-native execution

### 11. Known High-Risk Failure Areas

High-risk areas currently include:

- silent truncation of large files
- header normalization failures
- drift between old stored objects and new templates
- shared frontend changes affecting all five pages
- code changes landing without documentation updates

### 12. Design Summary

The current system should be understood as:

- a security-log-analysis platform refined through real samples
- a rule-first reporting system with controlled model enhancement
- a local-first engineering mainline optimized for review and learning retention
