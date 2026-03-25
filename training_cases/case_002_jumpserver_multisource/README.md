# Case 002：JumpServer 多源综合审计
<!-- security-log-analysis mainline -->

## 中文

### 1. 案例目的

本案例用于训练系统把 JumpServer 的登录、命令、文件传输和管理平面记录联合起来，输出一份固定结构的中文综合审计报告。

它是当前主线里最典型的“多文件综合链”案例之一，用来验证：

- 单文件与综合 Skill 的边界
- 多文件聚合是否正确
- 综合判断是否仍然保留事实边界
- 页面和下载报告是否结构一致

### 2. 适用范围

本案例适用于：

- 同批次 JumpServer 登录审计
- 命令审计
- 文件传输审计
- 管理平面操作记录

不适用于：

- 单一文件的独立审计验证
- 非 JumpServer 域材料

### 3. 分类目标

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

### 4. 对应 Skill

- `megaeth.identity.jumpserver_multi_source_review`
- `megaeth.identity.anomalous_access_review`
- `megaeth.identity.jumpserver_command_review`
- `megaeth.identity.jumpserver_transfer_review`
- `megaeth.identity.jumpserver_operation_review`

### 5. 样本应训练系统学会什么

本案例的核心不在单条日志解释，而在跨文件综合判断。系统应学会：

- 正确识别登录、命令、文件传输、管理平面四类材料
- 先做单文件分析，再做综合事件生成
- 将同一用户、同一资产和连续动作串成操作链
- 在不越界的前提下输出综合判断

### 6. 固定报告结构

本案例的综合报告必须保持固定结构：

- `综合结论`
- `主要依据如下`
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`

### 7. 训练重点

- 多文件归并必须基于完整数据
- 不能把预览裁剪误带入分析链
- 不能把旧对象模板和新模板混用
- Gemini 如参与增强，只能增强允许增强的综合段落

### 8. 常见失败模式

本案例历史上最容易出错的地方包括：

- 表头异常导致字段取空
- 大文件被裁剪成前几百行
- 单文件误挂综合 Skill
- 页面正确但下载报告仍旧缺段
- Gemini 触发了，但喂入摘要本身有偏差

### 9. 完成标准

本案例训练完成的最低标准是：

- 四类输入都识别正确
- 单文件 Skill 和综合 Skill 路由正确
- 综合报告结构固定且完整
- 页面版与下载版一致
- 文档、训练案例和实现同步更新

---

## English

### 1. Case Purpose

This case trains the system to combine JumpServer login, command, file-transfer, and control-plane records into a fixed-structure Chinese composite audit report.

It is one of the clearest examples of the current multi-file composite path and validates:

- the boundary between single-source and composite Skills
- correct multi-file aggregation
- composite judgment that remains fact-bounded
- structural consistency between page and export reports

### 2. Scope

This case applies to same-batch JumpServer:

- login audit
- command audit
- file-transfer audit
- control-plane activity

It does not apply to:

- standalone single-file review
- non-JumpServer material

### 3. Target Classification

- `source_type = jumpserver`
- `event_type = jumpserver_multi_source_audit`

### 4. Owning Skills

- `megaeth.identity.jumpserver_multi_source_review`
- `megaeth.identity.anomalous_access_review`
- `megaeth.identity.jumpserver_command_review`
- `megaeth.identity.jumpserver_transfer_review`
- `megaeth.identity.jumpserver_operation_review`

### 5. What the System Should Learn

The core of this case is cross-file synthesis, not line-by-line explanation. The system should learn to:

- recognize the four JumpServer source types
- perform single-source analysis before composite event generation
- chain user, asset, and sequential actions together
- output bounded composite judgment without overreach

### 6. Fixed Report Structure

The composite report must preserve this structure:

- `综合结论`
- `主要依据如下`
- `重点高危操作账户与命令汇总`
- `证据来源与导出链`
- `综合判断`

### 7. Training Focus

- aggregation must use full data, not preview slices
- old templates must not leak into composite outputs
- single-source files must not be routed directly to the composite Skill
- Gemini may only enhance explicitly allowed narrative sections

### 8. Common Failure Modes

Historically common failures include:

- header issues producing empty fields
- large files being truncated
- single-source files being misrouted to the composite Skill
- page and export reports drifting apart
- Gemini receiving distorted summaries

### 9. Completion Criteria

This case is complete only when:

- all four inputs are recognized correctly
- single-source and composite Skills are routed correctly
- the composite report structure is complete and stable
- page and export versions match
- docs, training cases, and implementation are updated together
