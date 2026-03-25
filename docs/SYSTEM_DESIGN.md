# 系统设计说明
<!-- security-log-analysis mainline -->

## 中文

### 1. 文档目的

本文档定义当前主线的系统设计边界、运行方式、核心模块职责与数据流转方式。

### 2. 系统范围

当前主线覆盖输入、归一化、分类、Skill 执行、风险判断、报告生成以及历史/学习沉淀；不包含自动处置、分布式执行、多租户和第二产品域。

### 3. 总体架构

系统分为输入与接入层、分析与报告层、留存与学习层三层。

### 4. 核心模块

API 层负责入口与页面输出；分析层负责归一化、Planner、Skill、风险与报告；留存层负责历史、调查与学习反馈。

### 5. 主要对象模型

当前主线围绕 RawEvent、NormalizedEvent、Finding、SecurityReport、Investigation、LearningRule、LearningFeedback 运作。

### 6. 运行与存储约束

默认端口为 8011，主要烟测接口为 /pipeline/overview，当前存储策略以 data/*.json 与归档目录为主。


## English

### 1. Purpose

This document defines the active system-design boundary, runtime shape, component ownership, and data flow of the current mainline.

### 2. System Scope

The current mainline covers intake, normalization, classification, Skill execution, risk judgment, reporting, and history/learning retention. It excludes auto-remediation, distributed execution, multi-tenancy, and any second product surface.

### 3. Architecture

The system is organized into three layers: intake/integration, analysis/reporting, and retention/learning.

### 4. Primary Components

The API layer exposes entry points and serves the UI. The analysis layer handles normalization, planning, Skills, risk scoring, and reporting. The retention layer stores history, investigations, and learning feedback.

### 5. Core Data Model

The current mainline revolves around RawEvent, NormalizedEvent, Finding, SecurityReport, Investigation, LearningRule, and LearningFeedback.

### 6. Runtime and Storage

The default runtime port is 8011, the main smoke endpoint is /pipeline/overview, and persistence is currently file-backed through data/*.json plus archive directories.
