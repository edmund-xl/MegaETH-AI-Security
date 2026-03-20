# `megaeth.cicd.pr_security_review`

## 中文

### 基本信息

- 中文名称：MegaETH PR 安全审查能力
- 模块：CI/CD
- 当前状态：已接入，启发式实现

### 作用

用于分析 PR、代码 diff、脚本片段和变更材料中的危险执行链、可疑命令调用与高风险代码模式。

### 典型输入

- GitHub PR 文本
- 代码 diff
- shell / Python / YAML 片段

### 当前触发线索

- `subprocess`
- `curl`
- `bash`

### 当前输出重点

- 危险执行流
- 可疑 shell 调用
- 需要人工复查的代码风险

### 当前限制

- 仍以关键词启发式为主
- 还没有做 AST、上下文依赖或仓库级语义分析

### 迭代方向

- 增加命令执行、下载执行、凭据滥用等更细的规则
- 结合仓库上下文做变更级判断

## English

### Basics

- Name: MegaETH PR Security Review
- Module: CI/CD
- Status: Active, heuristic implementation

### Purpose

Analyzes pull requests, code diffs, and change materials for dangerous execution flow and risky code patterns.

### Typical Inputs

- GitHub PR text
- code diffs
- shell / Python / YAML snippets

### Current Triggers

- `subprocess`
- `curl`
- `bash`

### Current Outputs

- dangerous execution flow
- suspicious shell usage
- code-risk review hints

### Current Limits

- still mostly keyword-driven
- no AST or repository-wide semantic review yet

### Iteration Direction

- add finer rules for download-and-execute, credential abuse, and command execution
- incorporate repository context into change review
