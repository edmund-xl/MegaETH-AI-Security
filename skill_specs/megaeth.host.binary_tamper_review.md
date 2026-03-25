# Skill Specification: `megaeth.host.binary_tamper_review`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.binary_tamper_review`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`host_integrity`
- 当前执行模式：规则主链

### 2. 能力目的

分析二进制替换、文件篡改和高风险落地行为，解释主机完整性破坏风险。该 Skill 的重点不是简单列出校验差异，而是回答“哪些文件变化对宿主安全有意义、它们更像正常变更还是异常落地、需要怎样的复核动作”。

### 3. 典型输入

- 主机完整性记录、文件校验差异、二进制替换线索
- 涉及落地文件、替换路径和发布时间的材料
- 文件散列、时间戳、目标路径、版本号、发布窗口、宿主角色等上下文字段
- 与系统服务、守护进程、启动项或关键业务二进制相关的变更清单
- 可与基线、进程告警或 systemd/service 风险样本交叉引用的主机材料

### 4. 输出契约

- 篡改风险摘要
- 可疑文件与路径
- 复核动作与时间窗说明
- 应明确区分“基线偏移”“需复核异常”“高风险替换”三类结论
- 页面与下载报告中应保留关键文件路径、宿主上下文和推荐复核动作
- 不应把缺少基线上下文的单条文件差异直接写成“已确认后门”

### 5. 触发与路由

当材料核心重心是文件替换、二进制落地、路径变更或完整性校验异常时命中本 Skill。若材料更像 systemd 服务配置、进程异常或账号风险，应分别交给 `systemd_service_risk`、`process_anomaly` 或 Identity 模块处理。

### 6. 判断边界

- 需要结合文件来源、发布时间和宿主环境复核。
- 不自动判定攻击成功。
- 升级、补丁、镜像更新或已知部署窗口中的文件变化应优先标记为“需核对变更单”。
- 没有文件来源、版本基线或业务背景时，结论不能越界到“恶意落地已成立”。

### 7. 上下游关系

- 上游常见于主机基线、文件校验或完整性监测导出。
- 下游常被 Host 综合报告引用，也可能作为事件链的“落地证据”进入更大范围的主机复核。
- 若未来允许增强，只能增强“篡改风险摘要”和“专业判断”这类叙述段。

### 8. 训练与参考资产

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 9. 常见失败模式

- 把发布窗口内的合法替换误写成高危篡改。
- 只列哈希变化，不解释文件角色、宿主角色和影响范围。
- 把单一异常文件泛化成“整机失陷”。

### 10. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 11. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.host.binary_tamper_review`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `host_integrity`
- Execution Mode: rule-first

### 2. Purpose

Analyze binary replacement, file tampering, and risky dropped-artifact behavior to explain host-integrity compromise risk. The goal is not merely to list checksum drift, but to answer which file changes matter for host security, whether they look like expected change or suspicious landing, and what review action is still required.

### 3. Typical Inputs

- host integrity records, checksum drift, and binary-replacement clues
- materials covering dropped files, replacement paths, and release timing
- context such as file hashes, timestamps, target paths, versions, release windows, and host roles
- change lists involving services, daemons, startup artifacts, or critical business binaries
- host-side material that may be cross-referenced with baseline, process alerts, or systemd/service risk samples

### 4. Output Contract

- tamper-risk summary
- suspicious files and paths
- review actions and time-window explanations
- it should clearly separate baseline drift, suspicious-but-unconfirmed change, and high-risk replacement
- page and export outputs must preserve key file paths, host context, and recommended review actions
- a single file diff without baseline context must not be turned into a confirmed backdoor statement

### 5. Trigger and Routing

This Skill is selected when the material centers on file replacement, dropped binaries, path changes, or integrity-check anomalies. If the sample is primarily about systemd configuration, process execution, or account risk, it should route to the corresponding neighboring Skill instead.

### 6. Decision Boundaries

- The interpretation must be reviewed against file origin, release timing, and host context.
- It must not automatically conclude successful compromise.
- Changes during patch windows, image refreshes, or known deployment events should first be labeled as “needs change-ticket verification.”
- Without file provenance, version baseline, or business context, the conclusion must not jump to confirmed malicious landing.

### 7. Upstream and Downstream Relationships

- Upstream is commonly host baseline, checksum, or integrity-monitoring export material.
- Downstream it is often quoted by Host composite reports as landing/tamper evidence.
- If controlled narrative enhancement is introduced later, it must stay within the risk-summary and professional-judgment sections.

### 8. Training and Reference Assets

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 9. Common Failure Modes

- Treating legitimate replacement during release windows as high-risk tampering.
- Listing hash changes without explaining file role, host role, or blast radius.
- Generalizing a single suspicious file into full-host compromise.

### 10. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 11. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
