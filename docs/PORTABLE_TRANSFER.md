# 跨设备迁移说明
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档说明如何把当前项目迁移到另一台电脑，并尽量保留代码、配置和上下文连续性。

### 2. 最小迁移集合

最小迁移集合包括：

- GitHub 仓库代码
- 本地环境配置

如果希望延续运行历史，还需要迁移：

- `data/`

如果希望延续项目上下文，还应优先阅读：

- `docs/HANDOFF.md`

### 3. 标准迁移步骤

推荐步骤如下：

1. 在新机器 clone 仓库
2. 创建虚拟环境
3. 安装依赖
4. 配置本地环境变量
5. 启动服务
6. 读取 handoff 文档

### 4. 注意事项

- 仅迁代码不等于迁运行历史
- 不同机器上的浏览器缓存与本地状态不会自动同步
- 新机器上的 Codex 应先读 handoff 再继续工作

## English

### 1. Purpose

This document explains how to move the current project to another machine while preserving code, configuration, and enough context continuity.

### 2. Minimum Transfer Set

The minimum transfer set includes:

- the GitHub repository code
- local environment configuration

If you need runtime continuity, also move:

- `data/`

If you need project-context continuity, read:

- `docs/HANDOFF.md`

### 3. Standard Migration Steps

Recommended steps:

1. clone the repository on the new machine
2. create a virtual environment
3. install dependencies
4. configure local environment variables
5. start the service
6. read the handoff document

### 4. Notes

- moving code does not automatically move runtime history
- browser cache and local UI state do not transfer automatically
- a new Codex session should read the handoff before continuing work
