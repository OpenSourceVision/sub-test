# sub-test

自动检测订阅链接有效性的GitHub Actions项目。

## 功能

- 每天北京时间12点自动检测URL有效性
- 支持手动触发
- 自动去除重复URL
- 测试URL连通性
- 输出有效URL到 `out.txt`
- 自动提交更新到仓库

## 文件说明

| 文件 | 说明 |
|------|------|
| `url.txt` | URL列表（一行一个，支持 `- "url"` 格式） |
| `out.txt` | 输出的有效URL |
| `log.txt` | 检测日志 |
| `convert.py` | Python检测脚本 |
| `.github/workflows/check-urls.yml` | GitHub Actions工作流 |

## 格式要求

`url.txt` 支持以下格式：
```
https://raw.githubusercontent.com/xxx/xxx.yaml
- "https://raw.githubusercontent.com/xxx/xxx.yaml"
```

## 手动触发

访问 Actions → Check URLs → Run workflow

## 定时任务

每天北京时间12点自动运行（UTC 4:00）
