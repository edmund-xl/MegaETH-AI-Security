# Changelog / 变更记录

## 中文版

### 0.3.23 - 2026-03-19

- 上传文件后，`统一输入` 不再留空，而是显示待分析清单，避免误以为文件没有进入当前会话
- JumpServer 单文件现在会落到更准确的独立 Skill：
  - `megaeth.identity.jumpserver_command_review`
  - `megaeth.identity.jumpserver_transfer_review`
  - `megaeth.identity.jumpserver_operation_review`
- JumpServer 单文件报告不再默认复用多源综合 Skill
- `Skill Library` 已同步补齐上述 3 条 JumpServer 单文件能力说明

### 0.3.21 - 2026-03-18

- 给 Skill 增加执行模式字段：
  - `rule_only`
  - `agent_optional`
- `Skill` 页现在会直接显示每条能力是规则版还是可挂 Agent
- 安全报告顶部新增“执行模式”字段
- 当报告实际走了 Agent 增强时，页面会明确提示当前由 Agent 增强生成
- 在 Skill 索引和 JumpServer 主 Skill spec 中补齐了这层说明

### 0.3.20 - 2026-03-18

- 将 JumpServer 的第一条 `MCP -> Agent -> Skill` 模型试点从 OpenAI 切换为 Gemini
- `megaeth.agent.core` 现在优先读取：
  - `GEMINI_API_KEY`
  - `GEMINI_MODEL_JUMPSERVER`
- 已用本地服务端环境实际验证 JumpServer 多源样本，确认：
  - `综合结论` 可由 Agent 动态生成
  - `7. 综合判断` 仍保留 MegaETH 固定模板边界
- README、Feature Snapshot、Agent / MCP 文档和 Runbook 已同步改成 Gemini 口径

### 0.3.19 - 2026-03-18

- 新增第一条 `MCP -> Agent -> Skill` 模型试点链：
  - `MCP`: JumpServer 多源审计输入
  - `Agent`: `megaeth.agent.core` 服务端 Gemini 模型绑定
  - `Skill`: `megaeth.identity.jumpserver_multi_source_review`
- 新增 `app/core/agent_model_binding.py`
- JumpServer 综合报告现在允许由 Agent 模型改写：
  - `综合结论`
  - `7. 综合判断`
  但仍然保持 MegaETH 固定模板和判断边界
- 未配置 `GEMINI_API_KEY` 时，会自动回退到现有规则版报告，不影响原有链路
- 在 README、Feature Snapshot、Agent / MCP 文档和 Runbook 中补齐了这条试点的打开方式与回退行为

### 0.3.18 - 2026-03-18

- 新增历史轻量化落库：
  - `raw_events.json`
  - `events.json`
  - `reports.json`
  不再重复存整块原始内容和大体积中间结构
- 现有历史在启动时会自动做一次轻量化整理
- 调查会话新增单独的压缩归档：
  - 在线页面只保留轻量摘要
  - 完整批次细节单独写入 `data/archives/investigations/*.json.gz`
- 在不影响页面摘要、调查记录和报告展示的前提下，将 `data/` 目录体积从约 `7.3M` 压到约 `932K`
- 这一步主要是为后面持续上传训练样本做准备，避免系统随着使用时间拉长而明显变慢

# 0.3.17 - 2026-03-18

- 把 JumpServer 综合报告从通用安全报告改成专属模板：
  - `综合结论`
  - `主要依据如下`
  - `重点高危操作账户与命令汇总`
  - `证据来源与导出链`
  - `综合判断`
- JumpServer 多源聚合新增更细的结构化字段：
  - 登录总量
  - 命令高风险语义分布
  - 文件传输总量
  - 管理平面操作者分布
  - 资源类型分布
  - 导出来源链
  - 高危账户风险计数
- 报告下载也切到同一套 JumpServer 专属模板，不再走旧的通用下载结构
- `case_002`、对应 Skill spec、案例库、功能快照、训练流程已同步更新

### 0.3.16 - 2026-03-18

- 按 JumpServer v2 模板升级 `case_002_jumpserver_multisource`
- 新增第 4 类 JumpServer 证据源：
  - `operation_audit`
- 旧登录快照改为补充样本，不再作为独立证据源重复计数
- JumpServer 综合结果新增管理平面摘要：
  - 导出
  - 授权/更新
  - 主机或账号创建
  - 会话创建
- 新增 `jumpserver_operation_review` 事件类型
- 同步更新：
  - case 文档
  - Skill spec
  - 训练流程
  - 功能快照
  - 前端标签与下载模板
  - 回归测试
### 0.3.15 - 2026-03-18

- 新增 JumpServer 多源审计训练落点：
  - `case_002_jumpserver_multisource`
  - `megaeth.identity.jumpserver_multi_source_review`
- 新增 `xlsx` 解析能力，支持 JumpServer Excel 审计材料直接进入系统
- 新增 JumpServer source / event 映射：
  - `login_auth`
  - `command_audit`
  - `file_transfer_audit`
  - `jumpserver_multi_source_audit`
- 上传同一批 JumpServer 多源日志时，系统会额外生成一条综合分析结果
- 报告语义按训练模板收成：
  - 高风险运维 / 调试链
  - 高风险待复核
  - 默认不直接判定外部入侵
- 在 README、案例库、功能快照、训练流程、Skill 索引中补齐 case 002 与 JumpServer Skill 入口

### 0.3.13 - 2026-03-16

- 新增 `megaeth.mcp.whitebox_appsec` 接入骨架，采用 MegaETH 自有命名，不暴露第三方产品名称
- 新增 `appsec` source/event/skill 映射：
  - `whitebox_recon_assessment`
  - `whitebox_exploit_validation`
  - `whitebox_security_report`
- 新增三份独立 Skill 规格：
  - `megaeth.appsec.whitebox_recon`
  - `megaeth.appsec.whitebox_exploit_validation`
  - `megaeth.appsec.whitebox_report_synthesis`
- 在 README / 系统设计 / 功能快照 / Agent-MCP 文档中补齐白盒应用安全能力说明
- 新增白盒 AppSec 训练模板目录，定义 Recon / Validation / Report 三段式训练顺序

### 0.3.12 - 2026-03-16

- split the Skill library into independent spec files under `skill_specs/`
- added a dedicated spec markdown file for every active MegaETH Skill
- turned `SKILL_LIBRARY.md` into a Skill index so future training and iteration can target one Skill at a time
- fully linked `training_case_001_host_baseline` into `megaeth.host.baseline_compliance_analysis`, including case assets, mapping rules, aggregation rules, and reporting requirements

### 0.3.10 - 2026-03-16

- 将 Bitdefender 设备采集从“单公司递归资产树”升级为“根资产树全层级递归”
- 新增公司/租户、自定义分组、全层级设备预览与统计，帮助解释控制台设备总量与公开 API 结果的偏差
- `导入终端资产到平台` 现在优先基于全层级资产树结果构建输入

### 0.3.9 - 2026-03-15

- replaced leftover dark and green UI remnants with a fully light Binance-inspired palette
- normalized planner, report, normalization, run-record, token, and status chips to the same black-gold design language
- bumped static asset versions again to force browsers onto the corrected light theme

### 0.3.8 - 2026-03-15

- 将前端视觉风格调整为更偏 Web3 控制台的方向
- 强化背景氛围、面板玻璃感、边框发光和 KPI 卡片层次
- 调整品牌图标与整体色彩系统，但保持现有信息架构和交互不变
- 将配色进一步收敛为更成熟、克制的深海蓝 + 青绿色体系，减少过强霓虹感
- 将主色体系切换为更接近 Binance 的黑金控制台风格，强化对比和品牌识别度

### 0.3.7 - 2026-03-15

- 将 `start.sh` 改为后台守护式启动，避免服务跟随启动会话结束而消失
- 增加 `.run-<port>.pid` 与 `.run-<port>.log`
- 更新 `stop.sh`，优先按 pid 文件停止服务
- 在 README 中补充运行方式说明

### 0.3.6 - 2026-03-15

- 新增 `CASE_LIBRARY.md`，正式收录已落地训练案例索引
- 为 `training_case_001_host_baseline` 新增仓库内案例目录
- 收录 case 001 的样本解读、目标报告样本、系统规则样本
- 在 README、功能快照、训练流程中补充案例样本链接

### 0.3.5 - 2026-03-15

- 移除前端和模型默认值中的 Bitdefender 明文 API key
- 改为服务端通过 `BITDEFENDER_API_KEY` 环境变量读取
- `start.sh` 支持从本地 `.env.local` 读取敏感配置
- 修复 `.gitignore` 中残留的合并冲突并加入 `.env.local` 忽略规则

### 0.3.4 - 2026-03-15

- 新增 `AGENT_MCP_LIBRARY.md`
- 为 Agent 和 MCP 增加单独的中英对照说明文档
- 在 README 文档索引中补充 Agent / MCP 入口
- 在 README、系统设计和 Agent / MCP 文档中补充架构关系图
- 移除仓库中的 Bitdefender 明文 API key，改为服务端环境变量 `BITDEFENDER_API_KEY`

### 0.3.11 - 2026-03-16

- deepened the Bitdefender MCP inventory route so it now returns policy and operating-system classification summaries
- attached the latest Bitdefender security report summary to the main network snapshot, including top hosts and top event types
- simplified the Bitdefender UI from raw API previews into a more productized connection summary view

### 0.3.22 - 2026-03-18

- fixed JumpServer XLSX parsing so headers like `*用户 / *资产 / *命令 / *动作` are normalized into the field names the pipeline actually reads
- removed the accidental `200`-row truncation before JumpServer aggregation, so login, command, file transfer, and operation summaries now run on the full worksheet
- replayed the real JumpServer sample set and verified the aggregate layer now restores the expected counts for login, command, transfer, and operation data
- tightened intake interaction so uploaded files stay staged until the manual analyze action runs, and prevented stale raw JSON from leaking into a new file-based analysis
- added a document-safe fallback so product docs and PRD-style markdown files no longer get misclassified as JumpServer or endpoint evidence just because they contain overlapping keywords

### 0.3.3 - 2026-03-15

- 将系统核心术语统一为 `Skill / Agent / MCP`
- 在 README、系统设计和功能快照中补充命名映射
- 将前端主菜单和页面文案同步到新命名方式
- 更新静态资源版本，确保页面展示切到最新术语

### 0.3.2 - 2026-03-15

- 将核心项目文档重写为中英对照版本
- 在文档重写过程中保留 case 001 主机基线训练说明
- 将 README 文档索引修正为仓库内相对链接

### 0.3.1 - 2026-03-15

- 将 API 路由拆分为 core / integration / UI 三层
- 增加共享 API 状态模块，避免 route 级重复 pipeline 状态
- 修复 README 合并冲突并重写为当前系统版本
- 将路由拆分和性能结构写入文档
- 将两天历史保留与集成缓存纳入架构说明
- 补回 `training_case_001_host_baseline` 文档记录
- 记录“一次一个 case”的训练工作流与主机基线对齐结果

### 0.3.0 - 2026-03-14

- 完成重建版工作台的产品化 UI
- 恢复双语切换、页面状态保留和 Intake 直接学习纠偏
- 增加系统设计、功能快照、重建指南、训练协作、迁移说明、发布流程文档
- 接入 Bitdefender GravityZone 的基础集成能力

### 0.2.0 - 2026-03-14

- 在新目录中重建可运行的 MegaETH AI Security 工作副本
- 恢复核心 ingestion / normalize / planner / findings / risk / report 流程
- 恢复 csv / json / log / pdf 的文件上传分析
- 加入 memory-based classification correction

### 0.1.0 - 2026-03-14

- 初始重建骨架

---

## English Version

### 0.3.13 - 2026-03-16

- added the `megaeth.mcp.whitebox_appsec` scaffold with MegaETH-native naming and no third-party product branding
- added `appsec` source/event/skill mappings for:
  - `whitebox_recon_assessment`
  - `whitebox_exploit_validation`
  - `whitebox_security_report`
- added three independent Skill specs:
  - `megaeth.appsec.whitebox_recon`
  - `megaeth.appsec.whitebox_exploit_validation`
  - `megaeth.appsec.whitebox_report_synthesis`
- documented the whitebox application security path across README, system design, feature snapshot, and Agent/MCP reference
- added a whitebox AppSec training template and formalized the Recon / Validation / Report training sequence

### 0.3.10 - 2026-03-16

- upgraded Bitdefender device collection from a single-company recursive crawl to a full root-level hierarchy crawl
- added company/tenant, custom-group, and full-hierarchy device previews and counters to explain gaps between console totals and public API results
- made `Import Asset Inventory Into Platform` prefer the full hierarchy view when building the imported input

### 0.3.8 - 2026-03-15

- shifted the frontend visual language toward a more Web3-style control console
- strengthened the atmosphere through layered backgrounds, glassy panels, glow borders, and more structured KPI cards
- updated the brand icon and color system while preserving the current information architecture and interaction flow
- refined the palette into a calmer deep-navy plus teal scheme with less aggressive neon glow
- switched the primary palette into a more Binance-like black-and-gold console direction with stronger contrast and clearer brand presence

### 0.3.7 - 2026-03-15

- changed `start.sh` to a background daemon-style launcher so the service no longer disappears with the launching session
- added `.run-<port>.pid` and `.run-<port>.log`
- updated `stop.sh` to stop the service via pid file first
- documented the runtime behavior in the README

### 0.3.6 - 2026-03-15

- Added `CASE_LIBRARY.md` as the formal landed-case index
- Added an in-repo case directory for `training_case_001_host_baseline`
- Stored the case 001 sample interpretation, target report sample, and system rules sample
- Added case sample links to README, feature snapshot, and training workflow

### 0.3.5 - 2026-03-15

- removed the Bitdefender plaintext API key from frontend code and model defaults
- switched Bitdefender connectivity to the server-side `BITDEFENDER_API_KEY` environment variable
- made `start.sh` load local sensitive configuration from `.env.local`
- fixed leftover merge-conflict content in `.gitignore` and added `.env.local` ignore rules

### 0.3.4 - 2026-03-15

- added `AGENT_MCP_LIBRARY.md`
- added a dedicated bilingual reference for Agent and MCP
- linked the Agent / MCP reference from the README index
- added architecture diagrams to the README, system design, and Agent / MCP reference
- removed the Bitdefender plaintext API key from the repository and switched to the server-side `BITDEFENDER_API_KEY` environment variable

### 0.3.3 - 2026-03-15

- standardized the core system vocabulary as `Skill / Agent / MCP`
- added naming mapping into the README, system design, and feature snapshot
- updated main frontend navigation and page copy to the new terminology
- bumped static asset versions so the browser picks up the latest wording

### 0.3.2 - 2026-03-15

- rewrote the core project documents into Chinese-first, English-following bilingual versions
- preserved case 001 host baseline training notes during the doc rewrite
- fixed the README document index to use repo-relative links

### 0.3.1 - 2026-03-15

- split API routes into core / integration / UI layers
- added shared API state to avoid route-level pipeline duplication
- fixed the README merge conflict and rewrote it to match the current system
- documented the route split and performance-oriented structure
- documented two-day retention and integration caching
- restored `training_case_001_host_baseline` documentation
- recorded the one-case-at-a-time workflow and the host baseline alignment

### 0.3.0 - 2026-03-14

- productized the rebuilt workbench UI
- restored bilingual switching, page-state persistence, and Intake learning/correction
- added system design, feature snapshot, rebuild, training, transfer, and release docs
- integrated the initial Bitdefender GravityZone capability set

### 0.2.0 - 2026-03-14

- rebuilt a working MegaETH AI Security workspace in a new directory
- restored the core ingestion / normalize / planner / findings / risk / report flow
- restored file-upload analysis for csv / json / log / pdf
- added memory-based classification correction

### 0.1.0 - 2026-03-14

- initial rebuild skeleton
