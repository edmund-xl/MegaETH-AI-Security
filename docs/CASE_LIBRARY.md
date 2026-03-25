# 案例库
<!-- security-log-analysis mainline -->

## 1. 文档目的

本文档列出当前已落地的训练案例、模板案例和它们对应的 Skill，作为样本驱动开发的索引入口。

## 2. 已落地案例

### 2.1 Case 001 - Host Baseline

- 路径：[/Users/lei/Documents/New project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/README.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_001_host_baseline/README.md)
- 目标域：Host
- 主要 Skill：
  - `megaeth.host.baseline_compliance_analysis`
  - `megaeth.host.integrity_monitor`
- 主要目标：
  - 基线缺口识别
  - 风险分层
  - 合规与修复建议输出

### 2.2 Case 002 - JumpServer Multi-Source

- 路径：[/Users/lei/Documents/New project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/README.md)
- 目标域：Identity / JumpServer
- 主要 Skill：
  - `megaeth.identity.jumpserver_multi_source_review`
- 主要目标：
  - 多源日志关联
  - 高风险运维链识别
  - 固定结构中文综合报告

## 3. 模板案例

### 3.1 Whitebox AppSec 模板

- 路径：[/Users/lei/Documents/New project/megaeth-ai-security-rebuild/training_cases/templates/appsec_whitebox_case_template/README.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/templates/appsec_whitebox_case_template/README.md)
- 对应 Skill：
  - `megaeth.appsec.whitebox_recon`
  - `megaeth.appsec.whitebox_exploit_validation`
  - `megaeth.appsec.whitebox_report_synthesis`
- 主要用途：
  - 承接未来白盒侦察、验证、综合报告类案例

## 4. 案例接入要求

新增案例时至少应补齐：

- 原始材料解释
- 目标输出样式
- 系统规则
- 归属 Skill
- 预期分类与风险边界

## 5. 维护要求

- 案例必须与对应 Skill 形成回写关系
- 案例文档必须与系统当前行为保持一致
- 同一主题的新案例应优先叠加到已有 Skill，而不是散落出新规则
