# 从 PBootCMS 迁移到 Hugo 指南

## 概述

本项目已从基于 PHP 的 PBootCMS 迁移到基于 Hugo 的静态网站生成器。

## 主要变化

### 技术栈

**之前 (PBootCMS):**
- PHP 后端
- MySQL 数据库
- 动态内容管理
- 服务器端渲染

**现在 (Hugo):**
- 静态网站生成器
- Markdown 文件存储内容
- 无需数据库
- 构建时生成 HTML
- 部署到 GitHub Pages

### 优势

1. **性能提升**
   - 静态 HTML，加载速度极快
   - 无需服务器端处理
   - CDN 友好

2. **安全性**
   - 无数据库，无 SQL 注入风险
   - 无服务器端代码执行
   - 静态文件，攻击面小

3. **维护成本**
   - 无需服务器维护
   - 无需数据库管理
   - GitHub Pages 免费托管

4. **版本控制**
   - 所有内容在 Git 中
   - 完整的历史记录
   - 易于协作和回滚

## 内容迁移

### 文章/页面

PBootCMS 的动态内容已转换为 Markdown 文件：

```
content/zh/
├── _index.md              # 首页
├── features/              # 功能特性
│   └── core-features/
├── installation/          # 安装指南
│   ├── requirements/
│   └── install/
└── pages/                 # 其他页面
    ├── about.md
    ├── contact.md
    └── faq.md
```

### 图片资源

图片已从以下位置迁移：
- `static/upload/` → `static/images/`
- `uploads/` → `static/images/`
- 模板图片 → `static/images/`

### URL 结构

**之前:**
```
http://zhuoyan.hn.cn/index.php?page=about
http://zhuoyan.hn.cn/article/123.html
```

**现在:**
```
https://hsq66.github.io/zhuoyan/about/
https://hsq66.github.io/zhuoyan/features/core-features/feature-1/
```

## 如何添加新内容

### 1. 创建新文章

```bash
# 使用 Hugo 命令
hugo new content/zh/features/new-feature.md

# 或手动创建文件
```

### 2. 编辑 Markdown 文件

```markdown
---
title: "文章标题"
description: "文章描述"
weight: 1
draft: false
---

## 标题

文章内容...
```

### 3. 添加图片

将图片放在 `static/images/` 目录，然后在 Markdown 中引用：

```markdown
![图片描述](/images/your-image.jpg)
```

### 4. 预览和发布

```bash
# 本地预览
npm run dev

# 构建
npm run build

# 推送到 GitHub（自动部署）
git add .
git commit -m "添加新内容"
git push origin main
```

## 保留的旧文件

以下目录保留用于参考，但不会在新网站中使用：

- `apps/` - PBootCMS 应用代码
- `core/` - PBootCMS 核心代码
- `template/default/` - 旧模板文件
- `*.php` - PHP 文件

这些文件已在 `.gitignore` 中排除，不会提交到 Git。

## 数据库内容

如果需要从旧数据库导出内容：

1. 导出数据库：
```bash
mysqldump -u username -p database_name > backup.sql
```

2. 将数据转换为 Markdown 文件（需要自定义脚本）

3. 放置在 `content/zh/` 相应目录

## 自定义主题

如果需要自定义 dot-hugo 主题：

1. 复制主题文件到项目根目录：
```bash
cp -r dot-hugo/layouts layouts/
cp -r dot-hugo/assets assets/
```

2. 修改文件

3. Hugo 会优先使用项目根目录的文件

## 常见问题

### Q: 如何实现动态功能（如表单提交）？

A: 使用第三方服务：
- 表单：Formspree, Netlify Forms
- 评论：Disqus, Utterances
- 搜索：Algolia, Lunr.js（已集成）

### Q: 如何管理多语言？

A: Hugo 内置多语言支持，在 `config/_default/languages.toml` 中配置。

### Q: 如何添加自定义 CSS/JS？

A: 
- CSS: 添加到 `assets/scss/custom.scss`
- JS: 添加到 `assets/js/` 并在配置中引用

### Q: 如何设置 SEO？

A: 在每个页面的 Front Matter 中设置：
```yaml
---
title: "页面标题"
description: "页面描述"
keywords: ["关键词1", "关键词2"]
---
```

## 需要帮助？

- Hugo 文档：https://gohugo.io/documentation/
- Dot 主题文档：https://docs.gethugothemes.com/dot/
- GitHub Issues：https://github.com/hsq66/zhuoyan/issues

## 回滚到旧版本

如果需要回滚到 PBootCMS：

1. 恢复 PHP 文件（从备份）
2. 恢复数据库
3. 配置 Web 服务器指向 `index.php`

建议保留旧系统的完整备份。
