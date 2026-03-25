# 接入与执行能力库
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档说明当前主线中的：

- 输入接入面
- 统一执行链
- Skill 与模型增强的分工
- 当前已接入数据源与典型映射

本文档的目标不是描述未来理想架构，而是说明当前仓库里真实存在、真实可用的接入和执行能力。

### 2. 当前接入面的定义

在当前主线中，接入面指的是安全材料进入系统的入口。它们全部服务于安全日志分析主线，不构成独立产品或第二控制面。

当前接入面包括：

- 文件上传
- 文本输入
- Bitdefender 材料导入
- Whitebox AppSec 材料输入
- JumpServer 审计材料输入
- EASM CSV 输入

### 3. 接入面的职责边界

接入面负责：

- 接收原始输入
- 基础文件识别
- 初步材料分流
- 形成调查批次

接入面不负责：

- 最终事件分类
- 报告结构定义
- 风险判断
- 页面持久化逻辑

### 4. 当前标准执行链

当前主线的标准执行链如下：

```text
ingest -> normalize -> plan -> single-source skill / composite aggregator -> risk -> report -> retain
```

各阶段职责如下：

#### 4.1 ingest

负责：

- 识别文件、文本和输入形态
- 读取 CSV、Excel、Markdown、文本等材料
- 给出文件层级提示

#### 4.2 normalize

负责：

- 标准化为统一事件模型
- 处理表头、字段、编码与基础聚合
- 为 Planner 提供路由信息

#### 4.3 plan

负责：

- 选择事件类型
- 选择 Skill
- 必要时生成综合事件
- 判断当前输入是走单文件直达链还是多文件综合链

#### 4.4 skill

负责：

- 领域分析
- findings 生成
- 结构化判断
- 报告片段输入

#### 4.5 composite aggregator

负责：

- 在多文件批次中建立跨文件上下文
- 生成综合事件
- 为综合 Skill 提供完整输入
#### 4.6 risk

负责：

- 风险分
- 风险标签
- 严重性和优先级收口
#### 4.7 report

负责：

- 页面报告
- Markdown 导出
- 段落结构统一
- 模型增强段落收口
#### 4.8 retain

负责：

- 历史记录
- 调查批次
- 学习反馈
- 训练案例沉淀

### 5. 当前已支持的输入类型

#### 5.1 Host baseline

典型输入：

- 主机基线检查结果
- 合规检查输出

主要去向：

- Host baseline Skills

#### 5.2 Endpoint / Bitdefender

典型输入：

- 安全平台导出材料
- 终端事件材料

主要去向：

- Endpoint 相关 Skills

#### 5.3 JumpServer

典型输入：

- 登录审计
- 命令审计
- 文件传输审计
- 管理平面操作记录

主要去向：

- JumpServer 单文件 Skills
- JumpServer 多源综合 Skill

#### 5.4 Whitebox AppSec

典型输入：

- 源码审计材料
- 白盒验证材料
- 综合报告输入

主要去向：

- Whitebox Recon
- Whitebox Exploit Validation
- Whitebox Report Synthesis

#### 5.5 EASM

典型输入：

- 服务面 CSV
- DNS CSV
- TLS / 证书 CSV
- ASN CSV
- IP 段 CSV

主要去向：

- EASM 单样本 Skills
- EASM 多文件综合 Skill

### 6. 当前典型输入到 Skill 的映射

当前典型映射方向如下：

- Host baseline 材料 -> Host baseline Skills
- JumpServer 单文件 -> 对应单文件 Skill
- JumpServer 多文件 -> 单文件 Skills + 聚合器 + 多源综合 Skill
- Whitebox 材料 -> Whitebox AppSec Skills
- EASM 单文件 -> 对应 EASM 单样本 Skill
- EASM 多文件 -> 单样本 Skills + 聚合器 + `easm_asset_assessment`

### 7. 单文件直达链与多文件综合链

当前主线至少包含两类执行路径：

#### 7.1 单文件直达链

```text
single file -> normalize -> plan -> single-source skill -> findings -> report
```

适用于：

- Host baseline
- JumpServer 单文件
- Whitebox 单阶段输入
- EASM 单文件

#### 7.2 多文件综合链

```text
multi-file batch -> normalize -> plan -> composite aggregator -> composite event -> composite skill -> report
```

适用于：

- JumpServer 多文件综合审计
- EASM 多文件综合评估
### 8. 模型增强边界

当前系统允许受控模型增强，但边界严格受限。

#### 7.1 模型增强允许做的事情

- 增强综合结论
- 增强专业判断
- 在固定结构内改善高层表达

#### 7.2 模型增强不允许做的事情

- 自由定义报告结构
- 取代事实抽取
- 改写字段 schema
- 决定数据去重或主键逻辑
### 9. 当前已接入的代表性增强场景

当前已接入的代表性场景包括：

- JumpServer 多源综合判断增强
- EASM 多文件综合 `assessment / professional_judgment` 增强

这些增强都遵循同一原则：

- 规则拥有事实
- 模型增强语言
- 失败时回退到规则版
### 10. JumpServer 与 EASM 的当前执行现实

#### 10.1 JumpServer

当前 JumpServer 的执行现实是：

- 单文件按登录、命令、文件传输、管理平面分别走单文件 Skill
- 多文件同批次输入会经过聚合器
- 聚合后形成多源综合事件
- 综合报告中的高层判断可由 Gemini 增强

#### 10.2 EASM

当前 EASM 的执行现实是：

- 服务、DNS、TLS、ASN、IP 等文件可以独立分析
- 多文件同批次输入会经过聚合器
- 聚合后形成 `easm_asset_assessment`
- 综合报告中的 `assessment / professional_judgment` 可由 Gemini 增强

### 11. 当前仓库中的“Agent / MCP”现实

尽管历史文档曾使用过更广的 `Agent / MCP` 说法，但在当前主线里，真正保留下来的现实是：

- 输入接入面
- Planner 与 Skill 执行链
- 受控模型增强

也就是说，当前仓库中的“能力执行”应被理解为：

- 接入面负责输入
- 主分析链负责分类与 Skill 执行
- 模型增强只作为报告层补充
### 12. 接入与执行治理规则

新增输入源或执行能力时，必须同步完成：

- 文件识别逻辑
- 归一化规则
- Planner 路由
- Skill 规格文档
- 页面验证
- 导出验证
- 测试
- 文档
### 13. 当前已知风险

当前接入与执行链的高风险点包括：

- 大文件只分析前几百行
- 表头异常导致字段取空
- 综合输入没有正确落到综合 Skill
- 页面与导出结构不一致
- 能力变更没有同步更新文档
- 聚合器没有正确形成综合事件
- 模型增强越界到事实层
### 14. 结论

当前接入与执行能力体系的正确理解方式是：

- 输入面只做材料进入
- 分析链负责事实、分类和结构
- Skill 负责领域能力
- 模型只增强允许增强的段落
- 所有变化都必须通过训练、测试和文档沉淀下来
- 当前主线同时支持单文件直达执行链与多文件综合执行链

---

## English

### 1. Purpose

This document explains the current mainline's:

- intake surfaces
- unified execution chain
- Skill and model-augmentation boundary
- landed data-source mappings

It describes the real capabilities that exist in the repository today.

### 2. Current Intake Surfaces

An intake surface is any entry point through which security materials enter the system. All of them serve the security-log-analysis mainline and do not constitute an independent product surface.

Current intake surfaces include:

- file upload
- text input
- Bitdefender imports
- Whitebox AppSec materials
- JumpServer audit materials
- EASM CSV inputs

### 3. Intake-Surface Boundaries

Intake is responsible for:

- receiving raw inputs
- basic file recognition
- initial material routing
- creating investigation batches

It is not responsible for:

- final event classification
- report-structure definition
- risk judgment
- persistence ownership

### 4. Standard Execution Chain

The current standard execution chain is:

```text
ingest -> normalize -> plan -> skill -> risk -> report -> retain
```

Each phase has a distinct responsibility boundary.

### 5. Supported Input Categories

The current mainline supports:

- Host baseline materials
- Endpoint / Bitdefender materials
- JumpServer audit materials
- Whitebox AppSec materials
- EASM CSV materials

### 6. Representative Intake-to-Skill Mapping

Typical mappings include:

- Host baseline materials -> Host baseline Skills
- JumpServer single files -> single-file JumpServer Skills
- JumpServer multi-file batches -> single-file Skills plus the multi-source composite Skill
- Whitebox materials -> Whitebox AppSec Skills
- EASM single files -> EASM single-source Skills
- EASM multi-file batches -> EASM single-source Skills plus `easm_asset_assessment`

### 7. Model-Augmentation Boundary

Controlled model augmentation may:

- enhance composite conclusions
- enhance professional judgment
- improve high-level wording inside a fixed structure

It may not:

- redefine report structure
- replace factual extraction
- redefine schema ownership
- take over identity or dedupe logic

### 8. Current Landed Augmentation Cases

Current examples include:

- JumpServer multi-source composite judgment enhancement
- EASM composite `assessment / professional_judgment` enhancement

### 9. Current Reality of Agent/MCP Language

Historically the project experimented with broader `Agent / MCP` vocabulary, but the current mainline should be understood more concretely as:

- intake surfaces
- the Planner-to-Skill execution chain
- controlled model augmentation at report time

### 10. Governance Rules

Any new intake surface or execution capability must land with:

- file recognition
- normalization
- Planner routing
- Skill specifications
- page validation
- export validation
- tests
- docs

### 11. Known Risks

Current high-risk areas include:

- truncating large files
- header failures causing empty fields
- composite inputs not reaching composite Skills
- page/export structure drift
- capability changes without doc updates

### 12. Summary

The current intake-and-execution system should be understood as:

- intake receives material
- the analysis chain owns facts, classification, and structure
- Skills own domain logic
- models only enhance explicitly allowed report sections
- durable changes must be retained through tests, cases, and docs
