# 重建指南
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档说明如何从仓库重新搭建当前项目，并恢复到可工作的状态。

### 2. 标准重建步骤

推荐步骤：

1. clone 仓库
2. 创建虚拟环境
3. 安装依赖
4. 启动服务
5. 做健康检查
6. 跑回归测试

### 3. 必做验证

重建后至少验证：

- `/health`
- `/pipeline/overview`
- `pytest tests/test_api.py -q`

### 4. 恢复原则

如果还需要恢复旧状态，建议顺序为：

1. 先恢复代码
2. 再恢复依赖
3. 再恢复数据
4. 最后恢复个人上下文

## English

### 1. Purpose

This document explains how to rebuild the project from the repository and recover a working state.

### 2. Standard Rebuild Steps

Recommended steps:

1. clone the repository
2. create a virtual environment
3. install dependencies
4. start the service
5. run health checks
6. run regression tests

### 3. Required Validation

After rebuild, verify at least:

- `/health`
- `/pipeline/overview`
- `pytest tests/test_api.py -q`

### 4. Recovery Rule

If old state must also be restored, use this order:

1. restore code first
2. then dependencies
3. then data
4. finally personal context
