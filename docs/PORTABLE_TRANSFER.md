# 跨设备迁移说明
<!-- security-log-analysis mainline -->

## 1. 目的

本文档说明如何在另一台电脑上继续使用当前项目，并尽量保留上下文和运行状态。

## 2. 最小迁移内容

若只需要迁移代码：

- GitHub 仓库代码
- `.env.local` 等本地配置

若还需要迁移当前工作状态，建议额外迁移：

- `data/`
- 本地学习与运行相关文件

## 3. 标准迁移步骤

```bash
git clone https://github.com/edmund-xl/MegaETH-AI-Security.git
cd MegaETH-AI-Security
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./start.sh
```

## 4. 新机器启动后应做的事

- 先阅读 `docs/HANDOFF.md`
- 再阅读 `README.md`
- 检查 `8011` 是否正常启动
- 用一组真实安全日志样本做一次烟测

## 5. 注意事项

- GitHub 中保存的是代码与文档，不自动包含本机运行数据
- 如果希望迁移历史记录，需要额外迁移 `data/`
- 若需要跨机器保持工作上下文，新的 Codex 会话应先读 handoff 文档
