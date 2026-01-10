# 🔧 GitHub Pages 设置指南

## ⚠️ 重要：需要在GitHub上启用Pages设置

如果您访问 https://hsq66.github.io/zhuoyan/ 还是看到README而不是网站，请按以下步骤操作：

---

## 📋 设置步骤

### 1️⃣ 访问仓库设置
1. 打开浏览器，访问：https://github.com/hsq66/zhuoyan
2. 点击仓库顶部的 **Settings**（设置）标签

### 2️⃣ 找到Pages设置
1. 在左侧菜单中，向下滚动找到 **Pages**
2. 点击 **Pages** 进入GitHub Pages设置页面

### 3️⃣ 配置Pages源
在 **Build and deployment** 部分：

**Source（源）设置**：
- 选择：**GitHub Actions** 
- ⚠️ 不要选择 "Deploy from a branch"

应该看到类似这样的界面：
```
Source: GitHub Actions
Your site is live at https://hsq66.github.io/zhuoyan/
```

### 4️⃣ 触发部署
设置完成后，有两种方式触发部署：

**方法1：推送代码（自动触发）**
```bash
git commit --allow-empty -m "触发GitHub Pages部署"
git push origin main
```

**方法2：手动触发**
1. 在GitHub仓库页面，点击 **Actions** 标签
2. 在左侧选择 **Deploy Hugo site to Pages** 工作流
3. 点击右侧的 **Run workflow** 按钮
4. 点击绿色的 **Run workflow** 确认

### 5️⃣ 查看部署状态
1. 点击 **Actions** 标签
2. 查看最新的工作流运行状态
3. 等待绿色的 ✅ 标记（通常需要2-3分钟）

### 6️⃣ 访问网站
部署成功后，访问：https://hsq66.github.io/zhuoyan/

---

## 🔍 故障排查

### 问题1：还是显示README
**原因**：Pages源设置为 "Deploy from a branch" 而不是 "GitHub Actions"

**解决**：
1. 进入 Settings > Pages
2. 将 Source 改为 **GitHub Actions**
3. 保存设置

### 问题2：Actions没有运行
**原因**：工作流权限未启用

**解决**：
1. 进入 Settings > Actions > General
2. 在 **Workflow permissions** 部分
3. 选择 **Read and write permissions**
4. 勾选 **Allow GitHub Actions to create and approve pull requests**
5. 点击 **Save**

### 问题3：部署失败
**查看日志**：
1. 点击 Actions 标签
2. 点击失败的工作流运行
3. 查看错误日志
4. 根据错误信息修复

---

## ✅ 验证部署成功

部署成功后，您应该看到：

1. **首页显示**：
   - 绿色主题的专业公司门户
   - Banner轮播图
   - 产品展示区
   - 关于我们和荣誉资质
   - 成功案例
   - 新闻动态

2. **导航菜单**：
   - 卓炎科技（首页）
   - 关于我们
   - 鼎英语
   - 智慧学习手机
   - OLED护眼台灯
   - 荣誉资质
   - 成功案例
   - 新闻动态

3. **页面底部**：
   - 公司信息
   - 联系方式
   - ICP备案号

---

## 🎯 快速检查清单

- [ ] GitHub仓库 Settings > Pages 已设置
- [ ] Source 选择为 "GitHub Actions"
- [ ] Actions 工作流已运行并成功
- [ ] 访问 https://hsq66.github.io/zhuoyan/ 显示网站而非README
- [ ] 网站首页正确显示所有内容
- [ ] 导航菜单可以正常工作
- [ ] 内页可以正常访问

---

## 📞 需要帮助？

如果按照以上步骤操作后仍有问题，请检查：

1. **Actions标签页**：查看工作流是否成功运行
2. **Pages设置**：确认Source是"GitHub Actions"而不是"Deploy from a branch"
3. **浏览器缓存**：清除浏览器缓存或使用无痕模式访问
4. **等待时间**：首次部署可能需要5-10分钟

---

## 🚀 一键触发部署

如果您已经完成了上述设置，运行以下命令触发部署：

```bash
git commit --allow-empty -m "🚀 触发GitHub Pages部署"
git push origin main
```

然后等待2-3分钟，访问：https://hsq66.github.io/zhuoyan/

---

**✨ 设置完成后，您的专业公司门户网站就会正式上线！**
