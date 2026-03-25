# 架构说明
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档提供系统结构视图，帮助开发、测试和交接快速理解当前主线。

### 2. 系统上下文

当前系统将安全材料和平台导入统一送入输入解析、归一化、Planner、Skill、风险判断和报告链。

### 3. 前后端关系

前端是单一静态工作台，后端由 FastAPI、核心分析链和本地持久化组成。

### 4. 运行关键路径

用户上传样本或平台导入后，系统按统一链路生成 Findings、报告和学习反馈。

### 5. 运行边界

当前只保留安全日志分析一个产品域，修改共享前端逻辑时必须验证五个页面。


## English

### 1. Purpose

This document provides a structural view of the system for development, testing, and handoff.

### 2. System Context

The current system routes uploaded materials and platform imports through intake parsing, normalization, planning, Skills, risk judgment, and reporting.

### 3. Frontend and Backend

The frontend is a single static workbench. The backend consists of FastAPI routes, the core analysis pipeline, and local persistence.

### 4. Runtime Path

After local upload or platform import, the system follows a single pipeline to produce Findings, reports, and learning feedback.

### 5. Boundary

Only the security-log-analysis product surface remains. Any shared frontend change must be validated across all five pages.
