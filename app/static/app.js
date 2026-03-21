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
      recentRunsCopy: "看最近有没有真实在处理事件。",
      coverageTitle: "能力覆盖范围",
      coverageCopy: "看哪些能力已接入真实执行。",
      flowTitle: "处理流程",
      flowCopy: "输入会按类型走不同链路。",
      architectureTitle: "架构关系图",
      architectureCopy: "连接层、分析主链和能力层如何协作。",
      historySummaryTitle: "运行沉淀",
      historySummaryCopy: "记录数量用来确认系统持续在运行。",
      plannerSummaryTitle: "系统准备调用这些能力",
      plannerSummaryCopy: "系统会按材料类型和已有经验选择能力。",
      normalizeSummaryTitle: "标准化结果摘要",
      normalizeSummaryCopy: "原始材料已变成统一事件结构。",
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
      memoryRuleCopy: "相似材料再次出现时，这条经验会直接带路。",
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
      targetsImportTitle: "真实资产入口",
      targetsImportCopy: "把资产清单和架构备注分开导入。",
      targetsQuickFeedTitle: "快速输入",
      targetsQuickFeedCopy: "常见目标分槽输入后直接入控制面。",
      targetsQuickFeedScopeTitle: "Scope 快速输入",
      targetsQuickFeedDiagramTitle: "架构备注",
      targetsQuickFeedAdd: "追加",
      targetsQuickFeedUpload: "选图 / 文件",
      targetsQuickFeedApply: "一键进入控制面",
      targetsQuickFeedApplyHint: "解析草稿后写入字段。",
      targetsImportStageTitle: "导入阶段",
      targetsImportManifestLabel: "资产清单",
      targetsImportDiagramLabel: "架构备注",
      targetsImportStageStaged: "暂存",
      targetsImportStageParsed: "解析",
      targetsImportStageApplied: "写入",
      targetsImportStageSaved: "保存",
      targetsImportNextActionEmpty: "先拖入文件或粘贴范围内容。",
      targetsImportNextActionDraft: "先解析草稿，再写入控制面。",
      targetsImportNextActionParsed: "写入下方控制面字段。",
      targetsImportNextActionApplied: "保存到后端控制面。",
      targetsImportNextActionSaved: "控制面已保存，可继续补充。",
      targetsImportNextActionStale: "草稿已变更，请重新解析。",
      viewSkillDirectoryTitle: "全部能力",
      viewSkillDirectoryCopy: "默认展示当前平台全部能力，你也可以按模块快速收窄并定位对应引擎。",
      skillsDirectoryNote: "默认展示当前平台全部能力；也可以按模块快速收窄。",
      viewLearningCopy: "这里会沉淀系统学到的分类经验，后续相似材料会优先复用这些判断。",
      uploadRunsWaiting: "还没有上传分析记录",
      learningReadyHint: "在输入页完成一次分析后，这里可以直接把正确判断保存成系统经验。",
      overviewPulseCopy: "最近一次真实分析留下的运行脉搏。",
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
      plannerSummaryCopy: "The Agent chooses Skills from material type and learned experience.",
      normalizeSummaryTitle: "Normalization Summary",
      normalizeSummaryCopy: "Raw material is now a unified event structure.",
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
      memoryRuleCopy: "This helps similar material reach the right path faster.",
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
      targetsImportTitle: "Real Asset Intake",
      targetsImportCopy: "Keep assets and architecture notes separate.",
      targetsQuickFeedTitle: "Quick Input",
      targetsQuickFeedCopy: "Split common targets into slots, then send them in one step.",
      targetsQuickFeedScopeTitle: "Quick Scope Entry",
      targetsQuickFeedDiagramTitle: "Architecture Notes",
      targetsQuickFeedAdd: "Add",
      targetsQuickFeedUpload: "Pick Diagram / File",
      targetsQuickFeedApply: "One-click Control Plane",
      targetsQuickFeedApplyHint: "Parse the draft, write the fields, save.",
      targetsImportStageTitle: "Import Stages",
      targetsImportManifestLabel: "Asset List",
      targetsImportDiagramLabel: "Architecture / Boundaries",
      targetsImportStageStaged: "Stage",
      targetsImportStageParsed: "Parse",
      targetsImportStageApplied: "Write",
      targetsImportStageSaved: "Save",
      targetsImportNextActionEmpty: "Drop files or paste scope content.",
      targetsImportNextActionDraft: "Parse the draft, then write it.",
      targetsImportNextActionParsed: "Write the parsed draft below.",
      targetsImportNextActionApplied: "Save the control plane.",
      targetsImportNextActionSaved: "The control plane is saved.",
      targetsImportNextActionStale: "The draft changed. Re-parse.",
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

const skillTrainingCases = {
  "megaeth.host.baseline_compliance_analysis": [
    { zh: "Case 001 · 主机基线审计", en: "Case 001 · Host baseline review" },
  ],
  "megaeth.host.integrity_monitor": [
    { zh: "Case 001 · 主机基线审计", en: "Case 001 · Host baseline review" },
  ],
  "megaeth.identity.jumpserver_command_review": [
    { zh: "Case 002 · JumpServer 命令审计", en: "Case 002 · JumpServer command review" },
  ],
  "megaeth.identity.jumpserver_transfer_review": [
    { zh: "Case 002 · JumpServer 文件传输审计", en: "Case 002 · JumpServer transfer review" },
  ],
  "megaeth.identity.jumpserver_operation_review": [
    { zh: "Case 002 · JumpServer 管理平面审计", en: "Case 002 · JumpServer operation review" },
  ],
  "megaeth.identity.jumpserver_multi_source_review": [
    { zh: "Case 002 · JumpServer 多源关联审计", en: "Case 002 · JumpServer multi-source review" },
  ],
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
  expandedSkillTraining: {},
  expandedSkillModules: {},
  language: "zh",
};

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
  if (document.getElementById("brand-title")) document.getElementById("brand-title").textContent = t("brandTitle");
  if (document.getElementById("brand-copy")) document.getElementById("brand-copy").textContent = t("brandCopy");
  if (document.getElementById("hero-eyebrow")) document.getElementById("hero-eyebrow").textContent = t("heroEyebrow");
  if (document.getElementById("system-status-label")) document.getElementById("system-status-label").textContent = t("systemStatus");
  const ui = t("ui");
  if (document.getElementById("section-overview-title")) document.getElementById("section-overview-title").textContent = ui.overviewTitle;
  if (document.getElementById("section-reports-title")) document.getElementById("section-reports-title").textContent = ui.reportsTitle;
  if (document.getElementById("section-investigations-title")) document.getElementById("section-investigations-title").textContent = ui.investigationsTitle;
  if (document.getElementById("section-history-title")) document.getElementById("section-history-title").textContent = ui.historyTitle;
  if (document.getElementById("section-bitdefender-title")) document.getElementById("section-bitdefender-title").textContent = ui.bitdefenderTitle;
  if (document.getElementById("bitdefender-copy")) document.getElementById("bitdefender-copy").textContent = ui.bitdefenderCopy;
  if (document.getElementById("bitdefender-import-note")) document.getElementById("bitdefender-import-note").textContent = ui.bitdefenderImportNote;
  if (document.getElementById("section-intake-input-title")) document.getElementById("section-intake-input-title").textContent = ui.intakeInputTitle;
  if (document.getElementById("upload-files-label")) document.getElementById("upload-files-label").textContent = ui.uploadFiles;
  if (document.getElementById("preview-normalize")) document.getElementById("preview-normalize").textContent = ui.previewNormalize;
  if (document.getElementById("preview-plan")) document.getElementById("preview-plan").textContent = ui.previewPlan;
  if (document.getElementById("analyze")) document.getElementById("analyze").textContent = ui.analyze;
  if (document.getElementById("section-planner-title")) document.getElementById("section-planner-title").textContent = ui.plannerTitle;
  if (document.getElementById("section-normalize-title")) document.getElementById("section-normalize-title").textContent = ui.normalizeTitle;
  if (document.getElementById("section-report-title")) document.getElementById("section-report-title").textContent = ui.reportTitle;
  const showCorrectionBtn = document.getElementById("show-correction-form");
  const correctionSkillsLabel = document.getElementById("correction-skills-label");
  const saveCorrectionBtn = document.getElementById("save-correction");
  if (showCorrectionBtn) showCorrectionBtn.textContent = ui.learnWrong;
  if (correctionSkillsLabel) correctionSkillsLabel.textContent = ui.correctionSkills;
  if (saveCorrectionBtn) saveCorrectionBtn.textContent = ui.saveCorrection;
  if (document.getElementById("section-file-runs-title")) document.getElementById("section-file-runs-title").textContent = ui.fileRunsTitle;
  if (document.getElementById("menu-group-security")) document.getElementById("menu-group-security").textContent = ui.menuSecurityGroup;
  if (document.getElementById("intake-dropzone-title")) document.getElementById("intake-dropzone-title").textContent = ui.intakeDropzoneTitle;
  if (document.getElementById("intake-dropzone-copy")) document.getElementById("intake-dropzone-copy").textContent = ui.intakeDropzoneCopy;
  if (document.getElementById("intake-editor-title")) document.getElementById("intake-editor-title").textContent = ui.intakeEditorTitle;
  if (document.getElementById("intake-editor-note")) document.getElementById("intake-editor-note").textContent = ui.intakeEditorNote;
  if (document.getElementById("intake-editor-badge")) document.getElementById("intake-editor-badge").textContent = ui.intakeEditorBadge;
  if (document.getElementById("run-bitdefender-test")) document.getElementById("run-bitdefender-test").textContent = ui.bitdefenderTest;
  if (document.getElementById("run-bitdefender-network")) document.getElementById("run-bitdefender-network").textContent = ui.bitdefenderNetwork;
  if (document.getElementById("import-bitdefender-network")) document.getElementById("import-bitdefender-network").textContent = ui.bitdefenderImportNetwork;
  if (document.getElementById("run-bitdefender-reports")) document.getElementById("run-bitdefender-reports").textContent = ui.bitdefenderReports;
  if (document.getElementById("run-bitdefender-report-links")) document.getElementById("run-bitdefender-report-links").textContent = ui.bitdefenderReportLinks;
  if (document.getElementById("import-bitdefender-latest-report")) document.getElementById("import-bitdefender-latest-report").textContent = ui.bitdefenderImportLatestReport;
  if (document.getElementById("import-bitdefender-reports")) document.getElementById("import-bitdefender-reports").textContent = ui.bitdefenderImportReports;
  if (document.getElementById("section-installed-skills-title")) document.getElementById("section-installed-skills-title").textContent = ui.installedSkillsTitle;
  if (document.getElementById("section-skill-matrix-title")) document.getElementById("section-skill-matrix-title").textContent = ui.skillMatrixTitle;
  if (document.getElementById("section-memory-feedback-title")) document.getElementById("section-memory-feedback-title").textContent = ui.memoryFeedbackTitle;
  if (document.getElementById("refresh-overview")) document.getElementById("refresh-overview").textContent = t("refresh");
  if (document.getElementById("refresh-reports")) document.getElementById("refresh-reports").textContent = t("refresh");
  if (document.getElementById("refresh-investigations")) document.getElementById("refresh-investigations").textContent = t("refresh");
  if (document.getElementById("refresh-history")) document.getElementById("refresh-history").textContent = t("refresh");
  if (document.getElementById("refresh-skills")) document.getElementById("refresh-skills").textContent = t("refresh");
  if (document.getElementById("refresh-matrix")) document.getElementById("refresh-matrix").textContent = t("refresh");
  if (document.getElementById("refresh-memory-feedback")) document.getElementById("refresh-memory-feedback").textContent = t("refresh");
  if (document.getElementById("skills-search")) document.getElementById("skills-search").placeholder = ui.searchSkillsPlaceholder;
  if (document.getElementById("skills-directory-note")) document.getElementById("skills-directory-note").textContent = ui.skillsDirectoryNote;
  if (document.getElementById("intake-upload-note")) document.getElementById("intake-upload-note").textContent = ui.intakeUploadNote;
  if (document.getElementById("intake-analyze-hint")) document.getElementById("intake-analyze-hint").textContent = ui.intakeAnalyzeHint;
  if (document.getElementById("download-report")) document.getElementById("download-report").textContent = ui.downloadReport;
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

function parseDelimitedList(value) {
  return String(value || "")
    .split(/[\n,]/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function formatDelimitedList(values) {
  return Array.isArray(values) ? values.join("\n") : "";
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
  await Promise.all([loadOverview(), loadReports(), loadInvestigations(), loadHistory(), loadMemoryFeedback()]);
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
  await Promise.all([loadMemoryFeedback()]);
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
      await Promise.all([loadOverview(), loadReports(), loadInvestigations(), loadHistory(), loadMemoryFeedback()]);
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
    await Promise.all([loadOverview(), loadReports(), loadHistory(), loadMemoryFeedback()]);
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
  await Promise.all([loadMemoryFeedback()]);
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
document.getElementById("refresh-memory-feedback").addEventListener("click", () => withRefreshState("refresh-memory-feedback", loadMemoryFeedback));
document.getElementById("run-bitdefender-test").addEventListener("click", () => runBitdefender("/integrations/bitdefender/test", uiState.language === "zh" ? "正在测试 Bitdefender 连接..." : "Testing Bitdefender connection..."));
document.getElementById("run-bitdefender-network").addEventListener("click", () => runBitdefender("/integrations/bitdefender/network", uiState.language === "zh" ? "正在读取终端与资产清单..." : "Loading asset and endpoint inventory..."));
document.getElementById("import-bitdefender-network").addEventListener("click", () => importBitdefender("/integrations/bitdefender/network/import", uiState.language === "zh" ? "正在把终端资产导入平台..." : "Importing asset inventory into the platform..."));
if (document.getElementById("run-bitdefender-reports")) document.getElementById("run-bitdefender-reports").addEventListener("click", () => runBitdefender("/integrations/bitdefender/reports", uiState.language === "zh" ? "正在读取可用报表目录..." : "Loading available report catalog..."));
if (document.getElementById("run-bitdefender-report-links")) document.getElementById("run-bitdefender-report-links").addEventListener("click", () => runBitdefender("/integrations/bitdefender/reports/download-links", uiState.language === "zh" ? "正在获取最新报表下载链接..." : "Fetching latest report download links..."));
document.getElementById("import-bitdefender-latest-report").addEventListener("click", () => importBitdefender("/integrations/bitdefender/reports/latest/import", uiState.language === "zh" ? "正在导入最新报表内容..." : "Importing the latest report content..."));
if (document.getElementById("import-bitdefender-reports")) document.getElementById("import-bitdefender-reports").addEventListener("click", () => importBitdefender("/integrations/bitdefender/reports/import", uiState.language === "zh" ? "正在导入报表目录元数据..." : "Importing report catalog metadata..."));
document.getElementById("analyze").addEventListener("click", analyzeRaw);
document.getElementById("download-report").addEventListener("click", downloadCurrentReport);
document.addEventListener("click", (event) => {
  const target = event.target.closest("[data-task-action]");
  if (!target) return;
  applyAppaTaskAction(target.dataset.taskId, target.dataset.taskAction);
});
document.addEventListener("click", (event) => {
  const target = event.target.closest("[data-run-action]");
  if (!target) return;
  applyAppaRunAction(target.dataset.runId, target.dataset.runAction);
});
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
document.getElementById("skills-search").addEventListener("input", () => renderSkills(uiState.skills));
document.getElementById("skills-search").addEventListener("input", () => renderMatrix(uiState.matrix));
document.getElementById("skills-filter").addEventListener("change", () => renderSkills(uiState.skills));
document.getElementById("skills-filter").addEventListener("change", () => renderMatrix(uiState.matrix));
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
hydrateAppaTargetsImport();
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
loadMemoryFeedback();
window.addEventListener("hashchange", () => setView(currentViewFromLocation()));
