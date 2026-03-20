# 项目状态 / Status

## 中文版

### 当前目标（Phase 1）

MegaETH AI Security 当前以“可运行、安全分析工作台”为目标：接收材料、归一化、规划 Skill、生成风险报告、支持反馈学习与 MCP 补充输入，不做生产自动化下发。

### 已完成

- `app/` 主服务可启动：`start.sh`、`stop.sh`、`run_server.py` 已形成可复用路径。
- 物料接入链路完成：`/ingest/files`、`/ingest/raw`、`/normalize/preview`、`/planner/preview`。
- 核心分析链完成：`normalizer -> planner -> skills -> risk -> report`，并与 `memory` 和 `history` 连接。
- Skill 发现能力：`/skills` 与 `/skills/matrix` 可验证。
- 历史与调查会话：`/reports/recent`、`/events/recent`、`/events/raw`、`/investigations/recent`、`/history`。
- 记忆学习闭环：`/memory/feedback`、`/memory/rules`、`/memory/learn/classification`。
- 平台接入：Bitdefender 与 Whitebox AppSec MCP 入口稳定可调用。
- 双语界面与页面状态联动保持可用。
- 回归测试：`tests/test_api.py` 覆盖健康检查、分类记忆、材料解析与报告生成。

### 进行中

- 继续扩展输入解析覆盖面（更多安全报告格式）。
- 改进报表可解释性（执行决策链字段可读性）。
- 明确 `backend/` 与 `frontend/` 的历史状态与剥离策略，避免与主服务混淆。

### 当前运行模式

- 人工发起输入 -> 自动生成分析报告 -> 人工确认 -> 记录学习反馈。
- 未启用生产自动执行与多租户隔离。

### 主命令

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
PORT=8010 ./start.sh
curl -sSf http://127.0.0.1:8010/health
curl -sSf http://127.0.0.1:8010/pipeline/overview
./stop.sh
```

## English

### Current Scope (Phase 1)

MegaETH AI Security is currently focused on a runnable security analysis workspace: ingest, normalize, skill planning, risk-report generation, and memory feedback. It is not enabled for production auto-execution.

### Completed

- Runnable app path with `start.sh`, `stop.sh`, and `run_server.py`.
- Ingestion and analysis endpoints are implemented for file/raw input, preview, planning, and report generation.
- Analysis core chain is connected with memory and history persistence.
- Skills surface (`/skills`, `/skills/matrix`) and history APIs are available.
- MCP import paths are in place for Bitdefender and Whitebox AppSec.
- Bilingual interface remains usable.
- Regression coverage exists in `tests/test_api.py`.

### In Progress

- More parser coverage for additional security materials.
- Better explanatory structure for risk reports.
- Clearer separation of legacy `backend/` + `frontend/` and primary app path.

### Current Mode

- User-driven intake with analyst-visible outputs and feedback-based memory updates.
- No production automation path is enabled.

### Main Commands

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
PORT=8010 ./start.sh
curl -sSf http://127.0.0.1:8010/health
curl -sSf http://127.0.0.1:8010/pipeline/overview
./stop.sh
```
