# Whitebox AppSec 案例模板
<!-- security-log-analysis mainline -->

## 1. 模板目的

本模板用于承接未来白盒应用安全样本，使 AppSec 训练案例具备统一目录结构、统一目标输出与统一规则沉淀方式。

## 2. 推荐目录内容

- `sample_interpretation.md`：样本解释
- `target_report.md`：目标报告样式
- `system_rules.md`：系统规则
- `notes.md`：补充说明（可选）

## 3. 对应 Skill

- `megaeth.appsec.whitebox_recon`
- `megaeth.appsec.whitebox_exploit_validation`
- `megaeth.appsec.whitebox_report_synthesis`

## 4. 使用要求

每个新白盒样本至少应明确：

- 属于侦察、验证还是综合报告阶段
- 期望命中的 Skill
- 正确的风险语义
- 目标输出结构与判断边界
