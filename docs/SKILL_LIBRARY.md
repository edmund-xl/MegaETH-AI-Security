# Skill Library / Skill 能力库

## 中文版

这份文档最适合在两种时候看：
- 你想知道系统现在到底有哪些 Skill，不想直接翻代码
- 你准备训练一个新 case，想先判断应该落到哪个 Skill

我不建议把它当成“名字目录”看。更实用的看法是：这里是一张能力地图，告诉你哪些 Skill 已经比较能打，哪些还只是占位或启发式阶段。

### 先看成熟度，而不是先看数量

现在 Skill 多了以后，一个很容易掉进去的坑是：名字看起来很多，误以为每个都很强。

实际更重要的是：
- 这个 Skill 有没有独立 spec
- 有没有真实 case 训练
- 当前成熟度在哪一档

后面你在 UI 的 `Skill` 页里看到的成熟度和已训练 case 数，和这里的 spec 体系是对应的。
现在还多了一层：
- `规则版`
- `可挂 Agent`

我一般把它理解成“执行方式”，不是成熟度。  
成熟度回答的是这条 Skill 练得够不够；执行方式回答的是它到底走纯规则，还是允许 Agent 在固定模板里增强内容。

### 当前比较值得优先信任的 Skill

这几条现在更成熟，后面做 case 时优先往它们上面叠：

- [megaeth.host.baseline_compliance_analysis](../skill_specs/megaeth.host.baseline_compliance_analysis.md)
- [megaeth.endpoint.process_anomaly](../skill_specs/megaeth.endpoint.process_anomaly.md)
- [megaeth.appsec.whitebox_report_synthesis](../skill_specs/megaeth.appsec.whitebox_report_synthesis.md)

第一条已经有完整 case 001，第二条是当前 endpoint 线里最稳的一条，第三条是后面 AppSec 训练的主要承接位。

### 按模块看 Skill

#### CI/CD

- [megaeth.cicd.pr_security_review](../skill_specs/megaeth.cicd.pr_security_review.md)
- [megaeth.cicd.secret_detection](../skill_specs/megaeth.cicd.secret_detection.md)

#### Endpoint

- [megaeth.endpoint.process_anomaly](../skill_specs/megaeth.endpoint.process_anomaly.md)

#### Host

- [megaeth.host.baseline_compliance_analysis](../skill_specs/megaeth.host.baseline_compliance_analysis.md)
- [megaeth.host.integrity_monitor](../skill_specs/megaeth.host.integrity_monitor.md)
- [megaeth.host.systemd_service_risk](../skill_specs/megaeth.host.systemd_service_risk.md)
- [megaeth.host.binary_tamper_review](../skill_specs/megaeth.host.binary_tamper_review.md)

#### Cloud

- [megaeth.cloud.config_audit](../skill_specs/megaeth.cloud.config_audit.md)
- [megaeth.cloud.identity_surface](../skill_specs/megaeth.cloud.identity_surface.md)

#### AppSec

- [megaeth.appsec.whitebox_recon](../skill_specs/megaeth.appsec.whitebox_recon.md)
- [megaeth.appsec.whitebox_exploit_validation](../skill_specs/megaeth.appsec.whitebox_exploit_validation.md)
- [megaeth.appsec.whitebox_report_synthesis](../skill_specs/megaeth.appsec.whitebox_report_synthesis.md)

#### EASM

- [megaeth.easm.asset_discovery](../skill_specs/megaeth.easm.asset_discovery.md)
- [megaeth.easm.service_scan](../skill_specs/megaeth.easm.service_scan.md)
- [megaeth.easm.tls_analysis](../skill_specs/megaeth.easm.tls_analysis.md)
- [megaeth.easm.vulnerability_scan](../skill_specs/megaeth.easm.vulnerability_scan.md)
- [megaeth.easm.external_intelligence](../skill_specs/megaeth.easm.external_intelligence.md)

#### Key

- [megaeth.key.kms_risk](../skill_specs/megaeth.key.kms_risk.md)
- [megaeth.key.private_key_exposure](../skill_specs/megaeth.key.private_key_exposure.md)

#### Identity

- [megaeth.identity.policy_risk_analysis](../skill_specs/megaeth.identity.policy_risk_analysis.md)
- [megaeth.identity.anomalous_access_review](../skill_specs/megaeth.identity.anomalous_access_review.md)
- [megaeth.identity.jumpserver_command_review](../skill_specs/megaeth.identity.jumpserver_command_review.md)
- [megaeth.identity.jumpserver_transfer_review](../skill_specs/megaeth.identity.jumpserver_transfer_review.md)
- [megaeth.identity.jumpserver_operation_review](../skill_specs/megaeth.identity.jumpserver_operation_review.md)
- [megaeth.identity.jumpserver_multi_source_review](../skill_specs/megaeth.identity.jumpserver_multi_source_review.md)

### 我一般怎么判断一个 case 该落哪条 Skill

我常用的判断方式是：

1. 先看材料主语是什么
   - 主机
   - 端点
   - 外部暴露
   - 身份 / 策略
2. 再看系统希望输出什么
   - 资产画像
   - 异常行为
   - 基线缺口
   - 综合报告
3. 最后再决定是落到已有 Skill 还是补一个新 Skill

这样做能避免“其实该扩展现有 Skill，却又新建一个名字很像的 Skill”。

### 这份文档和 `skill_specs/` 的关系

这里是索引层。真正要改行为，还是去改具体 spec：
- 触发线索
- 输入特征
- finding 类型
- 风险语义
- 报告风格
- 当前限制

所以如果你问“Skill 够不够专业”，真正答案不在这张索引表里，而在每个 spec 写得是否扎实、是否绑定真实 case。

---

## English Version

This document is most useful in two moments:
- you want to know what Skills already exist without opening code first
- you are about to train a new case and want to decide where it should land

I do not recommend reading it as a name directory. It is more useful as a capability map that tells you which Skills are already dependable and which ones are still placeholders or heuristic-stage.

### Look at maturity before quantity

Now that the number of Skills has grown, one trap becomes very common: there are many names, so it is easy to assume every Skill is strong.

What matters more is:
- does it have its own spec
- has it been trained with real cases
- what maturity level is it at

The maturity and trained-case indicators in the UI are meant to reflect this layer.

### Skills I currently trust the most

These are the ones I would build on first:

- [megaeth.host.baseline_compliance_analysis](../skill_specs/megaeth.host.baseline_compliance_analysis.md)
- [megaeth.endpoint.process_anomaly](../skill_specs/megaeth.endpoint.process_anomaly.md)
- [megaeth.appsec.whitebox_report_synthesis](../skill_specs/megaeth.appsec.whitebox_report_synthesis.md)

The first already has a stable real case behind it. The second is the strongest current endpoint path. The third is where upcoming AppSec synthesis work should accumulate.

### Skills by module

#### CI/CD

- [megaeth.cicd.pr_security_review](../skill_specs/megaeth.cicd.pr_security_review.md)
- [megaeth.cicd.secret_detection](../skill_specs/megaeth.cicd.secret_detection.md)

#### Endpoint

- [megaeth.endpoint.process_anomaly](../skill_specs/megaeth.endpoint.process_anomaly.md)

#### Host

- [megaeth.host.baseline_compliance_analysis](../skill_specs/megaeth.host.baseline_compliance_analysis.md)
- [megaeth.host.integrity_monitor](../skill_specs/megaeth.host.integrity_monitor.md)
- [megaeth.host.systemd_service_risk](../skill_specs/megaeth.host.systemd_service_risk.md)
- [megaeth.host.binary_tamper_review](../skill_specs/megaeth.host.binary_tamper_review.md)

#### Cloud

- [megaeth.cloud.config_audit](../skill_specs/megaeth.cloud.config_audit.md)
- [megaeth.cloud.identity_surface](../skill_specs/megaeth.cloud.identity_surface.md)

#### AppSec

- [megaeth.appsec.whitebox_recon](../skill_specs/megaeth.appsec.whitebox_recon.md)
- [megaeth.appsec.whitebox_exploit_validation](../skill_specs/megaeth.appsec.whitebox_exploit_validation.md)
- [megaeth.appsec.whitebox_report_synthesis](../skill_specs/megaeth.appsec.whitebox_report_synthesis.md)

#### EASM

- [megaeth.easm.asset_discovery](../skill_specs/megaeth.easm.asset_discovery.md)
- [megaeth.easm.service_scan](../skill_specs/megaeth.easm.service_scan.md)
- [megaeth.easm.tls_analysis](../skill_specs/megaeth.easm.tls_analysis.md)
- [megaeth.easm.vulnerability_scan](../skill_specs/megaeth.easm.vulnerability_scan.md)
- [megaeth.easm.external_intelligence](../skill_specs/megaeth.easm.external_intelligence.md)

#### Key

- [megaeth.key.kms_risk](../skill_specs/megaeth.key.kms_risk.md)
- [megaeth.key.private_key_exposure](../skill_specs/megaeth.key.private_key_exposure.md)

#### Identity

- [megaeth.identity.policy_risk_analysis](../skill_specs/megaeth.identity.policy_risk_analysis.md)
- [megaeth.identity.anomalous_access_review](../skill_specs/megaeth.identity.anomalous_access_review.md)
- [megaeth.identity.jumpserver_command_review](../skill_specs/megaeth.identity.jumpserver_command_review.md)
- [megaeth.identity.jumpserver_transfer_review](../skill_specs/megaeth.identity.jumpserver_transfer_review.md)
- [megaeth.identity.jumpserver_operation_review](../skill_specs/megaeth.identity.jumpserver_operation_review.md)

### How I decide where a new case should land

My usual rule is:

1. identify the main subject
   - host
   - endpoint
   - external exposure
   - identity / policy
2. identify the intended output
   - asset picture
   - anomaly analysis
   - baseline gap
   - synthesis report
3. decide whether to extend an existing Skill or create a new one

That avoids creating redundant Skill names when an existing Skill should simply be strengthened.

### How this file relates to `skill_specs/`

This file is the index layer. Real behavior lives in the per-Skill specs:
- trigger signals
- input patterns
- finding types
- risk semantics
- report style
- current limits

So if the question is “are the Skills actually professional enough,” the real answer lives in the specs and the linked real cases, not in this index alone.
