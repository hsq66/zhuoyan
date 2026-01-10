# 部署指南

## 推送到 GitHub

由于网络问题，您可能需要配置代理或使用其他方式推送代码。

### 方法 1: 使用 Git 命令推送

```bash
# 确保在 main 分支
git branch -M main

# 推送到 GitHub
git push -u origin main
```

### 方法 2: 如果遇到网络问题

如果遇到 GitHub 连接问题，可以尝试：

1. **配置 Git 代理**（如果您有代理）：
```bash
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

2. **使用 SSH 而不是 HTTPS**：
```bash
git remote set-url origin git@github.com:hsq66/zhuoyan.git
git push -u origin main
```

3. **使用 GitHub Desktop 或其他 Git 客户端**

### 方法 3: 手动上传

如果以上方法都不行，可以：
1. 访问 https://github.com/hsq66/zhuoyan
2. 使用 GitHub 网页界面上传文件
3. 或者使用 GitHub CLI: `gh repo create`

## 配置 GitHub Pages

推送成功后：

1. 访问仓库设置：https://github.com/hsq66/zhuoyan/settings/pages
2. 在 "Source" 下选择 "GitHub Actions"
3. GitHub Actions 会自动运行并部署网站

## 查看部署状态

- Actions 页面：https://github.com/hsq66/zhuoyan/actions
- 部署完成后，网站将在：https://hsq66.github.io/zhuoyan/

## 本地测试

在推送之前，可以本地测试：

```bash
# 安装 Hugo (如果还没安装)
# Windows: choco install hugo-extended
# 或从 https://github.com/gohugoio/hugo/releases 下载

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 访问 http://localhost:1313
```

## 构建测试

```bash
# 构建生产版本
npm run build

# 检查 public/ 目录中的输出
```

## 故障排除

### Hugo 未安装
下载并安装 Hugo Extended 版本：
https://github.com/gohugoio/hugo/releases

### 主题文件缺失
确保 dot-hugo 目录存在且包含所有文件。

### 图片未显示
- 检查图片路径是否正确
- 确保图片在 static/images/ 目录中
- 图片 URL 应该是相对路径，如 `/images/logo.png`

### GitHub Actions 失败
- 检查 .github/workflows/hugo.yml 文件
- 查看 Actions 日志获取详细错误信息
- 确保仓库有 Pages 权限

## 更新网站

修改内容后：

```bash
git add .
git commit -m "更新内容"
git push origin main
```

GitHub Actions 会自动重新部署。
