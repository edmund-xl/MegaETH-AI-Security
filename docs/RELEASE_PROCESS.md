# 发布流程
<!-- security-log-analysis mainline -->

## 1. 目的

本文档说明当前主线的标准发布流程，确保代码、文档、测试与远端仓库一致。

## 2. 发布前准备

- 完成目标功能或文档修改
- 回归五个页面
- 确认训练案例与 Skill 文档是否需要同步更新

## 3. 本地验证

```bash
node --check app/static/app.js
./.venv/bin/python -m pytest tests/test_api.py -q
curl -sSf http://127.0.0.1:8011/health
```

## 4. 发布步骤

1. 检查工作树
2. 提交代码
3. 推送当前工作分支
4. 同步 `main`
5. 核查 GitHub 文件与文档是否已经一致

## 5. 发布后检查

- GitHub 远端已更新
- 本地运行态正常
- 关键文档入口可读
- 近期样本链路仍可正常分析
