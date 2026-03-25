// Security-log-analysis mainline frontend runtime.
const i18n = {
  zh: {
    brandTitle: "AI 安全平台",
    brandCopy: "统一接收安全材料，由系统自动完成归一化、能力决策、风险判断和持续学习。",
    heroEyebrow: "MegaETH 安全平台",
    systemStatus: "系统状态",
    checking: "检查中...",
    refresh: "刷新",
    refreshing: "刷新中...",
    refreshed: "已更新",
    retry: "重试",
    viewMeta: {
      overview: ["概览", "集中查看平台运行状态、最近分析结论和沉淀下来的调查记录。"],
      intake: ["输入", "从统一入口提交材料，让系统自动完成整理、判断和报告输出。"],
      skills: ["技能", "按模块查看平台已经接入的分析能力单元，以及它们当前负责的方向。"],
      integrations: ["连接", "在这里管理外部安全平台连接层，把资产、终端、报表和事件入口带入系统工作流。"],
      memory: ["学习", "查看系统已经学会的分类经验，并把新的判断继续沉淀下来。"],
    },
    sidebarCopy: {
      overview: "先看系统是否真的在处理事件，再看最近报告、调查和沉淀记录。",
      intake: "从这里提交文件或原始材料，系统会自动归一化、分配技能并生成分析报告。",
      skills: "这里看平台已经接入哪些分析能力，以及每个模块当前覆盖了多少分析引擎。",
      integrations: "这里是外部平台连接层。当前 Bitdefender 已接入可直接使用的资产清单、终端列表和报表目录链路。",
      memory: "这里是系统学习层。每次你确认正确分类后，都可以在这里让系统学会。",
    },
    ui: {
      overviewTitle: "平台概览",
      reportsTitle: "近期报告",
      investigationsTitle: "调查会话",
      historyTitle: "历史记录",
      bitdefenderTitle: "Bitdefender 连接",
      bitdefenderCopy: "这里接入的是 Bitdefender GravityZone 连接层。当前更适合直接查看终端与资产覆盖情况，并把最新安全报表导入平台分析。",
      bitdefenderImportNote: "读取结果会留在当前页面；导入到平台的结果请到“输入”页面查看。",
      intakeInputTitle: "统一输入",
      uploadFiles: "上传文件",
      analyze: "归一化后分析",
      plannerTitle: "系统决策预览",
      normalizeTitle: "归一化结果",
      reportTitle: "安全报告",
      learnCorrect: "这次分类正确，记住它",
      learnWrong: "这次分类不对，我来纠正",
      correctionSkills: "选择正确的分析能力",
      saveCorrection: "保存这次纠正",
      fileRunsTitle: "上传执行记录",
      bitdefenderTest: "验证连接",
      bitdefenderNetwork: "读取终端与资产清单",
      bitdefenderImportNetwork: "导入终端资产到平台",
      bitdefenderReports: "读取可用报表目录",
      bitdefenderReportLinks: "获取最新报表下载链接",
      bitdefenderImportLatestReport: "导入最新报表内容",
      bitdefenderImportReports: "导入报表目录元数据",
      bitdefenderWaiting: "等待连接测试。",
      bitdefenderNoData: "还没有 Bitdefender 返回结果。",
      bitdefenderSummaryTitle: "Bitdefender 连接状态",
      bitdefenderClassificationTitle: "设备分类摘要",
      bitdefenderStructureTitle: "设备结构与分类线索",
      bitdefenderEndpointApiNote: "这里显示的是 Bitdefender Network API 当前直接返回的受管终端列表，不等于历史报表里出现过的所有主机。",
      bitdefenderHierarchyEndpointTitle: "全层级设备与分组线索",
      bitdefenderCompaniesTitle: "公司与租户预览",
      bitdefenderCustomGroupsTitle: "自定义分组预览",
      bitdefenderManagedEndpointTitle: "受管设备详情预览",
      bitdefenderLatestReportTitle: "最新安全报表摘要",
      bitdefenderTopHostsTitle: "高频主机",
      bitdefenderTopEventsTitle: "高频事件类型",
      bitdefenderPolicyTitle: "策略分布",
      bitdefenderOsTitle: "系统分布",
      bitdefenderCoverageTitle: "最新可分析内容",
      bitdefenderCoverageGapTitle: "资产可见性差异",
      bitdefenderCoverageGapCopy: "如果安全报表里已经出现大量主机，而 API 列表仍然很少，这更像是可见性缺口，而不是平台里真的没有这些设备。",
      bitdefenderGovernanceHint: "这里优先看策略分布、系统分布和受管情况，用来判断治理覆盖面，而不是追求一个不稳定的总设备数。",
      bitdefenderReportFocusCopy: "这里更适合作为最新安全结论摘要，帮助你快速看出高风险主机和事件集中面。",
      bitdefenderAvailableDataTitle: "当前可用数据类型",
      bitdefenderActionHint: "如果这里已经出现了新的安全报表摘要，就直接点击“导入最新报表内容”进入平台分析。",
      bitdefenderDefaultKeyNotice: "当前由服务端安全配置 Bitdefender 连接，不再在前端暴露 API key。现在更适合读取终端资产、可用报表，以及最新报表的下载入口。",
      integrationsSectionCopy: "这里集中管理外部安全控制台接入。当前已接入 Bitdefender 的资产清单、终端列表、报表目录和报表下载入口，后续还能继续扩展更多平台。",
      bitdefenderAssetNote: "这里更适合看资产覆盖、终端数量和分组线索，而不是把每个列表都当成最终结果页来读。",
      bitdefenderLatestReportHostNote: "如果 API 终端列表是 0，但安全审计报表里已有很多主机，这通常表示公开 Network API 当前没有返回受管终端清单，而不是平台里真的没有主机。",
      installedSkillsTitle: "全部能力",
      skillMatrixTitle: "模块总览",
      memoryLearnTitle: "让系统学习当前结果",
      memoryLearnCopy: "当你确认当前这份材料已经被正确归类后，可以把这次判断保存成系统经验。后续相似材料会优先参考相同的来源类型、事件类型和分析能力。",
      memoryRulesTitle: "学习规则",
      memoryFeedbackTitle: "学习反馈",
      loading: "加载中...",
      waitingPreview: "等待预览",
      waitingInput: "等待输入",
      waitingRun: "等待执行",
      noUploads: "还没有上传记录",
      ready: "就绪",
      noSkills: "当前还没有可展示的能力。",
      noMatrix: "当前还没有可展示的矩阵信息。",
      noMemoryRules: "还没有记忆规则。后续你纠正分类后，这里会逐步积累系统经验。",
      noMemoryFeedback: "还没有学习反馈记录。后续每次纠正分类，都会在这里留下痕迹。",
      noReports: "还没有报告记录。运行一次分析后，这里会显示最近生成的报告。",
      noInvestigations: "还没有调查会话。上传文件批次后，这里会自动出现会话记录。",
      noSummary: "暂无分析结论。",
      recentRunsTitle: "最近运行情况",
      recentRunsCopy: "这里看的是平台最近是否真的在处理事件，而不是仅仅完成了部署。",
      coverageTitle: "能力覆盖范围",
      coverageCopy: "这里看系统目前具备哪些能力，以及这些能力是否已经接入真实执行逻辑。",
      flowTitle: "处理流程说明",
      flowCopy: "用法上只需要把材料交给系统，但平台内部会根据输入类型走不同路径。",
      architectureTitle: "架构关系图",
      architectureCopy: "这张图用来说明连接层、分析主链和分析能力在平台里的协作关系。",
      historySummaryTitle: "运行沉淀",
      historySummaryCopy: "这里保留平台已经沉淀下来的记录数量，用来确认这套系统不是一次性页面状态。",
      plannerSummaryTitle: "系统准备调用这些能力",
      plannerSummaryCopy: "系统会根据材料类型、来源线索和已学习经验，选择最合适的分析能力。",
      normalizeSummaryTitle: "标准化结果摘要",
      normalizeSummaryCopy: "系统已经把原始材料转换成统一事件结构，后续的技能规划和风险报告都基于这份标准化事件。",
      reportSummaryTitle: "结论判断",
      reportReasonTitle: "为什么会这样判断",
      reportFactsTitle: "关键事实",
      reportCauseTitle: "可能原因",
      reportActionsTitle: "建议动作",
      reportChecksTitle: "快速核查",
      reportEscalationTitle: "升级条件",
      reportJudgmentTitle: "专业判断",
      reportEvidenceTitle: "关键证据",
      reportNextStepsTitle: "建议先做的动作",
      reportSnapshotTitle: "报告快照",
      reportsPathTitle: "本次使用的分析能力",
      investigationsEnginesTitle: "本批次使用的分析能力",
      memoryPatternTitle: "系统记住的特征",
      memorySavedSkillsTitle: "系统会优先调用这些能力",
      overviewSnapshotTitle: "平台快照",
      memoryRuleCopy: "这条经验会在系统再次遇到相似材料时，帮助它更快走到正确的分析路径。",
      memoryFeedbackSavedSkills: "保存的优先能力",
      memoryRulePreferredSkills: "优先调用能力",
      memoryRuleHeaders: "记住的表头特征",
      latestAnalysis: "最近一次分析",
      latest: "最新",
      searchSkillsPlaceholder: "搜索技能 / 模块 / 引擎",
      searchMemoryPlaceholder: "搜索学习记录 / 文件 / 事件",
      sourceTypePlaceholder: "选择正确的来源类型",
      eventTypePlaceholder: "选择正确的事件类型",
      menuOverview: "概览",
      menuIntake: "输入",
      menuSkills: "技能",
      menuIntegrations: "连接",
      menuMemory: "学习",
      menuSecurityGroup: "安全日志分析",
      viewSkillDirectoryTitle: "全部能力",
      viewSkillDirectoryCopy: "默认展示当前平台全部能力，你也可以按模块快速收窄并定位对应引擎。",
      skillsDirectoryNote: "默认展示当前平台全部能力；也可以按模块快速收窄。",
      viewLearningCopy: "这里会沉淀系统学到的分类经验，后续相似材料会优先复用这些判断。",
      uploadRunsWaiting: "还没有上传分析记录",
      learningReadyHint: "在输入页完成一次分析后，这里可以直接把正确判断保存成系统经验。",
      overviewPulseCopy: "这里展示的是平台最近一次真实分析留下的运行脉搏。",
      platformActive: "平台活跃",
      platformWaiting: "等待材料",
      statusReadyAnalyze: "可开始分析",
      statusWaitingInput: "等待输入",
      plannerPlannedSkills: "本次预计调用的能力",
      fileRunsSummaryCopy: "这里会按文件列出本次上传后的处理结果，方便你逐个回看。",
      intakeUploadNote: "上传文件只会先放进当前会话。真正开始归一化、能力决策和报告生成，要点“归一化后分析”。像 JumpServer 这类多源材料，建议同批上传。",
      intakeDropzoneTitle: "拖拽安全日志到这里",
      intakeDropzoneCopy: "或者从本地安全目录里选择文件",
      intakeEditorTitle: "当前输入会话",
      intakeEditorNote: "上传后的文件会先在这里生成待分析清单；如果你手动粘贴原始 JSON 或日志，也会从这里开始进入分析链。",
      intakeEditorBadge: "会话编辑区",
      intakeAnalyzeHint: "上传只是进入当前会话，真正开始处理要点这个按钮。",
      downloadReport: "下载报告",
      architectureMcp: "连接层负责连接外部平台并导入材料",
      architectureAgent: "分析主链负责归一化、决策、风险判断与报告",
      architectureSkill: "分析能力负责完成具体检测和提炼",
      architectureOutput: "最终沉淀为报告、历史、调查和学习反馈",
    }
  },
  en: {
    brandTitle: "AI Security Platform",
    brandCopy: "Ingest security materials and let the Agent handle normalization, Skill decisions, risk assessment, and continuous learning.",
    heroEyebrow: "MegaETH Security Platform",
    systemStatus: "Agent Status",
    checking: "Checking...",
    refresh: "Refresh",
    refreshing: "Refreshing...",
    refreshed: "Updated",
    retry: "Retry",
    viewMeta: {
      overview: ["Overview", "Review platform activity, recent conclusions, and the investigation records accumulated over time."],
      intake: ["Intake", "Submit materials through one entry point and let the system normalize, reason, and report automatically."],
      skills: ["Skill", "Browse active Skill capability units by module and see what each one is responsible for."],
      integrations: ["MCP", "Manage the MCP connection layer here and bring asset, endpoint, report, and event-entry data into the Agent workflow."],
      memory: ["Agent Learning", "Review what the Agent has learned and keep teaching it with new decisions."],
    },
    sidebarCopy: {
      overview: "Start with platform activity, then review recent reports, investigations, and stored history.",
      intake: "Submit files or raw materials here. The system will normalize, select skills, and produce a report.",
      skills: "Review which Skills are active and how each module is currently covered.",
      integrations: "This is the MCP layer. Bitdefender is already wired in for asset inventory, endpoint list, and report catalog workflows.",
      memory: "This is the Agent learning layer. Each confirmed result can become future guidance.",
    },
    ui: {
      overviewTitle: "Platform Overview",
      reportsTitle: "Recent Reports",
      investigationsTitle: "Investigation Sessions",
      historyTitle: "History",
      bitdefenderTitle: "Bitdefender Connection",
      bitdefenderCopy: "This panel connects the Bitdefender GravityZone MCP. It is most useful for endpoint and asset coverage visibility plus importing the latest security report into the platform.",
      bitdefenderImportNote: "Read actions stay on this page. For import actions, open the Intake page to review the platform result.",
      intakeInputTitle: "Unified Intake",
      uploadFiles: "Upload Files",
      analyze: "Normalize + Analyze",
      plannerTitle: "Agent Decision Preview",
      normalizeTitle: "Normalization Result",
      reportTitle: "Security Report",
      learnCorrect: "This classification is correct",
      learnWrong: "This classification is wrong",
      correctionSkills: "Choose the correct analysis skills",
      saveCorrection: "Save correction",
      fileRunsTitle: "Uploaded File Runs",
      bitdefenderTest: "Verify Connection",
      bitdefenderNetwork: "Load Asset And Endpoint Inventory",
      bitdefenderImportNetwork: "Import Asset Inventory Into Platform",
      bitdefenderReports: "Load Available Report Catalog",
      bitdefenderReportLinks: "Fetch Latest Report Download Links",
      bitdefenderImportLatestReport: "Import Latest Report Content",
      bitdefenderImportReports: "Import Report Catalog Metadata",
      bitdefenderWaiting: "Waiting for connection test.",
      bitdefenderNoData: "No Bitdefender response yet.",
      bitdefenderSummaryTitle: "Bitdefender Connection Status",
      bitdefenderClassificationTitle: "Device Classification Summary",
      bitdefenderStructureTitle: "Device Structure And Classification Clues",
      bitdefenderEndpointApiNote: "This shows the managed endpoint list returned directly by the Bitdefender Network API, not every host that may appear in historical reports.",
      bitdefenderHierarchyEndpointTitle: "Full Hierarchy Device And Group Clues",
      bitdefenderCompaniesTitle: "Company And Tenant Preview",
      bitdefenderCustomGroupsTitle: "Custom Group Preview",
      bitdefenderManagedEndpointTitle: "Managed endpoint detail preview",
      bitdefenderLatestReportTitle: "Latest Security Report Snapshot",
      bitdefenderTopHostsTitle: "Top Hosts",
      bitdefenderTopEventsTitle: "Top Event Types",
      bitdefenderPolicyTitle: "Policy Distribution",
      bitdefenderOsTitle: "Operating System Distribution",
      bitdefenderCoverageTitle: "Latest Analyzable Content",
      bitdefenderCoverageGapTitle: "Asset Visibility Gap",
      bitdefenderCoverageGapCopy: "If the latest security report already includes many hosts while the API endpoint list stays small, treat it as a visibility gap rather than evidence that the platform has no devices.",
      bitdefenderGovernanceHint: "Use this area to judge policy spread, OS mix, and managed coverage rather than chasing an unstable total endpoint number.",
      bitdefenderReportFocusCopy: "Use this area as a current security summary so you can quickly spot concentrated hosts and event types.",
      bitdefenderAvailableDataTitle: "Available Data Types",
      bitdefenderActionHint: "If a fresh security report summary is already shown here, the most useful next action is usually importing the latest report into the platform.",
      bitdefenderDefaultKeyNotice: "Bitdefender connectivity is now configured securely on the server side and the API key is no longer exposed in the frontend. Right now the most useful paths are asset inventory, report catalog access, and report download links.",
      integrationsSectionCopy: "This area is the connection hub for external security consoles. Bitdefender already provides asset inventory, endpoint list, report catalog, and report download entry points.",
      bitdefenderAssetNote: "This area is best used for asset coverage, endpoint totals, and grouping clues rather than treating each raw API list as a final analyst view.",
      bitdefenderLatestReportHostNote: "If the API endpoint list is 0 while the latest security audit report already contains many hosts, it usually means the public Network API is not returning the managed endpoint list right now, not that the platform has no hosts.",
      installedSkillsTitle: "All Skills",
      skillMatrixTitle: "Module Snapshot",
      memoryLearnTitle: "Teach The Agent From The Current Result",
      memoryLearnCopy: "When the current material has been classified correctly, save the judgment as Agent memory so similar materials can reuse it later.",
      memoryRulesTitle: "Agent Memory Rules",
      memoryFeedbackTitle: "Agent Learning Feedback",
      loading: "Loading...",
      waitingPreview: "Waiting for preview",
      waitingInput: "Waiting for input",
      waitingRun: "Waiting to run",
      noUploads: "No uploaded runs yet",
      ready: "Ready",
      noSkills: "No capabilities are available to display yet.",
      noMatrix: "No matrix data is available to display yet.",
      noMemoryRules: "No memory rules yet. Once you correct classifications, the system will accumulate experience here.",
      noMemoryFeedback: "No learning feedback yet. Each correction will leave a trace here.",
      noReports: "No reports yet. Run an analysis and recent reports will appear here.",
      noInvestigations: "No investigation sessions yet. Upload a batch of files and sessions will appear here.",
      noSummary: "No analysis summary yet.",
      recentRunsTitle: "Recent Activity",
      recentRunsCopy: "This shows whether the platform is actively processing events, not just deployed.",
      coverageTitle: "Capability Coverage",
      coverageCopy: "This shows which capabilities are currently available and whether they are backed by real execution logic.",
      flowTitle: "Processing Flow",
      flowCopy: "You only need to hand materials to the platform, but the internal route changes based on input type.",
      architectureTitle: "Architecture Map",
      architectureCopy: "This card shows how MCP, Agent, and Skill work together inside the platform.",
      historySummaryTitle: "Runtime Footprint",
      historySummaryCopy: "This preserves accumulated records so you can verify the system is more than a one-off page state.",
      plannerSummaryTitle: "The Agent plans to use these Skills",
      plannerSummaryCopy: "The Agent chooses the right Skills based on material type, source signals, and learned experience.",
      normalizeSummaryTitle: "Normalization Summary",
      normalizeSummaryCopy: "The system has converted the raw material into a unified event structure used by planning and reporting.",
      reportSummaryTitle: "Assessment",
      reportReasonTitle: "Why it was assessed this way",
      reportFactsTitle: "Key Facts",
      reportCauseTitle: "Likely Causes",
      reportActionsTitle: "Recommended Actions",
      reportChecksTitle: "Quick Checks",
      reportEscalationTitle: "Escalation Conditions",
      reportJudgmentTitle: "Professional Judgment",
      reportEvidenceTitle: "Key Evidence",
      reportNextStepsTitle: "Recommended Next Steps",
      reportSnapshotTitle: "Report Snapshot",
      reportsPathTitle: "Skills used by the Agent",
      investigationsEnginesTitle: "Skills used by the Agent in this batch",
      memoryPatternTitle: "Pattern remembered by the Agent",
      memorySavedSkillsTitle: "The Agent will prefer these Skills",
      overviewSnapshotTitle: "Platform Snapshot",
      memoryRuleCopy: "This experience helps the system reach the right analysis path more quickly when similar materials appear again.",
      memoryFeedbackSavedSkills: "Saved preferred skills",
      memoryRulePreferredSkills: "Preferred skills",
      memoryRuleHeaders: "Remembered header patterns",
      latestAnalysis: "Latest analysis",
      latest: "Latest",
      searchSkillsPlaceholder: "Search capabilities / module / engine",
      searchMemoryPlaceholder: "Search learned patterns / file / event",
      sourceTypePlaceholder: "Choose the correct source type",
      eventTypePlaceholder: "Choose the correct event type",
      menuOverview: "Overview",
      menuIntake: "Intake",
      menuSkills: "Skill",
      menuIntegrations: "MCP",
      menuMemory: "Agent Learning",
      menuSecurityGroup: "Security Log Analysis",
      viewSkillDirectoryTitle: "All Skills",
      viewSkillDirectoryCopy: "Show the full active Skill set by default, then narrow it down by module when needed.",
      skillsDirectoryNote: "The default view shows the full active Skill set. Use the module filter to narrow it down.",
      viewLearningCopy: "The Agent stores learned classification experience here so similar materials can reuse these judgments later.",
      uploadRunsWaiting: "No uploaded analysis runs yet",
      learningReadyHint: "Once one analysis is completed in Intake, you can save the correct judgment here as platform memory.",
      overviewPulseCopy: "This area reflects the operating pulse left by the most recent real analysis run.",
      platformActive: "Platform active",
      platformWaiting: "Waiting for material",
      statusReadyAnalyze: "Ready to analyze",
      statusWaitingInput: "Waiting for input",
      plannerPlannedSkills: "Planned Skills",
      fileRunsSummaryCopy: "This area lists the result of each uploaded file so you can review them one by one.",
      intakeUploadNote: "Uploading files only stages them in the current session. The actual normalization, planning, and reporting start when you click “Normalize + Analyze”. For multi-source material such as JumpServer, upload them in one batch.",
      intakeDropzoneTitle: "Drag and drop security logs here",
      intakeDropzoneCopy: "or browse files from your secure local storage",
      intakeEditorTitle: "Current Session Input",
      intakeEditorNote: "Uploaded files first become a staged manifest here. If you paste raw JSON or logs manually, the analysis chain also starts from this area.",
      intakeEditorBadge: "Session Editor",
      intakeAnalyzeHint: "Uploads only stage content in the current session. Click this button to actually start processing.",
      downloadReport: "Download Report",
      architectureMcp: "MCP connects external platforms and imports material",
      architectureAgent: "Agent owns normalization, decisions, risk judgment, and reporting",
      architectureSkill: "Skill performs the concrete analysis capability",
      architectureOutput: "The final output becomes reports, history, investigations, and learning feedback",
    }
  },
};

const categoryLabels = {
  appsec: "AppSec",
  cicd: "CI/CD",
  endpoint: "Endpoint",
  host: "Host",
  cloud: "Cloud",
  easm: "EASM",
  key: "Key",
  identity: "Identity",
};

const engineLabels = {
  pr_security_review: "MegaETH PR Review Engine",
  secret_detection: "MegaETH Secret Detection Engine",
  process_anomaly: "MegaETH Endpoint Behavior Engine",
  integrity_monitor: "MegaETH Host Integrity Engine",
  baseline_compliance_analysis: "MegaETH Host Baseline Engine",
  systemd_service_risk: "MegaETH Service Posture Engine",
  binary_tamper_review: "MegaETH Binary Review Engine",
  config_audit: "MegaETH Cloud Configuration Engine",
  asset_discovery: "MegaETH Asset Discovery Engine",
  service_scan: "MegaETH Exposure Surface Engine",
  tls_analysis: "MegaETH TLS Posture Engine",
  kms_risk: "MegaETH KMS Assurance Engine",
  private_key_exposure: "MegaETH Key Exposure Engine",
  policy_risk_analysis: "MegaETH Policy Reasoning Engine",
  anomalous_access_review: "MegaETH Access Review Engine",
  jumpserver_command_review: "MegaETH JumpServer Command Engine",
  jumpserver_transfer_review: "MegaETH JumpServer Transfer Engine",
  jumpserver_operation_review: "MegaETH JumpServer Control Plane Engine",
  jumpserver_multi_source_review: "MegaETH JumpServer Correlation Engine",
  identity_surface: "MegaETH Cloud Identity Engine",
  vulnerability_scan: "MegaETH Exposure Verification Engine",
  external_intelligence: "MegaETH External Intelligence Engine",
  whitebox_recon: "MegaETH Whitebox Recon Engine",
  whitebox_exploit_validation: "MegaETH Whitebox Validation Engine",
  whitebox_report_synthesis: "MegaETH Whitebox Report Engine",
};

const skillLabels = {
  "megaeth.host.baseline_compliance_analysis": { zh: "MegaETH 主机基线合规分析能力", en: "MegaETH Host Baseline Compliance Analysis" },
  "megaeth.cicd.pr_security_review": { zh: "MegaETH PR 安全审查能力", en: "MegaETH PR Security Review" },
  "megaeth.cicd.secret_detection": { zh: "MegaETH 密钥暴露检测能力", en: "MegaETH Secret Detection" },
  "megaeth.endpoint.process_anomaly": { zh: "MegaETH 端点行为分析能力", en: "MegaETH Endpoint Behavior Analysis" },
  "megaeth.host.integrity_monitor": { zh: "MegaETH 主机完整性分析能力", en: "MegaETH Host Integrity Analysis" },
  "megaeth.host.systemd_service_risk": { zh: "MegaETH 服务姿态分析能力", en: "MegaETH Service Posture Analysis" },
  "megaeth.host.binary_tamper_review": { zh: "MegaETH 二进制完整性审查能力", en: "MegaETH Binary Integrity Review" },
  "megaeth.cloud.config_audit": { zh: "MegaETH 云配置风险能力", en: "MegaETH Cloud Configuration Risk" },
  "megaeth.easm.asset_discovery": { zh: "MegaETH 外部资产发现能力", en: "MegaETH External Asset Discovery" },
  "megaeth.easm.service_scan": { zh: "MegaETH 服务暴露分析能力", en: "MegaETH Service Exposure Analysis" },
  "megaeth.easm.tls_analysis": { zh: "MegaETH TLS 姿态分析能力", en: "MegaETH TLS Posture Analysis" },
  "megaeth.key.kms_risk": { zh: "MegaETH KMS 风险分析能力", en: "MegaETH KMS Risk Analysis" },
  "megaeth.key.private_key_exposure": { zh: "MegaETH 私钥暴露检测能力", en: "MegaETH Private Key Exposure Detection" },
  "megaeth.identity.policy_risk_analysis": { zh: "MegaETH 身份策略风险分析能力", en: "MegaETH Identity Policy Risk Analysis" },
  "megaeth.identity.anomalous_access_review": { zh: "MegaETH 异常访问审查能力", en: "MegaETH Anomalous Access Review" },
  "megaeth.identity.jumpserver_command_review": { zh: "MegaETH JumpServer 命令审计能力", en: "MegaETH JumpServer Command Review" },
  "megaeth.identity.jumpserver_transfer_review": { zh: "MegaETH JumpServer 文件传输审计能力", en: "MegaETH JumpServer Transfer Review" },
  "megaeth.identity.jumpserver_operation_review": { zh: "MegaETH JumpServer 管理平面审计能力", en: "MegaETH JumpServer Operation Review" },
  "megaeth.identity.jumpserver_multi_source_review": { zh: "MegaETH JumpServer 多源关联审计能力", en: "MegaETH JumpServer Multi-Source Audit Review" },
  "megaeth.cloud.identity_surface": { zh: "MegaETH 云身份面分析能力", en: "MegaETH Cloud Identity Surface Analysis" },
  "megaeth.easm.vulnerability_scan": { zh: "MegaETH 外部漏洞验证能力", en: "MegaETH External Vulnerability Validation" },
  "megaeth.easm.external_intelligence": { zh: "MegaETH 外部情报关联能力", en: "MegaETH External Intelligence Correlation" },
  "megaeth.appsec.whitebox_recon": { zh: "MegaETH 白盒侦察分析能力", en: "MegaETH Whitebox Recon Analysis" },
  "megaeth.appsec.whitebox_exploit_validation": { zh: "MegaETH 白盒验证分析能力", en: "MegaETH Whitebox Validation Analysis" },
  "megaeth.appsec.whitebox_report_synthesis": { zh: "MegaETH 白盒综合报告能力", en: "MegaETH Whitebox Report Synthesis" },
};

const skillMeta = {
  "megaeth.host.baseline_compliance_analysis": { maturity: "L4", trainedCases: 1 },
  "megaeth.host.integrity_monitor": { maturity: "L3", trainedCases: 1 },
  "megaeth.endpoint.process_anomaly": { maturity: "L3", trainedCases: 0 },
  "megaeth.host.systemd_service_risk": { maturity: "L2", trainedCases: 0 },
  "megaeth.host.binary_tamper_review": { maturity: "L2", trainedCases: 0 },
  "megaeth.cloud.config_audit": { maturity: "L2", trainedCases: 0 },
  "megaeth.cloud.identity_surface": { maturity: "L2", trainedCases: 0 },
  "megaeth.easm.asset_discovery": { maturity: "L2", trainedCases: 0 },
  "megaeth.easm.service_scan": { maturity: "L2", trainedCases: 0 },
  "megaeth.easm.tls_analysis": { maturity: "L1", trainedCases: 0 },
  "megaeth.easm.vulnerability_scan": { maturity: "L1", trainedCases: 0 },
  "megaeth.easm.external_intelligence": { maturity: "L1", trainedCases: 0 },
  "megaeth.identity.policy_risk_analysis": { maturity: "L2", trainedCases: 0 },
  "megaeth.identity.anomalous_access_review": { maturity: "L1", trainedCases: 0 },
  "megaeth.identity.jumpserver_command_review": { maturity: "L2", trainedCases: 1 },
  "megaeth.identity.jumpserver_transfer_review": { maturity: "L2", trainedCases: 1 },
  "megaeth.identity.jumpserver_operation_review": { maturity: "L2", trainedCases: 1 },
  "megaeth.identity.jumpserver_multi_source_review": { maturity: "L3", trainedCases: 1 },
  "megaeth.key.kms_risk": { maturity: "L2", trainedCases: 0 },
  "megaeth.key.private_key_exposure": { maturity: "L1", trainedCases: 0 },
  "megaeth.cicd.pr_security_review": { maturity: "L2", trainedCases: 0 },
  "megaeth.cicd.secret_detection": { maturity: "L2", trainedCases: 0 },
  "megaeth.appsec.whitebox_recon": { maturity: "L2", trainedCases: 0 },
  "megaeth.appsec.whitebox_exploit_validation": { maturity: "L2", trainedCases: 0 },
  "megaeth.appsec.whitebox_report_synthesis": { maturity: "L2", trainedCases: 0 },
};

const moduleOrder = ["appsec", "host", "endpoint", "cloud", "easm", "identity", "key", "cicd"];

const moduleNarratives = {
  zh: {
    appsec: "偏白盒应用安全分析，适合侦察、验证与综合报告链路。",
    host: "偏主机基线、完整性和运行姿态分析，适合系统弱点与主机风险材料。",
    endpoint: "偏端点行为和终端侧安全信号，适合安全产品导出的终端事件。",
    cloud: "偏云配置与身份面风险，适合云环境审计、策略与暴露材料。",
    easm: "偏外部攻击面与暴露面分析，适合外网资产、服务、TLS 和漏洞材料。",
    identity: "偏身份权限与访问控制推理，适合 IAM、策略和异常访问场景。",
    key: "偏密钥、KMS 和敏感材料风险，适合签名、密钥暴露和凭据材料。",
    cicd: "偏代码与交付链安全，适合 PR、依赖、Secrets 与流水线场景。",
  },
  en: {
    appsec: "Focused on whitebox application security flows including recon, validation, and synthesis.",
    host: "Focused on host baseline, integrity, and posture analysis for system weakness materials.",
    endpoint: "Focused on endpoint behavior and managed endpoint security signals from security tools.",
    cloud: "Focused on cloud configuration and identity-surface risk across audit and posture materials.",
    easm: "Focused on external attack surface, services, TLS, and exposure verification.",
    identity: "Focused on identity, access policy, and anomalous access reasoning.",
    key: "Focused on KMS, key exposure, and sensitive cryptographic material handling.",
    cicd: "Focused on code, delivery chain, secrets, and CI/CD review scenarios.",
  },
};

const storageKeys = {
  activeView: "megaeth-active-view-v2",
  language: "megaeth-language-v1",
};

const legacyStorageKeys = ["megaeth-active-view", "megaeth-raw-input", "megaeth-raw-input-v2"];

const intakeState = {
  rawEvent: null,
  normalizedEvent: null,
  plannerPreview: null,
  report: null,
  uploadBatch: null,
  pendingFiles: [],
  analyzing: false,
};

const uiState = {
  overview: null,
  reports: [],
  investigations: [],
  history: null,
  skills: [],
  matrix: {},
  memoryRules: [],
  memoryFeedback: [],
  bitdefender: null,
  language: "zh",
};

const expandedSkillModules = new Set();

const sourceTypeOptions = ["host", "endpoint", "easm", "cloud", "kms", "github", "identity", "jumpserver", "login_auth", "command_audit", "file_transfer_audit", "operation_audit", "key", "cicd"];
const eventTypeOptions = [
  "host_integrity",
  "host_baseline_assessment",
  "endpoint_process",
  "external_asset",
  "service_exposure",
  "cloud_configuration",
  "kms_access",
  "github_pr",
  "identity_policy",
  "jumpserver_multi_source_audit",
  "login_auth_review",
  "jumpserver_command_review",
  "jumpserver_transfer_review",
  "jumpserver_operation_review",
];

const sourceTypeLabels = {
  zh: {
    host: "主机",
    endpoint: "端点",
    easm: "外部攻击面",
    cloud: "云环境",
    kms: "密钥管理",
    github: "代码仓库",
    identity: "身份权限",
    jumpserver: "JumpServer 审计",
    login_auth: "登录认证",
    command_audit: "命令审计",
    file_transfer_audit: "文件传输审计",
    operation_audit: "操作记录审计",
    key: "密钥材料",
    cicd: "CI/CD",
  },
  en: {
    host: "Host",
    endpoint: "Endpoint",
    easm: "EASM",
    cloud: "Cloud",
    kms: "KMS",
    github: "Code Repository",
    identity: "Identity",
    jumpserver: "JumpServer Audit",
    login_auth: "Login Auth",
    command_audit: "Command Audit",
    file_transfer_audit: "File Transfer Audit",
    operation_audit: "Operation Audit",
    key: "Key Material",
    cicd: "CI/CD",
  },
};

const eventTypeLabels = {
  zh: {
    host_integrity: "主机完整性风险",
    host_baseline_assessment: "主机基线评估",
    endpoint_process: "端点进程异常",
    external_asset: "外部资产线索",
    service_exposure: "服务暴露风险",
    tls_analysis: "TLS 姿态分析",
    easm_asset_assessment: "EASM 综合资产评估",
    cloud_configuration: "云配置风险",
    kms_access: "KMS 访问事件",
    github_pr: "代码变更审查",
    identity_policy: "身份策略风险",
    jumpserver_multi_source_audit: "JumpServer 多源审计",
    login_auth_review: "登录认证审查",
    jumpserver_command_review: "JumpServer 命令审查",
    jumpserver_transfer_review: "JumpServer 文件传输审查",
    jumpserver_operation_review: "JumpServer 操作记录审查",
  },
  en: {
    host_integrity: "Host Integrity Risk",
    host_baseline_assessment: "Host Baseline Assessment",
    endpoint_process: "Endpoint Process Anomaly",
    external_asset: "External Asset Signal",
    service_exposure: "Service Exposure Risk",
    tls_analysis: "TLS Posture Analysis",
    easm_asset_assessment: "EASM Composite Asset Assessment",
    cloud_configuration: "Cloud Configuration Risk",
    kms_access: "KMS Access Event",
    github_pr: "Code Change Review",
    identity_policy: "Identity Policy Risk",
    jumpserver_multi_source_audit: "JumpServer Multi-Source Audit",
    login_auth_review: "Login Authentication Review",
    jumpserver_command_review: "JumpServer Command Review",
    jumpserver_transfer_review: "JumpServer File Transfer Review",
    jumpserver_operation_review: "JumpServer Operation Review",
  },
};

function fillSelectOptions(selectId, values, placeholder, formatter = (value) => value) {
  const select = document.getElementById(selectId);
  if (!select) return;
  const current = select.value;
  select.innerHTML = "";
  const emptyOption = document.createElement("option");
  emptyOption.value = "";
  emptyOption.textContent = placeholder;
  select.appendChild(emptyOption);
  values.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = formatter(value);
    if (value === current) option.selected = true;
    select.appendChild(option);
  });
}

function t(key) {
  return i18n[uiState.language][key];
}

function localizedText(value) {
  if (value && typeof value === "object") {
    return value[uiState.language] || value.zh || value.en || "";
  }
  return String(value || "");
}

function termLabel(term) {
  const labels = {
    zh: {
      skill: "技能",
      skills: "技能",
      agent: "分析主链",
      mcp: "连接层",
      report: "报告",
    },
    en: {
      skill: "Skill",
      skills: "Skills",
      agent: "Agent",
      mcp: "MCP",
      report: "Report",
    },
  };
  return labels[uiState.language][term] || term;
}

function applyLanguage() {
  const lang = uiState.language;
  document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
  document.getElementById("brand-title").textContent = t("brandTitle");
  document.getElementById("brand-copy").textContent = t("brandCopy");
  document.getElementById("hero-eyebrow").textContent = t("heroEyebrow");
  document.getElementById("system-status-label").textContent = t("systemStatus");
  const ui = t("ui");
  document.getElementById("section-overview-title").textContent = ui.overviewTitle;
  document.getElementById("section-reports-title").textContent = ui.reportsTitle;
  document.getElementById("section-investigations-title").textContent = ui.investigationsTitle;
  document.getElementById("section-history-title").textContent = ui.historyTitle;
  document.getElementById("section-bitdefender-title").textContent = ui.bitdefenderTitle;
  document.getElementById("bitdefender-copy").textContent = ui.bitdefenderCopy;
  document.getElementById("bitdefender-import-note").textContent = ui.bitdefenderImportNote;
  document.getElementById("section-intake-input-title").textContent = ui.intakeInputTitle;
  document.getElementById("upload-files-label").textContent = ui.uploadFiles;
  if (document.getElementById("preview-normalize")) document.getElementById("preview-normalize").textContent = ui.previewNormalize;
  if (document.getElementById("preview-plan")) document.getElementById("preview-plan").textContent = ui.previewPlan;
  document.getElementById("analyze").textContent = ui.analyze;
  document.getElementById("section-planner-title").textContent = ui.plannerTitle;
  document.getElementById("section-normalize-title").textContent = ui.normalizeTitle;
  document.getElementById("section-report-title").textContent = ui.reportTitle;
  const showCorrectionBtn = document.getElementById("show-correction-form");
  const correctionSkillsLabel = document.getElementById("correction-skills-label");
  const saveCorrectionBtn = document.getElementById("save-correction");
  if (showCorrectionBtn) showCorrectionBtn.textContent = ui.learnWrong;
  if (correctionSkillsLabel) correctionSkillsLabel.textContent = ui.correctionSkills;
  if (saveCorrectionBtn) saveCorrectionBtn.textContent = ui.saveCorrection;
  document.getElementById("section-file-runs-title").textContent = ui.fileRunsTitle;
  document.getElementById("menu-group-security").textContent = ui.menuSecurityGroup;
  document.getElementById("intake-dropzone-title").textContent = ui.intakeDropzoneTitle;
  document.getElementById("intake-dropzone-copy").textContent = ui.intakeDropzoneCopy;
  document.getElementById("intake-editor-title").textContent = ui.intakeEditorTitle;
  document.getElementById("intake-editor-note").textContent = ui.intakeEditorNote;
  document.getElementById("intake-editor-badge").textContent = ui.intakeEditorBadge;
  document.getElementById("run-bitdefender-test").textContent = ui.bitdefenderTest;
  document.getElementById("run-bitdefender-network").textContent = ui.bitdefenderNetwork;
  document.getElementById("import-bitdefender-network").textContent = ui.bitdefenderImportNetwork;
  if (document.getElementById("run-bitdefender-reports")) document.getElementById("run-bitdefender-reports").textContent = ui.bitdefenderReports;
  if (document.getElementById("run-bitdefender-report-links")) document.getElementById("run-bitdefender-report-links").textContent = ui.bitdefenderReportLinks;
  if (document.getElementById("import-bitdefender-latest-report")) document.getElementById("import-bitdefender-latest-report").textContent = ui.bitdefenderImportLatestReport;
  if (document.getElementById("import-bitdefender-reports")) document.getElementById("import-bitdefender-reports").textContent = ui.bitdefenderImportReports;
  document.getElementById("section-installed-skills-title").textContent = ui.installedSkillsTitle;
  document.getElementById("section-skill-matrix-title").textContent = ui.skillMatrixTitle;
  if (document.getElementById("section-memory-rules-title")) document.getElementById("section-memory-rules-title").textContent = ui.memoryRulesTitle;
  if (document.getElementById("section-memory-feedback-title")) document.getElementById("section-memory-feedback-title").textContent = ui.memoryFeedbackTitle;
  document.getElementById("refresh-overview").textContent = t("refresh");
  document.getElementById("refresh-reports").textContent = t("refresh");
  document.getElementById("refresh-investigations").textContent = t("refresh");
  document.getElementById("refresh-history").textContent = t("refresh");
  document.getElementById("refresh-skills").textContent = t("refresh");
  document.getElementById("refresh-matrix").textContent = t("refresh");
  if (document.getElementById("refresh-memory-rules")) document.getElementById("refresh-memory-rules").textContent = t("refresh");
  if (document.getElementById("refresh-memory-feedback")) document.getElementById("refresh-memory-feedback").textContent = t("refresh");
  document.getElementById("skills-directory-note").textContent = ui.skillsDirectoryNote;
  if (document.getElementById("memory-search")) document.getElementById("memory-search").placeholder = ui.searchMemoryPlaceholder;
  document.getElementById("intake-upload-note").textContent = ui.intakeUploadNote;
  document.getElementById("intake-analyze-hint").textContent = ui.intakeAnalyzeHint;
  document.getElementById("download-report").textContent = ui.downloadReport;
  const filter = document.getElementById("skills-filter");
  if (filter) {
    const labels = uiState.language === "zh"
      ? {
          all: "全部能力",
          appsec: "应用安全",
          cicd: "CI/CD",
          endpoint: "端点",
          host: "主机",
          cloud: "云环境",
          easm: "外部攻击面",
          key: "密钥材料",
          identity: "身份权限",
        }
      : {
          all: "All Skills",
          appsec: "AppSec",
          cicd: "CI/CD",
          endpoint: "Endpoint",
          host: "Host",
          cloud: "Cloud",
          easm: "EASM",
          key: "Key Material",
          identity: "Identity",
        };
    Array.from(filter.options).forEach((option) => {
      option.textContent = labels[option.value] || option.value;
    });
  }
  if (document.getElementById("correction-source-type")) {
    fillSelectOptions("correction-source-type", sourceTypeOptions, ui.sourceTypePlaceholder, sourceTypeLabel);
  }
  if (document.getElementById("correction-event-type")) {
    fillSelectOptions("correction-event-type", eventTypeOptions, ui.eventTypePlaceholder, eventTypeLabel);
  }
  if (document.getElementById("correction-skills")) {
    populateCorrectionSkillOptions(intakeState.plannerPreview?.skills_to_execute || []);
  }
  document.getElementById("lang-zh").classList.toggle("active", lang === "zh");
  document.getElementById("lang-en").classList.toggle("active", lang === "en");
  document.querySelectorAll("[data-view='overview']").forEach((node) => node.textContent = ui.menuOverview);
  document.querySelectorAll("[data-view='intake']").forEach((node) => node.textContent = ui.menuIntake);
  document.querySelectorAll("[data-view='skills']").forEach((node) => node.textContent = ui.menuSkills);
  document.querySelectorAll("[data-view='integrations']").forEach((node) => node.textContent = ui.menuIntegrations);
  document.querySelectorAll("[data-view='memory']").forEach((node) => node.textContent = ui.menuMemory);
  if (!intakeState.rawEvent && !intakeState.normalizedEvent && !intakeState.plannerPreview && !intakeState.report) {
    document.getElementById("intake-status").textContent = ui.ready;
  }
  setView(currentViewFromLocation());
  renderPlannerPreview(intakeState.plannerPreview);
  renderNormalizeOutput(intakeState.normalizedEvent);
  renderReport(intakeState.report);
  renderFileRuns(intakeState.uploadBatch);
  if (uiState.overview) renderOverview(uiState.overview);
  if (uiState.reports.length) renderReports(uiState.reports);
  if (uiState.investigations.length) renderInvestigations(uiState.investigations);
  if (uiState.history) renderHistory(uiState.history);
  if (uiState.skills.length) renderSkills(uiState.skills);
  if (Object.keys(uiState.matrix).length) renderMatrix(uiState.matrix);
  if (uiState.memoryRules.length) renderMemoryRules(uiState.memoryRules);
  if (uiState.memoryFeedback.length) renderMemoryFeedback(uiState.memoryFeedback);
  renderBitdefender(uiState.bitdefender);
}

async function request(url, options = {}) {
  const response = await fetch(url, options);
  const text = await response.text();
  const data = text ? JSON.parse(text) : {};
  if (!response.ok) throw new Error(data.detail || data.error || text);
  return data;
}

function clearLegacyLocalState() {
  legacyStorageKeys.forEach((key) => localStorage.removeItem(key));
}

function currentViewFromLocation() {
  const hashView = window.location.hash.replace(/^#/, "").trim();
  const allowedViews = new Set(["overview", "intake", "skills", "integrations", "memory"]);
  if (allowedViews.has(hashView)) return hashView;
  const storedView = localStorage.getItem(storageKeys.activeView) || "overview";
  return allowedViews.has(storedView) ? storedView : "overview";
}

function setView(view) {
  document.querySelectorAll(".menu-item").forEach((item) => {
    item.classList.toggle("active", item.dataset.view === view);
  });
  document.querySelectorAll(".view").forEach((item) => {
    item.classList.toggle("active", item.dataset.section === view);
  });
  document.getElementById("view-title").textContent = t("viewMeta")[view][0];
  document.getElementById("view-copy").textContent = t("viewMeta")[view][1];
  document.getElementById("sidebar-copy").textContent = t("sidebarCopy")[view] || "";
  localStorage.setItem(storageKeys.activeView, view);
  if (window.location.hash !== `#${view}`) {
    window.history.replaceState(null, "", `#${view}`);
  }
}

function setHealth(text, tone = "idle") {
  const badge = document.getElementById("health-badge");
  badge.textContent = text;
  badge.className = `health-badge ${tone}`;
}

function uploadStatusText(data) {
  const uploadedCount = Number(data?.uploaded_count || 0);
  const resultCount = Number(data?.count || 0);
  const compositeGenerated = Boolean(data?.composite_generated);
  const visibleResults = (data?.results || []).filter((item) => item?.normalized_event?.event_type !== "jumpserver_multi_source_audit");
  const sourceCategoryCount = new Set(
    visibleResults
      .map((item) => item?.normalized_event?.source_type)
      .filter(Boolean)
  ).size;
  if (uiState.language === "zh") {
    if (compositeGenerated && uploadedCount > 0) {
      if (sourceCategoryCount > 0 && sourceCategoryCount !== uploadedCount) {
        return `已上传 ${uploadedCount} 个文件，覆盖 ${sourceCategoryCount} 类场景，生成 ${resultCount} 条分析结果（包含 1 条综合结果）。`;
      }
      return `已上传 ${uploadedCount} 个文件，生成 ${resultCount} 条分析结果（包含 1 条综合结果）。`;
    }
    return `已上传 ${uploadedCount || resultCount} 个文件，生成 ${resultCount} 条分析结果。`;
  }
  if (compositeGenerated && uploadedCount > 0) {
    if (sourceCategoryCount > 0 && sourceCategoryCount !== uploadedCount) {
      return `Uploaded ${uploadedCount} file(s), covering ${sourceCategoryCount} source category(ies), and produced ${resultCount} analysis result(s), including 1 composite result.`;
    }
    return `Uploaded ${uploadedCount} file(s) and produced ${resultCount} analysis result(s), including 1 composite result.`;
  }
  return `Uploaded ${uploadedCount || resultCount} file(s) and produced ${resultCount} analysis result(s).`;
}

function stagedUploadManifest(files) {
  const manifest = {
    mode: "staged_upload",
    status: uiState.language === "zh" ? "waiting_for_normalize_and_analyze" : "waiting_for_normalize_and_analyze",
    message:
      uiState.language === "zh"
        ? "文件已上传完成，等待点击“归一化后分析”后才会真正开始处理。"
        : "Files have been uploaded and are waiting for “Normalize + Analyze” before processing starts.",
    pending_files: files.map((file) => ({
      name: file.name,
      size_bytes: file.size,
      type: file.type || "application/octet-stream",
    })),
  };
  return JSON.stringify(manifest, null, 2);
}

function healthText(kind) {
  if (uiState.language === "zh") {
    if (kind === "healthy") return "正常";
    if (kind === "staged") return "等待分析";
    if (kind === "normalizing") return "归一化中...";
    if (kind === "planning") return "规划中...";
    if (kind === "analyzing") return "分析中...";
    if (kind === "uploading") return "上传中...";
  }
  if (kind === "healthy") return "Healthy";
  if (kind === "staged") return "Ready to analyze";
  if (kind === "normalizing") return "Normalizing...";
  if (kind === "planning") return "Planning...";
  if (kind === "analyzing") return "Analyzing...";
  if (kind === "uploading") return "Uploading...";
  return kind;
}

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function linkEl(href, className, text) {
  const node = document.createElement("a");
  if (className) node.className = className;
  node.href = href;
  node.target = "_blank";
  node.rel = "noreferrer";
  node.textContent = text;
  return node;
}

function createEmptyState(text) {
  return el("div", "empty-state", text);
}

function formatTime(value) {
  if (!value) return "暂无记录";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);
  return date.toLocaleString("zh-CN");
}

function moduleLabel(category) {
  return categoryLabels[category] || String(category || "Unknown");
}

function sourceTypeLabel(value) {
  return sourceTypeLabels[uiState.language][value] || String(value || (uiState.language === "zh" ? "未知" : "Unknown"));
}

function eventTypeLabel(value) {
  return eventTypeLabels[uiState.language][value] || String(value || (uiState.language === "zh" ? "未知事件" : "Unknown event"));
}

function engineLabel(adapter) {
  return engineLabels[adapter] || "MegaETH Analysis Engine";
}

function skillLabel(skillId) {
  const labels = skillLabels[skillId];
  return labels ? labels[uiState.language] : skillId;
}

function orderedCategories(categories) {
  return [...categories].sort((a, b) => {
    const aIndex = moduleOrder.indexOf(a);
    const bIndex = moduleOrder.indexOf(b);
    return (aIndex === -1 ? 99 : aIndex) - (bIndex === -1 ? 99 : bIndex);
  });
}

function skillSpecUrl(skillId) {
  return `https://github.com/edmund-xl/MegaETH-AI-Security/blob/main/skill_specs/${skillId}.md`;
}

function moduleNarrative(category) {
  return moduleNarratives[uiState.language][category] || "";
}

function skillMetaFor(skill) {
  return skillMeta[skill.skill_id] || {maturity: "L1", trainedCases: 0};
}

function executionModeLabel(mode) {
  const labels = {
    zh: {
      rule_only: "规则版",
      agent_optional: "可挂 Agent",
      agent_augmented: "Agent 增强",
    },
    en: {
      rule_only: "Rule-only",
      agent_optional: "Agent optional",
      agent_augmented: "Agent augmented",
    },
  };
  return labels[uiState.language][mode] || mode;
}

function maturityLabel(level) {
  const labels = {
    zh: {
      L1: "L1 占位",
      L2: "L2 启发式",
      L3: "L3 已训练",
      L4: "L4 稳定",
    },
    en: {
      L1: "L1 Placeholder",
      L2: "L2 Heuristic",
      L3: "L3 Trained",
      L4: "L4 Stable",
    },
  };
  return labels[uiState.language][level] || level;
}

function caseCountLabel(count) {
  return uiState.language === "zh" ? `已训练 ${count} 个 case` : `${count} trained case${count === 1 ? "" : "s"}`;
}

function skillStrategySummary(skill) {
  const triggers = skill.agent_trigger_conditions || [];
  const fallbacks = skill.rule_fallback_conditions || [];
  const contextPolicy = skill.max_context_policy || "full";
  if ((skill.execution_mode || "rule_only") === "rule_only") {
    return uiState.language === "zh"
      ? "默认走规则版，优先保证结构稳定、统计可重复和结果可控。"
      : "Defaults to rule-only execution for stable structure, repeatable statistics, and predictable output.";
  }
  const contextLabel = {
    zh: {
      full: "完整上下文",
      summary_first: "摘要优先",
      summary_plus_samples: "摘要 + 样本",
    },
    en: {
      full: "full context",
      summary_first: "summary first",
      summary_plus_samples: "summary + samples",
    },
  }[uiState.language][contextPolicy] || contextPolicy;
  const triggerText = triggers[0] || (uiState.language === "zh" ? "摘要和证据足够完整时" : "when summary evidence is complete");
  const fallbackText = fallbacks[0] || (uiState.language === "zh" ? "模型不可用时自动回退规则版" : "falls back to rule-only when the model is unavailable");
  return uiState.language === "zh"
    ? `优先条件：${triggerText}；回退条件：${fallbackText}；上下文策略：${contextLabel}。`
    : `Preferred when ${triggerText}; falls back when ${fallbackText}; context policy: ${contextLabel}.`;
}

function skillFamilyId(skill) {
  if (skill.category === "identity" && skill.skill_id.includes("jumpserver")) return "jumpserver_audit";
  return "";
}

function skillFamilyLabel(familyId) {
  const labels = {
    jumpserver_audit: {
      zh: "JumpServer Audit",
      en: "JumpServer Audit",
    },
    general: {
      zh: "其他能力",
      en: "Other Skills",
    },
  };
  return labels[familyId]?.[uiState.language] || "";
}

function bucketSkillsByFamily(skills) {
  const buckets = new Map();
  skills.forEach((skill) => {
    const familyId = skillFamilyId(skill) || "general";
    if (!buckets.has(familyId)) buckets.set(familyId, []);
    buckets.get(familyId).push(skill);
  });
  return [...buckets.entries()].sort(([a], [b]) => {
    if (a === "jumpserver_audit") return -1;
    if (b === "jumpserver_audit") return 1;
    return a.localeCompare(b);
  });
}

function buildSkillBucket(items) {
  const wrapper = el("div", "skill-bucket");
  const featured = items.slice(0, Math.min(2, items.length));
  const remaining = items.slice(featured.length);

  if (featured.length) {
    const featureGrid = el("div", "module-feature-grid");
    featured.forEach((skill, index) => {
      const metaInfo = skillMetaFor(skill);
      const card = el("article", `skill-feature-card ${index === 0 ? "primary" : ""}`.trim());
      const top = el("div", "skill-card-top");
      const title = el("div", "");
      title.appendChild(el("h5", "", skill.skill_name));
      title.appendChild(el("p", "card-copy", skill.description));
      top.appendChild(title);
      top.appendChild(linkEl(skillSpecUrl(skill.skill_id), "spec-link", uiState.language === "zh" ? "查看规格" : "Open Spec"));
      card.appendChild(top);
      const submeta = el("div", "skill-submeta");
      const family = skillFamilyId(skill);
      if (family) submeta.appendChild(el("span", "chip", skillFamilyLabel(family)));
      submeta.appendChild(el("span", "chip good", skill.stage === "tool-backed" ? (uiState.language === "zh" ? "已接入真实执行" : "Live execution") : (uiState.language === "zh" ? "待接入" : "Pending")));
      submeta.appendChild(el("span", "chip", maturityLabel(metaInfo.maturity)));
      submeta.appendChild(el("span", "chip", caseCountLabel(metaInfo.trainedCases)));
      submeta.appendChild(el("span", "chip", executionModeLabel(skill.execution_mode || "rule_only")));
      submeta.appendChild(el("span", "chip", uiState.language === "zh" ? `引擎：${engineLabel(skill.adapter)}` : `Engine: ${engineLabel(skill.adapter)}`));
      card.appendChild(submeta);
      card.appendChild(el("p", "card-copy", skillStrategySummary(skill)));
      featureGrid.appendChild(card);
    });
    wrapper.appendChild(featureGrid);
  }

  if (remaining.length) {
    const compactList = el("div", "skill-compact-list");
    remaining.forEach((skill) => {
      const metaInfo = skillMetaFor(skill);
      const row = el("div", "skill-row");
      row.appendChild(el("div", "skill-row-name", skill.skill_name));
      row.appendChild(el("div", "skill-row-copy", skill.description));
      const meta = el("div", "skill-row-meta");
      const family = skillFamilyId(skill);
      if (family) meta.appendChild(el("span", "chip", skillFamilyLabel(family)));
      meta.appendChild(el("span", "chip", maturityLabel(metaInfo.maturity)));
      meta.appendChild(el("span", "chip", caseCountLabel(metaInfo.trainedCases)));
      meta.appendChild(el("span", "chip", executionModeLabel(skill.execution_mode || "rule_only")));
      meta.appendChild(el("span", "chip", engineLabel(skill.adapter)));
      meta.appendChild(linkEl(skillSpecUrl(skill.skill_id), "spec-link", uiState.language === "zh" ? "规格" : "Spec"));
      row.appendChild(meta);
      row.appendChild(el("div", "skill-row-copy", skillStrategySummary(skill)));
      compactList.appendChild(row);
    });
    wrapper.appendChild(compactList);
  }

  return wrapper;
}

function rankSkill(skill) {
  const scoreMap = [
    ["baseline_compliance_analysis", 100],
    ["whitebox_report_synthesis", 95],
    ["whitebox_exploit_validation", 90],
    ["whitebox_recon", 88],
    ["process_anomaly", 86],
    ["asset_discovery", 84],
    ["config_audit", 82],
    ["policy_risk_analysis", 80],
    ["service_scan", 78],
    ["integrity_monitor", 76],
  ];
  let score = 50;
  scoreMap.forEach(([token, weight]) => {
    if (skill.skill_id.includes(token)) score = Math.max(score, weight);
  });
  if (skill.stage === "tool-backed") score += 5;
  return score;
}

function renderChips(values, tone = "") {
  const row = el("div", "token-list");
  values.forEach((value) => {
    const normalized = String(value || "").toLowerCase();
    let tokenTone = tone;
    if (!tokenTone) {
      if (normalized.includes("jumpserver")) tokenTone = "cyan";
      else if (normalized.includes("bitdefender")) tokenTone = "green";
      else if (normalized.includes("whitebox") || normalized.includes("appsec")) tokenTone = "violet";
      else if (normalized.includes("host")) tokenTone = "amber";
      else if (normalized.includes("identity")) tokenTone = "cyan";
      else if (normalized.includes("endpoint")) tokenTone = "green";
    }
    row.appendChild(el("span", `token ${tokenTone}`.trim(), value));
  });
  return row;
}

function updateButtonState(buttonId, label, disabled = false) {
  const button = document.getElementById(buttonId);
  if (!button) return;
  button.textContent = label;
  button.disabled = disabled;
}

async function withRefreshState(buttonId, loader) {
  updateButtonState(buttonId, t("refreshing"), true);
  const startedAt = Date.now();
  try {
    await loader();
    const elapsed = Date.now() - startedAt;
    if (elapsed < 450) {
      await new Promise((resolve) => setTimeout(resolve, 450 - elapsed));
    }
    updateButtonState(buttonId, t("refreshed"), false);
    setTimeout(() => updateButtonState(buttonId, t("refresh"), false), 900);
  } catch (error) {
    updateButtonState(buttonId, t("retry"), false);
    throw error;
  }
}

function renderSkills(skills) {
  uiState.skills = skills;
  populateCorrectionSkillOptions();
  const root = document.getElementById("skills-output");
  root.innerHTML = "";
  const filter = document.getElementById("skills-filter")?.value || "all";
  const filtered = skills.filter((skill) => {
    const matchesFilter = filter === "all" || skill.category === filter;
    return matchesFilter;
  });
  if (!filtered.length) {
    root.appendChild(createEmptyState(t("ui").noSkills));
    return;
  }
  const grouped = filtered.reduce((acc, skill) => {
    acc[skill.category] = acc[skill.category] || [];
    acc[skill.category].push(skill);
    return acc;
  }, {});
  const categories = orderedCategories(Object.keys(grouped));
  const trainedCount = filtered.filter((skill) => skillMetaFor(skill).trainedCases > 0).length;
  const directory = el("div", "skill-directory");

  const summary = el("div", "skill-summary-strip");
  [
    [uiState.language === "zh" ? "当前能力数" : "Live skills", String(filtered.length)],
    [uiState.language === "zh" ? "模块数量" : "Modules", String(categories.length)],
    [uiState.language === "zh" ? "已接入执行" : "Tool-backed", String(filtered.filter((skill) => skill.stage === "tool-backed").length)],
    [uiState.language === "zh" ? "已训练能力" : "Case-trained", String(trainedCount)],
  ].forEach(([label, value], index) => {
    const stat = el("div", `skill-stat tone-${index + 1}`);
    stat.appendChild(el("span", "meta-label", label));
    stat.appendChild(el("span", "skill-stat-value", value));
    summary.appendChild(stat);
  });
  directory.appendChild(summary);

  categories.forEach((category) => {
    const items = [...(grouped[category] || [])].sort((a, b) => rankSkill(b) - rankSkill(a));
    const trainedInModule = items.filter((skill) => skillMetaFor(skill).trainedCases > 0).length;
    const familyBuckets = bucketSkillsByFamily(items);

    const cluster = el("section", "module-cluster");
    cluster.dataset.category = category;
    const head = el("button", "module-cluster-head module-cluster-toggle");
    head.type = "button";
    const isExpanded = expandedSkillModules.has(category);
    const headText = el("div", "");
    headText.appendChild(el("h4", "", moduleLabel(category)));
    headText.appendChild(el("div", "compact-meta", uiState.language === "zh" ? `已训练 ${trainedInModule} / ${items.length}` : `${trainedInModule} / ${items.length} trained`));
    head.appendChild(headText);
    head.appendChild(el("span", "module-pill", uiState.language === "zh" ? `${items.length} 个能力` : `${items.length} capabilities`));
    head.appendChild(el("span", "module-toggle-glyph", isExpanded ? "−" : "+"));
    head.addEventListener("click", () => {
      if (expandedSkillModules.has(category)) expandedSkillModules.delete(category);
      else expandedSkillModules.add(category);
      renderSkills(uiState.skills);
    });
    cluster.appendChild(head);
    if (isExpanded) {
      const body = el("div", "module-cluster-body");
      familyBuckets.forEach(([familyId, familyItems]) => {
        if (familyBuckets.length > 1 || familyId !== "general") {
          const familyHead = el("div", "module-subhead");
          familyHead.appendChild(el("h5", "", skillFamilyLabel(familyId)));
          familyHead.appendChild(el("span", "module-pill", uiState.language === "zh" ? `${familyItems.length} 个能力` : `${familyItems.length} capabilities`));
          body.appendChild(familyHead);
        }
        body.appendChild(buildSkillBucket(familyItems));
      });
      cluster.appendChild(body);
    }

    directory.appendChild(cluster);
  });

  root.appendChild(directory);
}

function populateCorrectionSkillOptions(selected = []) {
  const select = document.getElementById("correction-skills");
  if (!select) return;
  const current = new Set(selected.length ? selected : Array.from(select.selectedOptions).map((option) => option.value));
  select.innerHTML = "";
  uiState.skills.forEach((skill) => {
    const option = document.createElement("option");
    option.value = skill.skill_id;
    option.textContent = `${skill.skill_name} · ${moduleLabel(skill.category)}`;
    option.selected = current.has(skill.skill_id);
    select.appendChild(option);
  });
}

function renderMatrix(matrix) {
  uiState.matrix = matrix;
  const root = document.getElementById("matrix-output");
  root.innerHTML = "";
  const filter = document.getElementById("skills-filter")?.value || "all";
  const entries = orderedCategories(Object.keys(matrix).filter((category) => filter === "all" || category === filter))
    .map((category) => [category, matrix[category]]);
  if (!entries.length) {
    root.appendChild(createEmptyState(t("ui").noMatrix));
    return;
  }
  const wrapper = el("div", "module-map");
  const totalSkills = entries.reduce((sum, [, skills]) => sum + skills.length, 0) || 1;
  entries.forEach(([category, skills]) => {
    const relevant = skills.filter(() => true);
    if (!relevant.length) return;
    const trainedCount = relevant.filter((skill) => skillMetaFor(skill).trainedCases > 0).length;
    const card = el("article", "module-map-card");
    const head = el("div", "module-map-head");
    head.appendChild(el("h4", "", moduleLabel(category)));
    head.appendChild(el("span", "matrix-count", uiState.language === "zh" ? `${relevant.length} 个能力` : `${relevant.length} capabilities`));
    card.appendChild(head);
    card.appendChild(el("p", "mini-copy", moduleNarrative(category)));
    card.appendChild(el("p", "mini-copy", uiState.language === "zh" ? `已训练能力 ${trainedCount} 个` : `${trainedCount} case-trained skill(s)`));
    const list = el("div", "module-map-list");
    [...relevant].sort((a, b) => rankSkill(b) - rankSkill(a)).slice(0, 3).forEach((skill, index) => {
      const item = el("div", "module-map-item");
      item.appendChild(el("span", "", `${index + 1}. ${skill.skill_name}`));
      item.appendChild(el("span", "", uiState.language === "zh" ? (skill.stage === "tool-backed" ? "已接入" : "待接入") : (skill.stage === "tool-backed" ? "Live" : "Pending")));
      list.appendChild(item);
    });
    card.appendChild(list);
    const bar = el("div", "module-map-bar");
    const fill = el("span", "");
    fill.style.width = `${Math.max(18, Math.round((relevant.length / totalSkills) * 100))}%`;
    bar.appendChild(fill);
    card.appendChild(bar);
    wrapper.appendChild(card);
  });
  root.appendChild(wrapper);
}

function renderMemoryRules(rules) {
  const root = document.getElementById("memory-rules-output");
  if (!root) return;
  uiState.memoryRules = rules;
  root.innerHTML = "";
  const keyword = (document.getElementById("memory-search")?.value || "").trim().toLowerCase();
  const filtered = rules.filter((rule) => {
    const haystack = [
      rule.name,
      rule.expected_source_type,
      rule.expected_event_type,
      ...(rule.header_tokens || []),
      ...(rule.filename_tokens || []),
      ...(rule.preferred_skills || []),
    ].join(" ").toLowerCase();
    return !keyword || haystack.includes(keyword);
  });
  if (!filtered.length) {
    root.appendChild(createEmptyState(t("ui").noMemoryRules));
    return;
  }
  const board = el("div", "memory-rules-board");
  const summary = el("div", "skill-summary-strip");
  [
    [uiState.language === "zh" ? "规则总数" : "Rules", String(filtered.length)],
    [uiState.language === "zh" ? "累计命中" : "Matches", String(filtered.reduce((sum, rule) => sum + Number(rule.usage_count || 0), 0))],
    [uiState.language === "zh" ? "自动沉淀" : "Auto learned", String(filtered.filter((rule) => !rule.manual).length)],
    [uiState.language === "zh" ? "人工纠正" : "Manual", String(filtered.filter((rule) => rule.manual).length)],
  ].forEach(([label, value]) => {
    const stat = el("div", "skill-stat");
    stat.appendChild(el("span", "meta-label", label));
    stat.appendChild(el("span", "skill-stat-value", value));
    summary.appendChild(stat);
  });
  board.appendChild(summary);
  board.appendChild(el("p", "section-note", uiState.language === "zh" ? "这里是系统已经沉淀下来的长期规则。它们会在后续遇到相似材料时直接参与分类和能力决策。" : "This panel shows the long-lived rules the Agent has already retained. They are reused directly when similar materials appear again."));
  const visualGrid = el("div", "memory-visual-grid");
  const sourceCard = el("article", "memory-visual-card");
  sourceCard.appendChild(el("h4", "", uiState.language === "zh" ? "规则来源构成" : "Rule Source Mix"));
  sourceCard.appendChild(el("p", "card-copy", uiState.language === "zh" ? "先看这些长期规则更多来自自动沉淀还是人工纠偏。" : "Start by checking whether retained rules mostly come from automated observations or manual corrections."));
  const sourceBars = el("div", "memory-bar-list");
  const sourceCounts = [
    [uiState.language === "zh" ? "自动" : "Auto", filtered.filter((rule) => !rule.manual).length, "cyan"],
    [uiState.language === "zh" ? "人工" : "Manual", filtered.filter((rule) => rule.manual).length, "violet"],
  ];
  const maxSource = Math.max(...sourceCounts.map(([, count]) => count), 1);
  sourceCounts.forEach(([label, count, tone]) => {
    const row = el("div", "memory-bar-row");
    row.appendChild(el("span", "meta-label", label));
    const track = el("div", "memory-track");
    const fill = el("span", `signal-fill ${tone}`);
    fill.style.width = `${Math.max(10, Math.round((count / maxSource) * 100))}%`;
    track.appendChild(fill);
    row.appendChild(track);
    row.appendChild(el("span", "signal-value", String(count)));
    sourceBars.appendChild(row);
  });
  sourceCard.appendChild(sourceBars);
  visualGrid.appendChild(sourceCard);
  const targetCard = el("article", "memory-visual-card");
  targetCard.appendChild(el("h4", "", uiState.language === "zh" ? "主要命中事件" : "Top Learned Targets"));
  targetCard.appendChild(el("p", "card-copy", uiState.language === "zh" ? "这里更像系统当前最容易复用的学习方向。" : "This reflects the event targets the system is most likely to reuse." ));
  const eventCounts = new Map();
  filtered.forEach((rule) => {
    const key = eventTypeLabel(rule.expected_event_type);
    eventCounts.set(key, (eventCounts.get(key) || 0) + Number(rule.usage_count || 0));
  });
  const topEvents = [...eventCounts.entries()].sort((a, b) => b[1] - a[1]).slice(0, 4);
  const maxEvent = Math.max(...topEvents.map(([, count]) => count), 1);
  const eventBars = el("div", "memory-bar-list");
  topEvents.forEach(([label, count]) => {
    const row = el("div", "memory-bar-row");
    row.appendChild(el("span", "meta-label", label));
    const track = el("div", "memory-track");
    const fill = el("span", "signal-fill green");
    fill.style.width = `${Math.max(10, Math.round((count / maxEvent) * 100))}%`;
    track.appendChild(fill);
    row.appendChild(track);
    row.appendChild(el("span", "signal-value", String(count)));
    eventBars.appendChild(row);
  });
  targetCard.appendChild(eventBars);
  visualGrid.appendChild(targetCard);
  board.appendChild(visualGrid);
  filtered.forEach((rule) => {
    const card = el("article", "memory-rule-card");
    const top = el("div", "memory-rule-top");
    const titleWrap = el("div", "");
    titleWrap.appendChild(el("h4", "", `${sourceTypeLabel(rule.expected_source_type)} · ${eventTypeLabel(rule.expected_event_type)}`));
    titleWrap.appendChild(el("p", "card-copy", t("ui").memoryRuleCopy));
    top.appendChild(titleWrap);
    top.appendChild(el("span", "memory-rule-strength", uiState.language === "zh" ? `命中 ${rule.usage_count || 0} 次` : `${rule.usage_count || 0} matches`));
    card.appendChild(top);
    const patternChipRow = el("div", "chip-row");
    patternChipRow.appendChild(el("span", "chip good", uiState.language === "zh" ? "系统会在相似材料中自动复用这条经验" : "This experience will be reused for similar materials"));
    card.appendChild(patternChipRow);
    const meta = el("div", "meta-grid");
    [
      [uiState.language === "zh" ? "目标来源" : "Target source", sourceTypeLabel(rule.expected_source_type)],
      [uiState.language === "zh" ? "目标事件" : "Target event", eventTypeLabel(rule.expected_event_type)],
      [uiState.language === "zh" ? "命中次数" : "Matches", String(rule.usage_count || 0)],
      [uiState.language === "zh" ? "最近命中" : "Last matched", formatTime(rule.last_matched_at || rule.updated_at)],
    ].forEach(([label, value]) => {
      const item = el("div", "meta-item");
      item.appendChild(el("span", "meta-label", label));
      item.appendChild(el("span", "meta-value", value));
      meta.appendChild(item);
    });
    card.appendChild(meta);

    const patternGrid = el("div", "memory-pattern-grid");
    if (Array.isArray(rule.preferred_skills) && rule.preferred_skills.length) {
      const block = el("div", "memory-pattern-block");
      block.appendChild(el("span", "meta-label", t("ui").memorySavedSkillsTitle));
      block.appendChild(renderChips(rule.preferred_skills.map((skillId) => skillLabel(skillId))));
      patternGrid.appendChild(block);
    }
    if (Array.isArray(rule.header_tokens) && rule.header_tokens.length) {
      const block = el("div", "memory-pattern-block");
      block.appendChild(el("span", "meta-label", t("ui").memoryPatternTitle));
      block.appendChild(renderChips(rule.header_tokens.slice(0, 8), "note"));
      patternGrid.appendChild(block);
    }
    if (patternGrid.childNodes.length) card.appendChild(patternGrid);
    if (rule.notes) {
      const note = el("div", "meta-item");
      note.appendChild(el("span", "meta-label", uiState.language === "zh" ? "备注" : "Notes"));
      note.appendChild(el("span", "meta-value", rule.notes));
      card.appendChild(note);
    }
    board.appendChild(card);
  });
  root.appendChild(board);
}

function renderMemoryFeedback(feedback) {
  uiState.memoryFeedback = feedback;
  const root = document.getElementById("memory-feedback-output");
  root.innerHTML = "";
  if (!feedback.length) {
    root.appendChild(createEmptyState(t("ui").noMemoryFeedback));
    return;
  }
  const recent = feedback.slice(0, 5);
  const timeline = el("div", "feedback-timeline feedback-timeline-compact");
  const summary = el("div", "skill-summary-strip");
  [
    [uiState.language === "zh" ? "最近反馈" : "Recent", String(recent.length)],
    [uiState.language === "zh" ? "来源文件" : "Files", String(new Set(recent.map((item) => item.filename || item.name || "unknown")).size)],
    [uiState.language === "zh" ? "自动沉淀" : "Auto", String(recent.filter((item) => !item.manual).length)],
  ].forEach(([label, value], index) => {
    const stat = el("div", `skill-stat tone-${index + 1}`);
    stat.appendChild(el("span", "meta-label", label));
    stat.appendChild(el("span", "skill-stat-value", value));
    summary.appendChild(stat);
  });
  timeline.appendChild(summary);
  recent.forEach((item) => {
    const row = el("div", "feedback-item");
    const line = el("div", "feedback-line");
    line.appendChild(el("span", "feedback-dot", ""));
    row.appendChild(line);
    const card = el("article", "feedback-card");
    const header = el("div", "feedback-header");
    const title = el("div", "");
    title.appendChild(el("h4", "", `${sourceTypeLabel(item.expected_source_type)} · ${eventTypeLabel(item.expected_event_type)}`));
    title.appendChild(el("p", "card-copy", uiState.language === "zh" ? `这次学习来自文件：${item.filename || "未记录文件名"}` : `This learning record came from: ${item.filename || "Unknown file"}`));
    header.appendChild(title);
    header.appendChild(el("span", "feedback-time", formatTime(item.created_at)));
    card.appendChild(header);
    const meta = el("div", "meta-grid");
    [
      [uiState.language === "zh" ? "修正来源" : "Corrected source", sourceTypeLabel(item.expected_source_type)],
      [uiState.language === "zh" ? "修正事件" : "Corrected event", eventTypeLabel(item.expected_event_type)],
      [uiState.language === "zh" ? "能力数量" : "Skill count", String((item.preferred_skills || []).length)],
      [uiState.language === "zh" ? "记录类型" : "Entry type", item.notes === "manual-correction-from-intake" ? (uiState.language === "zh" ? "人工纠正" : "Manual correction") : (uiState.language === "zh" ? "自动沉淀" : "Auto observation")],
    ].forEach(([label, value]) => {
      const cell = el("div", "meta-item");
      cell.appendChild(el("span", "meta-label", label));
      cell.appendChild(el("span", "meta-value", value));
      meta.appendChild(cell);
    });
    card.appendChild(meta);
    if (Array.isArray(item.preferred_skills) && item.preferred_skills.length) {
      const skillsRow = el("div", "feedback-summary-row");
      skillsRow.appendChild(el("span", "meta-label", t("ui").memorySavedSkillsTitle));
      skillsRow.appendChild(renderChips(item.preferred_skills.map((skillId) => skillLabel(skillId))));
      card.appendChild(skillsRow);
    }
    if (item.notes) {
      const note = el("div", "meta-item");
      note.appendChild(el("span", "meta-label", uiState.language === "zh" ? "备注" : "Notes"));
      note.appendChild(el("span", "meta-value", item.notes));
      card.appendChild(note);
    }
    row.appendChild(card);
    timeline.appendChild(row);
  });
  root.appendChild(timeline);
}

function renderOverview(data) {
  uiState.overview = data;
  const root = document.getElementById("overview-output");
  root.innerHTML = "";
  const metrics = data.metrics || {};
  const library = data.skill_library || {};
  const categories = Object.entries(library.categories || {});

  const heroStrip = el("div", "hero-kpi-grid");
  [
    {
      tone: "success",
      eyebrow: "SYSTEM INTEGRITY",
      value: metrics.events_processed > 0 ? (uiState.language === "zh" ? "活跃" : "Active") : (uiState.language === "zh" ? "空闲" : "Idle"),
      suffix: uiState.language === "zh" ? "Pipeline" : "Pipeline",
      copy: metrics.events_processed > 0
        ? (uiState.language === "zh" ? `当前已处理 ${metrics.events_processed} 条事件，分析链正在持续产出新的安全判断。` : `The platform has processed ${metrics.events_processed} events and the analysis pipeline is actively producing new conclusions.`)
        : (uiState.language === "zh" ? "当前没有新的事件进入分析链，平台处于空闲状态。" : "No new events have entered the analysis pipeline, and the platform is currently idle."),
    },
    {
      tone: "cyan",
      eyebrow: "AGENT STATUS",
      value: String((data.agent?.bound_skills || []).length || 0),
      suffix: uiState.language === "zh" ? "Bound Skills" : "Bound Skills",
      copy: uiState.language === "zh"
        ? `当前模型提供方：${String(data.agent?.model_provider || "unknown").toUpperCase()}。`
        : `Current model provider: ${String(data.agent?.model_provider || "unknown").toUpperCase()}.`,
    },
    {
      tone: "violet",
      eyebrow: "SKILL COVERAGE",
      value: String(library.total_skills ?? 0),
      suffix: uiState.language === "zh" ? "Skills" : "Skills",
      copy: uiState.language === "zh"
        ? `${library.tool_backed ?? 0} 个能力已接入真实执行，覆盖 ${categories.length} 个模块。`
        : `${library.tool_backed ?? 0} skills are live across ${categories.length} modules.`,
    },
  ].forEach((item) => {
    const card = el("article", `hero-kpi-card ${item.tone}`.trim());
    card.appendChild(el("span", "hero-kpi-eyebrow", item.eyebrow));
    const value = el("div", "hero-kpi-value");
    value.appendChild(el("span", "hero-kpi-number", item.value));
    value.appendChild(el("span", "hero-kpi-suffix", item.suffix));
    card.appendChild(value);
    card.appendChild(el("p", "card-copy", item.copy));
    heroStrip.appendChild(card);
  });
  const situationalGrid = el("div", "situational-grid");
  const signalCard = el("article", "signal-card");
  signalCard.appendChild(el("h4", "", uiState.language === "zh" ? "平台态势信号" : "Platform Signal Mix"));
  signalCard.appendChild(el("p", "card-copy", uiState.language === "zh" ? "先看平台目前把重心放在哪：处理事件、生成发现、能力覆盖，还是 Agent 绑定。" : "This shows where the platform is spending its effort right now: processing events, producing findings, extending coverage, or binding agent flows."));
  const signalList = el("div", "signal-list");
  const signalEntries = [
    [uiState.language === "zh" ? "事件处理" : "Processing", Number(metrics.events_processed || 0), "cyan"],
    [uiState.language === "zh" ? "发现生成" : "Findings", Number(metrics.findings_generated || 0), "green"],
    [uiState.language === "zh" ? "能力覆盖" : "Coverage", Number(library.total_skills || 0), "violet"],
    [uiState.language === "zh" ? "Agent 绑定" : "Agent Bindings", Number((data.agent?.bound_skills || []).length || 0), "red"],
  ];
  const maxSignal = Math.max(...signalEntries.map(([, value]) => value), 1);
  signalEntries.forEach(([label, value, tone]) => {
    const row = el("div", "signal-row");
    row.appendChild(el("span", "meta-label", label));
    const track = el("div", "signal-track");
    const fill = el("span", `signal-fill ${tone}`);
    fill.style.width = `${Math.max(10, Math.round((value / maxSignal) * 100))}%`;
    track.appendChild(fill);
    row.appendChild(track);
    row.appendChild(el("span", "signal-value", String(value)));
    signalList.appendChild(row);
  });
  signalCard.appendChild(signalList);
  situationalGrid.appendChild(signalCard);

  const runCard = el("article", "summary-card");
  runCard.appendChild(el("h4", "", uiState.language === "zh" ? "当前批次状态" : "Current Run State"));
  runCard.appendChild(el("p", "card-copy", uiState.language === "zh" ? "这里看最近一次真实分析有没有顺利跑完，以及最新处理时间。" : "This shows whether the latest real analysis run completed cleanly and when it last updated."));
  const snapshotRow = el("div", "chip-row");
  snapshotRow.appendChild(el("span", "chip good", `${t("ui").overviewSnapshotTitle}: ${metrics.events_processed > 0 ? t("ui").platformActive : t("ui").platformWaiting}`));
  runCard.appendChild(snapshotRow);
  const runMeta = el("div", "kpi-strip");
  [
    [uiState.language === "zh" ? "已处理事件" : "Events processed", String(metrics.events_processed ?? 0)],
    [uiState.language === "zh" ? "已生成发现" : "Findings generated", String(metrics.findings_generated ?? 0)],
    [uiState.language === "zh" ? "最近一次处理" : "Last processed", formatTime(metrics.last_event_at)],
    [uiState.language === "zh" ? "当前状态" : "Status", metrics.events_processed > 0 ? t("ui").statusReadyAnalyze : t("ui").statusWaitingInput],
  ].forEach(([label, value]) => {
    const tile = el("div", "kpi-tile");
    tile.appendChild(el("span", "kpi-label", label));
    tile.appendChild(el("span", "kpi-value", value));
    runMeta.appendChild(tile);
  });
  runCard.appendChild(runMeta);
  const libraryCard = el("article", "summary-card");
  libraryCard.appendChild(el("h4", "", uiState.language === "zh" ? "能力覆盖" : "Capability Coverage"));
  libraryCard.appendChild(el("p", "card-copy", uiState.language === "zh" ? "这里只回答一个问题：当前平台到底已经接了多少能力，而且其中多少真的能跑。" : "This answers one question: how much capability is actually connected, and how much of it can really run."));
  const libraryMeta = el("div", "meta-grid");
  [
    [uiState.language === "zh" ? "总能力数" : "Total capabilities", String(library.total_skills ?? 0)],
    [uiState.language === "zh" ? "已接入能力" : "Active capabilities", String(library.tool_backed ?? 0)],
    [uiState.language === "zh" ? "规则保底" : "Rule-only", String((library.execution_modes || {}).rule_only ?? 0)],
    [uiState.language === "zh" ? "Agent 可选" : "Agent optional", String((library.execution_modes || {}).agent_optional ?? 0)],
  ].forEach(([label, value]) => {
    const item = el("div", "meta-item");
    item.appendChild(el("span", "meta-label", label));
    item.appendChild(el("span", "meta-value", value));
    libraryMeta.appendChild(item);
  });
  libraryCard.appendChild(libraryMeta);

  const blocks = el("div", "overview-block");
  blocks.appendChild(heroStrip);
  blocks.appendChild(situationalGrid);
  blocks.appendChild(runCard);
  blocks.appendChild(libraryCard);
  root.appendChild(blocks);
}

function renderPlannerPreview(data) {
  const root = document.getElementById("planner-output");
  root.innerHTML = "";
  if (!data) {
    root.className = "stack-list loading-copy";
    root.textContent = t("ui").waitingPreview;
    return;
  }
  root.className = "stack-list";
  const summary = el("article", "planner-card");
  summary.appendChild(el("h4", "planner-title", t("ui").plannerSummaryTitle));
  summary.appendChild(el("p", "card-copy", data.analysis_reason || t("ui").plannerSummaryCopy));
  const meta = el("div", "meta-grid");
  [
    [uiState.language === "zh" ? "事件类型" : "Event type", data.classification?.classification?.map((value) => eventTypeLabel(value)).join(" / ") || (uiState.language === "zh" ? "未识别" : "Unidentified")],
      [uiState.language === "zh" ? "优先级" : "Priority", data.classification?.priority === "high" ? (uiState.language === "zh" ? "高" : "High") : data.classification?.priority === "low" ? (uiState.language === "zh" ? "低" : "Low") : (uiState.language === "zh" ? "常规" : "Normal")],
    [uiState.language === "zh" ? "调用能力数" : "Skill count", String((data.skills_to_execute || []).length)],
    [uiState.language === "zh" ? "规划状态" : "Planning status", (data.skills_to_execute || []).length ? (uiState.language === "zh" ? "已完成" : "Ready") : (uiState.language === "zh" ? "待确认" : "Pending")],
  ].forEach(([label, value]) => {
    const item = el("div", "meta-item");
    item.appendChild(el("span", "meta-label", label));
    item.appendChild(el("span", "meta-value", value));
    meta.appendChild(item);
  });
  summary.appendChild(meta);
  if (Array.isArray(data.skills_to_execute) && data.skills_to_execute.length) {
    summary.appendChild(el("p", "card-copy", t("ui").plannerPlannedSkills));
    summary.appendChild(renderChips(data.skills_to_execute.map((skillId) => skillLabel(skillId))));
  }
  root.appendChild(summary);
}

function getNormalizedJumpServerSections(report) {
  if (!report || report.report_template !== "jumpserver_multisource_v2") return null;
  const original = Array.isArray(report.structured_sections) ? report.structured_sections : [];
  const byTitle = new Map(original.map((section) => [section.title, JSON.parse(JSON.stringify(section))]));
  const summaryParagraph = report.assessment || report.summary || "本批 JumpServer 审计样本需要继续结合多源审计日志复核。";

  const conclusion = byTitle.get("综合结论：") || { title: "综合结论：", paragraphs: [summaryParagraph], bullets: [], subsections: [] };
  if (!Array.isArray(conclusion.paragraphs) || !conclusion.paragraphs.length) conclusion.paragraphs = [summaryParagraph];

  const basis = byTitle.get("主要依据如下：") || { title: "主要依据如下：", paragraphs: [], bullets: [], subsections: [] };
  const basisMap = new Map((basis.subsections || []).map((section) => [section.title, section]));
  const basisTitles = [
    "1. 登录侧",
    "2. 命令侧",
    "3. 文件传输侧",
    "4. 操作记录侧",
  ];
  basis.subsections = basisTitles.map((title) => (
    basisMap.get(title) || { title, paragraphs: [], bullets: ["当前样本在该维度暂未补齐足够细节，建议结合原始日志继续复核。"], subsections: [] }
  ));

  const focus = byTitle.get("5. 重点高危操作账户与命令汇总") || {
    title: "5. 重点高危操作账户与命令汇总",
    paragraphs: [],
    bullets: [],
    subsections: [],
  };
  if (!Array.isArray(focus.subsections) || !focus.subsections.length) {
    focus.subsections = [{
      title: "5.1 当前样本暂未提炼出可直接归档的高危账户画像",
      paragraphs: [],
      bullets: [
        "风险范围：待继续复核",
        "判断：当前样本已经呈现多源高风险语义，但还缺少足够稳定的账户级画像，后续应继续结合用户、资产、命令、文件传输和管理平面动作补齐。",
      ],
      subsections: [],
    }];
  }

  const provenance = byTitle.get("6. 证据来源与导出链") || {
    title: "6. 证据来源与导出链",
    paragraphs: [],
    bullets: ["当前尚未从管理平面完整还原导出来源链，需要继续补齐 operation_audit 证据。"],
    subsections: [],
  };
  if (!Array.isArray(provenance.bullets) || !provenance.bullets.length) {
    provenance.bullets = ["当前尚未从管理平面完整还原导出来源链，需要继续补齐 operation_audit 证据。"];
  }

  const judgment = byTitle.get("7. 综合判断") || {
    title: "7. 综合判断",
    paragraphs: [],
    bullets: [],
    subsections: [],
  };
  const judgmentBullets = Array.isArray(judgment.bullets) ? judgment.bullets : [];
  judgment.bullets = judgmentBullets.filter((item) => {
    const text = String(item || "").trim();
    if (!text) return false;
    if (text === "当前最需要 AI 学会区分的，不是“有没有 sudo”，而是：") return false;
    if (text === "哪个用户" || text === "在哪台资产" || text === "执行了哪些高危命令" || text === "命令是否与文件传输、登录、管理平面动作串成完整链条") return false;
    if (text === "因此，") return false;
    if (text === "- 哪个用户" || text === "- 在哪台资产" || text === "- 执行了哪些高危命令" || text === "- 命令是否与文件传输、登录、管理平面动作串成完整链条") return false;
    return true;
  });
  if (!judgment.bullets.length) {
    judgment.bullets = [
      "本批样本的最终定性应为：“未发现足以直接确认外部入侵成功的证据，但已发现多组需要重点审计和治理的高风险运维操作链，以及高影响管理平面操作。后续应以用户、资产、命令、会话、文件传输和管理平面变更六个维度进行联合判断，而不能仅依赖 JumpServer 原始风险标签。”",
    ];
  }

  return [conclusion, basis, focus, provenance, judgment];
}

function renderReport(report) {
  const root = document.getElementById("report-output");
  root.innerHTML = "";
  if (!report) {
    root.className = "stack-list loading-copy";
    root.textContent = t("ui").waitingRun;
    return;
  }
  root.className = "stack-list scroll";
  const renderStructuredBulletGroups = (items, container) => {
    if (!Array.isArray(items) || !items.length) return;
    let list = null;
    let currentItem = null;
    let nestedList = null;

    const ensureList = () => {
      if (!list) {
        list = el("ul", "bullet-list");
        container.appendChild(list);
      }
    };

    items.forEach((rawItem) => {
      const text = String(rawItem || "");
      if (!text.trim()) return;
      const isNested = /^\s*-\s+/.test(text);
      if (isNested) {
        if (!currentItem) {
          ensureList();
          currentItem = el("li", "", "");
          list.appendChild(currentItem);
        }
        if (!nestedList) {
          nestedList = el("ul", "bullet-list");
          currentItem.appendChild(nestedList);
        }
        nestedList.appendChild(el("li", "", text.replace(/^\s*-\s+/, "")));
        return;
      }
      ensureList();
      currentItem = el("li", "", text);
      list.appendChild(currentItem);
      nestedList = null;
    });
  };
  const renderStructuredSections = (sections) => {
    sections.forEach((section) => {
      const card = el("article", "report-card report-section");
      card.appendChild(el("h5", "", section.title || ""));
      (section.paragraphs || []).forEach((paragraph) => {
        card.appendChild(el("p", "card-copy", paragraph));
      });
      renderStructuredBulletGroups(section.bullets, card);
      if (Array.isArray(section.subsections) && section.subsections.length) {
        const wrap = el("div", "stack-list");
        section.subsections.forEach((subsection) => {
          const block = el("div", "report-card report-section");
          block.appendChild(el("h5", "", subsection.title || ""));
          (subsection.paragraphs || []).forEach((paragraph) => {
            block.appendChild(el("p", "card-copy", paragraph));
          });
          renderStructuredBulletGroups(subsection.bullets, block);
          wrap.appendChild(block);
        });
        card.appendChild(wrap);
      }
      root.appendChild(card);
    });
  };
  const top = el("article", "report-card");
  top.appendChild(el("h4", "", t("ui").reportSummaryTitle));
  top.appendChild(el("p", "card-copy", report.assessment || report.summary || t("ui").noSummary));
  const meta = el("div", "meta-grid");
  [
    [uiState.language === "zh" ? "结论类型" : "Verdict", report.verdict || "needs_review"],
    [uiState.language === "zh" ? "风险级别" : "Risk level", report.top_risk_label || "info"],
    [uiState.language === "zh" ? "风险分数" : "Risk score", String(report.overall_risk_score ?? 0)],
    [uiState.language === "zh" ? "发现数量" : "Finding count", String((report.findings || []).length)],
    [uiState.language === "zh" ? "执行模式" : "Execution mode", executionModeLabel(report.execution_mode || "rule_only")],
  ].forEach(([label, value]) => {
    const item = el("div", "meta-item");
    item.appendChild(el("span", "meta-label", label));
    item.appendChild(el("span", "meta-value", value));
    meta.appendChild(item);
  });
  top.appendChild(meta);
  if (Array.isArray(report.skills_selected) && report.skills_selected.length) {
    top.appendChild(el("p", "card-copy", uiState.language === "zh" ? "本次主要分析路径" : "Primary analysis path"));
    top.appendChild(renderChips(report.skills_selected.map((skillId) => skillLabel(skillId))));
  }
  if (report.execution_mode === "agent_augmented" && report.agent_context?.provider) {
    top.appendChild(
      el(
        "p",
        "section-note",
        uiState.language === "zh"
          ? `这次报告由 Agent 增强生成，模型提供方为 ${String(report.agent_context.provider).toUpperCase()}。`
          : `This report used Agent augmentation via ${String(report.agent_context.provider).toUpperCase()}.`,
      ),
    );
  }
  root.appendChild(top);

  const normalizedJumpServerSections = getNormalizedJumpServerSections(report);
  if (normalizedJumpServerSections && normalizedJumpServerSections.length) {
    renderStructuredSections(normalizedJumpServerSections);
    return;
  }

  if (report.event_type === "host_baseline_assessment") {
    const hostBaselineNarrative = {
      filesystem_isolation_issue: {
        zh: {
          title: "/var/log/audit 未单独分区",
          reason: "审计日志目录未使用独立分区，可能导致日志填满磁盘并影响系统稳定性。",
          impacts: ["日志耗尽攻击", "审计日志丢失", "系统稳定性降低"],
          recommendation: "为 /var/log/audit 创建独立分区并启用日志轮转。",
          level: "Medium",
        },
        en: {
          title: "/var/log/audit is not isolated",
          reason: "Audit logs are not on a dedicated partition, which can increase log-exhaustion and stability risk.",
          impacts: ["Log exhaustion", "Audit log loss", "System instability"],
          recommendation: "Create a dedicated partition for /var/log/audit and enable log rotation.",
          level: "Medium",
        },
      },
      temporary_directory_configuration: {
        zh: {
          title: "/var/tmp 未单独分区",
          reason: "临时目录未隔离，可能被滥用执行恶意脚本或用于临时文件劫持。",
          impacts: ["权限提升", "临时文件劫持"],
          recommendation: "为 /var/tmp 启用 nodev、nosuid、noexec 挂载参数。",
          level: "Medium",
        },
        en: {
          title: "/var/tmp is not isolated",
          reason: "The temporary directory is not isolated, increasing the risk of script abuse or temporary file hijacking.",
          impacts: ["Privilege escalation", "Temporary file hijacking"],
          recommendation: "Apply nodev, nosuid, and noexec mount flags to /var/tmp.",
          level: "Medium",
        },
      },
      log_permission_configuration: {
        zh: {
          title: "日志文件权限未正确配置",
          reason: "日志权限过宽或审计组件缺失，可能导致敏感信息泄露或日志篡改。",
          impacts: ["敏感信息泄露", "日志篡改", "审计能力不足"],
          recommendation: "收紧关键日志权限，并补齐 auditd 等审计组件。",
          level: "Medium",
        },
        en: {
          title: "Log permissions are too weak",
          reason: "Overly broad log permissions or missing audit components can expose sensitive data and weaken integrity.",
          impacts: ["Information disclosure", "Log tampering", "Reduced audit coverage"],
          recommendation: "Tighten critical log permissions and restore audit components such as auditd.",
          level: "Medium",
        },
      },
      unused_filesystem_modules: {
        zh: {
          title: "不必要文件系统模块已启用",
          reason: "未使用的文件系统模块会扩大主机攻击面，并可能被利用加载恶意镜像。",
          impacts: ["攻击面扩大", "恶意镜像加载风险"],
          recommendation: "禁用 cramfs、udf 等未使用文件系统模块。",
          level: "Low",
        },
        en: {
          title: "Unused filesystem modules are enabled",
          reason: "Unused filesystem modules increase attack surface and may help malicious image-loading paths.",
          impacts: ["Expanded attack surface", "Malicious image loading risk"],
          recommendation: "Disable unused filesystem modules such as cramfs and udf.",
          level: "Low",
        },
      },
    };

    const findingsCard = el("article", "report-card report-section");
    findingsCard.appendChild(el("h5", "", uiState.language === "zh" ? "关键安全发现" : "Key Security Findings"));
    const findingsWrap = el("div", "stack-list");
    (report.findings || []).forEach((finding, index) => {
      const narrative = hostBaselineNarrative[finding.risk_type]?.[uiState.language] || null;
      const block = el("div", "report-card report-section");
      block.appendChild(el("h5", "", `${index + 1}. ${narrative?.title || finding.summary}`));
      const evidenceValues = [];
      (finding.evidence || []).forEach((entry) => {
        Object.values(entry).forEach((value) => {
          if (Array.isArray(value)) evidenceValues.push(...value);
          else evidenceValues.push(String(value));
        });
      });
      if (narrative?.reason) {
        block.appendChild(el("p", "card-copy", `${uiState.language === "zh" ? "风险原因" : "Risk reason"}：${narrative.reason}`));
      }
      if (narrative?.impacts?.length) {
        block.appendChild(el("p", "card-copy", uiState.language === "zh" ? "潜在影响：" : "Potential impact:"));
        const impactList = el("ul", "bullet-list");
        narrative.impacts.forEach((item) => impactList.appendChild(el("li", "", item)));
        block.appendChild(impactList);
      }
      if (evidenceValues.length) {
        block.appendChild(el("p", "card-copy", uiState.language === "zh" ? "对应记录：" : "Observed records:"));
        const list = el("ul", "bullet-list");
        evidenceValues.slice(0, 4).forEach((item) => list.appendChild(el("li", "", String(item))));
        block.appendChild(list);
      }
      block.appendChild(el("p", "card-copy", `${uiState.language === "zh" ? "风险等级" : "Risk level"}：${narrative?.level || finding.risk_label}`));
      if (narrative?.recommendation || finding.recommendations?.length) {
        block.appendChild(el("p", "card-copy", `${uiState.language === "zh" ? "建议" : "Recommendation"}：${narrative?.recommendation || finding.recommendations[0]}`));
      }
      findingsWrap.appendChild(block);
    });
    findingsCard.appendChild(findingsWrap);
    root.appendChild(findingsCard);

    const riskCard = el("article", "report-card report-section");
    riskCard.appendChild(el("h5", "", uiState.language === "zh" ? "综合风险评估" : "Comprehensive Risk Assessment"));
    const riskMeta = el("div", "meta-grid");
    [
      [uiState.language === "zh" ? "配置风险" : "Configuration risk", uiState.language === "zh" ? "存在" : "Present"],
      [uiState.language === "zh" ? "攻击行为" : "Active attack", uiState.language === "zh" ? "未发现" : "Not observed"],
      [uiState.language === "zh" ? "权限风险" : "Privilege risk", uiState.language === "zh" ? "中等" : "Moderate"],
      [uiState.language === "zh" ? "综合等级" : "Overall level", report.top_risk_label || "medium"],
    ].forEach(([label, value]) => {
      const item = el("div", "meta-item");
      item.appendChild(el("span", "meta-label", label));
      item.appendChild(el("span", "meta-value", value));
      riskMeta.appendChild(item);
    });
    riskCard.appendChild(riskMeta);
    root.appendChild(riskCard);

    const actionsCard = el("article", "report-card report-section");
    actionsCard.appendChild(el("h5", "", uiState.language === "zh" ? "建议行动" : "Recommended Actions"));
    const actionGroups = [
      [uiState.language === "zh" ? "高优先级" : "High Priority", (report.recommended_actions || []).slice(0, 1)],
      [uiState.language === "zh" ? "中优先级" : "Medium Priority", (report.recommended_actions || []).slice(1, 3)],
      [uiState.language === "zh" ? "低优先级" : "Low Priority", (report.recommended_actions || []).slice(3, 5)],
    ];
    actionGroups.forEach(([title, items]) => {
      if (!items.length) return;
      actionsCard.appendChild(el("p", "card-copy", title));
      const list = el("ul", "bullet-list");
      items.forEach((item) => list.appendChild(el("li", "", item)));
      actionsCard.appendChild(list);
    });
    root.appendChild(actionsCard);
    return;
  }

  const narrative = [];
  if (report.professional_judgment) narrative.push(report.professional_judgment);
  if (Array.isArray(report.key_facts) && report.key_facts.length) narrative.push(report.key_facts[0]);
  if (Array.isArray(report.probable_causes) && report.probable_causes.length) narrative.push(report.probable_causes[0]);
  if (Array.isArray(report.recommended_actions) && report.recommended_actions.length) narrative.push(report.recommended_actions[0]);
  if (narrative.length) {
    const note = el("article", "report-card report-section emphasis");
    note.appendChild(el("h5", "", uiState.language === "zh" ? "分析摘要" : "Analyst Summary"));
    note.appendChild(el("p", "", narrative.join(uiState.language === "zh" ? " " : " ")));
    root.appendChild(note);
  }

  if (Array.isArray(report.evidence_highlights) && report.evidence_highlights.length) {
    const evidence = el("article", "report-card report-section");
    evidence.appendChild(el("h5", "", t("ui").reportEvidenceTitle));
    const list = el("ul", "bullet-list");
    report.evidence_highlights.forEach((item) => list.appendChild(el("li", "", item)));
    evidence.appendChild(list);
    root.appendChild(evidence);
  }

  if (Array.isArray(report.recommended_actions) && report.recommended_actions.length) {
    const nextSteps = el("article", "report-card report-section");
    nextSteps.appendChild(el("h5", "", t("ui").reportNextStepsTitle));
    const list = el("ul", "bullet-list");
    report.recommended_actions.slice(0, 5).forEach((item) => list.appendChild(el("li", "", item)));
    nextSteps.appendChild(list);
    root.appendChild(nextSteps);
  }

  const sections = [
    [t("ui").reportReasonTitle, report.why_flagged],
    [t("ui").reportFactsTitle, report.key_facts],
    [t("ui").reportCauseTitle, report.probable_causes],
    [t("ui").reportChecksTitle, report.quick_checks],
    [t("ui").reportEscalationTitle, report.escalation_conditions],
    [t("ui").reportJudgmentTitle, report.professional_judgment],
  ];
  sections.forEach(([title, value]) => {
    if (!value || (Array.isArray(value) && !value.length)) return;
    const section = el("article", "report-card report-section");
    section.appendChild(el("h5", "", title));
    if (Array.isArray(value)) {
      const list = el("ul", "bullet-list");
      value.forEach((item) => list.appendChild(el("li", "", item)));
      section.appendChild(list);
    } else {
      section.appendChild(el("p", "", value));
    }
    root.appendChild(section);
  });
}

function reportDownloadName(report) {
  const safeType = String(report?.event_type || "security_report").replace(/[^a-zA-Z0-9_-]+/g, "_");
  const timestamp = String(report?.generated_at || new Date().toISOString()).replace(/[:.]/g, "-");
  return `${safeType}_${timestamp}.md`;
}

function pushBulletSection(lines, title, items) {
  if (!Array.isArray(items) || !items.length) return;
  lines.push(`## ${title}`);
  lines.push("");
  items.forEach((item) => lines.push(`- ${item}`));
  lines.push("");
}

function flattenEvidence(finding) {
  const values = [];
  (finding?.evidence || []).forEach((entry) => {
    if (!entry || typeof entry !== "object") return;
    Object.values(entry).forEach((value) => {
      if (Array.isArray(value)) values.push(...value.map((item) => String(item)));
      else if (value !== null && value !== undefined && String(value).trim()) values.push(String(value));
    });
  });
  return values.slice(0, 5);
}

function buildHostBaselineDownload(report) {
  const lines = [];
  lines.push("# 主机基线分析报告");
  lines.push("");
  lines.push("## 结论判断");
  lines.push("");
  lines.push(report.assessment || report.summary || "");
  lines.push("");
  lines.push(`- 风险级别：${String(report.top_risk_label || "medium").toUpperCase()}`);
  lines.push(`- 风险分数：${report.overall_risk_score ?? 0}`);
  lines.push("");
  lines.push("## 关键安全发现");
  lines.push("");
  (report.findings || []).forEach((finding, index) => {
    lines.push(`### ${index + 1}. ${finding.summary}`);
    lines.push("");
    const evidence = flattenEvidence(finding);
    if (evidence.length) {
      lines.push("- 对应记录：");
      evidence.forEach((item) => lines.push(`  - ${item}`));
    }
    if (finding.recommendations?.length) {
      lines.push("- 建议动作：");
      finding.recommendations.forEach((item) => lines.push(`  - ${item}`));
    }
    lines.push("");
  });
  pushBulletSection(lines, "综合风险评估", report.key_facts);
  pushBulletSection(lines, "建议行动", report.recommended_actions);
  if (report.professional_judgment) {
    lines.push("## 专业判断");
    lines.push("");
    lines.push(report.professional_judgment);
    lines.push("");
  }
  return `${lines.join("\n").trim()}\n`;
}

function buildJumpServerDownload(report) {
  const lines = [];
  const pushStructuredBulletLines = (items) => {
    if (!Array.isArray(items) || !items.length) return;
    items.forEach((item) => {
      const text = String(item || "");
      if (!text.trim()) return;
      if (/^\s*-\s+/.test(text)) {
        lines.push(`  - ${text.replace(/^\s*-\s+/, "")}`);
      } else {
        lines.push(`- ${text}`);
      }
    });
    lines.push("");
  };
  const normalizedJumpServerSections = getNormalizedJumpServerSections(report);
  if (normalizedJumpServerSections && normalizedJumpServerSections.length) {
    normalizedJumpServerSections.forEach((section) => {
      lines.push(section.title || "");
      lines.push("");
      (section.paragraphs || []).forEach((paragraph) => {
        lines.push(paragraph);
        lines.push("");
      });
      pushStructuredBulletLines(section.bullets);
      if (Array.isArray(section.subsections) && section.subsections.length) {
        section.subsections.forEach((subsection) => {
          lines.push(subsection.title || "");
          lines.push("");
          (subsection.paragraphs || []).forEach((paragraph) => {
            lines.push(paragraph);
            lines.push("");
          });
          pushStructuredBulletLines(subsection.bullets);
        });
      }
    });
  } else {
    lines.push("综合结论：");
    lines.push("");
    lines.push(report.assessment || report.summary || "");
    lines.push("");
    lines.push(`- 结论类型：${report.verdict || "needs_review"}`);
    lines.push(`- 风险级别：${String(report.top_risk_label || "high").toUpperCase()}`);
    lines.push(`- 执行模式：${executionModeLabel(report.execution_mode || "rule_only")}`);
    lines.push(`- 分析能力：${(report.skills_selected || []).map((item) => skillLabel(item)).join(" / ")}`);
    lines.push("");
    pushBulletSection(lines, "关键事实", report.key_facts);
    pushBulletSection(lines, "可能原因", report.probable_causes);
    lines.push("重点关联链");
    lines.push("");
    (report.findings || []).forEach((finding, index) => {
      lines.push(`${index + 1}. ${finding.summary}`);
      lines.push("");
      const evidence = flattenEvidence(finding);
      if (evidence.length) {
        lines.push("- 关联证据：");
        evidence.forEach((item) => lines.push(`  - ${item}`));
      }
      if (finding.affected_assets?.length) {
        lines.push(`- 影响对象：${finding.affected_assets.join("、")}`);
      }
      if (finding.recommendations?.length) {
        lines.push("- 建议动作：");
        finding.recommendations.forEach((item) => lines.push(`  - ${item}`));
      }
      lines.push("");
    });
    pushBulletSection(lines, "快速核查", report.quick_checks);
    pushBulletSection(lines, "升级条件", report.escalation_conditions);
    if (report.professional_judgment) {
      lines.push("专业判断");
      lines.push("");
      lines.push(report.professional_judgment);
      lines.push("");
    }
  }
  return `${lines.join("\n").trim()}\n`;
}

function buildEndpointDownload(report) {
  const lines = [];
  lines.push("# 端点安全事件分析报告");
  lines.push("");
  lines.push("## 结论判断");
  lines.push("");
  lines.push(report.assessment || report.summary || "");
  lines.push("");
  lines.push(`- 风险级别：${String(report.top_risk_label || "info").toUpperCase()}`);
  lines.push(`- 发现数量：${(report.findings || []).length}`);
  lines.push("");
  pushBulletSection(lines, "关键事实", report.key_facts);
  pushBulletSection(lines, "关键证据", report.evidence_highlights);
  pushBulletSection(lines, "建议动作", report.recommended_actions);
  if (report.professional_judgment) {
    lines.push("## 专业判断");
    lines.push("");
    lines.push(report.professional_judgment);
    lines.push("");
  }
  return `${lines.join("\n").trim()}\n`;
}

function buildWhiteboxDownload(report) {
  const titleMap = {
    whitebox_recon_assessment: "应用白盒侦察报告",
    whitebox_exploit_validation: "应用白盒验证报告",
    whitebox_security_report: "应用白盒综合安全报告",
  };
  const lines = [];
  lines.push(`# ${titleMap[report.event_type] || "应用白盒分析报告"}`);
  lines.push("");
  lines.push("## 结论摘要");
  lines.push("");
  lines.push(report.assessment || report.summary || "");
  lines.push("");
  pushBulletSection(lines, "关键事实", report.key_facts);
  pushBulletSection(lines, "可能原因", report.probable_causes);
  if (Array.isArray(report.findings) && report.findings.length) {
    lines.push("## 发现清单");
    lines.push("");
    report.findings.forEach((finding, index) => {
      lines.push(`### ${index + 1}. ${finding.summary}`);
      lines.push("");
      flattenEvidence(finding).forEach((item) => lines.push(`- ${item}`));
      lines.push("");
    });
  }
  pushBulletSection(lines, "建议动作", report.recommended_actions);
  if (report.professional_judgment) {
    lines.push("## 专业判断");
    lines.push("");
    lines.push(report.professional_judgment);
    lines.push("");
  }
  return `${lines.join("\n").trim()}\n`;
}

function buildGenericDownload(report) {
  const lines = [];
  lines.push("# 安全报告");
  lines.push("");
  lines.push(`- 事件类型：\`${report.event_type || "unknown"}\``);
  lines.push(`- 来源类型：\`${report.source_type || "unknown"}\``);
  lines.push(`- 结论类型：\`${report.verdict || "needs_review"}\``);
  lines.push(`- 风险级别：\`${report.top_risk_label || "info"}\``);
  lines.push("");
  lines.push("## 结论判断");
  lines.push("");
  lines.push(report.assessment || report.summary || "");
  lines.push("");
  pushBulletSection(lines, "关键事实", report.key_facts);
  pushBulletSection(lines, "建议动作", report.recommended_actions);
  if (report.professional_judgment) {
    lines.push("## 专业判断");
    lines.push("");
    lines.push(report.professional_judgment);
    lines.push("");
  }
  return `${lines.join("\n").trim()}\n`;
}

function buildDownloadableReportText(report) {
  if (!report) return "";
  if (report.event_type === "host_baseline_assessment") return buildHostBaselineDownload(report);
  if (["jumpserver_multi_source_audit", "login_auth_review", "jumpserver_command_review", "jumpserver_transfer_review", "jumpserver_operation_review"].includes(report.event_type)) {
    return buildJumpServerDownload(report);
  }
  if (report.source_type === "endpoint" || report.event_type === "endpoint_process") return buildEndpointDownload(report);
  if (["whitebox_recon_assessment", "whitebox_exploit_validation", "whitebox_security_report"].includes(report.event_type)) {
    return buildWhiteboxDownload(report);
  }
  return buildGenericDownload(report);
}

function downloadCurrentReport() {
  if (!intakeState.report) return;
  const blob = new Blob([buildDownloadableReportText(intakeState.report)], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = reportDownloadName(intakeState.report);
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
}

function renderFileRuns(batch) {
  const root = document.getElementById("file-runs-output");
  root.innerHTML = "";
  if (batch?.pendingFiles?.length) {
    root.className = "stack-list";
    root.appendChild(
      el(
        "p",
        "section-note",
        uiState.language === "zh"
          ? `当前已上传 ${batch.pendingFiles.length} 个文件，等待点击“归一化后分析”开始处理。`
          : `${batch.pendingFiles.length} file(s) uploaded and waiting for “Normalize + Analyze”.`
      )
    );
    batch.pendingFiles.forEach((name) => {
      const card = el("article", "run-card");
      card.appendChild(el("h5", "", name));
      card.appendChild(
        el(
          "p",
          "card-copy",
          uiState.language === "zh" ? "文件已进入当前会话，但还没有开始分析。" : "The file is staged in the current session and has not been analyzed yet."
        )
      );
      root.appendChild(card);
    });
    return;
  }
  if (!batch || !batch.results?.length) {
    root.className = "stack-list loading-copy";
    root.textContent = t("ui").uploadRunsWaiting;
    return;
  }
  root.className = "stack-list scroll";
  root.appendChild(el("p", "section-note", t("ui").fileRunsSummaryCopy));
  batch.results.forEach((item) => {
    const card = el("article", "run-card");
    card.appendChild(el("h5", "", item.filename || (uiState.language === "zh" ? "未命名文件" : "Unnamed file")));
    card.appendChild(
      el(
        "p",
        "card-copy",
        uiState.language === "zh"
          ? `${sourceTypeLabel(item.normalized_event?.source_type)} -> ${eventTypeLabel(item.normalized_event?.event_type)}，本次共分配 ${(item.planner_preview?.skills_to_execute || []).length} 个能力。`
          : `${sourceTypeLabel(item.normalized_event?.source_type)} -> ${eventTypeLabel(item.normalized_event?.event_type)}, with ${(item.planner_preview?.skills_to_execute || []).length} planned skill(s).`
      )
    );
    const meta = el("div", "meta-grid");
    [
      [uiState.language === "zh" ? "风险级别" : "Risk level", item.report?.top_risk_label || "info"],
      [uiState.language === "zh" ? "风险分数" : "Risk score", String(item.report?.overall_risk_score ?? 0)],
      [uiState.language === "zh" ? "解析方式" : "Parser", item.raw_event?.payload?.parser_profile === "csv-tabular" ? "CSV" : item.raw_event?.payload?.parser_profile === "pdf-text" ? "PDF" : item.raw_event?.payload?.parser_profile === "json-structured" ? "JSON" : (item.raw_event?.payload?.parser_profile || "generic")],
      [uiState.language === "zh" ? "发现数量" : "Finding count", String((item.report?.findings || []).length)],
    ].forEach(([label, value]) => {
      const m = el("div", "meta-item");
      m.appendChild(el("span", "meta-label", label));
      m.appendChild(el("span", "meta-value", value));
      meta.appendChild(m);
    });
    card.appendChild(meta);
    if (item.planner_preview?.skills_to_execute?.length) {
      card.appendChild(renderChips(item.planner_preview.skills_to_execute.map((skillId) => skillLabel(skillId))));
    }
    root.appendChild(card);
  });
}

function persistRawInput() {
  return;
}

function renderNormalizeOutput(data) {
  const output = document.getElementById("normalize-output");
  if (!data) {
    output.textContent = t("ui").waitingInput;
    return;
  }
  output.textContent = "";
  const wrapper = document.createElement("div");
  wrapper.className = "stack-list";

  const card = el("article", "normalize-card");
  card.appendChild(el("h4", "", t("ui").normalizeSummaryTitle));
  card.appendChild(el("p", "card-copy", t("ui").normalizeSummaryCopy));
  const meta = el("div", "meta-grid");
  [
    [uiState.language === "zh" ? "事件 ID" : "Event ID", data.event_id || (uiState.language === "zh" ? "未生成" : "Not generated")],
    [uiState.language === "zh" ? "事件类型" : "Event type", eventTypeLabel(data.event_type)],
    [uiState.language === "zh" ? "来源类型" : "Source type", sourceTypeLabel(data.source_type)],
    [uiState.language === "zh" ? "事件时间" : "Timestamp", formatTime(data.timestamp)],
    [uiState.language === "zh" ? "资产名称" : "Asset name", data.asset_context?.asset_name || (uiState.language === "zh" ? "未提供" : "Not provided")],
    [uiState.language === "zh" ? "环境" : "Environment", data.asset_context?.environment || "unknown"],
  ].forEach(([label, value]) => {
    const item = el("div", "meta-item");
    item.appendChild(el("span", "meta-label", label));
    item.appendChild(el("span", "meta-value", String(value)));
    meta.appendChild(item);
  });
  card.appendChild(meta);

  const highlights = [];
  if (data.normalized_data?.filename) highlights.push(uiState.language === "zh" ? `文件：${data.normalized_data.filename}` : `File: ${data.normalized_data.filename}`);
  if (data.normalized_data?.parser_profile) highlights.push(uiState.language === "zh" ? `解析方式：${data.normalized_data.parser_profile}` : `Parser: ${data.normalized_data.parser_profile}`);
  if (data.normalized_data?.row_count !== undefined) highlights.push(uiState.language === "zh" ? `记录数：${data.normalized_data.row_count}` : `Rows: ${data.normalized_data.row_count}`);
  if (data.normalized_data?.target) highlights.push(uiState.language === "zh" ? `目标：${data.normalized_data.target}` : `Target: ${data.normalized_data.target}`);
  if (highlights.length) {
    card.appendChild(el("p", "card-copy", uiState.language === "zh" ? "已提取关键信息" : "Extracted highlights"));
    card.appendChild(renderChips(highlights, "note"));
  }

  const details = document.createElement("details");
  details.className = "details-block";
  const summary = document.createElement("summary");
  summary.textContent = uiState.language === "zh" ? "查看完整标准化结构" : "View full normalized structure";
  details.appendChild(summary);
  const pre = document.createElement("pre");
  pre.textContent = JSON.stringify(data, null, 2);
  details.appendChild(pre);
  card.appendChild(details);

  wrapper.appendChild(card);
  output.replaceChildren(wrapper);
}

function localizedRecentReportTitle(report) {
  if (uiState.language === "zh") return report.report_title || "最近分析结论";
  const map = {
    login_auth_review: "JumpServer Login Audit",
    jumpserver_command_review: "JumpServer Command Audit",
    jumpserver_transfer_review: "JumpServer File Transfer Audit",
    jumpserver_operation_review: "JumpServer Control Plane Audit",
    jumpserver_multi_source_audit: "JumpServer Composite Audit",
    host_baseline_assessment: "Host Baseline Assessment",
    endpoint_process: "Endpoint Security Review",
    whitebox_security_report: "Whitebox Security Report",
    whitebox_recon_assessment: "Whitebox Recon Report",
    whitebox_exploit_validation: "Whitebox Validation Report",
  };
  return map[report.event_type] || report.report_title || "Recent Assessment";
}

function localizedRecentReportCopy(report) {
  if (uiState.language === "zh") {
    return report.professional_judgment || report.assessment || report.summary || "暂无摘要。";
  }
  const findings = (report.findings || []).length;
  const risk = String(report.top_risk_label || "info").toLowerCase();
  const mode = executionModeLabel(report.execution_mode || "rule_only");
  const generic = `This report is currently classified as ${risk} risk, with ${findings} finding(s), generated via ${mode}.`;
  const byEvent = {
    login_auth_review: `This login audit highlights authentication outcomes and surrounding access context. Treat it as access evidence, not proof of compromise by itself. ${generic}`,
    jumpserver_command_review: `This command audit focuses on privileged execution, service control, remote operations, downloads, and binary execution patterns. ${generic}`,
    jumpserver_transfer_review: `This transfer audit focuses on uploaded artifacts, landing paths, permission changes, and follow-on execution signals. ${generic}`,
    jumpserver_operation_review: `This control-plane audit focuses on export actions, account or host creation, authorization changes, and other high-impact administrative events. ${generic}`,
    jumpserver_multi_source_audit: `This composite JumpServer audit correlates login, command, transfer, and control-plane activity to surface high-risk operation chains that need session-level review. ${generic}`,
    host_baseline_assessment: `This report reflects baseline and configuration weakness rather than active intrusion, and should be read as a governance and hardening signal. ${generic}`,
    endpoint_process: `This endpoint review summarizes process-side security signals and prioritizes host-level follow-up. ${generic}`,
    whitebox_security_report: `This whitebox report consolidates application findings into a security assessment with prioritized follow-up. ${generic}`,
    whitebox_recon_assessment: `This whitebox recon report summarizes externally observable application exposure and verification leads. ${generic}`,
    whitebox_exploit_validation: `This whitebox validation report summarizes exploitability checks and evidence quality. ${generic}`,
  };
  return byEvent[report.event_type] || generic;
}

function renderReports(reports) {
  uiState.reports = reports;
  const root = document.getElementById("reports-output");
  root.innerHTML = "";
  if (!reports.length) {
    root.appendChild(createEmptyState(t("ui").noReports));
    return;
  }
  const board = el("div", "reports-board");
  reports.slice(0, 5).forEach((report) => {
    const riskClass = ["critical", "high"].includes(String(report.top_risk_label || "").toLowerCase()) ? "report-card-alert" : ["medium"].includes(String(report.top_risk_label || "").toLowerCase()) ? "report-card-watch" : "report-card-calm";
    const card = el("article", `report-card ${report === reports[0] ? "priority" : ""} ${riskClass}`.trim());
    card.appendChild(el("h4", "", localizedRecentReportTitle(report)));
    card.appendChild(el("p", "card-copy", localizedRecentReportCopy(report)));
    const snapshot = el("div", "chip-row");
    snapshot.appendChild(el("span", "chip latest", `${t("ui").reportSnapshotTitle}: ${report.verdict || "needs_review"}`));
    snapshot.appendChild(el("span", `chip ${["critical", "high"].includes(String(report.top_risk_label || "").toLowerCase()) ? "report-chip-alert" : ["medium"].includes(String(report.top_risk_label || "").toLowerCase()) ? "report-chip-watch" : "report-chip-calm"}`.trim(), `${uiState.language === "zh" ? "风险" : "Risk"}: ${report.top_risk_label || "info"}`));
    card.appendChild(snapshot);
    const kpis = el("div", "kpi-strip");
    [
      [uiState.language === "zh" ? "风险级别" : "Risk level", report.top_risk_label || "info"],
      [uiState.language === "zh" ? "风险分数" : "Risk score", String(report.overall_risk_score ?? 0)],
      [uiState.language === "zh" ? "发现数量" : "Finding count", String((report.findings || []).length)],
      [uiState.language === "zh" ? "报告时间" : "Reported at", formatTime(report.generated_at || report.created_at)],
    ].forEach(([label, value]) => {
      const tile = el("div", "kpi-tile");
      tile.appendChild(el("span", "kpi-label", label));
      tile.appendChild(el("span", "kpi-value", value));
      kpis.appendChild(tile);
    });
    card.appendChild(kpis);
    if (report === reports[0]) {
      const latest = el("div", "chip-row");
      latest.appendChild(el("span", "chip latest", t("ui").latest));
      card.appendChild(latest);
    }
    if (Array.isArray(report.skills_selected) && report.skills_selected.length) {
      card.appendChild(el("p", "card-copy", t("ui").reportsPathTitle));
      card.appendChild(renderChips(report.skills_selected.map((skillId) => skillLabel(skillId)), "skill-accent"));
    }
    board.appendChild(card);
  });
  root.appendChild(board);
}

function renderInvestigations(items) {
  uiState.investigations = items;
  const root = document.getElementById("investigations-output");
  root.innerHTML = "";
  const grouped = [];
  const seen = new Set();
  const isCompositeInvestigationFile = (file) => file && file.source_type === "jumpserver" && file.event_type === "jumpserver_multi_source_audit";
  items.forEach((item) => {
    const firstFile = (item.files || []).find((file) => !isCompositeInvestigationFile(file)) || item.files?.[0] || {};
    const key = [
      firstFile.filename || "unknown",
      firstFile.event_type || "unknown",
      firstFile.source_type || "unknown",
    ].join("|");
    if (seen.has(key)) return;
    seen.add(key);
    grouped.push(item);
  });
  if (!grouped.length) {
    root.appendChild(createEmptyState(t("ui").noInvestigations));
    return;
  }
  grouped.slice(0, 4).forEach((item) => {
    const visibleFiles = (item.files || []).filter((file) => !isCompositeInvestigationFile(file));
    const firstFile = visibleFiles[0] || item.files?.[0] || {};
    const uploadedCount = item.result_count
      ? Number(item.file_count || visibleFiles.length || 0)
      : (visibleFiles.length || Number(item.file_count || 0));
    const resultCount = item.result_count
      ? Number(item.result_count || 0)
      : Number((item.files || []).length || item.file_count || 0);
    const compositeCount = Math.max(0, resultCount - uploadedCount);
    const sourceCategoryCount = new Set(
      visibleFiles.map((file) => file?.source_type).filter(Boolean)
    ).size;
    const card = el("article", "investigation-card");
    card.appendChild(el("h4", "", firstFile.filename || item.name || "未命名调查"));
    card.appendChild(
      el(
        "p",
        "card-copy",
        uiState.language === "zh"
          ? compositeCount > 0
            ? sourceCategoryCount > 0 && sourceCategoryCount !== uploadedCount
              ? `${sourceTypeLabel(firstFile.source_type)} 材料已经进入 ${eventTypeLabel(firstFile.event_type)} 调查链路；本批次上传 ${uploadedCount} 个文件，覆盖 ${sourceCategoryCount} 类场景，生成 ${resultCount} 条结果（含 ${compositeCount} 条综合结果）。`
              : `${sourceTypeLabel(firstFile.source_type)} 材料已经进入 ${eventTypeLabel(firstFile.event_type)} 调查链路；本批次上传 ${uploadedCount} 个文件，生成 ${resultCount} 条结果（含 ${compositeCount} 条综合结果）。`
            : `${sourceTypeLabel(firstFile.source_type)} 材料已经进入 ${eventTypeLabel(firstFile.event_type)} 调查链路；本批次上传 ${uploadedCount} 个文件，生成 ${resultCount} 条结果。`
          : compositeCount > 0
            ? sourceCategoryCount > 0 && sourceCategoryCount !== uploadedCount
              ? `${sourceTypeLabel(firstFile.source_type)} material entered the ${eventTypeLabel(firstFile.event_type)} investigation path; this batch uploaded ${uploadedCount} file(s), covered ${sourceCategoryCount} source category(ies), and produced ${resultCount} result(s), including ${compositeCount} composite result(s).`
              : `${sourceTypeLabel(firstFile.source_type)} material entered the ${eventTypeLabel(firstFile.event_type)} investigation path; this batch uploaded ${uploadedCount} file(s) and produced ${resultCount} result(s), including ${compositeCount} composite result(s).`
            : `${sourceTypeLabel(firstFile.source_type)} material entered the ${eventTypeLabel(firstFile.event_type)} investigation path; this batch uploaded ${uploadedCount} file(s) and produced ${resultCount} result(s).`
      )
    );
    const meta = el("div", "meta-grid");
    [
      [uiState.language === "zh" ? "最高风险" : "Top risk", item.top_risk_label || "info"],
      [uiState.language === "zh" ? "最高分数" : "Top score", String(item.top_risk_score ?? 0)],
      [uiState.language === "zh" ? "涉及能力数" : "Skills used", String((item.skills_seen || []).length)],
      [uiState.language === "zh" ? "创建时间" : "Created at", formatTime(item.created_at)],
    ].forEach(([label, value]) => {
      const cell = el("div", "meta-item");
      cell.appendChild(el("span", "meta-label", label));
      cell.appendChild(el("span", "meta-value", value));
      meta.appendChild(cell);
    });
    card.appendChild(meta);
    if (item === grouped[0]) {
      const latest = el("div", "chip-row");
      latest.appendChild(el("span", "chip latest", t("ui").latest));
      card.appendChild(latest);
    }
    if (Array.isArray(item.skills_seen) && item.skills_seen.length) {
      card.appendChild(el("p", "card-copy", t("ui").investigationsEnginesTitle));
      card.appendChild(renderChips(item.skills_seen.map((skillId) => skillLabel(skillId))));
    }
    root.appendChild(card);
  });
}

function renderHistory(data) {
  uiState.history = data;
  const root = document.getElementById("history-output");
  root.innerHTML = "";
  const reports = data.reports || [];
  const events = data.events || [];
  const rawEvents = data.raw_events || [];
  const investigations = data.investigations || [];
  const card = el("article", "history-card");
  card.appendChild(el("h4", "", t("ui").historySummaryTitle));
  card.appendChild(el("p", "card-copy", t("ui").historySummaryCopy));
  const meta = el("div", "meta-grid");
  [
    [uiState.language === "zh" ? "标准化事件" : "Normalized events", String(events.length)],
    [uiState.language === "zh" ? "原始输入" : "Raw inputs", String(rawEvents.length)],
    [uiState.language === "zh" ? "报告记录" : "Reports", String(reports.length)],
    [uiState.language === "zh" ? "调查会话" : "Investigations", String(investigations.length)],
  ].forEach(([label, value]) => {
    const item = el("div", "meta-item");
    item.appendChild(el("span", "meta-label", label));
    item.appendChild(el("span", "meta-value", value));
    meta.appendChild(item);
  });
  card.appendChild(meta);
  const compact = el("div", "compact-meta");
  compact.appendChild(el("span", "compact-stat", uiState.language === "zh" ? `最近事件：${formatTime(events[0]?.normalized_event?.timestamp || events[0]?.created_at)}` : `Latest event: ${formatTime(events[0]?.normalized_event?.timestamp || events[0]?.created_at)}`));
  compact.appendChild(el("span", "compact-stat", uiState.language === "zh" ? `最近输入：${formatTime(rawEvents[0]?.timestamp || rawEvents[0]?.created_at)}` : `Latest intake: ${formatTime(rawEvents[0]?.timestamp || rawEvents[0]?.created_at)}`));
  compact.appendChild(el("span", "compact-stat", uiState.language === "zh" ? `最近报告：${formatTime(reports[0]?.generated_at || reports[0]?.created_at)}` : `Latest report: ${formatTime(reports[0]?.generated_at || reports[0]?.created_at)}`));
  card.appendChild(compact);
  root.appendChild(card);
}

function renderBitdefender(data) {
  uiState.bitdefender = data;
  const root = document.getElementById("bitdefender-output");
  const status = document.getElementById("bitdefender-status");
  root.innerHTML = "";
  if (!data) {
    root.className = "stack-list";
    root.appendChild(el("p", "section-note", t("ui").integrationsSectionCopy));
    root.appendChild(createEmptyState(t("ui").bitdefenderNoData));
    status.textContent = t("ui").bitdefenderWaiting;
    return;
  }
  root.className = "stack-list";
  status.textContent = data.error
    ? (uiState.language === "zh" ? `最近结果：${data.error}` : `Latest result: ${data.error}`)
    : (uiState.language === "zh" ? "最近一次调用已完成。" : "Latest call completed.");
  root.appendChild(el("p", "section-note", t("ui").integrationsSectionCopy));

  const quickGrid = el("div", "hero-kpi-grid");
  [
    {
      tone: "success",
      eyebrow: uiState.language === "zh" ? "CONNECTION STATUS" : "CONNECTION STATUS",
      value: data.error ? (uiState.language === "zh" ? "异常" : "Issue") : (uiState.language === "zh" ? "在线" : "Live"),
      suffix: uiState.language === "zh" ? "MCP" : "MCP",
      copy: uiState.language === "zh" ? "这里优先判断连接层是否正常，以及是否值得继续导入分析。" : "This card focuses on whether the MCP is healthy and worth continuing into analysis.",
    },
    {
      tone: "cyan",
      eyebrow: uiState.language === "zh" ? "LATEST REPORT" : "LATEST REPORT",
      value: String(data.latest_report_summary?.row_count ?? 0),
      suffix: uiState.language === "zh" ? "Rows" : "Rows",
      copy: uiState.language === "zh" ? "如果最新报表已经有内容，通常最有价值的动作就是导入它。" : "If the latest report already has content, importing it is usually the most valuable next action.",
    },
    {
      tone: "violet",
      eyebrow: uiState.language === "zh" ? "NEXT ACTION" : "NEXT ACTION",
      value: uiState.language === "zh" ? "导入报表" : "Import",
      suffix: uiState.language === "zh" ? "Into Platform" : "Into Platform",
      copy: uiState.language === "zh" ? "不要纠结设备总数，更应该看最新报表有没有新的高风险信号。" : "Do not over-focus on total device counts; focus on whether the latest report has new high-risk signals.",
    },
  ].forEach((item) => {
    const card = el("article", `hero-kpi-card ${item.tone}`.trim());
    card.appendChild(el("span", "hero-kpi-eyebrow", item.eyebrow));
    const value = el("div", "hero-kpi-value");
    value.appendChild(el("span", "hero-kpi-number", item.value));
    value.appendChild(el("span", "hero-kpi-suffix", item.suffix));
    card.appendChild(value);
    card.appendChild(el("p", "card-copy", item.copy));
    quickGrid.appendChild(card);
  });
  root.appendChild(quickGrid);
  const statusGrid = el("div", "connection-status-grid");
  [
    [uiState.language === "zh" ? "连接健康" : "Connection Health", data.error ? (uiState.language === "zh" ? "需修复" : "Needs Repair") : (uiState.language === "zh" ? "正常" : "Healthy"), uiState.language === "zh" ? "先确认 MCP 连通，再决定要不要继续导入。" : "Confirm the MCP is reachable before importing further."],
    [uiState.language === "zh" ? "可分析内容" : "Ready-to-Analyze", `${data.latest_report_summary?.row_count ?? 0}`, uiState.language === "zh" ? "这里直接回答有没有值得导入的新东西。" : "This tells you whether there is something worth importing now."],
    [uiState.language === "zh" ? "推荐动作" : "Recommended Action", uiState.language === "zh" ? "导入最新报表" : "Import Latest Report", uiState.language === "zh" ? "如果这里只做一个动作，通常就是它。" : "If you only do one thing on this page, it is usually this."],
  ].forEach(([label, value, copy]) => {
    const card = el("article", "connection-status-card");
    card.appendChild(el("span", "meta-label", label));
    card.appendChild(el("strong", "", String(value)));
    card.appendChild(el("p", "card-copy", copy));
    statusGrid.appendChild(card);
  });
  root.appendChild(statusGrid);

  const summary = el("article", "summary-card");
  summary.appendChild(el("h4", "", t("ui").bitdefenderSummaryTitle));
  summary.appendChild(el("p", "card-copy", t("ui").bitdefenderDefaultKeyNotice));
  const statusMeta = el("div", "meta-grid");
  [
    [uiState.language === "zh" ? "连接状态" : "Connection status", data.error ? (uiState.language === "zh" ? "异常" : "Issue detected") : (uiState.language === "zh" ? "已连接" : "Connected")],
    [uiState.language === "zh" ? "最近结果" : "Latest result", data.error ? (uiState.language === "zh" ? "需要关注" : "Needs attention") : (uiState.language === "zh" ? "调用成功" : "Call completed")],
    [uiState.language === "zh" ? "公司 ID" : "Company ID", data.company_id || (uiState.language === "zh" ? "未发现" : "Not found")],
    [uiState.language === "zh" ? "可用报表数" : "Available reports", String(data.report_total ?? data.reports?.total ?? 0)],
  ].forEach(([label, value]) => {
    const item = el("div", "meta-item");
    item.appendChild(el("span", "meta-label", label));
    item.appendChild(el("span", "meta-value", String(value)));
    statusMeta.appendChild(item);
  });
  summary.appendChild(statusMeta);
  summary.appendChild(el("h4", "", t("ui").bitdefenderAvailableDataTitle));
  const dataTypes = el("div", "chip-row");
  const availableTypes = [
    uiState.language === "zh" ? "终端资产" : "Asset inventory",
    uiState.language === "zh" ? "安全报表" : "Security reports",
  ];
  if (Array.isArray(data.hierarchy_policies) && data.hierarchy_policies.length) {
    availableTypes.push(uiState.language === "zh" ? "策略分布" : "Policy distribution");
  }
  if (Array.isArray(data.hierarchy_os_families) && data.hierarchy_os_families.length) {
    availableTypes.push(uiState.language === "zh" ? "系统分布" : "OS distribution");
  }
  availableTypes.forEach((item) => dataTypes.appendChild(el("span", "chip good", item)));
  summary.appendChild(dataTypes);
  if (data.latest_report_summary) {
    summary.appendChild(el("h4", "", t("ui").bitdefenderCoverageTitle));
    summary.appendChild(el("p", "card-copy", t("ui").bitdefenderReportFocusCopy));
    const latestSummary = el("div", "meta-grid");
    [
      [uiState.language === "zh" ? "最新报表记录数" : "Latest report rows", String(data.latest_report_summary.row_count ?? 0)],
      [uiState.language === "zh" ? "最新报表主机数" : "Latest report hosts", String(data.latest_report_summary.unique_host_count ?? 0)],
      [uiState.language === "zh" ? "恶意软件检测" : "Malware detections", String(data.latest_report_summary.malware_count ?? 0)],
      [uiState.language === "zh" ? "网络攻击记录" : "Network attacks", String(data.latest_report_summary.attack_count ?? 0)],
      [uiState.language === "zh" ? "阻止网站" : "Blocked sites", String(data.latest_report_summary.blocked_count ?? 0)],
    ].forEach(([label, value]) => {
      const item = el("div", "meta-item");
      item.appendChild(el("span", "meta-label", label));
      item.appendChild(el("span", "meta-value", String(value)));
      latestSummary.appendChild(item);
    });
    summary.appendChild(latestSummary);
    summary.appendChild(el("p", "card-copy", t("ui").bitdefenderActionHint));
    if (Array.isArray(data.latest_report_summary.top_hosts) && data.latest_report_summary.top_hosts.length) {
      summary.appendChild(el("h5", "", t("ui").bitdefenderTopHostsTitle));
      const hosts = el("div", "chip-row");
      data.latest_report_summary.top_hosts.forEach((item) => {
        hosts.appendChild(el("span", "chip", `${item.name} · ${item.count}`));
      });
      summary.appendChild(hosts);
    }
    if (Array.isArray(data.latest_report_summary.top_event_types) && data.latest_report_summary.top_event_types.length) {
      summary.appendChild(el("h5", "", t("ui").bitdefenderTopEventsTitle));
      const events = el("div", "chip-row");
      data.latest_report_summary.top_event_types.forEach((item) => {
        events.appendChild(el("span", "chip", `${item.name} · ${item.count}`));
      });
      summary.appendChild(events);
    }
    const apiHosts = Number(data.endpoint_total ?? data.endpoints?.total ?? 0);
    const reportHosts = Number(data.latest_report_summary.unique_host_count ?? 0);
    if (reportHosts > apiHosts) {
      const gapCard = el("article", "report-card report-section");
      gapCard.appendChild(el("h5", "", t("ui").bitdefenderCoverageGapTitle));
      gapCard.appendChild(el("p", "card-copy", t("ui").bitdefenderCoverageGapCopy));
      const gapMeta = el("div", "meta-grid");
      [
        [uiState.language === "zh" ? "API 可见端点" : "API-visible endpoints", String(apiHosts)],
        [uiState.language === "zh" ? "报表出现主机" : "Hosts seen in reports", String(reportHosts)],
      ].forEach(([label, value]) => {
        const item = el("div", "meta-item");
        item.appendChild(el("span", "meta-label", label));
        item.appendChild(el("span", "meta-value", value));
        gapMeta.appendChild(item);
      });
      gapCard.appendChild(gapMeta);
      summary.appendChild(gapCard);
    }
  }
  root.appendChild(summary);
  const actionRail = el("div", "action-rail");
  const actionCard = el("article", "action-rail-card");
  actionCard.appendChild(el("h4", "", uiState.language === "zh" ? "这页真正能做什么" : "What This Page Actually Helps With"));
  const actionList = el("ul", "bullet-list");
  [
    uiState.language === "zh" ? "确认 Bitdefender 连接层是不是活的。" : "Confirm whether the Bitdefender MCP is alive.",
    uiState.language === "zh" ? "如果最新报表已经有内容，优先导入报表，而不是纠结设备总数。" : "If the latest report already has content, import it before over-focusing on device totals.",
    uiState.language === "zh" ? "资产导入更像补背景，报表导入更像直接进入分析。" : "Asset import adds context; report import gets you into analysis faster.",
  ].forEach((text) => actionList.appendChild(el("li", "", text)));
  actionCard.appendChild(actionList);
  actionRail.appendChild(actionCard);
  root.appendChild(actionRail);

}

async function loadHealth() {
  try {
    await request("/health");
    setHealth(healthText("healthy"), "idle");
  } catch (error) {
    setHealth(String(error), "error");
  }
}

async function loadOverview() {
  renderOverview(await request("/pipeline/overview"));
}

async function loadReports() {
  renderReports(await request("/reports/recent"));
}

async function loadInvestigations() {
  renderInvestigations(await request("/investigations/recent"));
}

async function loadHistory() {
  renderHistory(await request("/history"));
}

async function loadSkills() {
  renderSkills(await request("/skills"));
}

async function loadMatrix() {
  renderMatrix(await request("/skills/matrix"));
}

async function loadMemoryRules() {
  renderMemoryRules(await request("/memory/rules"));
}

async function loadMemoryFeedback() {
  renderMemoryFeedback(await request("/memory/feedback"));
}

function bitdefenderPayload() {
  return {};
}

async function runBitdefender(endpoint, statusCopy) {
  const status = document.getElementById("bitdefender-status");
  status.textContent = statusCopy;
  const data = await request(endpoint, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(bitdefenderPayload()),
  });
  renderBitdefender(data);
}

async function importBitdefender(endpoint, statusCopy) {
  const status = document.getElementById("bitdefender-status");
  status.textContent = statusCopy;
  const data = await request(endpoint, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(bitdefenderPayload()),
  });
  if (data.raw_event) {
    intakeState.rawEvent = data.raw_event;
    intakeState.normalizedEvent = data.normalized_event || null;
    intakeState.plannerPreview = data.planner_preview || null;
    intakeState.report = data.report;
    document.getElementById("raw-input").value = JSON.stringify(data.raw_event, null, 2);
    persistRawInput();
    renderNormalizeOutput(intakeState.normalizedEvent);
    renderPlannerPreview(intakeState.plannerPreview);
    renderReport(data.report);
    document.getElementById("intake-status").textContent = uiState.language === "zh" ? "Bitdefender 数据已导入平台并完成分析。" : "Bitdefender data has been imported into the platform and analyzed.";
    setView("intake");
  }
  await Promise.all([loadOverview(), loadReports(), loadInvestigations(), loadHistory(), loadMemoryRules(), loadMemoryFeedback()]);
  renderBitdefender(uiState.bitdefender);
}

async function previewNormalize() {
  setHealth(healthText("normalizing"), "busy");
  const payload = JSON.parse(document.getElementById("raw-input").value);
  persistRawInput();
  const data = await request("/normalize/preview", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  });
  intakeState.rawEvent = payload;
  intakeState.normalizedEvent = data;
  renderNormalizeOutput(data);
  document.getElementById("intake-status").textContent = uiState.language === "zh" ? "归一化预览已生成。" : "Normalization preview is ready.";
  setHealth(healthText("healthy"), "idle");
  await Promise.all([loadMemoryRules(), loadMemoryFeedback()]);
  return data;
}

async function previewPlan() {
  setHealth(healthText("planning"), "busy");
  const normalized = await previewNormalize();
  const data = await request("/planner/preview", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(normalized)
  });
  intakeState.plannerPreview = data;
  renderPlannerPreview(data);
  document.getElementById("intake-status").textContent = uiState.language === "zh" ? "技能规划预览已生成。" : "Skill planning preview is ready.";
  setHealth(healthText("healthy"), "idle");
}

async function analyzeRaw() {
  if (intakeState.analyzing) return;
  intakeState.analyzing = true;
  updateButtonState("analyze", uiState.language === "zh" ? "分析中..." : "Analyzing...", true);
  setHealth(healthText("analyzing"), "busy");
  try {
    if (intakeState.pendingFiles?.length) {
      const body = new FormData();
      intakeState.pendingFiles.forEach((file) => body.append("files", file));
      const data = await request("/ingest/files", { method: "POST", body });
      intakeState.pendingFiles = [];
      intakeState.uploadBatch = data;
      renderFileRuns(data);
      const first = data.results?.[0];
      if (first) {
        intakeState.rawEvent = first.raw_event;
        intakeState.normalizedEvent = first.normalized_event;
        intakeState.plannerPreview = first.planner_preview;
        intakeState.report = first.report;
        renderPlannerPreview(first.planner_preview);
        renderNormalizeOutput(first.normalized_event);
        renderReport(first.report);
        document.getElementById("raw-input").value = JSON.stringify(first.raw_event, null, 2);
        persistRawInput();
      }
      document.getElementById("intake-status").textContent = uploadStatusText(data);
      setHealth(healthText("healthy"), "idle");
      await Promise.all([loadOverview(), loadReports(), loadInvestigations(), loadHistory(), loadMemoryRules(), loadMemoryFeedback()]);
      return;
    }
    const rawText = document.getElementById("raw-input").value.trim();
    if (!rawText) {
      document.getElementById("intake-status").textContent = uiState.language === "zh" ? "当前没有待分析内容，请先上传文件或粘贴原始材料。" : "There is no staged content to analyze. Upload a file or paste raw material first.";
      setHealth(healthText("healthy"), "idle");
      return;
    }
    const payload = JSON.parse(rawText);
    persistRawInput();
    const report = await request("/ingest/raw", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    intakeState.rawEvent = payload;
    intakeState.report = report;
    renderReport(report);
    document.getElementById("intake-status").textContent = uiState.language === "zh" ? "分析已完成。" : "Analysis completed.";
    setHealth(healthText("healthy"), "idle");
    await Promise.all([loadOverview(), loadReports(), loadHistory(), loadMemoryRules(), loadMemoryFeedback()]);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    document.getElementById("intake-status").textContent =
      uiState.language === "zh" ? `分析失败：${message}` : `Analysis failed: ${message}`;
    setHealth(message, "error");
  } finally {
    intakeState.analyzing = false;
    updateButtonState("analyze", t("ui").analyze, false);
  }
}

async function uploadFiles(files) {
  try {
    if (!files.length) return;
    setHealth(healthText("uploading"), "busy");
    intakeState.pendingFiles = Array.from(files);
    intakeState.rawEvent = null;
    intakeState.normalizedEvent = null;
    intakeState.plannerPreview = null;
    intakeState.report = null;
    intakeState.uploadBatch = {
      pendingFiles: intakeState.pendingFiles.map((file) => file.name),
    };
    document.getElementById("raw-input").value = stagedUploadManifest(intakeState.pendingFiles);
    persistRawInput();
    renderPlannerPreview(null);
    renderNormalizeOutput(null);
    renderReport(null);
    renderFileRuns(intakeState.uploadBatch);
    document.getElementById("intake-status").textContent =
      uiState.language === "zh"
        ? `已上传 ${intakeState.pendingFiles.length} 个文件，等待点击“归一化后分析”。`
        : `${intakeState.pendingFiles.length} file(s) uploaded. Click “Normalize + Analyze” to start.`;
    setHealth(healthText("staged"), "idle");
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    document.getElementById("intake-status").textContent =
      uiState.language === "zh" ? `上传暂存失败：${message}` : `Failed to stage upload: ${message}`;
    setHealth(message, "error");
  }
}

async function saveCorrection() {
  const correctionSource = document.getElementById("correction-source-type");
  const correctionEvent = document.getElementById("correction-event-type");
  const correctionSkills = document.getElementById("correction-skills");
  const correctionForm = document.getElementById("correction-form");
  if (!intakeState.rawEvent || !correctionSource || !correctionEvent || !correctionSkills || !correctionForm) {
    return;
  }
  const expectedSourceType = correctionSource.value.trim();
  const expectedEventType = correctionEvent.value.trim();
  const selectedSkills = Array.from(correctionSkills.selectedOptions).map((option) => option.value);
  if (!expectedSourceType || !expectedEventType) {
    return;
  }
  await request("/memory/learn/classification", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
        raw_event: intakeState.rawEvent,
        expected_source_type: expectedSourceType,
        expected_event_type: expectedEventType,
        preferred_skills: selectedSkills.length ? selectedSkills : (intakeState.plannerPreview?.skills_to_execute || []),
        notes: "manual-correction-from-intake",
      }),
    });
  correctionForm.classList.add("hidden");
  await Promise.all([loadMemoryRules(), loadMemoryFeedback()]);
}

document.querySelectorAll(".menu-item").forEach((item) => {
  item.addEventListener("click", () => setView(item.dataset.view));
});

document.getElementById("refresh-overview").addEventListener("click", () => withRefreshState("refresh-overview", loadOverview));
document.getElementById("refresh-reports").addEventListener("click", () => withRefreshState("refresh-reports", loadReports));
document.getElementById("refresh-investigations").addEventListener("click", () => withRefreshState("refresh-investigations", loadInvestigations));
document.getElementById("refresh-history").addEventListener("click", () => withRefreshState("refresh-history", loadHistory));
document.getElementById("refresh-skills").addEventListener("click", () => withRefreshState("refresh-skills", loadSkills));
document.getElementById("refresh-matrix").addEventListener("click", () => withRefreshState("refresh-matrix", loadMatrix));
if (document.getElementById("refresh-memory-rules")) document.getElementById("refresh-memory-rules").addEventListener("click", () => withRefreshState("refresh-memory-rules", loadMemoryRules));
if (document.getElementById("refresh-memory-feedback")) document.getElementById("refresh-memory-feedback").addEventListener("click", () => withRefreshState("refresh-memory-feedback", loadMemoryFeedback));
document.getElementById("run-bitdefender-test").addEventListener("click", () => runBitdefender("/integrations/bitdefender/test", uiState.language === "zh" ? "正在测试 Bitdefender 连接..." : "Testing Bitdefender connection..."));
document.getElementById("run-bitdefender-network").addEventListener("click", () => runBitdefender("/integrations/bitdefender/network", uiState.language === "zh" ? "正在读取终端与资产清单..." : "Loading asset and endpoint inventory..."));
document.getElementById("import-bitdefender-network").addEventListener("click", () => importBitdefender("/integrations/bitdefender/network/import", uiState.language === "zh" ? "正在把终端资产导入平台..." : "Importing asset inventory into the platform..."));
if (document.getElementById("run-bitdefender-reports")) document.getElementById("run-bitdefender-reports").addEventListener("click", () => runBitdefender("/integrations/bitdefender/reports", uiState.language === "zh" ? "正在读取可用报表目录..." : "Loading available report catalog..."));
if (document.getElementById("run-bitdefender-report-links")) document.getElementById("run-bitdefender-report-links").addEventListener("click", () => runBitdefender("/integrations/bitdefender/reports/download-links", uiState.language === "zh" ? "正在获取最新报表下载链接..." : "Fetching latest report download links..."));
document.getElementById("import-bitdefender-latest-report").addEventListener("click", () => importBitdefender("/integrations/bitdefender/reports/latest/import", uiState.language === "zh" ? "正在导入最新报表内容..." : "Importing the latest report content..."));
if (document.getElementById("import-bitdefender-reports")) document.getElementById("import-bitdefender-reports").addEventListener("click", () => importBitdefender("/integrations/bitdefender/reports/import", uiState.language === "zh" ? "正在导入报表目录元数据..." : "Importing report catalog metadata..."));
document.getElementById("analyze").addEventListener("click", analyzeRaw);
document.getElementById("download-report").addEventListener("click", downloadCurrentReport);
const showCorrectionFormBtn = document.getElementById("show-correction-form");
if (showCorrectionFormBtn) {
  showCorrectionFormBtn.addEventListener("click", () => {
    const correctionForm = document.getElementById("correction-form");
    const correctionSource = document.getElementById("correction-source-type");
    const correctionEvent = document.getElementById("correction-event-type");
    if (!correctionForm || !correctionSource || !correctionEvent) return;
    correctionForm.classList.toggle("hidden");
    correctionSource.value = intakeState.normalizedEvent?.source_type || "";
    correctionEvent.value = intakeState.normalizedEvent?.event_type || "";
    populateCorrectionSkillOptions(intakeState.plannerPreview?.skills_to_execute || []);
  });
}
const saveCorrectionButton = document.getElementById("save-correction");
if (saveCorrectionButton) saveCorrectionButton.addEventListener("click", saveCorrection);
document.getElementById("file-upload").addEventListener("change", (event) => {
  uploadFiles(event.target.files);
  event.target.value = "";
});
document.getElementById("raw-input").addEventListener("input", persistRawInput);
document.getElementById("skills-filter").addEventListener("change", () => renderSkills(uiState.skills));
document.getElementById("skills-filter").addEventListener("change", () => renderMatrix(uiState.matrix));
if (document.getElementById("memory-search")) document.getElementById("memory-search").addEventListener("input", () => renderMemoryRules(uiState.memoryRules));
document.getElementById("lang-zh").addEventListener("click", () => {
  uiState.language = "zh";
  localStorage.setItem(storageKeys.language, "zh");
  applyLanguage();
});
document.getElementById("lang-en").addEventListener("click", () => {
  uiState.language = "en";
  localStorage.setItem(storageKeys.language, "en");
  applyLanguage();
});

clearLegacyLocalState();
uiState.language = localStorage.getItem(storageKeys.language) || "zh";
document.getElementById("raw-input").value = "";
if (document.getElementById("correction-source-type")) {
  fillSelectOptions("correction-source-type", sourceTypeOptions, uiState.language === "zh" ? "选择正确的来源类型" : "Choose the correct source type", sourceTypeLabel);
}
if (document.getElementById("correction-event-type")) {
  fillSelectOptions("correction-event-type", eventTypeOptions, uiState.language === "zh" ? "选择正确的事件类型" : "Choose the correct event type", eventTypeLabel);
}
renderPlannerPreview(null);
renderNormalizeOutput(null);
renderReport(null);
renderFileRuns(null);
document.getElementById("intake-status").textContent = t("ui").ready;
applyLanguage();
loadHealth();
loadOverview();
loadReports();
loadInvestigations();
loadHistory();
loadSkills();
loadMatrix();
loadMemoryRules();
loadMemoryFeedback();
window.addEventListener("hashchange", () => setView(currentViewFromLocation()));
