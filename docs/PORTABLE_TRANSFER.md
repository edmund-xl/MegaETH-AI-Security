# Portable Transfer / 跨机器迁移

## 中文版

这份文档用于把当前环境按“可落地、可继续训练”方式迁移到另一台机器。

### 迁移路径

- 只迁移代码与文档：适合演示或备份，不带历史学习状态。
- 代码 + data：适合继续训练，保持已有经验。

官方备份包位置：
- `~/Desktop/megaeth-ai-security-rebuild-archives/`

### 1）只迁移代码和文档（最小包）

在源机器执行：

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./scripts/backup.sh
```

`./scripts/backup.sh` 当前会排除 `.venv`、`__pycache__`、`.pytest_cache`、`dist`，输出 `megaeth-ai-security-rebuild-backup-<timestamp>.tar.gz`。

目标机器解包：

```bash
tar -xzf ~/Desktop/megaeth-ai-security-rebuild-archives/megaeth-ai-security-rebuild-backup-*.tar.gz
cd megaeth-ai-security-rebuild
./start.sh
```

### 2）带上学习状态继续训练（推荐）

先做上面同样的代码备份，再单独同步 `data/` 目录：

```bash
tar -xzf megaeth-ai-security-rebuild-backup-*.tar.gz
cd megaeth-ai-security-rebuild
cp /source/path/data/*.json ./data/
./start.sh
```

至少需要带出的文件：

- `data/events.json`
- `data/raw_events.json`
- `data/reports.json`
- `data/investigations.json`
- `data/memory_rules.json`
- `data/memory_feedback.json`

### 迁移后第一件事

```bash
open 'http://127.0.0.1:8010'
```

再执行一次本地测试：

```bash
./.venv/bin/pytest -q
```

这样能确认新机器依赖、模型加载和配置链路没有丢。

### 常见坑

- 没带 `data/` 会丢失 Memory，会导致后续分析行为变“新手模式”。
- 只拷贝 `.run-*.pid` 这类运行时文件没意义，反而会干扰启动。
- `start.sh` 的端口默认 8010，目标机器已有端口占用要直接改成 `PORT=8011 ./start.sh`。
- 远端 `python`/`screen` 版本差异会导致启动行为变化，先跑完整脚本再上线。
- 备份路径不写权限时备份脚本会静默失败，先确认 `~/Desktop` 可写。

### 迁移验收

- 服务能启动且页面可访问
- 主要 API/界面可用（至少打开 Overview 与 Intake）
- `data` 文件成功覆盖（若走训练迁移）

## English Version

This is the practical migration flow for moving the project to another machine.

### Two migration modes

- Code + docs only: for demo or backup.
- Code + data: for continuing training with accumulated memory.

### Code and docs only

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./scripts/backup.sh
```

Extract on the target machine:

```bash
tar -xzf ~/Desktop/megaeth-ai-security-rebuild-archives/megaeth-ai-security-rebuild-backup-*.tar.gz
cd megaeth-ai-security-rebuild
./start.sh
```

### Keep training state

Transfer `data/*.json` separately after unpacking:

```bash
cp /source/path/data/*.json ./data/
cd megaeth-ai-security-rebuild
./start.sh
```

Required files:
- `data/events.json`
- `data/raw_events.json`
- `data/reports.json`
- `data/investigations.json`
- `data/memory_rules.json`
- `data/memory_feedback.json`

### Checklist after transfer

- app starts on `127.0.0.1:8010` (or custom `PORT`)
- open UI and verify core pages
- run `./.venv/bin/pytest -q` once
