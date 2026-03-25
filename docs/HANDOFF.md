# 交接文档
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

用于新机器、新 Codex 会话或新协作者快速恢复上下文。

### 2. 当前唯一产品域

仓库当前只服务于安全日志分析。

### 3. 当前产品形态

系统应被理解为可训练、可复核、可持续校准的安全日志分析工作台。

当前已经稳定存在的重点分析域包括：

- Host baseline
- Endpoint 平台事件
- JumpServer 单文件与多源审计
- Whitebox AppSec 三段式分析
- EASM 单样本与多样本综合分析

其中 EASM 当前状态是：

- 单一样本可单独分析
- 多文件可生成 `easm_asset_assessment` 综合结果
- 综合报告支持规则事实抽取
- 综合报告的 `综合结论 / 专业判断` 可由 Gemini 增强

### 4. 当前工作模式

推荐续接顺序是样本、目标输出、分类、报告、文档和 GitHub 同步。

### 5. 已知教训

跨项目材料、大文件处理、共享层越界和浏览器大输入缓存都是高风险坑。


## English

### 1. Purpose

Allow a new machine, Codex session, or collaborator to recover context quickly.

### 2. Single Active Product Surface

The repository currently serves only security log analysis.

### 3. Current Product Shape

The system should be treated as a trainable, reviewable, continuously calibratable security-log-analysis workbench.

The main implemented analysis domains currently include:

- Host baseline
- Endpoint platform events
- JumpServer single-source and multi-source audit analysis
- Whitebox AppSec three-stage analysis
- EASM single-source and composite analysis

Current EASM status:

- Single-source files can be analyzed independently
- Multi-file inputs can produce a composite `easm_asset_assessment`
- Composite reporting keeps rule-based factual extraction
- The composite `assessment` and `professional_judgment` can be Gemini-enhanced

### 4. Continuation Pattern

The recommended continuation order is samples, target outputs, classification, reporting, documentation, and GitHub sync.

### 5. Known Pitfalls

Cross-project data, large-file handling, shared-layer overreach, and large browser-stored raw inputs are all recurring risks.
