@echo off
echo 开始部署到GitHub Pages...

cd public
git init
git add -A
git commit -m "优化首页 - 突出五大核心业务"
git push -f https://github.com/hsq66/zhuoyan.git HEAD:gh-pages
cd ..

echo 部署完成！
echo 网站地址: https://hsq66.github.io/zhuoyan/
pause
