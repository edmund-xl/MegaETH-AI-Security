# 运行手册 / Runbook

## 中文版

### 1. 最小可运行路径（推荐）

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PORT=8010 ./start.sh
```

- 默认服务监听 `127.0.0.1:8010`
- 停止命令：`PORT=8010 ./stop.sh`
- 服务日志：`.run-8010.log`

如果这台电脑会经常重启，我建议直接装 `launchd`，别再靠手动记忆：

```bash
./scripts/install_launch_agent.sh
```

这一步会把服务注册成“登录后自动启动”。如果你想撤掉：

```bash
./scripts/uninstall_launch_agent.sh
```

### 2. 手动启动（开发调试）

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
source .venv/bin/activate
export PORT=8010
export BITDEFENDER_API_KEY=你的key
export GEMINI_API_KEY=你的服务端key
python run_server.py
```

如果你要打开 JumpServer 的 `MCP -> Agent -> Skill` 试点，还可以再补一行：

```bash
export GEMINI_MODEL_JUMPSERVER=gemini-2.5-flash
```

这一步是干嘛的：
- `GEMINI_API_KEY` 用于让 `megaeth.agent.core` 在服务端调用 Gemini
- `GEMINI_MODEL_JUMPSERVER` 用于单独指定 JumpServer 这条链的模型
- 如果不配，JumpServer 还是能跑，只是继续走规则版结论

### 3. 常用检查（按顺序）

- 健康检查：`curl -sSf http://127.0.0.1:8010/health`
- 流程预览：`curl -sSf http://127.0.0.1:8010/pipeline/overview`
- 能力清单：`curl -sSf http://127.0.0.1:8010/skills`
- 最近报告：`curl -sSf http://127.0.0.1:8010/reports/recent`
- 最近历史：`curl -sSf http://127.0.0.1:8010/history`

### 4. 快速功能验证（最少成本）

```bash
cat >/tmp/runbook_sample.csv <<'EOF'
发现名称,风险评分,平台,合规标准
未安装 auditd,99,Unix,PCI DSS v4.0.1
未开启日志审计,90,Unix,CIS v8.0
EOF
```

```bash
curl -sS -F "files=@/tmp/runbook_sample.csv" http://127.0.0.1:8010/ingest/files
```

期望输出：
- HTTP 200
- `results[0].normalized_event.source_type` 有值
- `results[0].report.findings` 非空
- `results[0].report.overall_risk_score` 不为空

### 5. Memory 纠偏示例

在 `/tmp/xxx` 分别保存两次相似输入后，可通过 `POST /memory/learn/classification` 强制更新预期分类：
- `expected_source_type`
- `expected_event_type`
- `preferred_skills`

如果你在同类样本上反复出现误判，优先补充 `notes` 后提交记忆反馈，而不是直接改规则文件。

### 6. 常见故障与应对

- 端口占用：先 `./stop.sh`，再确认 `lsof -i :8010` 没有残留进程。
- 虚拟环境不存在：确认 `pip` 命令是 `.venv/bin/pip`。
- 依赖安装失败：先 `pip install --upgrade pip`，再重装。
- 文件上传失败：先尝试纯文本 csv；二进制 PDF/日志可能要求可解析文本。
- `curl` 返回 500：查看 `.run-8010.log`，重点看最新 20~40 行报错。

### 7. 兼容旧控制面（可选）

如果你在做历史回归，可在 `backend/` + `frontend/` 目录内执行旧的研究控制面脚本，但不要把它当作本项目当前主发布路径。

## English

### 1. Minimal runnable path

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PORT=8010 ./start.sh
```

- Service URL: `127.0.0.1:8010`
- Stop: `PORT=8010 ./stop.sh`
- Log: `.run-8010.log`

### 2. Manual start

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
source .venv/bin/activate
export PORT=8010
export GEMINI_API_KEY=your_server_key
python run_server.py
```

Optional for the JumpServer pilot:

```bash
export GEMINI_MODEL_JUMPSERVER=gemini-2.5-flash
```

This does three things:
- `GEMINI_API_KEY` enables server-side Gemini calls in `megaeth.agent.core`
- `GEMINI_MODEL_JUMPSERVER` lets you set a model just for JumpServer
- without them, JumpServer still works, but stays on the rule-based narrative path

### 3. Health checks

- `curl -sSf http://127.0.0.1:8010/health`
- `curl -sSf http://127.0.0.1:8010/pipeline/overview`
- `curl -sSf http://127.0.0.1:8010/skills`
- `curl -sSf http://127.0.0.1:8010/reports/recent`

### 4. Minimal functional check

- Create a sample CSV file and post to `/ingest/files`.
- Expect report output with non-empty findings and numeric risk score.

### 5. Troubleshooting

- If port is in use: stop current service, clear leftover process, restart.
- If dependency install fails: upgrade pip and retry in clean virtualenv.
- If uploads fail: start with plain text CSV first to isolate parser issues.
- If the API returns 500: use `.run-8010.log` as the first debug source.
