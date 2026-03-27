# CI/CD 日志采集与 API 推送规范
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档用于约束 `CI/CD` 相关日志的采集内容、字段要求、格式要求和 API 推送方式，以支持以下 Skill 的分析、训练和报告生成：

- `megaeth.cicd.pr_security_review`
- `megaeth.cicd.secret_detection`

目标不是收集“尽可能多”的日志，而是收集**足以支撑判断的结构化上下文**。

### 2. 适用范围

本规范适用于以下来源：

- GitHub
- GitLab
- Jenkins
- GitHub Actions
- GitLab CI
- ArgoCD
- Harbor
- 其他构建、部署、审查、凭据扫描相关系统

### 3. 必需日志类型

建议优先采集以下三类日志：

1. PR / Merge Request 审查日志
2. Secret / Credential 检测日志
3. Pipeline / Workflow / 部署执行日志

这三类日志齐备后，`CI/CD` 分析链就可以开始稳定运行。

### 4. 日志内容要求

#### 4.1 PR / 代码审查日志

适用于 `megaeth.cicd.pr_security_review`。

最低字段要求：

- `event_id`
- `source_system`
- `repo_name`
- `pr_id` 或 `merge_request_id`
- `title`
- `author`
- `base_branch`
- `head_branch`
- `status`
- `created_at`
- `updated_at`
- `changed_files`
- `patch` 或可替代的 diff 片段
- `commit_ids`

推荐补充字段：

- `review_comments`
- `approvers`
- `labels`
- `pipeline_status`
- `linked_issue`
- `changed_workflows`
- `changed_scripts`
- `changed_secrets_related_files`

设计要求：

- 必须能看出改了哪些文件
- 必须能看出是否涉及工作流、部署脚本、配置或依赖
- 不能只有标题和描述，没有变更内容

#### 4.2 Secret / 凭据检测日志

适用于 `megaeth.cicd.secret_detection`。

最低字段要求：

- `event_id`
- `source_system`
- `repo_name`
- `file_path`
- `line_number`
- `secret_type`
- `matched_value_redacted`
- `rule_id`
- `commit_id`
- `author`
- `timestamp`

推荐补充字段：

- `branch`
- `first_seen_commit`
- `scanner_name`
- `confidence`
- `is_test_value`
- `surrounding_context_redacted`

设计要求：

- 必须保留命中位置
- 必须说明规则类型
- 必须提供脱敏上下文
- 不允许只推送一句“发现 secret”

#### 4.3 Pipeline / Workflow / 部署执行日志

这类日志同时支撑 `pr_security_review` 和 `secret_detection` 的上下文判断。

最低字段要求：

- `event_id`
- `source_system`
- `pipeline_id`
- `workflow_name`
- `job_name`
- `runner`
- `status`
- `trigger_type`
- `trigger_actor`
- `start_time`
- `end_time`
- `environment`

推荐补充字段：

- `artifact_name`
- `deployment_target`
- `script_excerpt_redacted`
- `related_pr_id`
- `related_commit_id`
- `approval_state`

设计要求：

- 必须能判断变更是否进入执行面
- 必须能判断是否影响生产环境
- 最好能保留脚本或关键命令的脱敏片段

### 5. 字段规范要求

所有日志都应满足以下基础要求：

- 每条事件必须有稳定唯一的 `event_id`
- 必须有统一格式的时间戳，推荐 `UTC ISO 8601`
- 必须有 `source_system`
- 必须有事件类型或事件族，例如 `pr_review`、`secret_detection`、`pipeline_run`
- 必须有仓库标识或项目标识
- 敏感值必须脱敏，不能直接推送明文凭据

推荐的公共字段：

- `event_id`
- `source_system`
- `event_family`
- `repo_name`
- `timestamp`
- `environment`
- `severity`
- `raw_ref`

### 6. 格式要求

推荐优先级如下：

1. `JSONL`
2. 批量 `JSON`
3. `CSV`

不推荐：

- 非结构化文本
- 截图
- 邮件正文直接转发
- 手工拼接日志

原因：

- 系统需要做归一化
- 需要做字段映射
- 需要做训练样本沉淀
- 结构化格式的维护成本最低

### 7. API 推送要求

#### 7.1 推送方式

推荐方式：

- `HTTP POST`
- `Content-Type: application/json`
- 支持批量推送

推荐接口路径：

```http
POST /ingest/cicd/events
```

#### 7.2 请求体结构

统一请求体建议如下：

```json
{
  "source_system": "github",
  "event_family": "pr_review",
  "events": [
    {
      "event_id": "pr-12345-20260327-01",
      "repo_name": "megaeth/security-platform",
      "pr_id": 12345,
      "title": "Update deployment workflow and env handling",
      "author": "alice",
      "base_branch": "main",
      "head_branch": "feature/workflow-change",
      "status": "open",
      "created_at": "2026-03-27T08:10:00Z",
      "updated_at": "2026-03-27T08:20:00Z",
      "changed_files": [
        ".github/workflows/deploy.yml",
        "scripts/release.sh"
      ],
      "patch": "redacted diff content",
      "pipeline_status": "success",
      "commit_ids": ["abc123", "def456"]
    }
  ]
}
```

#### 7.3 Secret 日志推送示例

```json
{
  "source_system": "github",
  "event_family": "secret_detection",
  "events": [
    {
      "event_id": "secret-001",
      "repo_name": "megaeth/security-platform",
      "file_path": "config/prod.env",
      "line_number": 18,
      "secret_type": "AWS_ACCESS_KEY",
      "matched_value_redacted": "AKIA************",
      "rule_id": "aws-access-key",
      "commit_id": "abc123",
      "author": "bob",
      "timestamp": "2026-03-27T09:00:00Z"
    }
  ]
}
```

#### 7.4 Pipeline 日志推送示例

```json
{
  "source_system": "github_actions",
  "event_family": "pipeline_run",
  "events": [
    {
      "event_id": "pipeline-20260327-001",
      "repo_name": "megaeth/security-platform",
      "pipeline_id": "gha-99881",
      "workflow_name": "deploy-production",
      "job_name": "deploy",
      "runner": "ubuntu-latest",
      "status": "success",
      "trigger_type": "push",
      "trigger_actor": "alice",
      "start_time": "2026-03-27T09:15:00Z",
      "end_time": "2026-03-27T09:22:00Z",
      "environment": "prod",
      "deployment_target": "k8s-prod-cluster-01",
      "script_excerpt_redacted": "kubectl apply -f ...",
      "related_commit_id": "abc123"
    }
  ]
}
```

### 8. 给运维同事的明确要求

可以直接把以下要求转给运维：

- 日志必须结构化，优先 `JSONL` 或批量 `JSON`
- 每条事件必须带唯一 `event_id`
- 必须带时间戳、来源系统、仓库名、事件类型
- PR 类必须带 diff/patch 或至少变更文件列表
- Secret 类必须带命中位置、规则类型、脱敏上下文
- Pipeline 类必须带 workflow、job、status、environment
- 敏感值必须脱敏，不能推送明文凭据
- 字段命名必须稳定，不能频繁变更
- 同一批次内事件类型尽量一致

### 9. 最小可行接入建议

如果只想尽快把 `CI/CD` 分析先跑起来，建议先提供：

1. `PR / diff / review` 日志
2. `secret_detection` 日志
3. `pipeline_run` 日志

这三类到位后，就可以先支撑：

- PR 安全审查
- 凭据泄露检测
- 变更是否进入执行面的上下文判断

### 10. 验收标准

一份合格的 CI/CD 日志接入至少应满足：

- 单条日志能稳定映射到统一字段
- 同类日志字段稳定
- 能支撑 `pr_security_review`
- 能支撑 `secret_detection`
- 页面与导出报告中的关键信息可复核

---

## English

### 1. Purpose

This document defines the content requirements, field requirements, format requirements, and API push requirements for `CI/CD` log collection so the system can support:

- `megaeth.cicd.pr_security_review`
- `megaeth.cicd.secret_detection`

The goal is not to collect “as many logs as possible,” but to collect **structured context that is sufficient for reviewable judgment**.

### 2. Scope

This specification applies to:

- GitHub
- GitLab
- Jenkins
- GitHub Actions
- GitLab CI
- ArgoCD
- Harbor
- other build, deploy, review, and secret-scanning systems

### 3. Required Log Families

Prioritize these three log families first:

1. PR / Merge Request review logs
2. Secret / credential detection logs
3. Pipeline / workflow / deployment execution logs

Once these three are available, the `CI/CD` analysis chain can start operating reliably.

### 4. Content Requirements

#### 4.1 PR / Code Review Logs

Used primarily by `megaeth.cicd.pr_security_review`.

Minimum required fields:

- `event_id`
- `source_system`
- `repo_name`
- `pr_id` or `merge_request_id`
- `title`
- `author`
- `base_branch`
- `head_branch`
- `status`
- `created_at`
- `updated_at`
- `changed_files`
- `patch` or an equivalent diff excerpt
- `commit_ids`

Recommended additional fields:

- `review_comments`
- `approvers`
- `labels`
- `pipeline_status`
- `linked_issue`
- `changed_workflows`
- `changed_scripts`
- `changed_secrets_related_files`

Design expectations:

- the payload must reveal which files changed
- it must indicate whether workflows, deploy scripts, configs, or dependencies were modified
- title/description alone is insufficient

#### 4.2 Secret / Credential Detection Logs

Used primarily by `megaeth.cicd.secret_detection`.

Minimum required fields:

- `event_id`
- `source_system`
- `repo_name`
- `file_path`
- `line_number`
- `secret_type`
- `matched_value_redacted`
- `rule_id`
- `commit_id`
- `author`
- `timestamp`

Recommended additional fields:

- `branch`
- `first_seen_commit`
- `scanner_name`
- `confidence`
- `is_test_value`
- `surrounding_context_redacted`

Design expectations:

- hit location must be preserved
- rule type must be preserved
- a redacted context excerpt should be included
- a generic “secret found” event is not sufficient

#### 4.3 Pipeline / Workflow / Deployment Logs

These logs provide shared execution context for both `pr_security_review` and `secret_detection`.

Minimum required fields:

- `event_id`
- `source_system`
- `pipeline_id`
- `workflow_name`
- `job_name`
- `runner`
- `status`
- `trigger_type`
- `trigger_actor`
- `start_time`
- `end_time`
- `environment`

Recommended additional fields:

- `artifact_name`
- `deployment_target`
- `script_excerpt_redacted`
- `related_pr_id`
- `related_commit_id`
- `approval_state`

Design expectations:

- it must be possible to tell whether a change reached the execution surface
- it must be possible to tell whether production was affected
- redacted script or command excerpts are highly useful

### 5. Common Field Requirements

All logs should satisfy the following:

- every event must have a stable unique `event_id`
- timestamps should use a consistent format, preferably `UTC ISO 8601`
- every event should include `source_system`
- every event should include an event family such as `pr_review`, `secret_detection`, or `pipeline_run`
- repository or project identity must be present
- secrets must be redacted before delivery

Recommended common fields:

- `event_id`
- `source_system`
- `event_family`
- `repo_name`
- `timestamp`
- `environment`
- `severity`
- `raw_ref`

### 6. Format Requirements

Recommended priority order:

1. `JSONL`
2. batch `JSON`
3. `CSV`

Not recommended:

- unstructured text
- screenshots
- forwarded email bodies
- manually concatenated logs

Why:

- the system needs normalization
- field mapping must be stable
- training samples must be retained
- structured formats are the lowest-maintenance option

### 7. API Push Requirements

#### 7.1 Delivery Method

Recommended method:

- `HTTP POST`
- `Content-Type: application/json`
- support batched delivery

Recommended endpoint shape:

```http
POST /ingest/cicd/events
```

#### 7.2 Common Request Body

Recommended request structure:

```json
{
  "source_system": "github",
  "event_family": "pr_review",
  "events": [
    {
      "event_id": "pr-12345-20260327-01",
      "repo_name": "megaeth/security-platform",
      "pr_id": 12345,
      "title": "Update deployment workflow and env handling",
      "author": "alice",
      "base_branch": "main",
      "head_branch": "feature/workflow-change",
      "status": "open",
      "created_at": "2026-03-27T08:10:00Z",
      "updated_at": "2026-03-27T08:20:00Z",
      "changed_files": [
        ".github/workflows/deploy.yml",
        "scripts/release.sh"
      ],
      "patch": "redacted diff content",
      "pipeline_status": "success",
      "commit_ids": ["abc123", "def456"]
    }
  ]
}
```

#### 7.3 Secret Event Example

```json
{
  "source_system": "github",
  "event_family": "secret_detection",
  "events": [
    {
      "event_id": "secret-001",
      "repo_name": "megaeth/security-platform",
      "file_path": "config/prod.env",
      "line_number": 18,
      "secret_type": "AWS_ACCESS_KEY",
      "matched_value_redacted": "AKIA************",
      "rule_id": "aws-access-key",
      "commit_id": "abc123",
      "author": "bob",
      "timestamp": "2026-03-27T09:00:00Z"
    }
  ]
}
```

#### 7.4 Pipeline Event Example

```json
{
  "source_system": "github_actions",
  "event_family": "pipeline_run",
  "events": [
    {
      "event_id": "pipeline-20260327-001",
      "repo_name": "megaeth/security-platform",
      "pipeline_id": "gha-99881",
      "workflow_name": "deploy-production",
      "job_name": "deploy",
      "runner": "ubuntu-latest",
      "status": "success",
      "trigger_type": "push",
      "trigger_actor": "alice",
      "start_time": "2026-03-27T09:15:00Z",
      "end_time": "2026-03-27T09:22:00Z",
      "environment": "prod",
      "deployment_target": "k8s-prod-cluster-01",
      "script_excerpt_redacted": "kubectl apply -f ...",
      "related_commit_id": "abc123"
    }
  ]
}
```

### 8. What to Ask Operations To Provide

You can send the following requirements directly to the operations team:

- logs must be structured, preferably `JSONL` or batched `JSON`
- each event must contain a unique `event_id`
- each event must include timestamp, source system, repository name, and event family
- PR events must include diff/patch or at least changed-file lists
- secret events must include hit location, rule type, and redacted context
- pipeline events must include workflow, job, status, and environment
- secrets must be redacted; plaintext credentials must never be pushed
- field names must remain stable over time
- batched pushes should preferably keep one event family per batch

### 9. Minimum Viable Integration

If the goal is to get `CI/CD` analysis running quickly, start with:

1. `PR / diff / review` logs
2. `secret_detection` logs
3. `pipeline_run` logs

These three log families are enough to support:

- PR security review
- secret exposure detection
- execution-surface context for code changes

### 10. Acceptance Criteria

A CI/CD log integration is acceptable only when:

- each event type maps cleanly into the normalized field model
- fields are stable within each event family
- the logs are sufficient for `pr_security_review`
- the logs are sufficient for `secret_detection`
- key evidence remains reviewable in both UI and exported report
