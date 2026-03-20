# `megaeth.identity.jumpserver_multi_source_review`

## 中文

### 基本信息

- 中文名称：MegaETH JumpServer 多源关联审计能力
- 模块：Identity
- 当前状态：已接入，已完成 `case_002_jumpserver_multisource` 第一轮训练落点
- 执行方式：`可挂 Agent`
  - 默认仍可走规则版
  - 已接入 `megaeth.agent.core + Gemini` 试点，用于增强 `综合结论` 与 `7. 综合判断`

### 作用

这是 JumpServer 场景下的主 Skill。它不看单条命令，而是把登录、命令、文件传输、操作记录几类材料拼成一条高风险会话链。

我一般会把它理解成“JumpServer 审计总控 Skill”。只要后面你给的是多份 JumpServer 周报、审计导出、命令与传输日志组合，这条 Skill 都应该是主落点。

### 典型输入

- `userloginlog.xlsx`
- `command.xlsx`
- `ftplog.xlsx`
- `operatelog.xlsx`
- 同一批上传的 JumpServer 多份 xlsx 审计材料

### 当前触发线索

- `登录 IP`
- `认证方式`
- `命令`
- `会话`
- `风险等级`
- `文件名`
- `动作`
- `资源类型`
- `组织名称`
- `/tmp/`
- `sudo`
- `systemctl`
- `chmod`
- `scp`
- `rsync`
- `curl`
- `telnet`
- `nc`

### 当前输出重点

- 高风险账户汇总
- 跨源高风险链
- 上传 /tmp -> 放权 -> 执行 -> 网络验证
- 导出 / 授权 / 主机或账号创建 / 会话创建等管理平面动作
- 高风险运维链 / 调试链
- 判断边界与后续复核动作

### 已同步训练案例

- 案例：
  [case_002_jumpserver_multisource/README.md](../training_cases/case_002_jumpserver_multisource/README.md)
- 核心训练模板：
  [jumpserver_training_template_and_enhanced_conclusion.md](../training_cases/case_002_jumpserver_multisource/jumpserver_training_template_and_enhanced_conclusion.md)

### 当前训练结果

- 分类：
  - `source_type = jumpserver`
  - `event_type = jumpserver_multi_source_audit`
- 支持的中间输入类型：
  - `login_auth`
  - `command_audit`
  - `file_transfer_audit`
  - `operation_audit`
- 报告语义：
  - 默认不直接判定外部入侵
  - 优先输出高风险运维 / 调试链
  - 当证据足够时提升为 `high_risk_pending_review`
- 当前专属报告模板：
  - `综合结论`
  - `主要依据如下`
    - 登录侧
    - 命令侧
    - 文件传输侧
    - 操作记录侧
  - `重点高危操作账户与命令汇总`
  - `证据来源与导出链`
  - `综合判断`

### 当前固定对齐规则

这条 Skill 后面不要再把 JumpServer 综合报告当成“可以自由总结”的材料处理。当前已经固定下来的规则是：

- 以 `case_002_jumpserver_multisource` 里的增强版结论样本作为唯一目标模板
- 报告结构要尽量贴着训练样本原稿
- 综合结论允许根据当前真实数据动态生成，但判断边界要保持一致。
- 不要为了更短、更像摘要而压缩结论
- 不要把 `5.1 ~ 5.8` 这种重点账户段落合并成一个泛化列表
- 下载版和页面版都应该服从同一套结构约束

这一步很重要。JumpServer 这类材料本质上不是单一 IOC 事件，而是“多源操作链与管理平面背景”的联合判断。如果把它重新压成通用摘要，系统就学不会你真正要的边界感。

### 当前规则边界

- 不把 JumpServer 代理地址直接当成真实攻击源
- 不信任导出里的原始 `风险等级 = 接受(0)`
- 不因为单条 `sudo` / `systemctl` 直接判定入侵
- `/tmp` 上传加执行应标记为高风险，但不自动等于恶意
- 管理平面操作是背景支撑证据，不能替代主机侧执行证据
- 优先做同用户、同资产、相近时间窗、相同文件名的跨源关联

### 当前限制

- 目前还是启发式聚合，不是严格会话图谱
- FTP 会话和命令会话号无法自动一一对应时，仍然依赖近似时间窗与文件名关联
- 还没有纳入你真实生产样本里的完整资产重要性和授权维护窗口信息

### 迭代方向

- 引入更稳定的用户-资产-会话图谱
- 加入资产角色和维护窗口语义
- 让“高风险运维”和“已确认恶意”之间的边界更稳
- 每个 JumpServer case 训练后，都要回写到这份 Skill spec

## English

### Basics

- Name: MegaETH JumpServer Multi-Source Audit Review
- Module: Identity
- Status: Active, with the first training landing from `case_002_jumpserver_multisource`
- Execution mode: `Agent optional`
  - still works in rule-only mode by default
  - now piloted with `megaeth.agent.core + Gemini` to enhance the composite conclusion and section 7

### Purpose

This is the main Skill for JumpServer review. It does not treat single commands as final evidence. Instead, it joins login, command, file transfer, and operation-audit material into one higher-confidence operation chain.

### Typical inputs

- `userloginlog.xlsx`
- `command.xlsx`
- `ftplog.xlsx`
- `operatelog.xlsx`
- the same upload batch containing multiple JumpServer xlsx audit exports

### Current triggers

- `登录 IP`
- `认证方式`
- `命令`
- `会话`
- `风险等级`
- `文件名`
- `动作`
- `资源类型`
- `组织名称`
- `/tmp/`
- `sudo`
- `systemctl`
- `chmod`
- `scp`
- `rsync`
- `curl`
- `telnet`
- `nc`

### Current outputs

- high-risk account summaries
- cross-source high-risk chains
- upload to /tmp -> permission change -> execution -> network verification
- export / authorization / host-or-account creation / session creation as control-plane evidence
- high-risk operations / debugging chains
- judgment boundaries and follow-up review actions

### Synced training case

- Case:
  [case_002_jumpserver_multisource/README.md](../training_cases/case_002_jumpserver_multisource/README.md)
- Core training template:
  [jumpserver_training_template_and_enhanced_conclusion.md](../training_cases/case_002_jumpserver_multisource/jumpserver_training_template_and_enhanced_conclusion.md)

### Current training outcome

- classification:
  - `source_type = jumpserver`
  - `event_type = jumpserver_multi_source_audit`
- supported intermediate inputs:
  - `login_auth`
  - `command_audit`
  - `file_transfer_audit`
  - `operation_audit`
- report semantics:
  - do not default to external intrusion confirmed
  - prioritize high-risk operations / debugging chains
  - escalate to `high_risk_pending_review` when evidence is strong enough
- fixed report structure:
  - `综合结论`
  - `主要依据如下`
    - login
    - command
    - file transfer
    - operation audit
  - `重点高危操作账户与命令汇总`
  - `证据来源与导出链`
  - `综合判断`

### Current boundary rules

- do not treat JumpServer proxy IP as the true attack source
- do not trust exported native `风险等级 = 接受(0)`
- do not classify intrusion from a single `sudo` / `systemctl`
- `/tmp` upload plus execution is high risk, but not automatically malicious
- control-plane actions support the narrative, but do not replace host-side execution evidence
- prefer same user, same asset, nearby time window, and same filename for cross-source correlation

### Current limits

- current correlation is heuristic, not a full session graph
- when FTP sessions and command sessions do not map directly, the logic still relies on time window and filename proximity
- the system still needs more real production cases with maintenance-window context and asset criticality

### Iteration direction

- introduce a more stable user-asset-session graph
- add asset-role and maintenance-window semantics
- sharpen the boundary between high-risk operations and confirmed malicious activity
- sync every future JumpServer case back into this Skill spec
