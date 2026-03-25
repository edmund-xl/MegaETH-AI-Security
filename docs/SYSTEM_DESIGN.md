# 系统设计说明
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档描述 MegaETH AI Security Platform 当前主线的系统设计。重点说明：

- 系统边界
- 运行架构
- 核心模块职责
- 主要数据模型
- 分析链路
- 当前实现限制

本文档服务于开发、维护、回归测试和交接，不用于市场宣传。

### 2. 系统边界

当前仓库只服务于一个产品域：

- 安全日志分析

系统当前负责的能力包括：

- 本地文件与文本输入
- 平台材料导入
- 原始事件归一化
- 事件分类与 Skill 路由
- 风险判断与报告生成
- 历史、调查与学习沉淀

系统当前不负责：

- 自动处置
- 分布式扫描编排
- 多租户隔离
- 第二产品域

### 3. 逻辑分层

当前系统按三层组织：

- 输入与接入层
  - 文件上传
  - 文本输入
  - 平台导入入口
- 分析与报告层
  - 归一化
  - Planner
  - Skill 执行
  - 风险判断
  - 报告生成
- 留存与学习层
  - 历史记录
  - 调查会话
  - 学习反馈
  - 训练案例

### 4. 核心模块

#### 4.1 API 层

负责：

- 暴露后端接口
- 承载前端页面
- 接收上传和分析触发请求

主要位置：

- `/app/api`
- `/app/main.py`

#### 4.2 分析层

负责：

- 文件识别与摄取
- 原始事件标准化
- Planner 分类
- Skill 执行
- 风险判断
- 报告构建

主要位置：

- `/app/core`
- `/app/skills`
- `/app/utils`

#### 4.3 留存层

负责：

- 历史事件存储
- 调查记录
- 报告落库
- 学习反馈

当前存储方式以本地 JSON 与压缩归档为主。

### 5. 主要数据对象

当前主线围绕以下对象运作：

- `RawEvent`
  - 原始输入或导入后的事件载荷
- `NormalizedEvent`
  - 归一化后的统一事件模型
- `Finding`
  - 单条分析结果
- `SecurityReport`
  - 报告对象
- `Investigation`
  - 调查批次
- `LearningRule`
  - 长期规则
- `LearningFeedback`
  - 最近学习反馈

### 6. 核心运行链路

标准链路如下：

```text
原始安全材料 / 平台导入
-> 输入解析
-> 归一化
-> Planner 分类
-> Skill 执行
-> 风险判断
-> 报告生成
-> 历史 / 调查 / 学习沉淀
```

### 7. 当前已落地分析域

当前已经稳定落地的主分析域包括：

- Host baseline
- Endpoint 平台事件
- JumpServer 单文件与多源审计
- Whitebox AppSec 三段式分析
- EASM 单样本与多样本综合分析

### 8. 当前设计约束

当前设计有以下明确约束：

- 页面固定为五页工作台
- 默认端口为 `8011`
- 共享层改动必须验证五个页面
- 真实样本训练必须同步检查页面与下载结果一致性
- 文档更新必须和代码更新同步

### 9. 当前限制

当前系统更适合：

- 分析
- 审计
- 报告
- 学习沉淀

当前系统还不适合：

- 大规模自动处置
- 高并发远程执行
- 企业级多环境调度

## English

### 1. Purpose

This document defines the current system design of MegaETH AI Security Platform. It covers:

- system boundary
- runtime architecture
- component ownership
- primary data models
- analysis flow
- known implementation limits

This document is intended for engineering, maintenance, regression, and handoff.

### 2. System Boundary

The repository currently serves only one product surface:

- security log analysis

It is responsible for:

- local file and text intake
- platform-material import
- raw-event normalization
- event classification and Skill routing
- risk judgment and report generation
- history, investigation, and learning retention

It does not currently cover:

- auto-remediation
- distributed scan orchestration
- multi-tenancy
- any second product surface

### 3. Logical Layers

The system is organized into three layers:

- intake and integration
- analysis and reporting
- retention and learning

### 4. Core Components

#### 4.1 API Layer

The API layer:

- exposes backend endpoints
- serves the frontend
- receives upload and analysis-trigger requests

Primary locations:

- `/app/api`
- `/app/main.py`

#### 4.2 Analysis Layer

The analysis layer handles:

- file recognition and ingest
- raw-event normalization
- Planner classification
- Skill execution
- risk judgment
- report construction

Primary locations:

- `/app/core`
- `/app/skills`
- `/app/utils`

#### 4.3 Retention Layer

The retention layer stores:

- historical events
- investigations
- persisted reports
- learning feedback

Persistence is currently file-backed through local JSON plus compressed archives.

### 5. Primary Data Objects

The current mainline revolves around:

- `RawEvent`
- `NormalizedEvent`
- `Finding`
- `SecurityReport`
- `Investigation`
- `LearningRule`
- `LearningFeedback`

### 6. Core Runtime Flow

```text
Raw security material / platform import
-> intake parsing
-> normalization
-> Planner classification
-> Skill execution
-> risk judgment
-> report generation
-> history / investigation / learning retention
```

### 7. Implemented Analysis Domains

Currently landed analysis domains include:

- Host baseline
- Endpoint platform events
- JumpServer single-source and multi-source audit analysis
- Whitebox AppSec three-stage analysis
- EASM single-source and composite analysis

### 8. Design Constraints

Current design constraints include:

- a fixed five-page workbench UI
- default runtime port `8011`
- shared-layer changes must be validated across all five pages
- real-sample training must verify page/export consistency
- documentation updates must land together with code changes

### 9. Current Limits

The system is currently optimized for:

- analysis
- auditing
- reporting
- learning retention

It is not yet optimized for:

- large-scale auto-remediation
- high-concurrency remote execution
- enterprise-grade multi-environment orchestration
