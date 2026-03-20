# megaeth.appsec.whitebox_recon

## 中文

### 基本信息
- Skill ID: `megaeth.appsec.whitebox_recon`
- 模块: `appsec`
- 当前状态: `L2 / 规则与接入骨架已落地`

### 作用
对应用代码与运行目标做白盒侦察，提炼潜在攻击面、关键入口、鉴权边界和后续应重点验证的路径。

### 典型输入
- 代码仓库路径
- 运行中的目标地址
- 应用级配置文件

### 当前触发线索
- `source_type = appsec`
- `event_type = whitebox_recon_assessment`

### 当前输出重点
- 攻击面摘要
- 候选验证路径
- 暴露模式与优先排查线索

### 当前限制
- 当前是 MegaETH 自有白盒 MCP 骨架，不绑定任何第三方实现细节
- 尚未接入真实 exploit 执行结果

### 迭代方向
- 增加路由、鉴权边界、输入点的结构化 schema
- 关联后续 exploit validation 结果形成闭环

### 对应训练落点
- 未来白盒侦察类案例应同步到这个 Skill
- 推荐先使用：
  [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)

## English

### Basics
- Skill ID: `megaeth.appsec.whitebox_recon`
- Module: `appsec`
- Current status: `L2 / heuristic + integration scaffold`

### Purpose
Perform whitebox reconnaissance against an application codebase and running target to surface attack paths, trust boundaries, and validation priorities.

### Typical Inputs
- Repository path
- Running target URL
- Application configuration

### Current Triggers
- `source_type = appsec`
- `event_type = whitebox_recon_assessment`

### Current Output Focus
- Attack surface summary
- Candidate validation paths
- Exposure patterns and triage leads

### Current Limits
- MegaETH-native clean-room scaffold only
- Does not yet ingest live exploit validation output

### Iteration Direction
- Add structured schemas for routes, auth boundaries, and input sinks
- Join later validation results into a closed whitebox workflow

### Training Sync Target
- Future whitebox reconnaissance cases should sync into this Skill
- Recommended template:
  [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)
