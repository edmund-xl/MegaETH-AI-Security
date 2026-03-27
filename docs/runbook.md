# 运行手册
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档说明如何启动、停止、检查、诊断和恢复当前系统。它面向：

- 日常本地运行
- 页面异常排查
- 样本训练时的运行确认
- 服务掉线后的恢复

### 2. 运行前检查

启动前建议确认：

- 已进入仓库根目录
- Python 虚拟环境可用
- 依赖已安装
- 默认端口 `8011` 未被其它服务占用

标准进入方式：

```bash
cd MegaETH-AI-Security
```

### 3. 启动

标准启动方式：

```bash
./start.sh
```

默认访问地址：

- [http://127.0.0.1:8011](http://127.0.0.1:8011)

### 4. 停止

标准停止方式：

```bash
PORT=8011 ./stop.sh
```

如果只需要确认服务是否已停，可以再次检查端口或健康接口。

### 5. 健康检查

日常最重要的检查包括：

- `/health`
- `/pipeline/overview`

建议命令：

```bash
curl http://127.0.0.1:8011/health
curl http://127.0.0.1:8011/pipeline/overview
```

典型预期：

- `/health` 返回 `{"status":"ok"}`
- `/pipeline/overview` 返回平台概览 JSON

### 6. 前端检查

如果页面异常，优先检查：

- 页面是否能打开
- 是否还在吃旧的 JS/CSS 资源
- 是否需要强刷浏览器缓存

推荐动作：

- 浏览器执行 `Cmd + Shift + R`
- 核对页面引用的 `styles.css?v=...` 和 `app.js?v=...`

### 7. 常见故障与排查顺序

当前最常见的问题包括：

- 页面持续加载中
- 上传后分析异常
- 大文件计数不准
- 下载报告与页面不一致
- 服务掉线

推荐排查顺序：

1. 服务是否还活着
2. 健康接口是否正常
3. 页面是否吃到最新 JS/CSS
4. 后端接口是否正常返回
5. 样本是否被正确摄取和归一化

### 8. 页面持续加载中的排查

遇到“全部加载中”时，优先检查：

- 前端初始化是否被空引用打断
- 某个共享 `app.js` 分支是否访问了不存在的 DOM
- 后端概览接口是否返回 `200`

最小检查集：

```bash
curl http://127.0.0.1:8011/health
curl http://127.0.0.1:8011/pipeline/overview
curl http://127.0.0.1:8011/reports/recent
curl http://127.0.0.1:8011/investigations/recent
```

### 9. 上传与分析异常排查

如果上传或分析结果不对，优先检查：

- 当前输入会话是否被旧输入污染
- 文件是否属于正确的事件域
- Planner 是否选中了正确 Skill
- 报告页面与导出结构是否一致

### 10. 大文件排查

遇到大文件时，不能只看“能不能打开”，还必须检查：

- 原始总行数
- 实际参与分析的行数
- 表头归一化是否正确
- 展示裁剪是否误伤分析链

这类问题在：

- JumpServer
- EASM
- 各类表格型输入

上都属于高风险项。

### 11. 报告不一致排查

如果页面和下载报告不一致，优先检查：

- 报告模板是否只改了页面链
- 旧对象是否还在走旧模板
- 综合报告和单文件报告是否使用了不同摘要源

### 12. 服务掉线与恢复

如果页面无法访问，优先确认：

1. 服务进程是否仍在运行
2. 健康接口是否可访问
3. 启停脚本是否仍指向 `8011`
4. 守护脚本是否正常工作

恢复顺序：

1. 重新启动服务
2. 检查 `/health`
3. 强刷浏览器
4. 再验证主要页面

### 13. 测试与验证

日常最重要的回归入口是：

```bash
PYTHONPATH=. .venv/bin/pytest tests/test_api.py -q
```

前端语法检查可用：

```bash
node --check app/static/app.js
```

### 14. 性能与运行稳定性检查

当前主线的长期运行稳定性主要依靠以下机制：

- 历史文件有硬上限与保留窗口
- `/history` 只返回摘要，不返回完整历史数组
- JSON 文件读取带进程内缓存
- Skill 训练案例索引带缓存
- 学习页只加载仍然可见的反馈面板

当系统出现“越跑越慢”的怀疑时，优先检查：

1. `data/` 是否被手工放大或破坏了保留规则
2. `/history` 是否仍返回摘要结构
3. `training_cases/` 是否被扩展到异常大的 README 扫描面
4. 前端是否重新引入了无意义请求

### 15. 运行维护规则

运行维护必须遵守：

- 共享层改动必须回归五个页面
- 不得使用其他项目样本污染当前运行历史
- 大文件问题必须核查行数、表头、聚合和导出
- 静态资源改动必须同步提升 JS/CSS 版本
- 能力变化必须同步更新文档

### 16. 结论

当前运行手册最重要的原则是：

- 先确认服务和接口
- 再确认前端资源
- 再确认样本和路由
- 最后确认报告、文档和 GitHub 是否同步

---

## English

### 1. Purpose

This document explains how to start, stop, verify, diagnose, and recover the current system. It is intended for:

- routine local operation
- UI issue triage
- runtime validation during sample training
- service recovery after drops

### 2. Pre-Run Checks

Before starting, confirm:

- you are in the repository root
- the Python virtual environment is available
- dependencies are installed
- port `8011` is not already occupied

### 3. Start

Standard startup:

```bash
./start.sh
```

Default URL:

- [http://127.0.0.1:8011](http://127.0.0.1:8011)

### 4. Stop

Standard stop:

```bash
PORT=8011 ./stop.sh
```

### 5. Health Checks

The two most important checks are:

- `/health`
- `/pipeline/overview`

Recommended commands:

```bash
curl http://127.0.0.1:8011/health
curl http://127.0.0.1:8011/pipeline/overview
```

### 6. Frontend Checks

If the UI behaves strangely, verify:

- the page opens
- the latest JS/CSS assets are being served
- the browser cache has been force-refreshed

### 7. Common Failures and Debug Order

The most common current problems include:

- endless page loading
- post-upload analysis failures
- large-file count drift
- page/export mismatch
- service drops

Recommended triage order:

1. confirm the service is alive
2. confirm health endpoints respond
3. confirm the page is using the latest JS/CSS
4. confirm backend endpoints return valid data
5. confirm the sample was ingested and normalized correctly

### 8. Diagnosing Endless Loading

When the UI stays in a loading state, check:

- whether frontend initialization was interrupted by a null DOM access
- whether shared `app.js` logic is touching removed nodes
- whether overview endpoints return `200`

### 9. Diagnosing Upload and Analysis Issues

When upload or analysis results look wrong, check:

- stale intake contamination
- correct event-domain selection
- correct Skill routing
- page/export structural consistency

### 10. Large-File Diagnostics

For large files, do not stop at “it opens.” Also validate:

- raw row count
- analyzed row count
- header normalization
- whether display truncation leaked into analysis logic

### 11. Report Mismatch Diagnostics

When page and exported reports diverge, check:

- whether only the page path was updated
- whether older stored objects still use older templates
- whether single-source and composite reports use different summary sources

### 12. Service Recovery

When the UI is unreachable, check:

1. whether the process is still running
2. whether `/health` responds
3. whether startup scripts still point to `8011`
4. whether the watchdog layer is functioning

### 13. Regression and Validation

Primary regression entry:

```bash
PYTHONPATH=. .venv/bin/pytest tests/test_api.py -q
```

Frontend syntax check:

```bash
node --check app/static/app.js
```

### 14. Performance and Runtime Stability Checks

Long-running stability in the current mainline depends on the following controls:

- history files have bounded retention and hard caps
- `/history` returns summary data instead of full history arrays
- JSON reads use an in-process cache
- the Skill training-case index is cached
- the learning view only loads the still-visible feedback panel

When the system appears slower over time, check these first:

1. whether `data/` has been manually enlarged or retention behavior has been broken
2. whether `/history` still returns summary-shaped data
3. whether `training_cases/` has grown into an unexpectedly large README scan surface
4. whether the frontend has reintroduced unnecessary requests

### 15. Operational Rules

Operational maintenance must preserve:

- five-page regression after shared-layer changes
- no cross-project sample contamination
- full row/header/aggregation/export validation for large files
- synchronized JS/CSS cache-busting
- documentation updates alongside capability changes

### 16. Summary

The most important operational rule is:

- verify service and APIs first
- then verify frontend assets
- then verify samples and routing
- finally verify reports, docs, and GitHub synchronization
