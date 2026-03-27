# Changelog
<!-- security-log-analysis mainline -->

## 中文

### 2026-03-27

#### 性能与长期运行优化

- 将 `/history` 调整为摘要接口，避免首页为历史面板加载完整数组
- 为 JSON 文件读取增加进程内缓存，减少未变化数据的重复解析
- 为 Skill 训练案例索引增加缓存，避免概览和技能页反复扫描 `training_cases/`
- 为学习页移除对已删除“学习规则”面板的无意义请求
- 将近期报告与学习反馈接口调整为摘要载荷，降低概览页和学习页的长期负载

#### 文档与规范同步

- 在 `README`、`SYSTEM_DESIGN`、`STATUS`、`runbook` 中补充当前性能约束和长期运行说明
- 修复核心文档英文段与中文段不同步的问题，统一当前真实架构口径
- 新增 `CI/CD` 日志采集与 API 推送规范文档
- 将 `docs/`、`skill_specs/`、`training_cases/` 继续提升到更接近正式工程文档的标准

### 2026-03-25

#### EASM 分析链接入

- 新增 EASM 单样本分析能力
- 新增 EASM 多样本综合分析能力
- 新增 `easm_asset_assessment` 综合结果生成
- 将 EASM 多文件综合报告的 `assessment / professional_judgment` 接入受控 Gemini 增强

#### 文档体系重写

- 重写根目录与 `docs/` 文档，统一为安全日志分析主线的软件工程文档结构
- 重写 `skill_specs/` 与 `training_cases/` 文档模板，使其与当前产品边界和训练流程一致
- 补充跨设备续接所需的交接文档、迁移文档与运行文档

#### 仓库卫生与边界收敛

- 清理已废弃产品线相关的文档残留和目录级元数据痕迹
- 明确仓库只承载安全日志分析主线
- 统一运行端口、运行手册和发布说明到 `8011`

### 2026-03-22

#### 前端与运行稳定性修正

- 收敛前端页面结构，仅保留 `概览 / 输入 / 技能 / 连接 / 学习`
- 修正服务启动、静态资源版本和健康检查相关问题
- 清理历史错误状态导致的页面“加载中”问题

### 2026-03-18

#### JumpServer 与训练主线增强

- 强化 JumpServer 单文件与多源分析链
- 固化 JumpServer 综合报告结构与训练模板
- 收紧学习、历史、下载与展示之间的一致性要求

---

## English

### 2026-03-27

#### Performance and Long-Running Optimizations

- changed `/history` into a summary endpoint so the homepage no longer loads full history arrays
- added in-process caching for JSON file reads to avoid repeatedly parsing unchanged files
- added caching for the Skill training-case index so overview and skills pages do not rescan `training_cases/` on each request
- removed unnecessary learning-view requests for the retired rules panel
- changed recent-reports and learning-feedback endpoints to summary payloads, reducing long-term load on overview and learning views

#### Documentation and Specification Synchronization

- documented current runtime performance constraints in `README`, `SYSTEM_DESIGN`, `STATUS`, and `runbook`
- fixed parity issues where English core-doc sections had drifted from the Chinese source of truth
- added a dedicated `CI/CD` log collection and API push specification
- continued raising `docs/`, `skill_specs/`, and `training_cases/` toward a more formal engineering-document standard

### 2026-03-25

#### EASM Analysis Pipeline

- added EASM single-source analysis
- added EASM composite multi-file analysis
- added composite `easm_asset_assessment` generation
- enabled controlled Gemini enhancement for EASM composite `assessment / professional_judgment`

#### Documentation System Rewrite

- rewrote root and `docs/` documents into a security-log-analysis engineering-document set
- rewrote `skill_specs/` and `training_cases/` templates to match the current product boundary and training workflow
- added handoff, transfer, and runtime documents needed for cross-device continuation

#### Repository Hygiene and Scope Convergence

- removed metadata and documentation residue from the retired product line
- made the repository explicitly single-surface around security log analysis
- aligned runtime port, runbook, and release notes to `8011`

### 2026-03-22

#### Frontend and Runtime Stability Fixes

- converged the frontend to the five-page workbench only: `Overview / Intake / Skills / Integrations / Learning`
- fixed service startup, static-asset versioning, and health-check issues
- removed loading-state failures caused by stale frontend state

### 2026-03-18

#### JumpServer and Training-Mainline Enhancements

- strengthened JumpServer single-file and composite multi-source analysis
- stabilized the JumpServer composite report structure and training template
- tightened consistency across learning, history, downloads, and on-page rendering
