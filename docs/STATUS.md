# 当前状态
<!-- security-log-analysis mainline -->

## 1. 当前主线

当前仓库只保留：

- 安全日志分析

## 2. 运行基线

- 默认端口：`8011`
- 健康检查：`/health`
- 主要烟测接口：`/pipeline/overview`
- 回归测试入口：`tests/test_api.py`

## 3. 当前已确认能力

- 五页面前端主线：概览、输入、技能、连接、学习
- Host baseline 分析与训练案例
- JumpServer 单文件与多源综合分析
- Bitdefender 导入入口
- Whitebox AppSec 三段式能力骨架
- 历史记录、调查会话、学习反馈

## 4. 当前工作方式

- 使用真实样本推进能力迭代
- 使用目标输出作为报告校准基准
- 使用案例与 Skill 文档共同沉淀系统行为边界

## 5. 快速检查命令

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
curl -sSf http://127.0.0.1:8011/health
curl -sSf http://127.0.0.1:8011/pipeline/overview
./.venv/bin/python -m pytest tests/test_api.py -q
```
