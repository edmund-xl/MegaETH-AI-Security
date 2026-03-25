# Case 002：JumpServer 多源综合审计
<!-- security-log-analysis mainline -->

## 1. 案例目的

本案例用于训练系统将 JumpServer 的登录、命令、文件传输和操作记录联合起来，输出一份固定结构的中文综合审计报告。

## 2. 分类目标

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

单文件进入时，可先识别为：

- `login_auth_review`
- `jumpserver_command_review`
- `jumpserver_transfer_review`
- `jumpserver_operation_review`

同批次多文件时，应额外生成综合结果。

## 3. 对应 Skill

- 主 Skill：`megaeth.identity.jumpserver_multi_source_review`
- 单文件支撑 Skill：
  - `megaeth.identity.anomalous_access_review`
  - `megaeth.identity.jumpserver_command_review`
  - `megaeth.identity.jumpserver_transfer_review`
  - `megaeth.identity.jumpserver_operation_review`

## 4. 训练重点

- 不把代理地址直接当作攻击源
- 不因为单条 `sudo` 或 `systemctl` 直接判定入侵
- 识别“上传 -> 放权 -> 执行 -> 服务变更 / 网络验证”这类高风险链
- 固定报告结构与判断边界

## 5. 参考资产

- [jumpserver_training_template_and_enhanced_conclusion.md](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases/case_002_jumpserver_multisource/jumpserver_training_template_and_enhanced_conclusion.md)

## 6. 报告结构要求

固定输出结构如下：

- `综合结论`
- `主要依据如下`
  - 登录侧
  - 命令侧
  - 文件传输侧
  - 操作记录侧
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`

## 7. 维护要求

未来新增 JumpServer 样本时，应优先对齐本案例，不得擅自缩短固定模板或改变判断边界。
