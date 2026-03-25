# Skill Specification: `megaeth.endpoint.process_anomaly`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.endpoint.process_anomaly`
- 所属模块：`Endpoint`
- 适用产品域：`安全日志分析`
- 对应事件类型：`process_alert`
- 当前执行模式：规则主链

### 2. 能力目的

分析进程异常、端点告警和可疑执行行为，输出可复核的主机侧风险判断。该 Skill 在端点侧承担“执行链解释器”的职责：它不只是罗列命令行和进程树，而是要把父子进程关系、告警来源、宿主角色和时间窗组织成一条可复核的执行叙述，帮助报告层回答“发生了什么、为什么值得关注、还缺什么证据”。

### 3. 典型输入

- 端点平台告警、进程树、命令行与父子进程信息
- 与主机可疑执行行为相关的事件材料
- 包含 `process_name`、`parent_process`、`command_line`、`user`、`host`、`timestamp`、`severity` 等字段的结构化告警
- 来自 Bitdefender、EDR、Sysmon 或主机导出的执行行为摘要
- 需要与主机基线、完整性结果或登录材料交叉复核的单文件样本

### 4. 输出契约

- 异常进程摘要
- 高风险执行线索
- 复核和处置建议
- 页面与导出中都应出现清楚的“异常执行链说明”，而不是只堆字段
- 若输入足够，应指出关键父进程、关键参数、宿主机角色和需要追补的旁证
- 不应输出虚构的 ATT&CK 技术或未在输入中出现的持久化结论

### 5. 触发与路由

当材料核心重心是进程行为、执行链、父子进程或端点异常告警时命中本 Skill。若同批材料同时包含主机完整性、登录侧或服务风险证据，本 Skill 仍只负责“执行链异常”这部分事实和判断，不替代其它 Host/Identity Skill。

### 6. 判断边界

- 异常进程不自动等于入侵成立。
- 需要结合宿主机角色、时间窗和其他证据解释异常性。
- 对合法运维工具、批量发布脚本和已知巡检进程，要优先解释“为什么异常”而不是直接定性。
- 若缺少父子进程关系、关键参数或触发上下文，结论应停在“需复核”，不能越级写成“已确认恶意执行”。

### 7. 上下游关系

- 上游通常来自 `file_ingest -> normalizer -> planner` 的端点告警解析链。
- 下游可能进入 Host 模块综合摘要，也可能被综合报告引用为“执行异常证据”。
- 当后续引入训练样本或 Gemini 增强时，只允许增强叙述段，不允许改写原始进程事实。

### 8. 训练与参考资产

- 暂无正式案例。

### 9. 常见失败模式

- 把父进程和子进程顺序写反，导致执行链叙述错误。
- 只摘录高危关键字，不解释宿主角色和上下文，输出会显得像告警转写。
- 把一次性安全工具执行、运维脚本或批处理误写成“入侵落地”。

### 10. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 11. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.endpoint.process_anomaly`
- Module: `Endpoint`
- Product Surface: `Security Log Analysis`
- Event Type: `process_alert`
- Execution Mode: rule-first

### 2. Purpose

Analyze process anomalies, endpoint alerts, and suspicious execution behavior to produce reviewable host-side risk judgments. This Skill serves as the execution-chain interpreter for endpoint material: it should turn parent-child process relationships, alert origin, host role, and timing into a coherent narrative instead of merely echoing raw fields.

### 3. Typical Inputs

- endpoint alerts, process trees, command lines, and parent-child process data
- event material related to suspicious execution behavior on endpoints
- structured alerts containing fields such as `process_name`, `parent_process`, `command_line`, `user`, `host`, `timestamp`, and `severity`
- summaries exported from Bitdefender, EDR, Sysmon, or host-side execution telemetry
- single-file samples that need to be cross-checked with host baseline, integrity, or login-side evidence

### 4. Output Contract

- anomalous-process summary
- high-risk execution signals
- review and containment recommendations
- the page and exported report should include a clear execution-chain narrative rather than a field dump
- when input is sufficient, identify the key parent process, key parameters, host role, and missing corroborating evidence
- the Skill must not invent ATT&CK techniques or persistence conclusions not present in the input

### 5. Trigger and Routing

This Skill is selected when the material centers on process behavior, execution chains, parent-child process relations, or endpoint anomaly alerts. If the same batch also contains host integrity, login-side, or service-risk evidence, this Skill still owns only the execution-anomaly slice.

### 6. Decision Boundaries

- An anomalous process does not automatically prove a confirmed intrusion.
- The anomaly should be interpreted together with host role, time window, and corroborating evidence.
- Known admin tools, deployment scripts, and inspection binaries should first be explained in context rather than directly labeled as malicious.
- If parent-child relations, critical arguments, or triggering context are missing, the conclusion must remain at “needs review” instead of jumping to confirmed malicious execution.

### 7. Upstream and Downstream Relationships

- Upstream typically comes from the endpoint-alert parsing chain in `file_ingest -> normalizer -> planner`.
- Downstream it may feed Host-module summaries or be quoted by composite reports as execution-anomaly evidence.
- If Gemini enhancement is introduced later, it must be limited to narrative sections and must not rewrite raw execution facts.

### 8. Training and Reference Assets

- No formal case yet.

### 9. Common Failure Modes

- Reversing parent and child process order, which breaks the execution narrative.
- Copying high-risk keywords without explaining host role or context, making the output read like a raw alert.
- Mislabeling one-off security tools, admin scripts, or batch jobs as confirmed compromise.

### 10. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 11. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
