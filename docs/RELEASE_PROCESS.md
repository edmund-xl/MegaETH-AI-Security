# 发布流程
<!-- security-log-analysis mainline -->

## 中文

### 1. 目的

本文档定义当前主线的标准发布流程。

### 2. 适用范围

适用于：

- 功能迭代
- 文档更新
- 样本训练更新
- 页面修正

### 3. 标准发布顺序

推荐顺序如下：

1. 完成功能或修复
2. 回归页面
3. 跑测试
4. 跑文档审查脚本
5. 更新文档
6. 提交当前分支
7. 推送当前分支
8. 需要时同步 `main`
9. 检查 GitHub 页面与运行态

### 4. 发布前必须同步的内容

发布前应检查：

- 代码
- 测试
- 文档审查脚本结果
- 文档
- 训练案例
- GitHub 远端

### 5. 发布后检查

发布后至少检查：

- 页面正常
- 服务正常
- 文档可读
- GitHub 口径一致

## English

### 1. Purpose

This document defines the standard release process for the current mainline.

### 2. Scope

It applies to:

- feature iterations
- documentation updates
- sample-training updates
- UI corrections

### 3. Standard Release Order

Recommended order:

1. complete the feature or fix
2. regress the UI
3. run tests
4. run the documentation audit script
5. update documentation
6. commit the working branch
7. push the working branch
8. synchronize `main` when needed
9. verify GitHub and runtime state

### 4. Items That Must Be Synchronized

Before release, review:

- code
- tests
- documentation audit results
- documentation
- training cases
- GitHub remote state

### 5. Post-Release Checks

After release, verify at least:

- UI usability
- service health
- readable documentation
- GitHub consistency
