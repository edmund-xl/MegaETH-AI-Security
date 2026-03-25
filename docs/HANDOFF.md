# 交接文档
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档用于帮助以下场景快速恢复上下文：

- 新电脑接手本项目
- 新 Codex 会话继续当前主线
- 新协作者加入维护

它不是产品宣传文档，而是持续开发和交接的工程文档。

### 2. 当前唯一产品域

仓库当前只服务于一个产品域：

- 安全日志分析

这条边界是硬约束。任何新的功能讨论、样本训练、页面修改和文档更新，都必须围绕安全日志分析展开。

### 3. 当前产品形态

当前系统应被理解为：

- 本地优先的安全日志分析工作台
- 可训练、可复核、可持续校准的分析系统
- 规则主链优先、受控模型增强的报告系统

系统不应被理解为：

- 自动攻击平台
- 自动处置中心
- 多产品域控制台

### 4. 当前已落地主分析域

当前主线已稳定落地以下分析域：

- Host baseline
- Endpoint 平台事件
- JumpServer 单文件与多源审计
- Whitebox AppSec 三段式分析
- EASM 单样本分析
- EASM 多样本综合分析

### 5. 当前 EASM 状态

EASM 当前已经具备以下能力：

- 单一样本可独立分析
- 多文件可综合分析
- 可生成 `easm_asset_assessment`
- 综合报告保留规则事实抽取
- 综合报告中的 `assessment / professional_judgment` 可由 Gemini 增强

### 6. 推荐续接顺序

如果要继续推进主线，推荐顺序如下：

1. 获取样本
2. 获取目标输出示例
3. 校准分类与 Skill 路由
4. 校准报告结构与判断语言
5. 验证页面与下载一致性
6. 补齐训练案例与学习反馈
7. 更新文档
8. 同步 GitHub

### 7. 当前必须记住的边界

#### 7.1 产品边界

- 不再引入第二产品域
- 不跨项目混用样本
- 不允许共享层顺手改坏五页面前端

#### 7.2 样本训练边界

训练时不能只验证“解析成功”，还必须验证：

- 表头归一化
- 行数完整性
- 聚合是否使用全量数据
- 页面输出
- 报告导出
- 已落库旧对象兼容性

#### 7.3 文档同步边界

能力变化时，不允许只改代码或只改 README。至少同步检查：

- `README.md`
- `docs/HANDOFF.md`
- `docs/STATUS.md`
- `docs/FEATURE_SNAPSHOT.md`
- `docs/TRAINING_WORKFLOW.md`
- 相关 `training_cases`
- 相关 `skill_specs`

### 8. 当前运行基线

- 默认端口：`8011`
- 健康检查：`/health`
- 主要烟测接口：`/pipeline/overview`
- 主要回归测试：`tests/test_api.py`

### 9. 新机器续接步骤

新机器接手时，推荐按以下顺序恢复：

1. clone 仓库
2. 安装 Python 依赖
3. 启动本地服务
4. 阅读本文档与 `README`
5. 阅读 `docs/STATUS.md`
6. 再开始接新的样本和目标输出

### 10. 当前交接结论

如果新的协作者或 Codex 会话要继续本项目，应该默认理解：

- 主线只做安全日志分析
- 五页面前端是当前唯一 UI 工作台
- 样本驱动训练是主要推进方式
- 当前最值得继续强化的域包括：
  - JumpServer
  - Whitebox AppSec
  - EASM

---

## English

### 1. Purpose

This document is the project handoff guide for:

- a new machine
- a new Codex session
- a new collaborator joining the project

It is an engineering continuation document, not a product marketing document.

### 2. Single Active Product Surface

The repository now serves only one product surface:

- security log analysis

That boundary is a hard constraint.

### 3. Current Product Shape

The system should currently be understood as:

- a local-first security log analysis workbench
- a trainable, reviewable, continuously calibratable analysis system
- a rule-first reporting pipeline with controlled model augmentation

It should not be understood as:

- an automated attack platform
- an auto-remediation center
- a multi-surface control plane

### 4. Implemented Analysis Domains

The active mainline includes:

- Host baseline
- Endpoint platform events
- JumpServer single-source and multi-source audit analysis
- Whitebox AppSec three-stage analysis
- EASM single-source analysis
- EASM composite multi-file analysis

### 5. Current EASM Status

EASM currently supports:

- standalone single-file analysis
- composite multi-file analysis
- generation of `easm_asset_assessment`
- rule-owned factual extraction
- Gemini-enhanced `assessment` and `professional_judgment`

### 6. Recommended Continuation Order

When continuing the project, the preferred order is:

1. obtain samples
2. obtain target outputs
3. calibrate classification and Skill routing
4. calibrate report structure and judgment language
5. verify page/export consistency
6. retain training cases and learning feedback
7. update docs
8. sync GitHub

### 7. Boundaries That Must Be Preserved

#### 7.1 Product Boundary

- do not reintroduce a second product surface
- do not mix cross-project samples
- do not break the shared five-page frontend while making local changes

#### 7.2 Sample-Training Boundary

Training must validate more than parser success:

- header normalization
- row-count integrity
- full-data aggregation
- page output
- exported report output
- compatibility with older stored objects

#### 7.3 Documentation Boundary

Capability changes must not stop at code or README updates. Also review:

- `README.md`
- `docs/HANDOFF.md`
- `docs/STATUS.md`
- `docs/FEATURE_SNAPSHOT.md`
- `docs/TRAINING_WORKFLOW.md`
- related `training_cases`
- related `skill_specs`

### 8. Runtime Baseline

- default port: `8011`
- health endpoint: `/health`
- smoke endpoint: `/pipeline/overview`
- regression entry: `tests/test_api.py`

### 9. New-Machine Continuation Steps

On a new machine:

1. clone the repository
2. install Python dependencies
3. start the local service
4. read this document and the README
5. read `docs/STATUS.md`
6. then continue with new samples and target outputs

### 10. Handoff Summary

A new collaborator or Codex session should assume:

- the only active mainline is security log analysis
- the five-page frontend is the only active UI workbench
- sample-driven training is the primary way of moving the project forward
- the most valuable domains to continue refining are:
  - JumpServer
  - Whitebox AppSec
  - EASM
