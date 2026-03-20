# Rebuild Guide / 重建指南

## 中文版

### 目标

这份文档用于在目录损坏、文件丢失、需要迁移时，让 AI 或新协作者重建出高度相似的系统。

### 重建后必须具备的特征

- FastAPI 后端 + 静态前端工作台
- 五个主页面：Overview / Intake / Skills / Integrations / Memory
- 单入口 Intake
- 文件上传与原始输入分析
- Memory 学习与纠偏机制
- 本地 JSON 存储
- 中英文切换
- 页面刷新保留当前页面

### 关键产品要求

- Overview：平台快照、近期报告、调查会话、历史摘要
- Intake：统一输入、技能分配预览、归一化结果、Security Report、Uploaded File Runs
- Skills：像能力目录，不是 JSON dump
- Integrations：作为外部安全平台接入中心，至少要包含 Bitdefender
- Memory：展示规则与反馈，并强调系统会复用这些经验

### 后端必须包含的模块

- `EventNormalizer`
- `Planner`
- `SecurityPipeline`
- `RiskEngine`
- `ReportEngine`
- `HistoryService`
- `MemoryService`
- `file_ingest`
- `store`

### 必须保留的 API

- `GET /health`
- `GET /skills`
- `GET /skills/matrix`
- `GET /pipeline/overview`
- `GET /reports/recent`
- `GET /events/recent`
- `GET /events/raw`
- `GET /investigations/recent`
- `GET /history`
- `GET /memory/rules`
- `GET /memory/feedback`
- `POST /memory/learn/classification`
- `POST /normalize/preview`
- `POST /planner/preview`
- `POST /event`
- `POST /ingest/raw`
- `POST /ingest/files`
- Bitdefender 相关接口

### Memory 行为要求

- 每次成功分析都可以自动 observation
- 用户可以确认“这次分类正确”
- 用户可以纠正“这次分类不对”
- 纠正时：
  - source type 用下拉
  - event type 用下拉
  - skills 可多选
  - 不需要手写规则名
- 手工规则优先
- 相似规则自动合并

### UI 行为要求

- 中英文切换
- 刷新浏览器保留当前页面
- Refresh 按钮有状态反馈
- 输入框内容可本地保留
- 不要在品牌区写“重建版”“开发进度”等字样

### 最低恢复标准

- 可以启动
- 可以上传文件
- 可以生成 normalized event
- 可以生成 planner preview
- 可以输出 Security Report
- 可以写入 history
- 可以写入 memory rules / feedback
- 可以在前端直接学习和纠偏

---

## English Version

### Goal

This document is used to let an AI or a new collaborator rebuild a highly similar system when the directory is damaged, files are lost, or migration is required.

### Required Characteristics

- FastAPI backend + static frontend workbench
- Five main pages: Overview / Intake / Skills / Integrations / Memory
- Unified Intake entry
- File-upload and raw-input analysis
- Memory-based learning and correction
- Local JSON persistence
- Chinese / English switching
- Preserve current page on refresh

### Key Product Requirements

- Overview: platform snapshot, recent reports, investigation sessions, history summary
- Intake: unified input, skill planning preview, normalization result, Security Report, Uploaded File Runs
- Skills: capability directory rather than JSON dump
- Integrations: external security platform hub with Bitdefender at minimum
- Memory: rules and feedback, with emphasis on reuse of learned experience

### Required Backend Modules

- `EventNormalizer`
- `Planner`
- `SecurityPipeline`
- `RiskEngine`
- `ReportEngine`
- `HistoryService`
- `MemoryService`
- `file_ingest`
- `store`

### Required APIs

- core health / skills / overview / history / memory routes
- analysis entry routes
- Bitdefender integration routes

### Required Memory Behavior

- Automatic observation after successful analysis
- Manual confirmation for correct classification
- Manual correction for wrong classification
- Dropdown source type
- Dropdown event type
- Multi-select skills
- No handwritten rule names
- Manual rules override automatic ones
- Similar rules merge automatically

### Required UI Behavior

- Chinese / English switching
- Preserve current page on refresh
- Refresh buttons show status
- Inputs can be locally preserved
- No “rebuild version” or “development progress” branding language

### Minimum Recovery Standard

- The app can start
- Files can be uploaded
- Normalized events can be generated
- Planner preview works
- Security Report works
- History can be persisted
- Memory rules and feedback can be persisted
- The frontend can directly learn and correct
