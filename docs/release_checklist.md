# 发布检查清单
<!-- security-log-analysis mainline -->

## 1. 代码与运行

- [ ] 服务可在 `8011` 正常启动
- [ ] `curl -sSf http://127.0.0.1:8011/health` 正常
- [ ] `curl -sSf http://127.0.0.1:8011/pipeline/overview` 正常

## 2. 页面与体验

- [ ] `概览` 正常加载
- [ ] `输入` 正常上传与分析
- [ ] `技能` 正常展示模块与能力
- [ ] `连接` 正常展示接入状态
- [ ] `学习` 正常展示最近反馈

## 3. 回归验证

- [ ] `node --check app/static/app.js` 通过
- [ ] `./.venv/bin/python -m pytest tests/test_api.py -q` 通过

## 4. 文档同步

- [ ] README 已更新
- [ ] 相关 docs 已更新
- [ ] 相关 `skill_specs/` 已更新
- [ ] 相关 `training_cases/` 已更新

## 5. GitHub 同步

- [ ] 本地提交已完成
- [ ] 远端 `main` 已同步
- [ ] 需要保留的工作分支已同步
