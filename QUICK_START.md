# 快速开始指南

## 🎉 项目改造完成！

您的网站已成功从 PBootCMS 迁移到 Hugo + dot-hugo 主题。

## 📋 已完成的工作

✅ 创建 Hugo 网站结构  
✅ 配置 dot-hugo 主题  
✅ 创建中文内容和文档  
✅ 设置 GitHub Actions 自动部署  
✅ 配置 GitHub Pages  
✅ 迁移图片资源  
✅ 创建多语言支持  
✅ 添加部署和迁移指南  

## 🚀 下一步操作

### 1. 推送代码到 GitHub

由于网络问题，您需要手动推送代码：

```bash
# 方法 A: 使用 HTTPS（可能需要代理）
git push -u origin main

# 方法 B: 使用 SSH
git remote set-url origin git@github.com:hsq66/zhuoyan.git
git push -u origin main

# 方法 C: 使用 GitHub Desktop
# 打开 GitHub Desktop，选择此仓库，点击 "Push origin"
```

### 2. 配置 GitHub Pages

推送成功后：

1. 访问：https://github.com/hsq66/zhuoyan/settings/pages
2. 在 "Source" 下选择 **"GitHub Actions"**
3. 保存设置

### 3. 等待部署完成

- 查看部署状态：https://github.com/hsq66/zhuoyan/actions
- 首次部署大约需要 2-3 分钟
- 部署完成后，网站将在：**https://hsq66.github.io/zhuoyan/**

## 💻 本地开发

### 安装 Hugo

**Windows:**
```bash
# 使用 Chocolatey
choco install hugo-extended

# 或从官网下载
# https://github.com/gohugoio/hugo/releases
```

**macOS:**
```bash
brew install hugo
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install hugo

# 或下载二进制文件
wget https://github.com/gohugoio/hugo/releases/download/v0.128.0/hugo_extended_0.128.0_linux-amd64.deb
sudo dpkg -i hugo_extended_0.128.0_linux-amd64.deb
```

### 启动开发服务器

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 访问 http://localhost:1313
```

### 构建生产版本

```bash
npm run build
```

## 📝 内容管理

### 添加新文档

```bash
# 创建新的功能文档
hugo new content/zh/features/new-feature.md

# 创建新的安装指南
hugo new content/zh/installation/new-guide.md
```

### 编辑内容

直接编辑 `content/zh/` 目录下的 Markdown 文件：

```markdown
---
title: "文档标题"
description: "文档描述"
weight: 1
draft: false
---

## 标题

内容...
```

### 添加图片

1. 将图片放在 `static/images/` 目录
2. 在 Markdown 中引用：

```markdown
![图片描述](/images/your-image.jpg)
```

## 🔧 自定义配置

### 修改网站信息

编辑 `hugo.toml`:
```toml
title = "您的网站标题"
baseURL = "https://hsq66.github.io/zhuoyan/"
```

### 修改主题颜色

编辑 `hugo.toml` 中的 `[params.variables]` 部分：
```toml
[params.variables]
color_primary = "#02007e"  # 主色调
body_color = "#f9f9f9"     # 背景色
```

### 修改导航菜单

编辑 `config/_default/languages.toml` 中的 `[[zh.menu.main]]` 部分。

## 📚 文档结构

```
content/zh/
├── _index.md              # 首页
├── features/              # 功能特性
│   └── core-features/
│       ├── _index.md
│       ├── feature-1.md
│       └── feature-2.md
├── installation/          # 安装指南
│   ├── _index.md
│   ├── requirements/
│   │   ├── _index.md
│   │   └── system-requirements.md
│   └── install/
│       ├── _index.md
│       └── quick-start.md
└── pages/                 # 其他页面
    ├── about.md
    ├── contact.md
    └── faq.md
```

## 🔍 常用命令

```bash
# 开发
npm run dev              # 启动开发服务器
npm run build            # 构建生产版本
npm run clean            # 清理构建文件

# Git
git add .                # 添加所有更改
git commit -m "消息"     # 提交更改
git push origin main     # 推送到 GitHub

# Hugo
hugo new content/zh/path/file.md  # 创建新文件
hugo server --buildDrafts         # 包含草稿预览
```

## 📖 参考文档

- **Hugo 官方文档**: https://gohugo.io/documentation/
- **Dot 主题文档**: https://docs.gethugothemes.com/dot/
- **Markdown 语法**: https://www.markdownguide.org/
- **部署指南**: 查看 `DEPLOY.md`
- **迁移指南**: 查看 `MIGRATION_GUIDE.md`

## ❓ 故障排除

### Hugo 命令未找到
确保已安装 Hugo Extended 版本，并添加到系统 PATH。

### 推送失败
- 检查网络连接
- 尝试使用 SSH 而不是 HTTPS
- 配置 Git 代理（如果有）

### 网站未更新
- 检查 GitHub Actions 是否成功运行
- 清除浏览器缓存
- 等待几分钟让 CDN 更新

### 图片不显示
- 确保图片在 `static/images/` 目录
- 使用绝对路径：`/images/xxx.jpg`
- 检查图片文件名大小写

## 🎯 下一步建议

1. **完善内容**
   - 根据原网站内容补充文档
   - 添加更多功能介绍
   - 完善常见问题

2. **优化 SEO**
   - 为每个页面添加 description
   - 设置合适的 keywords
   - 添加 sitemap（Hugo 自动生成）

3. **添加功能**
   - 集成评论系统（Disqus/Utterances）
   - 添加统计分析（Google Analytics）
   - 集成表单服务（Formspree）

4. **自定义主题**
   - 修改颜色和字体
   - 添加自定义 CSS
   - 调整布局

## 📧 需要帮助？

如有问题，请：
- 查看文档：`README.md`, `DEPLOY.md`, `MIGRATION_GUIDE.md`
- 提交 Issue：https://github.com/hsq66/zhuoyan/issues
- 查看 Hugo 社区：https://discourse.gohugo.io/

---

**祝您使用愉快！** 🎉
