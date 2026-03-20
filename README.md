# MegaETH AI Security Platform

## 中文版

这一套东西可以直接理解成：把安全材料丢进来，系统帮你做归一化、分流、调用对应 Skill，然后给出中文安全报告。它现在最适合拿来做两件事，一是日常把零散日志、CSV、报表拉进来统一看，二是按真实 case 一条一条把分析能力训练扎实。

我一般会先把它当成“可训练的安全工作台”，而不是标准产品。这样心态会比较对：先跑起来，先验证链路，再去抠报告质量和 Skill 深度。之前踩过的坑也基本都在文档里补上了，尤其是服务启动、文档同步、训练 case 落地这三件事。

### 快速开始

下面这条是最小可运行路径，照着跑基本就能起来：

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./start.sh
```

这几步分别是：
- 进入项目目录
- 准备独立 Python 环境，避免污染系统环境
- 激活虚拟环境
- 安装运行依赖
- 后台启动服务

默认地址：
- [http://127.0.0.1:8010](http://127.0.0.1:8010)

如果你已经确认这套服务要长期放在这台 Mac 上，我一般会顺手把开机自启一起装了，不然后面电脑一重启就会忘记拉服务：

```bash
./scripts/install_launch_agent.sh
```

这一步是把服务注册成当前用户登录后自动启动。以后重启电脑，只要登录系统，`8010` 就会自己回来。

如果你只是想确认服务活着，可以直接跑：

```bash
curl http://127.0.0.1:8010/health
```

正常会返回：

```json
{"status":"ok"}
```

停服务：

```bash
PORT=8010 ./stop.sh
```

如果后面不想继续自动启动了：

```bash
./scripts/uninstall_launch_agent.sh
```

换端口启动：

```bash
PORT=8011 ./start.sh
```

这里有个我踩过的坑：以前服务是跟着当前会话走的，看起来像是“突然挂了”。现在 `start.sh` 已经改成后台托管，会在根目录生成：
- `.run-8010.pid`
- `.run-8010.log`

真出问题时，先看日志最省时间：

```bash
tail -n 80 .run-8010.log
```

### 跑起来之后怎么用

最短体验路径我建议这样走：

1. 打开 `Overview`
   这一步是确认系统有没有活着、最近有没有结果、MCP 连没连上。

2. 去 `Intake`
   用一份文本、CSV、日志或者报表试一次 `归一化后分析`。

3. 看右侧三块结果
   - `Agent 决策预览`
   - `归一化结果`
   - `安全报告`

4. 去 `Skill`
   看这次命中的 Skill 是什么、成熟度怎么样、有没有 spec。

5. 去 `Agent 学习`
   看这次有没有形成长期规则，还是只是一次最近学习反馈。

如果你接的是 Bitdefender，一般会这样用：

```text
MCP 页验证连接
-> 看“最新可分析内容”
-> 点“导入最新报表内容”
-> 回到 Intake 看报告
```

这个顺序比在连接页里盯一堆摘要数字更有意义。前面我们已经把那页从“API 调试台”收成了“动作入口”，所以现在最重要的不是设备总数，而是有没有值得导入分析的新内容。

### 当前目录怎么理解

现在目录已经收过一轮，根目录比之前干净很多。真正常用的是这些：

```text
megaeth-ai-security-rebuild/
├── app/              # 后端、前端静态页、核心分析链
├── docs/             # 说明文档、案例索引、工程笔记
├── scripts/          # 归档、发布、后台运行辅助脚本
├── skill_specs/      # 每个 Skill 的独立规格
├── training_cases/   # 已落地 case 和模板
├── tests/            # 回归测试
├── data/             # 本地运行数据和学习记录
├── README.md
├── CHANGELOG.md
├── VERSION
├── start.sh
└── stop.sh
```

我平时最常看的位置是：
- [docs](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/docs)
- [skill_specs](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/skill_specs)
- [training_cases](/Users/lei/Documents/New%20project/megaeth-ai-security-rebuild/training_cases)

### 这套系统现在已经能做什么

别把它理解成“安全大模型前台”，更接近下面这条链：

```text
原始材料 / 外部平台数据
-> MCP 接入或文件解析
-> Agent 归一化和分流
-> Skill 执行
-> 风险判断
-> 中文报告
-> 历史 / 调查 / 学习沉淀
```

目前已经稳定的范围包括：
- 文本输入和文件上传
- `csv / json / log / txt / yaml / yml / md / 文本型 pdf`
- Bitdefender GravityZone MCP 接入
- JumpServer `MCP -> Agent -> Skill` 试点链
  - `MCP` 负责接 4 类 JumpServer 审计文件
  - `Agent` 可在服务端调用模型生成综合结论与综合判断
  - `Skill` 继续约束固定报告结构
- Host baseline case 001
- AppSec whitebox 三段式骨架
- 中英文 UI
- 最近两天历史保留

如果你想把 JumpServer 这条试点真的打开，最少要补一个环境变量：

```bash
export GEMINI_API_KEY=你的服务端key
```

可选项：

```bash
export GEMINI_MODEL_JUMPSERVER=gemini-2.5-flash
```

这一步是干嘛的：
- 没有 `GEMINI_API_KEY` 时，JumpServer 仍然能分析，只是综合结论和综合判断继续走本地规则
- 有了 `GEMINI_API_KEY` 时，`megaeth.agent.core` 会在不改结构模板的前提下，帮你把 JumpServer 综合结论和第 7 段写得更贴真实数据

### 如果你要继续训练它

最有效的方式还是一条 case 一条 case 来，不要一上来就想“全自动变聪明”。

当前已经落地的案例：
- [Case 001 - Host Baseline Assessment](./training_cases/case_001_host_baseline/README.md)
- [Case 002 - JumpServer Multi-Source Audit Review](./training_cases/case_002_jumpserver_multisource/README.md)

我后面训练时会默认按这个顺序同步：
- 代码
- 测试
- 对应 Skill spec
- 对应 case 文档
- GitHub

这是前面反复踩坑之后固定下来的，不然很容易出现“代码改了，文档没跟上”或者“本地对了，GitHub 还是旧的”。

### 常见坑

#### 1. 页面看起来没变化

先不要急着怀疑代码没生效，很多次问题都出在静态资源缓存。最省事的做法：

```bash
Cmd + Shift + R
```

如果还是不对，再看页面引用的 `app.js?v=...` 和 `styles.css?v=...` 版本号有没有更新。

#### 2. 服务突然访问不了

现在大概率不是代码坏了，而是本地服务没跑。先查：

```bash
curl http://127.0.0.1:8010/health
tail -n 80 .run-8010.log
```

如果没起来，直接再跑：

```bash
./start.sh
```

#### 3. Bitdefender 数据看着不完整

这个不是你的错，也不一定是我们实现错。当前公开 API 和控制台视图口径并不完全一致，所以不要把“设备总数”当成最重要的信息。更值得看的，是：
- 最新安全报表里有没有新风险
- 有没有值得导入的平台分析内容
- 策略分布和系统分布是不是异常

#### 4. 训练结果没落到文档里

这个以前确实出过问题。现在规则是：一个 case 训完，不只改代码，还要同步到对应 Skill spec 和 case 文档。后面如果你发现哪条 case 在文档里没落地，可以直接当 bug 提。

### 还需要继续看的文档

如果你是第一次接手，我建议按这个顺序看：
- [系统设计与架构](./docs/SYSTEM_DESIGN.md)
- [功能快照](./docs/FEATURE_SNAPSHOT.md)
- [Skill 总索引](./docs/SKILL_LIBRARY.md)
- [Agent / MCP 说明](./docs/AGENT_MCP_LIBRARY.md)
- [案例库](./docs/CASE_LIBRARY.md)
- [训练协作流程](./docs/TRAINING_WORKFLOW.md)

如果你准备跨机器迁移或留运行快照，再看：
- [跨机器迁移](./docs/PORTABLE_TRANSFER.md)
- [发布与归档流程](./docs/RELEASE_PROCESS.md)

---

## English Version

This project is easiest to think of as a trainable security workbench: you feed it logs, CSVs, reports, or external platform data, and it turns them into normalized events, routes them through the right Skills, and produces Chinese-first security reports. The sweet spot right now is practical analysis plus case-by-case training, not abstract platform theory.

I usually treat it as an engineering workbench first. Get it running, validate one real path, then refine report quality and Skill depth. That mindset works much better than expecting a polished product on day one.

### Quick Start

This is the smallest runnable path:

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./start.sh
```

What these steps do:
- enter the project directory
- create an isolated Python environment
- activate it
- install runtime dependencies
- start the local service in the background

Default URL:
- [http://127.0.0.1:8010](http://127.0.0.1:8010)

Health check:

```bash
curl http://127.0.0.1:8010/health
```

Expected response:

```json
{"status":"ok"}
```

Stop the service:

```bash
PORT=8010 ./stop.sh
```

Start on another port:

```bash
PORT=8011 ./start.sh
```

One pitfall we already hit earlier: the service used to die with the shell session. That is fixed now, and `start.sh` writes:
- `.run-8010.pid`
- `.run-8010.log`

When something feels off, check the log before guessing:

```bash
tail -n 80 .run-8010.log
```

### What to do after it starts

The shortest useful walkthrough is:

1. Open `Overview`
   Use it to confirm the platform is alive and recent results exist.

2. Go to `Intake`
   Upload one text, CSV, log, or report and run `Normalize and Analyze`.

3. Read the three result blocks
   - `Agent Decision Preview`
   - `Normalization Summary`
   - `Security Report`

4. Open `Skill`
   Check which Skill was used, how mature it is, and whether a spec exists.

5. Open `Agent Learning`
   See whether the run became a long-lived rule or just a recent learning event.

For Bitdefender, the most practical flow is:

```text
Open MCP
-> verify the connection
-> check whether there is fresh analyzable content
-> import the latest report
-> return to Intake for the actual analysis result
```

That path is much more useful than staring at raw inventory stats.

### Directory layout

The repository has already been cleaned up once. The root now keeps only the files you actually touch often, and the rest lives under `docs/` and `scripts/`.

```text
megaeth-ai-security-rebuild/
├── app/
├── docs/
├── scripts/
├── skill_specs/
├── training_cases/
├── tests/
├── data/
├── README.md
├── CHANGELOG.md
├── VERSION
├── start.sh
└── stop.sh
```

The directories I look at most often are:
- [docs](./docs/)
- [skill_specs](./skill_specs/)
- [training_cases](./training_cases/)

### What the system currently does well

The actual flow is:

```text
raw material / external platform data
-> MCP import or file parsing
-> Agent normalization and routing
-> Skill execution
-> risk judgment
-> report
-> history / investigation / learning
```

Stable areas right now include:
- text input and file upload
- `csv / json / log / txt / yaml / yml / md / text-based pdf`
- Bitdefender GravityZone MCP
- Host baseline case 001
- AppSec whitebox three-stage scaffold
- bilingual UI
- two-day history retention

### If you want to keep training it

The right way is still one case at a time.

Current landed case:
- [Case 001 - Host Baseline Assessment](./training_cases/case_001_host_baseline/README.md)

The sync discipline from now on is:
- code
- tests
- matching Skill spec
- matching case docs
- GitHub

That rule exists because we already hit the opposite failure mode more than once.

### Common pitfalls

#### 1. The page looks unchanged

Very often this is static asset caching, not a failed code change. The fastest check is a hard refresh:

```bash
Cmd + Shift + R
```

If it still looks old, verify the `app.js?v=...` and `styles.css?v=...` versions changed.

#### 2. The service suddenly becomes unreachable

Usually the service is simply not running. Check:

```bash
curl http://127.0.0.1:8010/health
tail -n 80 .run-8010.log
```

Then restart if needed:

```bash
./start.sh
```

#### 3. Bitdefender data looks incomplete

That does not automatically mean the implementation is wrong. The public API view and the control center view do not perfectly match. Treat fresh report content as more important than raw device totals.

#### 4. Training changes are missing in docs

That happened before. The rule now is: a finished case is not done until its Skill spec and case docs are updated too.

### What to read next

If you are onboarding, this order works well:
- [System design](./docs/SYSTEM_DESIGN.md)
- [Feature snapshot](./docs/FEATURE_SNAPSHOT.md)
- [Skill library](./docs/SKILL_LIBRARY.md)
- [Agent / MCP library](./docs/AGENT_MCP_LIBRARY.md)
- [Case library](./docs/CASE_LIBRARY.md)
- [Training workflow](./docs/TRAINING_WORKFLOW.md)

If you are preparing migration or milestone snapshots, also read:
- [Portable transfer](./docs/PORTABLE_TRANSFER.md)
- [Release process](./docs/RELEASE_PROCESS.md)
