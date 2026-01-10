---
title: "快速开始"
description: "5分钟快速安装指南"
weight: 1
---

## 快速开始

本指南将帮助您在 5 分钟内完成基本安装。

### 步骤 1: 下载安装包

```bash
# 使用 git 克隆仓库
git clone https://github.com/hsq66/zhuoyan.git
cd zhuoyan
```

### 步骤 2: 安装依赖

```bash
# 安装 Node.js 依赖
npm install

# 或使用 yarn
yarn install
```

### 步骤 3: 配置环境

```bash
# 复制配置文件模板
cp .env.example .env

# 编辑配置文件
nano .env
```

### 步骤 4: 初始化数据库

```bash
# 运行数据库迁移
npm run migrate

# 导入初始数据
npm run seed
```

### 步骤 5: 启动服务

```bash
# 开发模式
npm run dev

# 生产模式
npm run build
npm start
```

### 验证安装

访问 `http://localhost:3000` 查看是否安装成功。

默认管理员账号：
- 用户名: admin
- 密码: admin123

**重要提示：** 首次登录后请立即修改默认密码！

### 下一步

- [详细配置指南](../configuration/)
- [安全设置](../../security/)
- [性能优化](../../optimization/)
