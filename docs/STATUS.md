# 当前状态
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档用于快速说明当前主线状态、运行基线和已确认能力。

### 2. 当前主线

仓库当前只保留：

- 安全日志分析

### 3. 运行基线

当前运行基线如下：

- 默认端口：`8011`
- 主要健康接口：`/health`
- 主要烟测接口：`/pipeline/overview`
- 测试入口：`tests/test_api.py`

### 4. 当前已确认能力

当前已确认能力包括：

- 五页面前端主线
- Host baseline
- JumpServer 单文件与多源审计
- Bitdefender 输入分析
- Whitebox AppSec 三段式分析
- EASM 单样本与多样本综合分析
- 学习反馈链

### 5. 当前运行方式

当前系统以本地运行和本地持久化为主，适合：

- 样本驱动训练
- 页面复核
- 报告导出
- 交互式校准

### 6. 当前维护原则

当前维护必须遵守：

- 不新增第二产品域
- 改共享层必须回归五个页面
- 能力变化必须同步更新文档
- GitHub 主线和本地主线必须保持一致

## English

### 1. Purpose

This document gives a quick view of the current mainline state, runtime baseline, and confirmed capabilities.

### 2. Active Mainline

The repository currently preserves only:

- security log analysis

### 3. Runtime Baseline

The current runtime baseline is:

- default port: `8011`
- primary health endpoint: `/health`
- primary smoke endpoint: `/pipeline/overview`
- regression entry: `tests/test_api.py`

### 4. Confirmed Capabilities

Confirmed capabilities currently include:

- the five-page frontend workbench
- Host baseline
- JumpServer single-source and multi-source audit analysis
- Bitdefender input analysis
- Whitebox AppSec three-stage analysis
- EASM single-source and composite analysis
- the learning-feedback pipeline

### 5. Current Operating Style

The system is currently local-first and file-backed, suitable for:

- sample-driven training
- UI review
- report export
- interactive calibration

### 6. Maintenance Rules

Current maintenance must preserve:

- no second product surface
- all five pages regressed after shared-layer changes
- docs updated together with capability changes
- local and GitHub mainline kept aligned
