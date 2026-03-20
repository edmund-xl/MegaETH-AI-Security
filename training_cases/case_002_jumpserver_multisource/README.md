# Case 002 - JumpServer Multi-Source Audit Review

## 中文

### 这条 case 是干嘛的

这条 case 不是让系统学会“看到 sudo 就报警”，而是让系统学会把 JumpServer 的多源日志拼成一条判断链。

重点是把下面几类材料放到同一次分析里看：

- 最新登录日志
- 命令审计日志
- 文件传输日志
- 操作记录日志

较早的登录快照现在只保留为补充对照样本，不再作为独立证据源重复计数。

我会把它当成后面 JumpServer 训练的基线 case。后面你再给新的 JumpServer 样本，我会继续往同一个 Skill 上叠，不会另起一条散的规则。

### 当前目标分类

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

单文件上传时，系统也会先识别成这些中间类型：

- `login_auth`
- `command_audit`
- `file_transfer_audit`
- `operation_audit`

但当它们出现在同一批上传里，系统会额外生成一条综合分析结果。

### 这次案例的关键目标

- 不把 JumpServer 代理地址直接当攻击源
- 不把单条 `sudo` / `systemctl` 当成入侵
- 识别“上传 -> 提权 -> 放权 -> 执行 -> 服务变更 / 网络验证”这种高风险链
- 学会输出“哪个用户、在哪台资产、做了什么高危动作、形成了什么链、最后怎么定性”

### 案例资产

- 核心训练模板与增强版结论（v2，已纳入 operation log）：
  [jumpserver_training_template_and_enhanced_conclusion.md](./jumpserver_training_template_and_enhanced_conclusion.md)

### 当前系统里的主 Skill

- Primary Skill:
  - `megaeth.identity.jumpserver_multi_source_review`
- Supporting Skill:
  - `megaeth.identity.anomalous_access_review`

### 当前系统希望输出成什么样

- 报告语言：中文
- 报告语义：
  - 更像高风险运维 / 调试链
  - 或高风险待复核
  - 默认不直接下结论说“外部入侵已成立”
- 重点输出：
  - 高风险账户
  - 跨源关联链
  - 判断边界
  - 后续复核动作

### 这次已经固定下来的报告结构

这条 case 后面不要再回到那种通用安全报告字段堆叠了。现在固定要按下面这套输出：

- `综合结论`
- `主要依据如下`
  - 登录侧
  - 命令侧
  - 文件传输侧
  - 操作记录侧
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`

我这次专门把这件事收成了 JumpServer 的专属报告模板。原因很简单：这类日志不是单点 IOC，它更像“多源操作链画像”，如果继续用通用模板，信息会散，也学不会你真正想要的判断边界。

### 这次的最终对齐要求

这条 case 之后不要再让我“理解后优化”了。后面 JumpServer 综合报告要遵守这条规则：

- 以你给出的增强版结论样本作为唯一目标模板
- 结构要贴着原稿走
- 综合结论允许根据当前真实数据动态生成，但不能脱离这份样本的判断边界。
- 标签、小节编号、段落顺序都不要随意改
- 不要为了“更像总结”而压缩
- 不要把长结论重新写成更短版本

更直接一点说：

- `综合结论` 就按你给的那段长结论写
- `1. 登录侧` 到 `4. 操作记录侧` 要按原稿展开
- `5.1 ~ 5.8` 这些重点账户小节要保留
- `6. 证据来源与导出链`
- `7. 综合判断`

如果系统当前数据还不够完整，也应该优先保住模板结构，而不是把整段删掉。

当前唯一对齐基准就是：

- [jumpserver_training_template_and_enhanced_conclusion.md](./jumpserver_training_template_and_enhanced_conclusion.md)

## English

### What this case is for

This case is not about flagging every `sudo` or `systemctl` command. It teaches the system to join multiple JumpServer evidence sources into one security judgment chain.

The important inputs are:

- latest login logs
- command audit logs
- file transfer logs
- operation audit logs

The older login snapshot is now treated only as a supplemental comparison sample and should not be counted as a separate evidence source.

This is the baseline JumpServer training case. Future JumpServer cases should continue to train the same Skill instead of creating scattered rules.

### Target classification

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

When files are uploaded one by one, the system may first classify them as:

- `login_auth`
- `command_audit`
- `file_transfer_audit`
- `operation_audit`

When they arrive in the same batch, the system should also generate one composite analysis result.

### Key outcome we want

- do not treat JumpServer proxy IP as the real attack source
- do not treat a single `sudo` / `systemctl` as an intrusion
- detect chains like upload -> privilege escalation -> permission relaxation -> execution -> service or network verification
- report which user, on which asset, performed which risky actions, what chain was formed, and how it should be classified

### Case assets

- Core training template and enhanced conclusion sample:
  [jumpserver_training_template_and_enhanced_conclusion.md](./jumpserver_training_template_and_enhanced_conclusion.md)

### Primary system Skill

- Primary Skill:
  - `megaeth.identity.jumpserver_multi_source_review`
- Supporting Skill:
  - `megaeth.identity.anomalous_access_review`

### Expected output style

- report language: Chinese
- report semantics:
  - high-risk operations / debugging chain
  - or high-risk pending review
  - not direct “external intrusion confirmed” by default
- focus output:
  - high-risk accounts
  - cross-source chains
  - judgment boundaries
  - follow-up review actions

### Report structure now fixed for this case

This case should no longer fall back to the generic security-report layout.

The expected output structure is now:

- `综合结论`
- `主要依据如下`
  - login
  - command
  - file transfer
  - operation audit
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`

This matters because JumpServer material behaves more like a multi-source operations chain than a single IOC-style incident report. If we keep rendering it as a generic report, the meaning gets diluted.
