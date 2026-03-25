# 运行手册
<!-- security-log-analysis mainline -->

## 1. 目的

本文档说明本地运行、重启、健康检查、常见诊断与恢复方式。

## 2. 启动

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
./start.sh
```

## 3. 停止

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
PORT=8011 ./stop.sh
```

## 4. 健康检查

```bash
curl -sSf http://127.0.0.1:8011/health
curl -sSf http://127.0.0.1:8011/pipeline/overview
```

## 5. 常见诊断

### 5.1 页面持续加载中

优先检查：

- 服务是否已启动
- `health` 是否正常
- 静态资源是否强刷
- 浏览器缓存是否仍在使用旧版本资源

### 5.2 上传后分析异常

优先检查：

- 当前样本是否完整上传
- 历史脏数据是否混入
- 分类与 Skill 路由是否正确
- 下载版与页面版是否一致

### 5.3 服务掉线

优先检查：

- `start.sh` / `stop.sh` 默认端口是否为 `8011`
- watchdog 与 launch agent 是否仍在工作
- 当前机器上的端口是否冲突

## 6. 回归验证

```bash
cd '/Users/lei/Documents/New project/megaeth-ai-security-rebuild'
node --check app/static/app.js
./.venv/bin/python -m pytest tests/test_api.py -q
```

## 7. 运行原则

- 任何共享层改动都必须验证五个页面
- 不允许用其他项目文件污染当前运行态
- 发布前必须确认 GitHub 与本地已同步
