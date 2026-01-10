# 🔧 启用GitHub Actions部署 - 解决方案

## 问题：Source没有"GitHub Actions"选项

您当前看到的是 **Deploy from a branch**，这是因为GitHub Actions工作流还没有运行过。

---

## ✅ 解决步骤

### 方法1：手动触发Actions工作流（推荐）

1. **访问Actions页面**
   - 打开：https://github.com/hsq66/zhuoyan/actions

2. **找到工作流**
   - 在左侧列表中，点击 **"Deploy Hugo site to Pages"**

3. **手动运行**
   - 点击右上角的 **"Run workflow"** 按钮
   - 在弹出的下拉菜单中，再次点击绿色的 **"Run workflow"** 按钮

4. **等待完成**
   - 等待工作流运行完成（约2-3分钟）
   - 看到绿色的 ✅ 标记表示成功

5. **返回Pages设置**
   - 回到 Settings > Pages
   - 现在 Source 下拉菜单应该会出现 **"GitHub Actions"** 选项
   - 选择它！

---

### 方法2：使用当前的"Deploy from a branch"设置

如果您想快速看到网站，可以暂时使用这个方法：

1. **在Pages设置中**：
   - Source: **Deploy from a branch**
   - Branch: 选择 **gh-pages** 分支（如果有）
   - 或者选择 **main** 分支，文件夹选择 **/public**

2. **但这需要我们调整部署方式**

让我为您创建一个gh-pages分支部署方案：

---

## 🚀 方案A：创建gh-pages分支（最简单）

我现在帮您构建并推送到gh-pages分支：

```bash
# 构建网站
hugo --cleanDestinationDir --baseURL "https://hsq66.github.io/zhuoyan/"

# 进入public目录
cd public

# 初始化git
git init
git add -A
git commit -m "部署网站到gh-pages"

# 推送到gh-pages分支
git push -f https://github.com/hsq66/zhuoyan.git main:gh-pages

# 返回上级目录
cd ..
```

然后在GitHub Pages设置中：
- Source: **Deploy from a branch**
- Branch: **gh-pages**
- Folder: **/ (root)**
- 点击 **Save**

---

## 🎯 方案B：等待Actions运行后切换

1. 先让Actions工作流运行一次（方法1）
2. 运行成功后，GitHub会自动识别
3. 返回Pages设置，选择"GitHub Actions"

---

## 📋 我现在帮您做什么？

我建议使用**方案A**（gh-pages分支），因为：
- ✅ 立即生效，不需要等待
- ✅ 不需要复杂的Actions权限设置
- ✅ 更简单直接

让我现在就帮您部署到gh-pages分支！
