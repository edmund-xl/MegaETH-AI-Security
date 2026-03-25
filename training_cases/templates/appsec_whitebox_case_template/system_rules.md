# Whitebox AppSec 系统规则模板
<!-- security-log-analysis mainline -->

## 1. 分类规则

- 侦察类样本 -> `whitebox_recon_assessment`
- 验证类样本 -> `whitebox_exploit_validation`
- 综合报告类样本 -> `whitebox_security_report`

## 2. 技能规则

- `whitebox_recon_assessment` -> `megaeth.appsec.whitebox_recon`
- `whitebox_exploit_validation` -> `megaeth.appsec.whitebox_exploit_validation`
- `whitebox_security_report` -> `megaeth.appsec.whitebox_report_synthesis`

## 3. 报告规则

- 输出必须贴近目标报告示例
- 不得混淆侦察线索、已确认问题和综合治理建议
