# MegaETH AI Security 架构说明 / Architecture Notes

## 中文版

这份说明以当前仓库主运行路径为准：`app/` 里的安全分析服务与同目录静态前端。`backend/` 与旧的 `frontend/` 目前仍保留为历史/兼容实现，不作为当前最小可运行路径的主线。

## 系统形态

- `app/main.py`：FastAPI 入口与静态入口。
- `app/core/`：`normalize -> planner -> skills -> risk -> report` 的主链。
- `app/skills/`：安全能力库（Skill）。
- `app/core/memory_service.py`/`app/utils`：分类记忆与持久化。
- `app/integrations/`：Bitdefender、白盒应用安全等 MCP 接入。
- `app/static/`：当前可直接使用的前端页面。
- `configs/`：本地可调参数与实验配置。
- `data/`：报告、输入样例、测试材料。
- `tests/`：核心接口与流水线回归。
- `docs/`：产品、方案、训练与发布文档。

## 一次分析循环

- 1) 原始输入进入 `memory` 回放规则（有历史经验先补齐归一化线索）。
- 2) `normalizer` 将输入转为 `NormalizedEvent`。
- 3) `planner` 依据素材类型/来源/上下文输出待执行 `skills`。
- 4) `skills` 产出 `findings` 并透过 `risk_engine` 计算风险分级。
- 5) `report_engine` 生成统一结构的 `SecurityReport`。
- 6) `history` 记录事件、报告、调查会话；`memory` 同步写入学习反馈。

对外看板建议按这个顺序展示：`/health` -> `/pipeline/overview` -> `/skills` -> `/ingest/files` -> `/reports/recent`。

## 可见系统边界

- 支持单文件、多文件、文本与二进制可解析材料的快速接入。
- 支持分类纠偏：用户可以通过 `memory` 反馈让下一次输入更贴近实际归类。
- 支持外部系统补充材料：Bitdefender、Whitebox 应用安全。
- 支持近期结果回看，不依赖数据库即可在单机运行。

## 当前阶段不做的事情

- 不做分布式执行器。
- 不做企业级权限、租户隔离与审计链。
- 不把扫描结果直接接入生产自动处置；默认是半自动、可审计的分析流程。

## English

This document describes the current runnable stack in this repository: the FastAPI service in `app/` and static UI in `app/static/`.

## System Shape

- `app/main.py`: FastAPI entry and static mount.
- `app/core/`: analysis chain (`normalizer -> planner -> skills -> risk_engine -> report_engine`).
- `app/skills/`: executable security capability units.
- `app/core/memory_service.py` and `app/utils`: memory learning and event parsing helpers.
- `app/integrations/`: MCP connectors.
- `app/static/`: built-in UI shell.

## Runtime Loop

1) New input enters memory enrichment.
2) Normalization into a typed event object.
3) Planner selects skills.
4) Skills generate findings and risk engine scores them.
5) Report engine builds a structured security report.
6) History stores outputs; memory stores learning feedback.

## Default Scope

The default target is a research-first, operator-visible workflow with correction loops, not a fully automated production executor.
