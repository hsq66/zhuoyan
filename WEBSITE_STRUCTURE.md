# 卓炎科技网站完整结构

## 网站导航结构

基于原PBootCMS网站 (zhuoyan.hn.cn) 的完整结构迁移到Hugo静态网站

### 主导航菜单

1. **首页** `/`
   - 公司简介
   - 核心业务展示
   - 成功案例
   - 荣誉资质

2. **关于我们** `/about/`
   - 公司简介
   - 企业使命
   - 核心业务
   - 分支机构

3. **产品中心** `/services/`
   - **鼎英语** `/services/ai-english/`
     - 成长体系 `/services/ai-english/growth-system/`
     - 学习方案 `/services/ai-english/learning-plan/`
     - 核心技术 `/services/ai-english/core-tech/`
   - **智慧学习手机** `/services/smart-phone/`
   - **OLED护眼台灯** `/services/oled-lamp/`
   - **卫星通信服务** `/services/satellite/`
   - **数字化咨询** `/services/digital/`

4. **荣誉资质** `/honors/`
   - AI英语平台超级合伙人 `/honors/ai-partner/`
   - 教学机器人品牌 `/honors/robot-brand/`
   - 空气净化品牌 `/honors/air-purification/`

5. **成功案例** `/cases/`
   - 深圳燎原实训 (在公司新闻中)
   - 万千家长口碑 `/cases/parent-reviews/`
   - 优秀产品实践 `/cases/excellent-practice/`

6. **新闻资讯** `/news/`
   - **公司新闻** `/news/company/`
     - 鼎英语--深圳燎原实训
     - 普及太快！我们该不该对机器人征税呢
   - **行业新闻** `/news/industry/`
   - **常见问题** `/news/faq/`
     - 鼎英语主要特色是什么？

7. **联系我们** `/contact/`
   - 联系方式
   - 公司地址
   - 在线留言

## 数据库内容迁移清单

### ✅ 已完成迁移的15条内容

| ID | 标题 | 分类 | Hugo路径 |
|----|------|------|----------|
| 61 | 关于我们 | scode=1 | `/about.md` |
| 59 | 联系我们 | scode=12 | `/contact.md` |
| 38 | 普及太快！我们该不该对机器人征税呢 | scode=16 | `/news/company/robot-tax.md` |
| 62 | 鼎英语--深圳燎原实训 | scode=16 | `/news/company/liaoyuan-training.md` |
| 63 | 鼎英语主要特色是什么？ | scode=18 | `/news/faq/dingyingyu-features.md` |
| 3 | 鼎英语-核心技术优势 | scode=3 | `/services/ai-english/core-tech.md` |
| 2 | 鼎英语-颠覆性的学习方案 | scode=3 | `/services/ai-english/learning-plan.md` |
| 1 | 鼎英语成长体系 | scode=3 | `/services/ai-english/growth-system.md` |
| 11 | 智慧学习手机 | scode=4 | `/services/smart-phone.md` |
| 13 | OLED护眼台灯-学习版 | scode=5 | `/services/oled-lamp.md` |
| 17 | AI英语平台超级合伙人 | scode=7 | `/honors/ai-partner.md` |
| 19 | 教学机器人品牌 | scode=7 | `/honors/robot-brand.md` |
| 20 | 空气净化品牌 | scode=7 | `/honors/air-purification.md` |
| 64 | 万千家长的口碑好评 | scode=9 | `/cases/parent-reviews.md` |
| 65 | 优秀产品实践 | scode=9 | `/cases/excellent-practice.md` |

## 公司信息

### 联系方式
- **电话：** 18923719468
- **邮箱：** axel@long.kim
- **QQ：** 45451202
- **官网：** www.zhuoyan.tech

### 分支机构

**深圳总部：**
广东省深圳市龙岗区龙城街道办龙平西路137号祥情世纪城市广场二楼

**市场运营中心（海南）：**
海南省澄迈县老城镇高新技术产业示范区海南生态软件园孵化楼五楼1001室

**深圳研发中心：**
广东省深圳市南山区粤海街道海天一路11号软件产业基地5栋A座4栋433

## 核心业务

1. **AI智能英语** - 鼎英语学习平台，助力50万+学员快速提升
2. **智慧学习手机** - 小嘢马学习手机，专注学习，防沉迷
3. **OLED护眼台灯** - 健康照明，减少90%有害蓝光
4. **卫星通信服务** - 综合卫星通信物联解决方案
5. **数字化咨询** - 工业4.0数字化信息咨询服务

## 网站特色

- **专业性：** 公司门户网站，展示企业实力和产品优势
- **完整性：** 100%迁移原网站所有数据库内容
- **结构化：** 清晰的导航结构，符合企业网站标准
- **SEO优化：** 完整的meta信息，利于搜索引擎收录

## 技术栈

- **静态网站生成器：** Hugo
- **主题：** dot-hugo
- **部署平台：** GitHub Pages
- **原网站：** PBootCMS (PHP)
- **数据库：** SQLite (已完整提取)

## 下一步

1. 测试Hugo本地构建
2. 优化主题样式
3. 添加更多图片和媒体资源
4. 配置GitHub Actions自动部署
5. 绑定域名 zhuoyan.hn.cn
