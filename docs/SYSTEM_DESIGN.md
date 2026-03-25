# 系统设计说明
<!-- security-log-analysis mainline -->

## 1. 文档目的

本文档定义 MegaETH AI Security Platform 当前主线的系统设计边界、运行方式、核心模块职责与数据流转方式。

本文档回答以下问题：

- 系统解决什么问题
- 当前范围与非范围是什么
- 请求如何在系统中流动
- 哪些模块承担哪些职责
- 数据如何落库与保留

## 2. 系统范围

### 2.1 当前范围

平台当前服务于分析师可见、可复核的安全日志分析工作流，覆盖：

- 文件与文本输入
- 外部安全平台导入
- 安全材料归一化
- Planner 分类与 Skill 路由
- Finding 生成与风险判断
- 中文安全报告生成
- 历史记录、调查会话与学习反馈保留

### 2.2 非当前范围

以下能力明确不在当前主线范围内：

- 自动处置与自动封禁
- 分布式任务调度
- 多租户隔离
- 大规模企业编排
- 独立第二产品域

## 3. 总体架构

系统分为三层：

- 输入与接入层
- 分析与报告层
- 留存与学习层

```text
输入 / 平台导入
-> 解析与归一化
-> Planner 分类
-> Skill 执行
-> 风险判断
-> 报告生成
-> 历史 / 调查 / 学习沉淀
```

## 4. 核心模块

### 4.1 API 层

关键文件：

- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/main.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/main.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/api/routes.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/api/routes.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/api/core_routes.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/api/core_routes.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/api/integration_routes.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/api/integration_routes.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/api/ui_routes.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/api/ui_routes.py)

职责：

- 暴露输入、历史、调查、学习、连接等接口
- 承载平台接入入口
- 输出静态前端页面

### 4.2 分析层

关键文件：

- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/normalizer.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/normalizer.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/planner.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/planner.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/skills/implementations.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/skills/implementations.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/risk_engine.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/risk_engine.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/report_engine.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/report_engine.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/pipeline.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/pipeline.py)

职责：

- 将输入材料转为统一事件模型
- 根据 `source_type` 与 `event_type` 进行分类和 Skill 路由
- 执行 Skill，生成 Findings
- 进行风险判断与报告合成

### 4.3 留存与学习层

关键文件：

- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/history.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/history.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/core/memory_service.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/core/memory_service.py)
- [/Users/lei/Documents/New project/megaeth-ai-security-rebuild/app/utils/store.py](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/app/utils/store.py)

职责：

- 保存近期事件、报告和调查记录
- 维护轻量历史窗口
- 保存学习反馈与长期规则
- 将大体积调查快照与在线状态分离

## 5. 主要对象模型

当前主线围绕以下对象运作：

- `RawEvent`
- `NormalizedEvent`
- `Finding`
- `SecurityReport`
- `Investigation`
- `LearningRule`
- `LearningFeedback`

当前阶段采用 JSON 文件存储，而不是数据库。

## 6. 接入模型

当前可见接入面包括：

- 文件上传与文本输入
- Bitdefender 导入
- Whitebox AppSec 输入骨架

这些接入面是数据来源或补充分析来源，不是独立产品域。

## 7. UI 边界

前端固定为五个页面：

- 概览
- 输入
- 技能
- 连接
- 学习

共享前端逻辑一旦变更，必须验证这五个页面全部可用。

## 8. 存储与运行策略

### 8.1 运行端口

- 运行端口：`8011`
- 健康检查：`/health`
- 主要烟测接口：`/pipeline/overview`

### 8.2 存储策略

- `data/*.json`：近期在线状态
- `data/archives/`：历史快照与归档
- 保持轻量在线数据，避免大文本和大对象直接常驻前端

## 9. 设计约束

- 系统必须是可审阅、可复核的分析平台
- 训练案例是设计资产的一部分，不是附属材料
- 学习规则不能静默覆盖 case 明确要求
- 单页或单模块任务不得顺手重构其他模块
