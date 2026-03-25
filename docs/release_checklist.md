# 发布检查清单
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档提供发布前的最小但可执行检查项。

### 2. 代码与运行

发布前确认：

- 工作树状态清楚
- 关键改动已提交
- `8011` 服务可启动
- `/health` 正常
- `/pipeline/overview` 正常

### 3. 页面与体验

发布前确认以下五页可正常使用：

- 概览
- 输入
- 技能
- 连接
- 学习

### 4. 回归验证

发布前至少完成：

- `node --check app/static/app.js`
- `pytest tests/test_api.py -q`
- 关键样本烟测

### 5. 文档与同步

发布前确认：

- 受影响文档已同步更新
- 训练案例与 Skill 说明已同步
- GitHub 分支已推送
- 需要时已同步 `main`

## English

### 1. Purpose

This document provides the minimum executable pre-release checklist.

### 2. Code and Runtime

Before release, confirm:

- the worktree is understood
- key changes are committed
- the `8011` service starts correctly
- `/health` is healthy
- `/pipeline/overview` is healthy

### 3. UI Checks

Before release, confirm these five pages are usable:

- Overview
- Intake
- Skills
- Integrations
- Learning

### 4. Regression

Before release, complete at least:

- `node --check app/static/app.js`
- `pytest tests/test_api.py -q`
- a smoke run on representative samples

### 5. Documentation and Sync

Before release, confirm:

- affected docs are updated
- training cases and Skill specs are synchronized
- GitHub branches are pushed
- `main` is synchronized when appropriate
