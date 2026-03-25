# 重建指南
<!-- security-log-analysis mainline -->

## 1. 目的

本文档说明当项目目录损坏、环境丢失或需要在新目录中重建时，如何恢复到可运行状态。

## 2. 重建步骤

```bash
cd '/Users/lei/Documents/New project'
git clone https://github.com/edmund-xl/MegaETH-AI-Security.git megaeth-ai-security-rebuild
cd megaeth-ai-security-rebuild
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./start.sh
```

## 3. 必做验证

```bash
curl -sSf http://127.0.0.1:8011/health
curl -sSf http://127.0.0.1:8011/pipeline/overview
./.venv/bin/python -m pytest tests/test_api.py -q
```

## 4. 可选恢复项

如果需要恢复历史运行态，可在确认代码无误后再拷回：

- `data/`
- `.env.local`

## 5. 原则

- 先恢复代码与测试通过
- 再恢复历史数据
- 不要在代码未校验时直接恢复旧运行态
