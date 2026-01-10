# 卓研知识库与支持中心

基于 Hugo 静态网站生成器和 Dot 主题构建的知识库与技术支持中心。

## 🚀 特性

- ✨ 基于 Hugo 的快速静态网站
- 📱 响应式设计，支持移动端
- 🔍 内置搜索功能
- 🌐 多语言支持（中文）
- 📝 Markdown 编写文档
- 🎨 基于 Dot 主题的专业外观
- 🚀 自动部署到 GitHub Pages

## 📋 前置要求

- [Hugo Extended](https://gohugo.io/installation/) v0.128.0 或更高版本
- [Node.js](https://nodejs.org/) v16 或更高版本
- [Git](https://git-scm.com/)

## 🛠️ 本地开发

### 1. 克隆仓库

```bash
git clone https://github.com/hsq66/zhuoyan.git
cd zhuoyan
```

### 2. 安装依赖

```bash
npm install
```

### 3. 启动开发服务器

```bash
npm run dev
```

访问 `http://localhost:1313` 查看网站。

## 📦 构建

构建生产版本：

```bash
npm run build
```

构建后的文件将输出到 `public/` 目录。

## 🚀 部署

本项目配置了 GitHub Actions 自动部署工作流。当代码推送到 `main` 分支时，会自动构建并部署到 GitHub Pages。

### 配置 GitHub Pages

1. 进入仓库的 Settings > Pages
2. Source 选择 "GitHub Actions"
3. 推送代码到 main 分支即可自动部署

网站将发布到：`https://hsq66.github.io/zhuoyan/`

## 📝 内容管理

### 添加新文档

在 `content/zh/` 目录下创建 Markdown 文件：

```bash
# 创建新的功能文档
hugo new content/zh/features/new-feature.md

# 创建新的安装指南
hugo new content/zh/installation/new-guide.md
```

### 文档结构

```
content/zh/
├── _index.md              # 首页
├── features/              # 功能特性
│   └── core-features/
├── installation/          # 安装指南
│   ├── requirements/
│   └── install/
└── pages/                 # 其他页面
    ├── faq.md
    └── contact.md
```

### Front Matter 示例

```yaml
---
title: "文档标题"
description: "文档描述"
weight: 1
draft: false
---

文档内容...
```

## 🎨 自定义

### 修改配置

主要配置文件：
- `hugo.toml` - Hugo 主配置
- `config/_default/params.toml` - 主题参数
- `config/_default/languages.toml` - 语言配置

### 修改样式

主题样式位于 `dot-hugo/assets/scss/` 目录。

### 添加图片

将图片放在以下目录：
- `static/images/` - 网站图片
- `content/zh/*/images/` - 文档相关图片

## 📚 文档

- [Hugo 文档](https://gohugo.io/documentation/)
- [Dot 主题文档](https://docs.gethugothemes.com/dot/)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📧 联系方式

- 网站：https://zhuoyan.hn.cn
- GitHub：https://github.com/hsq66
- 邮箱：support@example.com

---

由卓研团队用 ❤️ 构建
