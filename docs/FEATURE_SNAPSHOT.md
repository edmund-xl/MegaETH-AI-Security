# Feature Snapshot / 功能快照

## 中文版

这份文档不讲理念，只回答一个问题：现在这套系统已经能稳定干什么，哪些还只是方向。

如果你刚接手项目，我一般建议先看这里，再去看 Skill spec 和具体 case。这样你会先知道“手里有什么”，不会一上来就扎进实现细节。

### 现在已经稳定可用的

#### 输入与分析

- 文本输入
- 批量文件上传
- `csv / json / log / txt / yaml / yml / md / 文本型 pdf`
- 上传后先进入待分析状态，不会自动跑；只有点击 `归一化后分析` 才真正开始处理
- 归一化预览
- Agent 决策预览
- 归一化后分析
- 中文安全报告

#### 性能与存储

- 历史数据默认只保留最近 2 天
- 页面只读取最近窗口，不会把全部历史一次性拖进来
- `raw_events / events / reports` 已切成轻量化落库
- 大样本训练后，系统保留的是后续页面和调查真正会用到的摘要字段，而不是把大块中间内容重复写入多份历史文件
- 每次调查批次的完整细节会单独压成 `json.gz` 归档，和页面摘要分开保存

#### 页面层

- `Overview`
- `Intake`
- `Skill`
- `MCP`
- `Agent Learning`
- `APPA Pentest Workbench`
  - `Dashboard`
  - `Analytics`
  - `Reports`
- 中英文切换
- 刷新后保留当前页面

#### Agent 主链

- `normalizer`
- `planner`
- `skills`
- `risk_engine`
- `report_engine`
- `history`
- `memory_service`
- JumpServer Agent 模型试点
  - 当前只挂在 `megaeth.agent.core`
  - 当前只用于 `megaeth.identity.jumpserver_multi_source_review`
  - 没配 `GEMINI_API_KEY` 时自动回退到规则版报告

#### MCP

- Bitdefender
  - 连接验证
  - 最新可分析内容
  - 导入终端资产到平台
  - 导入最新报表内容
- Whitebox AppSec
  - 已有骨架
  - 已有三段式训练落点

#### APPA 渗透测试工作台

- 和安全日志分析产品分离，不共用同一套语义和工作流
- 已有独立控制面：
  - engagement
  - run
  - finding
  - report
- `Launch New Scan` 会真实生成新的运行批次
- `Audit Report` 会下载当前最新 APPA 审计报告
- `Dashboard / Analytics / Reports` 已经是可切换的真实工作台视图，不再只是占位标签

#### 学习

- 自动 observation
- 长期学习规则
- 最近学习反馈
- 重复规则合并
- 手工规则优先于自动规则

### 现在已经落地的训练成果

#### Case 001 - Host Baseline Assessment

- 案例目录：
  [training_cases/case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- 主 Skill：
  [megaeth.host.baseline_compliance_analysis.md](../skill_specs/megaeth.host.baseline_compliance_analysis.md)
- 当前稳定结果：
  - `riskanalytics` 类文件稳定映射到
    - `host_risk_analytics`
    - `host_baseline_assessment`
  - 默认中文报告
  - 默认 `medium`
  - finding 聚合成 4 类，不再逐行直出

#### Case 002 - JumpServer Multi-Source Audit Review

- 案例目录：
  [training_cases/case_002_jumpserver_multisource/README.md](../training_cases/case_002_jumpserver_multisource/README.md)
- 主 Skill：
  [megaeth.identity.jumpserver_multi_source_review.md](../skill_specs/megaeth.identity.jumpserver_multi_source_review.md)
- 当前稳定结果：
  - 支持多份 JumpServer `xlsx` 审计文件
  - 能识别登录、命令、文件传输、操作记录四类中间输入
  - 带 `*` 的 JumpServer 表头会自动归一化成系统字段，不会再因为字段名不一致把 `用户 / 资产 / 命令 / 动作` 读空
  - 登录与命令审计会基于完整 `xlsx` 行数聚合，不再被错误裁成前 `200` 行
  - 较早登录快照会降级成补充样本，不再重复计数
  - 同批上传时生成综合分析结果
  - 输出高风险账户、跨源操作链、判断边界与复核动作
  - 综合报告已经切到专属模板：
    - `综合结论`
    - `主要依据如下`
    - `重点高危操作账户与命令汇总`
    - `证据来源与导出链`
    - `综合判断`

### 现在已经能看见的 Skill 层信息

`Skill` 页面现在不再只是平铺卡片，已经能直接看：
- 模块分组
- 成熟度
- 已训练 case 数
- 对应 spec 入口

这点很重要，因为它让 Skill 不再只是“代码里有个名字”，而是真正可以持续训练和维护的对象。

### 还在往前推，但别假设已经很成熟

这些方向已经有结构，但深度还在继续补：
- AppSec 白盒综合报告
- EASM 复合报告
- 更多外部平台 MCP
- 更多真实 case 回归
- 更强的 PDF/OCR 支持

### 我会怎么用这份快照

如果你问我“这版本能不能拿来继续训练”，我会先看三件事：
- 关键页面是不是都在
- 主分析链是不是都通
- 至少一个真实 case 是不是已经被系统稳定吸收

以现在这版来说，这三件事都是满足的。

---

## English Version

This document answers one practical question: what is already stable and usable right now, and what is still a work in progress.

If I were onboarding into the project, I would read this before diving into implementation details. It tells you what you actually have in hand.

### Stable and usable now

#### Intake and analysis

- text input
- batch file upload
- `csv / json / log / txt / yaml / yml / md / text-based pdf`
- normalization preview
- Agent decision preview
- normalize-and-analyze flow
- Chinese-first security reporting

#### UI

- `Overview`
- `Intake`
- `Skill`
- `MCP`
- `Agent Learning`
- `APPA Pentest Workbench`
  - `Dashboard`
  - `Analytics`
  - `Reports`
- bilingual switch
- active page preserved after refresh

#### Agent core flow

- `normalizer`
- `planner`
- `skills`
- `risk_engine`
- `report_engine`
- `history`
- `memory_service`
- JumpServer Agent model pilot
  - currently bound to `megaeth.agent.core`
  - currently used only for `megaeth.identity.jumpserver_multi_source_review`
  - automatically falls back to rule-based reporting when `GEMINI_API_KEY` is missing

#### MCP

- Bitdefender
  - connection verification
  - latest analyzable content
  - import endpoint assets
  - import latest report content
- Whitebox AppSec
  - scaffold exists
  - three-stage training path exists

#### APPA Pentest Workbench

- independent from the security log analysis product and does not reuse the same workflow semantics
- ships with its own control-plane objects:
  - engagement
  - run
  - finding
  - report
- `Launch New Scan` now creates a real run
- `Audit Report` now downloads the latest APPA audit report
- `Dashboard / Analytics / Reports` are now real switchable workbench views rather than placeholder tabs

#### Learning

- automatic observations
- long-lived learning rules
- recent learning feedback
- duplicate rule merging
- manual rule priority over auto rules

### Landed training result

#### Case 001 - Host Baseline Assessment

- Case directory:
  [training_cases/case_001_host_baseline/README.md](../training_cases/case_001_host_baseline/README.md)
- Primary Skill:
  [megaeth.host.baseline_compliance_analysis.md](../skill_specs/megaeth.host.baseline_compliance_analysis.md)
- Stable outcome:
  - `riskanalytics` materials now map to
    - `host_risk_analytics`
    - `host_baseline_assessment`
  - Chinese-first reports
  - default `medium`
  - findings aggregate into four categories instead of raw row-by-row output

### What the Skill layer now exposes

The `Skill` page now shows:
- module grouping
- maturity
- trained case count
- direct spec links

For JumpServer, the single-source routes are now split instead of forcing everything into the composite review:
- `megaeth.identity.anomalous_access_review` for login-only material
- `megaeth.identity.jumpserver_command_review` for command-only material
- `megaeth.identity.jumpserver_transfer_review` for file-transfer-only material
- `megaeth.identity.jumpserver_operation_review` for operation-audit material
- `megaeth.identity.jumpserver_multi_source_review` only when the batch is truly multi-source

That matters because Skills are no longer just names in code. They are becoming trainable, maintainable capability units.

### In progress, but not fully mature yet

These paths exist, but still need more training depth:
- AppSec whitebox synthesis reporting
- composite EASM reporting
- more external MCPs
- broader real-case regression
- deeper PDF / OCR support

### How I use this snapshot

If I want to know whether the platform is in a good state for continued training, I check:
- are the core pages present
- does the main analysis chain still work
- has at least one real case been stably absorbed

For the current version, the answer is yes.
