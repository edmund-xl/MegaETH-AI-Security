# 运行手册
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

说明本地运行、重启、健康检查、常见诊断和恢复方式。

### 2. 启动与停止

通过 start.sh 和 stop.sh 管理 8011 端口服务。

### 3. 健康检查

标准检查包括 /health 与 /pipeline/overview。

### 4. 常见诊断

重点关注页面持续加载、上传后分析异常和服务掉线。

### 5. 运行原则

共享层改动必须验证全部五个页面，并避免跨项目材料污染运行态。


## English

### 1. Purpose

Describe local runtime, restart, health checks, common diagnostics, and recovery steps.

### 2. Start and Stop

Use start.sh and stop.sh to manage the service on port 8011.

### 3. Health Checks

Standard checks include /health and /pipeline/overview.

### 4. Common Diagnostics

Focus on endless loading, post-upload analysis issues, and service drops.

### 5. Operational Rule

Shared-layer changes must be validated across all five pages and must not contaminate runtime state with data from other projects.
