# 运行手册
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档说明如何启动、停止、检查、诊断和恢复当前系统。

### 2. 启动

标准启动方式：

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./start.sh
```

### 3. 停止

标准停止方式：

```bash
PORT=8011 ./stop.sh
```

### 4. 健康检查

标准检查包括：

- `/health`
- `/pipeline/overview`

建议检查方式：

```bash
curl http://127.0.0.1:8011/health
curl http://127.0.0.1:8011/pipeline/overview
```

### 5. 常见诊断

当前最常见的问题包括：

- 页面持续加载中
- 上传后分析异常
- 大文件计数不准
- 下载报告与页面不一致
- 服务掉线

### 6. 优先排查顺序

推荐按以下顺序排查：

1. 服务是否还活着
2. 健康接口是否正常
3. 页面是否吃到最新 JS/CSS
4. 后端接口是否正常返回
5. 样本是否被正确摄取与归一化

### 7. 运行原则

运行维护必须遵守：

- 共享层改动必须验证五个页面
- 不得使用其他项目样本污染当前运行历史
- 大文件问题必须核查行数、表头、聚合和导出
- 静态资源改动必须同步提升 JS/CSS 版本

## English

### 1. Purpose

This document explains how to start, stop, verify, diagnose, and recover the current system.

### 2. Start

Standard startup:

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./start.sh
```

### 3. Stop

Standard stop:

```bash
PORT=8011 ./stop.sh
```

### 4. Health Checks

Standard checks include:

- `/health`
- `/pipeline/overview`

Suggested commands:

```bash
curl http://127.0.0.1:8011/health
curl http://127.0.0.1:8011/pipeline/overview
```

### 5. Common Diagnostics

The most common issues currently include:

- endless page loading
- post-upload analysis failures
- large-file count drift
- page/export mismatch
- service drops

### 6. Recommended Debug Order

Recommended order:

1. confirm the service is alive
2. confirm health endpoints respond
3. confirm the page is using the latest JS/CSS
4. confirm backend endpoints return valid data
5. confirm the sample was ingested and normalized correctly

### 7. Operational Rules

Operational maintenance must preserve:

- all five pages regressed after shared-layer changes
- no cross-project sample contamination
- large-file issues checked at row/header/aggregation/export level
- JS and CSS cache-busting versions bumped together
