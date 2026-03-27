# 当前状态
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档用于快速说明当前主线状态、运行基线、已确认能力与当前优先事项。

### 2. 当前主线

仓库当前只保留：

- 安全日志分析

任何其它产品域都不在当前主线范围内。

### 3. 当前运行基线

当前本地运行基线如下：

- 默认端口：`8011`
- 健康检查：`/health`
- 主要概览接口：`/pipeline/overview`
- 历史摘要接口：`/history`
- 主要测试入口：`tests/test_api.py`

### 4. 当前已确认能力

当前已经确认可用的能力包括：

- 五页面前端工作台
- Host baseline 分析
- JumpServer 单文件分析
- JumpServer 多源综合审计
- Bitdefender 平台材料分析
- Whitebox AppSec 三段式分析
- EASM 单样本分析
- EASM 多样本综合分析
- 学习反馈链

### 5. 当前 EASM 运行状态

EASM 当前已经具备：

- 单文件 EASM 样本独立分析
- 多文件 EASM 样本综合分析
- `easm_asset_assessment` 综合结果生成
- 受控 Gemini 增强的综合结论与专业判断

### 6. 当前适用场景

当前系统适合：

- 样本驱动训练
- 页面复核
- 中文报告导出
- 交互式分析与校准

当前系统不适合：

- 自动处置
- 多租户管理
- 高并发远程任务调度

### 7. 当前优先事项

当前维护和开发优先顺序为：

1. 安全日志样本训练
2. Skill 路由和报告质量校准
3. 页面与导出一致性验证
4. 文档与 GitHub 同步

### 8. 当前维护原则

当前维护必须遵守：

- 不新增第二产品域
- 改共享前端逻辑必须回归五个页面
- 大文件输入必须验证全量聚合
- 能力变化必须同步更新文档
- 本地主线与 GitHub 主线保持一致

### 9. 当前性能基线

当前性能基线已经明确包含：

- 历史数据有硬上限与保留窗口
- `/history` 返回摘要而非完整历史数组
- JSON 文件读取带进程内缓存
- Skill 训练案例索引带缓存
- 学习页不会再为已删除的规则面板发起请求

这意味着当前主线适合长期本地运行，但尚不等同于数据库级无限扩展架构。

### 10. 当前交接结论

如果今天开始接手项目，应默认理解：

- 这是一个安全日志分析工作台
- 当前最有价值的训练域是 JumpServer、Whitebox AppSec、EASM
- 所有能力改动都必须同时看：
  - 代码
  - 页面
  - 报告导出
  - 文档

---

## English

### 1. Purpose

This document provides a quick status view of the active mainline, runtime baseline, confirmed capabilities, and current priorities.

### 2. Active Mainline

The repository currently preserves only:

- security log analysis

No other product surface is part of the active mainline.

### 3. Runtime Baseline

The current local runtime baseline is:

- default port: `8011`
- health endpoint: `/health`
- overview endpoint: `/pipeline/overview`
- history summary endpoint: `/history`
- regression entry: `tests/test_api.py`

### 4. Confirmed Capabilities

Confirmed capabilities currently include:

- the five-page frontend workbench
- Host baseline analysis
- JumpServer single-file analysis
- JumpServer multi-source composite auditing
- Bitdefender material analysis
- Whitebox AppSec three-stage analysis
- EASM single-source analysis
- EASM composite multi-file analysis
- the learning-feedback pipeline

### 5. Current EASM Status

EASM currently supports:

- standalone single-file analysis
- composite multi-file analysis
- generation of `easm_asset_assessment`
- controlled Gemini enhancement for composite judgment sections

### 6. Intended Usage

The current system is suitable for:

- sample-driven training
- UI review
- Chinese report export
- interactive analysis and calibration

It is not suitable for:

- auto-remediation
- multi-tenant operation
- high-concurrency remote task orchestration

### 7. Current Priorities

Current maintenance and development priorities are:

1. security-log sample training
2. Skill routing and report-quality calibration
3. page/export consistency validation
4. documentation and GitHub synchronization

### 8. Maintenance Rules

Current maintenance must preserve:

- no second product surface
- five-page regression after shared frontend changes
- full-data validation for large-file inputs
- document updates alongside capability changes
- alignment between local mainline and GitHub mainline

### 9. Performance Baseline

The current performance baseline explicitly includes:

- bounded retention and hard caps for history data
- `/history` returns summary data instead of full history arrays
- JSON file reads use an in-process cache
- the Skill training-case index is cached
- the learning view no longer requests data for the removed rules panel

This means the current mainline is suitable for sustained local use, but it is not yet a database-backed architecture designed for unbounded growth.

### 10. Status Summary

Anyone taking over the project today should assume:

- this is a security log analysis workbench
- JumpServer, Whitebox AppSec, and EASM are the most valuable training domains
- every capability change must be verified across:
  - code
  - UI
  - report export
  - documentation
