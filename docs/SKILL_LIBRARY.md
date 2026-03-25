# Skill 能力库
<!-- security-log-analysis mainline -->

## 1. 文档目的

本文档提供当前主线所有 Skill 的索引、模块归属与规格说明入口。

## 2. 模块视图

### 2.1 CI/CD

- [megaeth.cicd.pr_security_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.cicd.pr_security_review.md)
- [megaeth.cicd.secret_detection](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.cicd.secret_detection.md)

### 2.2 Endpoint

- [megaeth.endpoint.process_anomaly](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.endpoint.process_anomaly.md)

### 2.3 Host

- [megaeth.host.baseline_compliance_analysis](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.host.baseline_compliance_analysis.md)
- [megaeth.host.integrity_monitor](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.host.integrity_monitor.md)
- [megaeth.host.systemd_service_risk](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.host.systemd_service_risk.md)
- [megaeth.host.binary_tamper_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.host.binary_tamper_review.md)

### 2.4 Cloud

- [megaeth.cloud.config_audit](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.cloud.config_audit.md)
- [megaeth.cloud.identity_surface](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.cloud.identity_surface.md)

### 2.5 AppSec

- [megaeth.appsec.whitebox_recon](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.appsec.whitebox_recon.md)
- [megaeth.appsec.whitebox_exploit_validation](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.appsec.whitebox_exploit_validation.md)
- [megaeth.appsec.whitebox_report_synthesis](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.appsec.whitebox_report_synthesis.md)

### 2.6 EASM

- [megaeth.easm.asset_discovery](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.easm.asset_discovery.md)
- [megaeth.easm.external_intelligence](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.easm.external_intelligence.md)
- [megaeth.easm.service_scan](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.easm.service_scan.md)
- [megaeth.easm.tls_analysis](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.easm.tls_analysis.md)
- [megaeth.easm.vulnerability_scan](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.easm.vulnerability_scan.md)

### 2.7 Identity

- [megaeth.identity.anomalous_access_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.identity.anomalous_access_review.md)
- [megaeth.identity.policy_risk_analysis](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.identity.policy_risk_analysis.md)
- [megaeth.identity.jumpserver_command_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.identity.jumpserver_command_review.md)
- [megaeth.identity.jumpserver_transfer_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.identity.jumpserver_transfer_review.md)
- [megaeth.identity.jumpserver_operation_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.identity.jumpserver_operation_review.md)
- [megaeth.identity.jumpserver_multi_source_review](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.identity.jumpserver_multi_source_review.md)

### 2.8 Key Security

- [megaeth.key.kms_risk](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.key.kms_risk.md)
- [megaeth.key.private_key_exposure](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs/megaeth.key.private_key_exposure.md)

## 3. 阅读顺序建议

如果需要快速理解当前主线能力，建议优先阅读：

- Host baseline 相关 Skill
- Endpoint 相关 Skill
- JumpServer 相关 Skill
- Whitebox AppSec 相关 Skill

## 4. 管理原则

- 规格说明是行为边界的正式来源
- 训练案例是 Skill 的落地佐证
- 当系统行为发生显著变化时，应同步更新对应 Skill 规格说明
