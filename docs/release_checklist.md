# 版本发布清单 / Release Checklist

## 中文版（按顺序执行）

- [ ] `cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'`
- [ ] `python3.13 -m venv .venv`（若尚未建环境）
- [ ] `source .venv/bin/activate`
- [ ] `pip install -r requirements.txt`
- [ ] 确认 `BITDEFENDER_API_KEY` 已加载（必要时放入 `.env.local` 并重启服务）
- [ ] `python -m pytest -q`
- [ ] `PORT=8010 ./start.sh`
- [ ] `curl -sSf http://127.0.0.1:8010/health`
- [ ] `curl -sSf http://127.0.0.1:8010/pipeline/overview`
- [ ] `curl -sSf http://127.0.0.1:8010/pipeline/overview | jq '.metrics.events_processed'`
- [ ] `curl -sSf http://127.0.0.1:8010/skills`
- [ ] `curl -sSf http://127.0.0.1:8010/skills/matrix`
- [ ] `curl -sSf http://127.0.0.1:8010/history`
- [ ] `curl -sSf http://127.0.0.1:8010/reports/recent`
- [ ] `printf "发现名称,风险评分,平台,合规标准\\n未安装 auditd,99,Unix,PCI DSS v4.0.1\\n" > /tmp/sample.csv`
- [ ] 上传一次最小样本文件并确认返回报告：`curl -s -F "files=@/tmp/sample.csv" http://127.0.0.1:8010/ingest/files`
- [ ] `curl -sSf http://127.0.0.1:8010/memory/rules`
- [ ] `curl -sSf http://127.0.0.1:8010/memory/feedback`
- [ ] `./stop.sh`

附注（常见坑）：
- `jq` 不可用时可省略 JSON 取字段步骤，只检查 HTTP 200。
- `/.run-8010.pid` 和 `/.run-8010.log` 由启动脚本生成，发布前建议保留 1 份关键段日志。

### 后备兼容路径（非主线）

- [ ] `cd '<your_legacy_workspace>'`（仅用于历史回归，如存在 `legacy` 兼容环境再执行）
- [ ] `make verify-phase1`
- [ ] 与当前主线对账：确保不把这些命令当主发布路径，仅用于比对。

## English

- [ ] `cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'`
- [ ] `python3.13 -m venv .venv` (if missing)
- [ ] `source .venv/bin/activate`
- [ ] `pip install -r requirements.txt`
- [ ] Set `BITDEFENDER_API_KEY` (prefer `.env.local`) if MCP imports are needed.
- [ ] `python -m pytest -q`
- [ ] `PORT=8010 ./start.sh`
- [ ] `curl -sSf http://127.0.0.1:8010/health`
- [ ] `curl -sSf http://127.0.0.1:8010/pipeline/overview`
- [ ] `curl -sSf http://127.0.0.1:8010/skills`
- [ ] `curl -sSf http://127.0.0.1:8010/skills/matrix`
- [ ] `curl -sSf http://127.0.0.1:8010/history`
- [ ] Create a tiny sample file (e.g. `/tmp/sample.csv`) with at least one row.
- [ ] Upload one small sample file and check report output via `/ingest/files`.
- [ ] `curl -sSf http://127.0.0.1:8010/ingest/files -F "files=@/tmp/sample.csv"`
- [ ] `curl -sSf http://127.0.0.1:8010/memory/rules`
- [ ] `curl -sSf http://127.0.0.1:8010/memory/feedback`
- [ ] `./stop.sh`

Legacy note: if you must run the historical compatibility stack in `backend/`, only do that after this checklist has passed and document that it is a separate validation path.
