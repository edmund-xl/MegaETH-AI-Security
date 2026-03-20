# Release Process / 发布流程

## 中文版

这份文档用于约束“今天能上线吗”和“哪次要做本机归档”。

### 你先分两类处理

- 日常迭代：每天都可能有，主要同步 GitHub。
- 里程碑归档：关键变更节点，额外产出本机可迁移包和 manifest。

### 日常迭代（强制执行）

```bash
git status
git add .
git commit -m "..."
git push
```

`git status` 先确认只包含预期文件，`git add` 后看一次 `git status`，避免把日志或临时环境文件一起推。

提交前建议至少跑一次：

```bash
./.venv/bin/pytest -q
```

这个仓库的 Python 测试依赖当前 `.venv`，`./.venv` 未准备好时先执行 `./start.sh` 一次让环境创建。

### 里程碑归档（建议执行）

满足以下任一情况时，建议顺带执行：

- 完整接入新外部平台或 MCP 能力
- 新增/重写关键 Skill 或模块
- Memory 与分类规则产生明显提升
- 报告质量、准确率或可解释性有阶段性跃升
- 你要把某个稳定状态迁移到新机器

运行：

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./scripts/release.sh
```

`./scripts/release.sh` 当前会做：

- `README.md`、`CHANGELOG.md`、`VERSION`、`docs/` 下核心文档、`scripts/backup.sh`、`start.sh`、`stop.sh` 是否存在
- `./.venv/bin/pytest -q`
- 执行 `./scripts/backup.sh`，生成 `.tar.gz`
- 生成 `~/Desktop/megaeth-ai-security-rebuild-archives/release-manifest-<timestamp>.md`
- 清理旧的 release manifest（保留最近两次）

### 本次更新必须回填哪些文档

1. 新页面 / 新视图 / 新 API：同步到 `docs/FEATURE_SNAPSHOT.md`、`docs/SYSTEM_DESIGN.md`
2. 新技能 / 新模块：同步 `docs/SKILL_LIBRARY.md`、`skill_specs/` 与 `docs/CASE_LIBRARY.md`（如适用）
3. 训练行为变化：同步 `docs/TRAINING_WORKFLOW.md`、`CHANGELOG.md`
4. 跨机器迁移或运行方式变化：同步 `docs/PORTABLE_TRANSFER.md`

### 训练案例的保留要求

围绕某个 `training_case` 做变更时，提交前确认：

- `README.md` 仍写清本次 case 边界
- `docs/FEATURE_SNAPSHOT.md` 仍保留当前能力状态
- `docs/TRAINING_WORKFLOW.md` 仍解释新规约
- `CHANGELOG.md` 仍记录关键修正

### 经验坑位（常见错误）

- `release.sh` 写死了 `./.venv/bin/pytest`，如果没在项目根创建对应虚拟环境会直接失败。
- `./scripts/release.sh` 里要求文件列表不全会提前退出，不要期待它“自动修复”。
- 归档目录可能很大，先确认 `ARCHIVE_DIR` 可写。
- 已有服务运行中也可以归档，但更推荐先停掉本机敏感演示服务再打包，避免抓到半更新状态。

### 快速自检清单

1. 代码、测试、文档三件套是否都更新？
2. 训练案例/skill 变更是否写进 `CHANGELOG.md`？
3. 本次运行端口、数据目录状态是否可复现？

## English Version

This document separates two release patterns:

- Day-to-day iteration: push to GitHub directly.
- Milestone archive: add a local backup + manifest for reproducibility.

### Day-to-Day

```bash
git status
git add .
git commit -m "..."
git push
```

Run at least:

```bash
./.venv/bin/pytest -q
```

### Milestone Archive

Run when any major capability changes, new external integrations, major skill/module updates, or when you need a clean machine-transfer snapshot.

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./scripts/release.sh
```

`release.sh` validates required docs, runs tests, runs `./scripts/backup.sh`, and writes a manifest to `~/Desktop/megaeth-ai-security-rebuild-archives`.

### What to update in docs

- New UI/API: `docs/FEATURE_SNAPSHOT.md`, `docs/SYSTEM_DESIGN.md`
- New skill/module: `docs/SKILL_LIBRARY.md`, `skill_specs/`
- Training changes: `docs/TRAINING_WORKFLOW.md`, `CHANGELOG.md`
- Transfer/runtime change: `docs/PORTABLE_TRANSFER.md`

### Common pitfalls

- `./.venv/bin/pytest` requires a working `.venv` in repo root.
- Missing required files in `release.sh` will fail fast.
- Keep archive path writable before running release.
