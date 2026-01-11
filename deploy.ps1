# Hugo网站部署脚本 - 部署到GitHub Pages (gh-pages分支)

Write-Host "开始部署Hugo网站到GitHub Pages..." -ForegroundColor Green

# 1. 清理并构建网站
Write-Host "步骤 1: 构建Hugo网站..." -ForegroundColor Yellow
hugo --cleanDestinationDir
if ($LASTEXITCODE -ne 0) {
    Write-Host "Hugo构建失败！" -ForegroundColor Red
    exit 1
}

# 2. 进入public目录
Write-Host "步骤 2: 准备部署文件..." -ForegroundColor Yellow
cd public

# 3. 初始化git（如果需要）
if (-not (Test-Path ".git")) {
    git init
    git remote add origin https://github.com/hsq66/zhuoyan.git
}

# 4. 添加所有文件并提交
Write-Host "步骤 3: 提交更改..." -ForegroundColor Yellow
git add -A
$commitDate = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
git commit -m "部署网站 - $commitDate"

# 5. 强制推送到gh-pages分支
Write-Host "步骤 4: 推送到gh-pages分支..." -ForegroundColor Yellow
git push -f origin HEAD:gh-pages

# 6. 返回主目录
cd ..

Write-Host "部署完成！" -ForegroundColor Green
Write-Host "网站地址: https://hsq66.github.io/zhuoyan/" -ForegroundColor Cyan
Write-Host "请到GitHub仓库设置中确认：" -ForegroundColor Yellow
Write-Host "Settings > Pages > Source: Deploy from a branch" -ForegroundColor White
Write-Host "Branch: gh-pages, Folder: / (root)" -ForegroundColor White
