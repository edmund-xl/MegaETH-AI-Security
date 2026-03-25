# 架构说明
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档从结构视角说明系统如何工作，重点帮助开发、测试和交接快速理解：

- 前后端关系
- 主要运行路径
- 模块之间的连接方式
- 哪些边界不能被跨越

### 2. 系统上下文

当前系统接收两类主要输入：

- 本地安全材料
- 平台导入结果

这些输入统一进入同一条分析链，再输出：

- Findings
- 安全报告
- 调查记录
- 学习反馈

### 3. 前端架构

当前前端是单一静态工作台，固定五页：

- `概览`
- `输入`
- `技能`
- `连接`
- `学习`

前端负责：

- 展示当前主线状态
- 触发上传与分析
- 浏览能力、导入与学习结果

### 4. 后端架构

后端由以下部分组成：

- FastAPI 路由层
- 核心分析链
- 持久化层
- 静态资源服务

其中核心分析链按以下顺序工作：

- ingest
- normalize
- plan
- execute skills
- score risk
- generate reports

### 5. 运行关键路径

用户行为与系统运行的最常见路径是：

```text
上传文件 / 文本输入
-> 创建调查批次
-> 文件摄取与识别
-> 归一化
-> Planner 选择事件类型与 Skills
-> Skill 输出 findings
-> 报告生成
-> 历史与学习沉淀
```

### 6. 关键结构关系

可以把当前系统理解成以下关系：

```text
输入源 -> 归一化事件 -> Planner -> Skill -> Findings -> Reports -> History/Learning
```

各层职责不要混淆：

- 输入层不做最终判断
- 归一化层不做报告生成
- Planner 不直接写报告
- Skill 不直接替代持久化层

### 7. 主要边界

当前有几个必须遵守的边界：

- 只保留安全日志分析一个产品域
- 共享前端逻辑改动必须验证五个页面
- 不允许跨项目样本污染当前运行历史
- 大文件处理不能只验证“读出来”，还要验证聚合与页面输出

### 8. 当前实现现实

当前架构更偏：

- 本地分析工作台
- 训练驱动能力扩展
- 规则与受控模型增强并存

而不是：

- 云原生分布式系统
- 多租户 SaaS 平台
- 全自动处置编排中心

## English

### 1. Purpose

This document explains the system from a structural perspective, focusing on:

- frontend and backend relationship
- primary runtime paths
- connections between modules
- boundaries that must not be crossed

### 2. System Context

The system currently ingests two major categories of input:

- local security materials
- platform-imported results

These inputs enter a single analysis pipeline and produce:

- findings
- security reports
- investigations
- learning feedback

### 3. Frontend Architecture

The frontend is a single static workbench with five fixed pages:

- `概览`
- `输入`
- `技能`
- `连接`
- `学习`

The frontend is responsible for:

- showing platform state
- triggering upload and analysis
- browsing capabilities, integrations, and learning outputs

### 4. Backend Architecture

The backend consists of:

- FastAPI routes
- the core analysis pipeline
- the persistence layer
- static asset serving

The core pipeline currently works in this order:

- ingest
- normalize
- plan
- execute skills
- score risk
- generate reports

### 5. Primary Runtime Path

The most common user-to-system path is:

```text
upload file / text input
-> create investigation batch
-> file ingest and recognition
-> normalization
-> Planner selects event types and Skills
-> Skills produce findings
-> report generation
-> history and learning retention
```

### 6. Key Structural Relationship

The current system can be summarized as:

```text
input sources -> normalized events -> Planner -> Skills -> findings -> reports -> history/learning
```

Responsibilities should remain separated:

- intake does not make final judgments
- normalization does not generate final reports
- Planner does not directly author reports
- Skills do not replace the persistence layer

### 7. Primary Boundaries

The current architecture enforces several boundaries:

- only one product surface remains: security log analysis
- shared frontend changes must be validated across all five pages
- cross-project samples must not pollute current runtime history
- large-file handling must validate aggregation and rendered outputs, not just parser success

### 8. Current Reality

The architecture is currently closer to:

- a local analysis workbench
- a training-driven capability platform
- a hybrid of deterministic logic and controlled model augmentation

It is not currently a:

- cloud-native distributed system
- multi-tenant SaaS platform
- full auto-remediation orchestration center
