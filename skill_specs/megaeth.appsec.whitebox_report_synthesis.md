# megaeth.appsec.whitebox_report_synthesis

## 中文

### 基本信息
- Skill ID: `megaeth.appsec.whitebox_report_synthesis`
- 模块: `appsec`
- 当前状态: `L2 / 规则与接入骨架已落地`

### 作用
将白盒侦察与验证结果汇总为一份更适合交付的应用安全综合报告，突出结论、验证结果和优先治理动作。

### 典型输入
- 执行摘要
- 已确认与候选发现
- 优先行动建议

### 当前触发线索
- `source_type = appsec`
- `event_type = whitebox_security_report`

### 当前输出重点
- 综合判断
- 已确认问题摘要
- 优先行动计划

### 当前限制
- 目前偏平台化综合摘要，仍需后续 case 训练打磨语言风格
- 尚未拆分为细粒度漏洞章节

### 迭代方向
- 结合真实 case 打磨中文交付风格
- 增加章节化输出与优先级分层

### 对应训练落点
- 未来白盒综合报告类案例应同步到这个 Skill
- 推荐先使用：
  [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)

## English

### Basics
- Skill ID: `megaeth.appsec.whitebox_report_synthesis`
- Module: `appsec`
- Current status: `L2 / heuristic + integration scaffold`

### Purpose
Synthesize whitebox recon and validation outputs into a delivery-grade application security report that highlights conclusions, proof-backed issues, and priority actions.

### Typical Inputs
- Executive summary
- Confirmed and candidate findings
- Priority remediation actions

### Current Triggers
- `source_type = appsec`
- `event_type = whitebox_security_report`

### Current Output Focus
- Overall judgment
- Confirmed issue summary
- Priority action plan

### Current Limits
- Still oriented around platform summaries and needs case-trained phrasing
- Not yet split into fine-grained vulnerability chapters

### Iteration Direction
- Tune Chinese delivery style with real training cases
- Add section-based reporting and stronger priority layering

### Training Sync Target
- Future whitebox synthesis report cases should sync into this Skill
- Recommended template:
  [training_cases/templates/appsec_whitebox_case_template/README.md](../training_cases/templates/appsec_whitebox_case_template/README.md)
