
# JumpServer 多源日志训练样本模板 + 增强版结论样本（更新版，含 operate log）

## 0. 更新说明

本次更新基于你重新提供的 `operatelog_2026-03-17_16-15-48.xlsx`。

更新后的判断如下：

1. 这份 `operatelog` **不是之前给过的重复文件**，而是一个新的日志类型。  
2. 当前真正应作为训练输入的 **4 类唯一证据源** 是：
   - 最新登录日志 `userloginlog_2026-03-17_16-17-45.xlsx`
   - 命令审计日志 `command_2026-03-17_15-38-39.xlsx`
   - 文件传输日志 `ftplog_2026-03-17_16-03-23.xlsx`
   - 操作记录日志 `operatelog_2026-03-17_16-15-48.xlsx`
3. 较早的登录日志 `userloginlog_2026-03-17_15-34-48.xlsx` 与最新登录日志属于同一种报表快照，后者多 2 条更新记录。后续不应再把它作为独立证据源重复计数，只保留为补充对照样本。

---

## 1. 目标

这份文档同时包含两部分内容：

1. **标准训练样本模板**  
   用于让 AI 学会如何把 JumpServer 的 4 类日志拼成一条安全判断链。

2. **增强版结论样本**  
   基于本次真实日志生成，适合作为 Codex / AI Skill 的学习材料。

---

## 2. 本次样本对应的 4 类唯一证据源

### 2.1 证据源角色映射（更新后）

| 文件角色 | 实际文件 | 在训练系统中的 source_type | source_role | 主要作用 |
|---|---|---|---|---|
| 登录日志最新快照 | `userloginlog_2026-03-17_16-17-45.xlsx` | `login_auth` | `primary_identity_source` | 提供登录成功/失败、MFA、认证失败原因 |
| 命令审计日志 | `command_2026-03-17_15-38-39.xlsx` | `command_audit` | `primary_behavior_source` | 提供高危命令、会话、账号、资产、输出 |
| 文件传输日志 | `ftplog_2026-03-17_16-03-23.xlsx` | `file_transfer_audit` | `payload_transfer_source` | 提供上传/下载、路径、账号、会话 |
| 操作记录日志 | `operatelog_2026-03-17_16-15-48.xlsx` | `operation_audit` | `control_plane_audit_source` | 提供导出、主机/账号创建、资产授权、节点更新、会话创建等管理平面动作 |

### 2.2 补充参考源

| 文件角色 | 实际文件 | 处理方式 |
|---|---|---|
| 旧登录快照 | `userloginlog_2026-03-17_15-34-48.xlsx` | 仅作补充对照，不作为独立统计来源 |

### 2.3 证据优先级（更新后）

```json
{
  "evidence_priority": {
    "command_audit": "P1",
    "file_transfer_audit": "P1",
    "login_auth": "P2",
    "operation_audit": "P2",
    "login_auth_old_snapshot": "P4"
  }
}
```

解释：

- **P1：命令日志、文件传输日志**  
  最能说明主机侧真实动作与文件投放行为。
- **P2：最新登录日志、操作记录日志**  
  前者用于身份、认证异常与时间线判断；后者用于管理平面动作、导出来源、资产授权和主机/账号创建背景判断。
- **P4：旧登录快照**  
  只作为补充参考，不应重复统计。

---

## 3. 训练样本设计原则（更新后）

1. 不能把 JumpServer 代理地址直接当成真实攻击源。
2. 不能因为出现 `sudo` / `systemctl` 就直接判定入侵。
3. 不能因为出现 `/tmp` 上传和二进制执行就直接判定恶意，但必须判为高风险。
4. 不能直接信任 JumpServer 导出的 `风险等级=接受(0)`。
5. 不能只看单条日志，必须看**登录 -> 传输 -> 提权 -> 执行 -> 服务变更 / 网络测试**的会话链。
6. 当 FTP 会话号和命令会话号无法直接对应时，应优先按：
   - 同用户
   - 同资产
   - 相近时间窗
   - 相同文件名 / 二进制名
   进行关联。
7. 操作记录日志中的 `create / update / export` 属于**管理平面证据**，可用于解释：
   - 主机和账号是否为新接入
   - 资产授权是否刚调整
   - 样本文件是否由管理员导出
   - 会话是否在相近时间被建立
   但它**不能替代主机侧命令执行证据**。
8. 管理平面操作与主机侧高危命令应分开定性：
   - `operation_audit` 更偏向 **高影响管理动作**
   - `command_audit` 更偏向 **主机侧高危执行动作**
9. 对 AI 的训练重点不是“看到了什么单条日志”，而是“哪类证据能证明什么，哪类证据只能做背景支撑”。

---

## 4. 标准训练样本模板（JSON，更新后）

```json
{
  "sample_id": "jumpserver_case_001",
  "case_name": "JumpServer Multi-Source Weekly Audit Review",
  "analysis_scope": {
    "time_range": "",
    "sources": [
      {
        "file_name": "userloginlog_2026-03-17_16-17-45.xlsx",
        "source_type": "login_auth",
        "source_role": "primary_identity_source"
      },
      {
        "file_name": "command_2026-03-17_15-38-39.xlsx",
        "source_type": "command_audit",
        "source_role": "primary_behavior_source"
      },
      {
        "file_name": "ftplog_2026-03-17_16-03-23.xlsx",
        "source_type": "file_transfer_audit",
        "source_role": "payload_transfer_source"
      },
      {
        "file_name": "operatelog_2026-03-17_16-15-48.xlsx",
        "source_type": "operation_audit",
        "source_role": "control_plane_audit_source"
      }
    ],
    "supplemental_sources": [
      {
        "file_name": "userloginlog_2026-03-17_15-34-48.xlsx",
        "source_type": "login_auth",
        "source_role": "supplemental_snapshot_only"
      }
    ]
  },
  "evidence_priority": {
    "command_audit": "P1",
    "file_transfer_audit": "P1",
    "login_auth": "P2",
    "operation_audit": "P2",
    "login_auth_old_snapshot": "P4"
  },
  "field_mapping": {
    "login_auth": {
      "user": "用户名",
      "src_ip": "登录 IP",
      "mfa": "MFA",
      "reason": "原因",
      "reason_desc": "原因描述",
      "auth_token": "认证令牌",
      "auth_method": "认证方式",
      "status": "状态",
      "login_time": "登录日期"
    },
    "command_audit": {
      "user": "用户",
      "asset": "资产",
      "command": "命令",
      "session_id": "会话",
      "account": "账号",
      "output": "输出",
      "event_ts": "时间戳",
      "event_time": "日期",
      "src_ip": "远端地址",
      "native_risk": "风险等级"
    },
    "file_transfer_audit": {
      "user": "用户",
      "asset": "资产",
      "account": "账号",
      "operation": "操作",
      "filename": "文件名",
      "event_time": "开始日期",
      "success": "成功",
      "downloadable": "可下载",
      "session_id": "会话",
      "src_ip": "远端地址"
    },
    "operation_audit": {
      "user": "用户",
      "action": "动作",
      "resource_type": "资源类型",
      "resource": "资源",
      "src_ip": "远端地址",
      "org_name": "组织名称",
      "event_time": "日期"
    }
  },
  "evidence_summary": {
    "login_findings": [],
    "command_findings": [],
    "file_transfer_findings": [],
    "operation_findings": [],
    "evidence_provenance": [],
    "cross_source_correlations": []
  },
  "high_risk_accounts": [
    {
      "user": "",
      "risk_scope": "host_execution | control_plane | mixed",
      "assets": [],
      "risk_actions": [],
      "representative_commands": [],
      "supporting_sources": [],
      "judgement": ""
    }
  ],
  "risk_classification": {
    "overall_level": "",
    "category": "",
    "confidence": "",
    "why_not_direct_intrusion": "",
    "why_still_high_risk": ""
  },
  "final_conclusion": "",
  "recommended_followups": []
}
```

---

## 5. 推荐的自然语言输出模板（更新后）

```text
[案件范围]
本次分析基于 4 类 JumpServer 审计日志：
1. 登录日志
2. 命令审计日志
3. 文件传输日志
4. 操作记录日志

[登录侧结论]
说明成功/失败情况、失败原因、MFA 情况、IP 是否可直接用于攻击源判断。

[命令侧结论]
说明高危命令类型、主要操作账户、主要资产、是否存在提权/服务控制/下载执行/横向移动/权限变更/明文密钥使用。

[文件传输侧结论]
说明是否存在上传到 /tmp、root 账号上传、上传二进制、归档下载、可疑文件投放。

[操作记录侧结论]
说明是否存在：
- 日志导出
- 主机/账号创建
- 资产授权调整
- 节点变更
- 用户会话创建
并说明这些动作对主机侧行为理解的支撑作用。

[跨日志关联结论]
说明是否形成以下链条：
管理平面创建/授权 -> 登录 -> 文件上传 -> 提权 -> 移动/放权 -> 执行 -> 服务变更/网络测试

[重点高危账户汇总]
逐个列出：
- 用户
- 风险范围（主机执行 / 管理平面 / 混合）
- 资产
- 代表命令或动作
- 风险动作
- 判断

[证据来源与导出链]
说明：
- 哪些日志是管理员导出的
- 导出时间是否与本次样本时间吻合
- 哪些证据属于主机侧
- 哪些证据属于管理平面

[综合风险定性]
说明这更像：
- 已确认恶意入侵
- 高风险待复核
- 高风险运维
- 高风险管理平面操作
- 普通运维
- 低风险行为

[判断边界]
明确说明当前不能证明什么，已经足以说明什么。

[建议动作]
说明后续需要补哪些证据或治理动作。
```

---

## 6. 跨源关联模板（更新后）

### 6.1 主机侧高危链模板

```json
{
  "cross_source_correlations": [
    {
      "user": "",
      "asset": "",
      "time_window": "",
      "correlation_chain": [
        "login_success",
        "file_upload",
        "privilege_escalation",
        "chmod_or_move",
        "binary_execution",
        "service_change_or_network_test"
      ],
      "confidence": "",
      "judgement": ""
    }
  ]
}
```

### 6.2 管理平面到主机侧的支撑链模板

```json
{
  "cross_source_correlations": [
    {
      "user": "",
      "resource_or_asset": "",
      "time_window": "",
      "correlation_chain": [
        "host_or_account_create",
        "asset_authorization_update",
        "session_create",
        "login_success",
        "host_command_activity"
      ],
      "confidence": "",
      "judgement": ""
    }
  ]
}
```

### 6.3 证据导出链模板

```json
{
  "evidence_provenance": [
    {
      "export_user": "Administrator(admin)",
      "resource_type": "用户登录日志 | 命令记录 | 文件传输",
      "export_time": "",
      "related_file": "",
      "judgement": "该样本具备明确的导出来源记录"
    }
  ]
}
```

---

## 7. 增强版结论样本（更新后，给 Codex / AI Skill 学习）

下面这版是基于当前 4 类唯一日志源整理出的增强版样本，可直接作为训练目标。

```text
综合结论：

本批 JumpServer 审计样本未发现足以直接判定“外部入侵已成立”的强证据，但已明显暴露出大量高风险运维操作、二进制投放与执行、服务启停、跨主机传输、明文密钥调用，以及管理平面上的主机/账号创建、资产授权调整和日志导出行为。整体风险画像更接近“高权限运维动作密集 + 管理平面高影响变更 + 原始审计标签失真 + 需要会话级复核”的场景，而非已经闭环确认的外部攻击事件。

主要依据如下：

1. 登录侧
- 最新登录快照共 397 条记录，其中成功 336 条，失败 61 条。
- 失败记录主要集中在用户名/密码错误、OTP 失效或无效，未体现明显分布式爆破或多源异常尝试特征。
- 登录失败较多的账户主要包括：
  - abel.chen：28 次
  - william.c：9 次
  - guanghong：6 次
- 登录 IP 基本统一显示为 10.30.0.4，更可能是 JumpServer 代理地址，因此不能直接作为攻击源判断依据。

2. 命令侧
- 命令审计共 10000 条，其中混有大量终端控制字符、tmux 和 Claude/Codex 交互噪声；去噪后可识别有效命令约 4700 条。
- 去噪后反复出现的高风险语义包括：
  - 提权：sudo、sudo su、sudo su -
  - 服务控制：systemctl start / stop / restart / status
  - 删除替换：rm -rf、mv、ln -sf
  - 权限变更：chmod、chown
  - 横向/远程操作：ssh、scp、rsync、telnet、nc
  - 下载执行：curl | bash、wget 下载二进制
  - 本地执行：./binary
  - 明文敏感参数：cast send --private-key ...
- JumpServer 原始风险等级均显示为“接受(0)”，与真实操作风险不匹配，不能作为最终判断依据。

3. 文件传输侧
- 文件传输日志共 9 条。
- 其中最值得关注的是 Yan(wenze.yan) 在 512f(192.168.0.206) 上，以 root 账号向 /tmp 连续上传：
  - /tmp/bft-rpc-client
  - /tmp/inside-rpc-client
  - /tmp/p2p-memberlist-client
- 后续命令日志中可观察到对应的：
  - mv /tmp/... .
  - chmod 0777
  - ./bft-rpc-client
  - ./inside-rpc-client
  - ./p2p-memberlist-client --target ...
- 这已经形成“上传 -> 落地 -> 放权 -> 执行 -> 连通性测试”的高风险操作链。

4. 操作记录侧
- 操作记录日志共 52 条：
  - 创建(create)：34 条
  - 更新(update)：9 条
  - 导出(export)：9 条
- 主要操作者：
  - Administrator(admin)：45 条
  - Feng(liquan.feng)：3 条
  - Zhang(hongbo)：2 条
  - Chen(abel.chen)：1 条
  - Yan(wenze.yan)：1 条
- 资源类型分布：
  - 账号：11
  - 主机：11
  - 用户会话：10
  - 文件传输：6
  - 资产授权：6
  - 节点：3
  - 命令记录：2
  - 用户：2
  - 用户登录日志：1
- 关键管理平面特征包括：
  - 2026/03/17 15:34:49 导出用户登录日志
  - 2026/03/17 15:38:56、15:39:16 导出命令记录
  - 2026/03/17 15:39:58、15:40:05、15:40:23、16:02:39、16:03:11、16:03:24 导出文件传输
  - 2026/03/14 21:43:57 - 22:06:14，Administrator(admin) 批量创建 pnet-runner-0、pnet-tko-seq-0/1/2、pnet-tko-coordinator-0、pnet-tko-opstack-0、pnet-tko-stateless-0、pnet-tko-rpc-0/1、securelink-vcpe-tokyo-tencent、wyman-doc-agent-0 等主机及对应账号
  - 2026/03/15 - 2026/03/16，存在 hongbo、zhuguang(Wyman)、storage-group、developer policy 等资产授权或节点更新
- 这些记录说明：
  - 本次样本具备明确导出来源
  - 部分主机和账号可能是新接入或刚完成授权配置
  - 管理平面变化可以为后续主机命令活动提供背景，但不能替代主机侧执行证据

5. 重点高危操作账户与命令汇总

5.1 Yang(ming.yang)
- 风险范围：主机执行
- 风险特征（去噪后近似统计）：
  - 提权约 61 次
  - 服务控制约 41 次
  - 删除/替换约 24 次
  - 远程/横向操作约 39 次
  - 权限变更约 23 次
- 主要涉及资产：
  - pnet-tko-rpc-1(43.167.223.166)
  - pnet-tko-seq-0(43.133.28.69)
  - gray2-tko-rpc-0(10.40.128.31)
  - pnet-tko-seq-2(101.32.99.137)
  - pnet-runner-0(43.153.183.211)
- 代表命令：
  - sudo su
  - systemctl stop rpc-node
  - systemctl start rpc-node
  - rm -rf db
  - mv db db-bak
  - rsync -av db ubuntu@43.133.28.154:/home/blockchain/
  - scp /opt/megaeth/bin/mega-kailua ubuntu@43.167.214.36:~/
  - chmod 777 /home/blockchain/
  - chown -R rpc-node:rpc-node rpc-node
- 判断：
  更像批量节点修复、热升级、数据迁移或服务切换，而非典型外部攻击者行为；但由于同时出现提权、服务启停、数据目录替换、跨主机同步和权限放开，应定性为“高风险运维会话”。

5.2 Yan(wenze.yan)
- 风险范围：主机执行
- 主要资产：
  - 512f(192.168.0.206)
- 代表动作与命令：
  - 上传 /tmp/bft-rpc-client
  - 上传 /tmp/inside-rpc-client
  - 上传 /tmp/p2p-memberlist-client
  - mv /tmp/bft-rpc-client .
  - chmod 0777 bft-rpc-client
  - ./bft-rpc-client get-leader
  - mv /tmp/inside-rpc-client .
  - chmod 0777 inside-rpc-client
  - ./inside-rpc-client
  - mv /tmp/p2p-memberlist-client .
  - chmod 0777 p2p-memberlist-client
  - ./p2p-memberlist-client --target 152.32.135.103:10002
  - curl -i http://152.32.135.103:8090
  - telnet 118.193.35.157 9605
- 判断：
  这是本批日志中最典型的“文件投放 -> 权限放开 -> 本地执行 -> 网络探测/连通性验证”高风险链条，应直接作为 AI 的重点高风险样本。

5.3 Chen(abel.chen)
- 风险范围：主机执行
- 主要资产：
  - tnet2-tko-stateless-validator-0(10.40.128.12)
- 代表命令：
  - sudo su
  - wget http://transfer.nonprod.megaeth.com/.../megaeth-witness
  - chmod +x megaeth-witness
  - mv megaeth-witness /opt/megaeth/bin/witness-generator-test
  - systemctl stop witness-generator
  - systemctl start witness-generator
  - systemctl stop stateless-validator
  - systemctl start stateless-validator
  - chmod +x test_validator.sh
  - ./test_validator.sh
- 判断：
  这一组行为更接近“内部二进制替换 + 服务重启 + 测试脚本验证”的变更链，属于典型高风险发布/验证操作。

5.4 Chen(achen)
- 风险范围：主机执行
- 风险特征（去噪后近似统计）：
  - 提权约 63 次
  - 下载执行约 14 次
  - 远程/横向操作约 27 次
  - 权限变更约 10 次
- 主要资产：
  - pnet-runner-0(43.153.183.211)
  - pnet-tko-rpc-1(43.167.223.166)
  - pnet-tko-rpc-0(43.133.28.154)
  - pnet-tko-seq-0/1/2
  - pnet-tko-coordinator-0
  - pnet-tko-opstack-0
  - pnet-tko-stateless-0
- 代表命令：
  - sudo su -
  - wget https://cloud.gravityzone.bitdefender.com/.../setup_downloader.tar
  - tar xvf setup_downloader.tar
  - ./installer
  - systemctl restart rpc-node
  - scp -p /tmp/patch.sh ...
  - ssh -q -t $i "sudo bash /tmp/patch.sh"
- 判断：
  该账户的行为更像批量安装安全软件、执行补丁或远程维护，但从审计视角已经具备“跨主机批量分发 + 提权执行 + 服务变更”的特征，应归类为“高风险批量运维链”。

5.5 Zhang(hongbo)
- 风险范围：主机执行 + 管理平面背景
- 风险特征（去噪后近似统计）：
  - 服务控制约 108 次
  - 提权约 35 次
- 主要资产：
  - tnet2-tko-gh-runner-0(10.40.128.2)
  - tnet2-tko-seq-0(10.40.128.17)
  - tnet2-tko-seq-2(10.40.128.16)
  - tnet2-tko-rpc-0(10.40.128.15)
- 代表命令：
  - sudo su
  - ./tools/hot-upgrade-sequencer.sh ...
  - ./tools/hot-upgrade-rpc.sh ...
  - systemctl status mega-reth
  - systemctl status rpc-node
- 管理平面相关动作：
  - 创建用户会话
  - 关联到 hongbo 资产授权调整
- 判断：
  该账户更偏向发布/热升级操作，风险来自 runner 驱动多节点变更和频繁提权，而不是明显的恶意载荷行为，应定性为“高权限发布操作”。

5.6 Cheung(william.c)
- 风险范围：主机执行
- 主要资产：
  - pnet-tko-seq-1(43.153.143.71)
  - pnet-tko-seq-0(43.133.28.69)
- 代表命令：
  - curl -L https://foundry.paradigm.xyz | bash && foundryup
  - cast send --private-key 0x... --gas-limit 1000000 ...
  - export ETH_RPC_URL=http://localhost:9545
- 判断：
  这组行为有两层风险：
  - 供应链风险：通过 curl|bash 直接安装外部组件
  - 凭证暴露风险：在命令行直接使用 `--private-key`
  即使使用的是测试私钥，这种模式也应被 AI 标记为高风险敏感参数暴露。

5.7 Wen(zhuguang)
- 风险范围：主机执行
- 主要资产：
  - wyman-doc-agent-0(10.40.180.11)
- 代表命令：
  - curl -fsSL https://claude.ai/install.sh | bash
  - curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
- 判断：
  这类行为未必恶意，但属于典型“外部脚本直拉直执行”模式，AI 应学会将其标记为“高风险下载执行”，而不是普通安装命令。

5.8 Administrator(admin)
- 风险范围：管理平面
- 关键动作：
  - 导出用户登录日志 / 命令记录 / 文件传输
  - 批量创建主机和账号
  - 更新节点、用户、资产授权
- 判断：
  这是高影响控制平面账户，不体现为主机上的恶意执行，但对资产接入、权限边界、日志流转和证据链完整性有决定性影响。AI 应单独学习“高风险管理平面操作”这一类，不应与主机命令风险混为一谈。

6. 证据来源与导出链
- 操作记录日志明确显示，本次登录日志、命令日志、文件传输日志均由 Administrator(admin) 在 2026/03/17 15:34 - 16:03 期间导出。
- 这意味着：
  - 样本来源链较清晰
  - 日志文件本身具备导出来源佐证
  - 后续训练系统可以把 `operation_audit.export` 作为“证据链完整性”的一个字段学习

7. 综合判断
- 当前最需要 AI 学会区分的，不是“有没有 sudo”，而是：
  - 哪个用户
  - 在哪台资产
  - 执行了哪些高危命令
  - 命令是否与文件传输、登录、管理平面动作串成完整链条
- 本批样本中最典型的训练对象包括：
  1) Yan(wenze.yan) 的 /tmp 二进制上传与执行链
  2) Yang(ming.yang) 的提权 + 服务启停 + 数据目录替换 + 跨主机同步链
  3) Chen(abel.chen) 的内部二进制替换 + 服务重启 + 测试脚本链
  4) Chen(achen) 的多主机安装/补丁分发链
  5) Cheung(william.c) 的 curl|bash + 明文私钥调用链
  6) Administrator(admin) 的高影响管理平面创建/授权/导出链
- 因此，本批样本的最终定性应为：
  “未发现足以直接确认外部入侵成功的证据，但已发现多组需要重点审计和治理的高风险运维操作链，以及高影响管理平面操作。后续应以用户、资产、命令、会话、文件传输和管理平面变更六个维度进行联合判断，而不能仅依赖 JumpServer 原始风险标签。”
```

---

## 8. 最适合让 AI 学会的判断边界（更新后）

```text
1. 不能把 10.30.0.4 直接当成攻击源，它更像 JumpServer 代理地址。
2. 不能因为有 sudo / systemctl 就直接判定入侵，但这些都应进入高风险行为评分。
3. 不能因为有 /tmp 上传和二进制执行就直接判定恶意，但必须判高风险并触发人工复核。
4. 不能直接信任 JumpServer 导出的“接受(0)”。
5. 不能把管理平面 create/update/export 当成主机执行证据，但它们可以解释主机和账号接入、授权和日志导出来源。
6. 不能只看单条日志，必须把登录、命令、文件传输、操作记录拼成完整判断链。
7. `curl | bash`、`wget + installer`、`cast send --private-key` 这类动作应单独作为高风险模式学习。
8. FTP 会话和命令会话不一定一一对应，必要时应按同用户 + 同资产 + 相近时间窗 + 文件名关联。
9. 训练目标不是“自动定罪”，而是“自动给出有边界感的高质量安全定性”。
```

---

## 9. 给 Codex 的最小实现要求（同步更新）

1. 训练模板中必须支持 `operation_audit` 作为第四类正式输入源。  
2. 结论层必须把风险分成：
   - 主机执行风险
   - 管理平面风险
   - 混合风险
3. 输出中必须单独保留：
   - `evidence_provenance`
   - `operation_findings`
4. 对重复快照类文件，必须支持：
   - 自动识别为 `supplemental_snapshot_only`
   - 不重复计数
5. 风险输出中必须支持单独标签：
   - `privilege_escalation`
   - `service_control`
   - `payload_transfer`
   - `download_and_execute`
   - `secret_exposure`
   - `lateral_movement`
   - `control_plane_change`
   - `evidence_export`

---
