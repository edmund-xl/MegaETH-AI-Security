# Skill Specification: `megaeth.host.systemd_service_risk`
<!-- security-log-analysis mainline -->

## 中文

### 1. 基本信息

- Skill ID：`megaeth.host.systemd_service_risk`
- 所属模块：`Host`
- 适用产品域：`安全日志分析`
- 对应事件类型：`systemd_service_change / host_integrity`
- 当前执行模式：规则主链

### 2. 能力目的

审查 systemd 服务、开放服务和运维侧服务变更风险，解释服务层暴露与控制问题。该 Skill 要把服务定义、启动方式、执行路径和宿主上下文联系起来，帮助系统区分“正常运维配置”“配置偏移”“具有持久化/高风险落地特征的服务异常”。

### 3. 典型输入

- 服务列表、systemd 配置、端口与暴露材料
- 服务变更记录和运维动作相关材料
- `service_name`、`ExecStart`、`User`、`WorkingDirectory`、`Environment`、`Restart` 等关键字段
- 主机导出的 systemctl 配置、服务清单、异常守护进程说明
- 与文件落地、进程执行或主机基线偏移需要联合解释的服务侧证据

### 4. 输出契约

- 高风险服务项
- 服务暴露面说明
- 治理建议与复核重点
- 页面和下载报告中应保留关键服务名、启动路径、运行身份和高风险配置点
- 若材料足够，应说明该服务更像业务依赖、运维组件还是可疑持久化点
- 不应把一个启用状态异常直接写成“持久化后门已确认”

### 5. 触发与路由

当输入重心是服务清单、systemd、服务变更或端口暴露时命中本 Skill。若真正的重心是二进制替换、进程行为或网络暴露，应分别交给相邻 Host/Endpoint Skill。

### 6. 判断边界

- 不对单个服务名直接给出入侵结论。
- 需要结合端口、资产角色和变更背景解释风险。
- 对运维代理、监控组件和业务守护进程，要优先判断其合法性来源，而不是只看“开机自启”就提高结论等级。
- 若缺少服务来源、部署说明或执行路径背景，应保留“需复核服务合法性”的判断层级。

### 7. 上下游关系

- 上游常来自主机配置导出、systemd 单元清单或基线偏移结果。
- 下游常被 Host 综合报告引用，也可能和 `binary_tamper_review`、`process_anomaly` 联合解释。
- 若后续引入增强，只允许增强服务风险叙述，不允许改写原始配置事实。

### 8. 训练与参考资产

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 9. 常见失败模式

- 把所有开机自启服务都当成可疑持久化。
- 只抄 ExecStart，不解释服务身份、工作目录和部署背景。
- 把配置偏移写成攻击成立，而不是“高风险配置需复核”。

### 10. 当前实现说明

- 当前实现以规则主链为主，必要时仅对允许的叙述段落叠加受控增强。
- 输出质量依赖输入材料完整度、字段质量和目标样本的约束程度。
- 分类、模板、风险语义或训练资产变化时，必须同步更新本规格。

### 11. 维护要求

- 当分类、路由条件、输出结构、风险语义或训练资产发生变化时，必须同步更新本文件。
- 若新增真实样本，应在 `training_cases/` 中建立或更新对应案例文档，并确保页面展示与下载报告口径一致。

## English

### 1. Basics

- Skill ID: `megaeth.host.systemd_service_risk`
- Module: `Host`
- Product Surface: `Security Log Analysis`
- Event Type: `systemd_service_change / host_integrity`
- Execution Mode: rule-first

### 2. Purpose

Review systemd services, exposed services, and operational service-change risk to explain service-layer exposure and control issues. This Skill should tie together service definitions, startup paths, execution identities, and host context so the system can separate expected service behavior from risky persistence-like service drift.

### 3. Typical Inputs

- service inventories, systemd configurations, and exposure material
- service-change records and operational action material
- key fields such as `service_name`, `ExecStart`, `User`, `WorkingDirectory`, `Environment`, and `Restart`
- exported systemctl data, service inventories, and daemon anomaly notes
- service-side evidence that must be interpreted together with file landing, process execution, or host baseline drift

### 4. Output Contract

- high-risk service items
- service exposure explanations
- governance recommendations and review focus
- page and export outputs should retain the service name, startup path, runtime identity, and high-risk configuration points
- when input is sufficient, it should explain whether a service looks like business dependency, ops component, or suspicious persistence-like entry
- a single abnormal enabled state must not be written as confirmed persistence

### 5. Trigger and Routing

This Skill is selected when the input centers on service lists, systemd configuration, service changes, or port exposure. If the actual center of gravity is binary replacement, process execution, or network exposure, it should route to the neighboring Host/Endpoint Skill instead.

### 6. Decision Boundaries

- A single service name must not be treated as proof of compromise.
- Risk must be explained using port exposure, asset role, and change background.
- Ops agents, monitoring components, and business daemons should first be evaluated for provenance instead of being escalated only because they auto-start.
- If provenance, deployment notes, or execution-path context are missing, the conclusion should remain at “service legitimacy requires review.”

### 7. Upstream and Downstream Relationships

- Upstream commonly comes from host configuration exports, systemd unit inventories, or baseline-drift outputs.
- Downstream it is often cited by Host composite reports and may be interpreted together with `binary_tamper_review` or `process_anomaly`.
- If narrative enhancement is introduced later, it must stay within the risk explanation and must not rewrite raw config facts.

### 8. Training and Reference Assets

- [Case 001 - Host Baseline](../training_cases/case_001_host_baseline/README.md)

### 9. Common Failure Modes

- Treating every auto-start service as suspicious persistence.
- Copying `ExecStart` without explaining identity, working directory, or deployment context.
- Converting config drift into confirmed attack language instead of high-risk review language.

### 10. Current Implementation Notes

- The current implementation is rule-first, with controlled augmentation only on explicitly allowed narrative sections.
- Output quality depends on input completeness, field quality, and the tightness of target-sample constraints.
- Whenever classification, templates, risk semantics, or training assets change, this specification must be updated together.

### 11. Maintenance Requirements

- Update this file whenever classification, routing conditions, output structure, risk semantics, or training assets change.
- When new real samples are introduced, create or update the matching case document under `training_cases/` and keep page/export behavior aligned.
