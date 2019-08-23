======
张凯朝
======

Email: zhangkaizhao@gmail.com

技术
====

* **编程语言**：熟悉 Python。了解其他语言 C、Java、JavaScript、Ruby、Go、Rust 等。
* **网络协议**：熟悉 HTTP/1.1 常用部分。
* **前端开发**：熟悉 HTML/XHTML，CSS，Ajax 等。了解 SASS、Node.js 等技术。
* **后端开发**：熟悉 Django、Flask、Tornado、aiohttp、Gunicorn 等 Python 框架/服务器。熟悉 WSGI 协议。了解 uWSGI、Uvicorn 等服务器/容器。了解 ASGI 协议。熟悉 Python 语言标准库及大部分常见第三方库比如 ORM SQLAlchemy、任务队列 Celery 等等。了解其他编程语言的后端开发框架及服务器。
* **API 设计**：RESTful 实践者。了解 JSON Schema、Swagger/OpenAPI 等。
* **数据存储**：熟悉 SQLite、Redis、Cassandra 等数据库。了解 MySQL/MariaDB、PostgreSQL、MongoDB 等数据库。
* **消息队列**：了解 AMQP/RabbitMQ、Redis 的 pubsub 功能。
* **服务器**：熟悉 Apache、nginx 等。了解 lighttpd、haproxy 等。
* **系统设计**：熟悉 MVC 软件设计、通过消息队列解偶服务依赖、使用插件机制可配置不同实现等。了解微服务。
* **开发环境**：熟悉 GNU/Linux（Debian/Ubuntu、Fedora、Arch Linux、Gentoo 等）和 FreeBSD 等。
* **开发工具**：熟悉 Git、Vim、各种 UNIX 小工具等。熟悉 Supervisor 进程管理系统。了解 Docker 容器虚拟化技术。
* **云平台**：熟悉 Google AppEngine(Python)。了解 AWS EC2/CloudWatch 等。
* **开发管理**：熟悉敏捷开发（Scrum）、持续集成（TeamCity）、代码审核（Gerrit、git-review）等。

工作经历
========

软件开发工程师 - 英特尔（中国）有限公司
---------------------------------------

2016-02 至 2017-04，深圳

工作内容：Safe Family 项目的服务器后端 CloudServices 开发（见后面项目描述）。

软件开发工程师 - 广州七乐康药业连锁有限公司
-------------------------------------------

2015-05 至 2015-10，广州

工作内容：隶属广州电商平台开发，Python 开发团队（大白云诊之用药助手项目及其他小项目等）的技术指导和实现。

技术栈：Python、Django、Celery、Whoosh 等。

高级软件开发工程师 - 广东彩惠智能科技有限公司
---------------------------------------------

2014-06 至 2015-01，广州

工作内容：互联网彩票代购系统彩乐透项目的开发（见后面项目描述）。

软件开发工程师 - 广州远云网络科技有限公司
-----------------------------------------

2011-05 至 2014-01，广州

工作内容：

* Syncbox 产品 Web server 后台的开发和维护、Linux 客户端以及相应的 DDNS 服务器端和客户端的开发维护（见后面项目描述）。
* 路由器产品 WIT-FII 公共网站的架构及实现以及相应的桌面客户端的开发（见后面项目描述）。

软件开发工程师 - 广州网融网络技术有限公司
-----------------------------------------

2010-05 至 2011-05，广州

工作内容：

* 自动升级服务器后台和客户端（基于 Google Omaha 项目）的开发。
* 文件同步服务端及客户端的原型开发。
* 证联项目的前期技术调研和原型开发（OpenID/OAuth）。
* 服务器及其他工作、项目相关管理系统的部署管理。

技术栈：Python、Tornado、wxPython、MongoDB、Java、Tomcat 等。

软件开发工程师 - 上海润普网络信息技术有限责任公司
-------------------------------------------------

2008-09 至 2009-12，广州

工作内容：

* EveryDo 各产品的开发。
* 协助产品的部署和运营。

技术栈：Python、Zope 3 等。

设备工程师 - 汕头超声显示器有限公司
-----------------------------------

2006-04 至 2008-07，汕头

工作内容：

* 前工序和后工序生产设备的维护维修。
* 相关配件、夹具的设计和完善。

设计技术栈：AutoCAD 和 SolidWorks。

项目
====

个人小项目
----------

时间：2008 至今

* **repos**：本地代码库管理工具。技术栈：Rust。
* **gnome-shell-extension-tray-icons**：GNOME shell extension - Tray icons。技术栈：GNOME Shell、JavaScript。
* **supportbot**：简单的问答助手库，基于模糊匹配和全文索引。技术栈：Python、fuzzywuzzy、jieba、Whoosh。
* **AUR packages**：为 Arch Linux 打包一些不错的新软件程序。技术栈：Arch Linux、Bash 等。
* **sfss**：大量小文件存储服务，基于豆瓣开源的 Beasdb。技术栈：Python、Beansdb。
* **magicoding**：基于 Tornado appengine demo 的小博客，运行在 Google AppEngine 上。技术栈：Python、Tornado、Markdown、Google AppEngine 等。

更多小项目及详情请见个人网站及 GitHub 代码库（见后面链接）。

Safe Family - 英特尔（中国）有限公司
------------------------------------

时间：2016-03 至 2017-03

描述：跨平台家庭设备保护系统，支持 Android、iOS 和 Windows 平台。功能包括：应用程序可用性控制；网页网址访问控制（仅限 Android 和 Windows 平台）；设备可使用时段控制（仅限 Android 和 iOS 平台）；电子地图围栏设定（仅限 Android 和 iOS 平台）；新装应用程序、访问网页网址、设备使用时间的请求即时通知和即时回应控制；设备所在地址变动的及时上报和设备进出电子地图围栏的及时通知；活动历史记录和查阅；设备位置及时跟踪。

工作内容：后台（命名为 CloudServices）主导开发。

*注：更多项目详细介绍请查阅另外提供的内容，以及查阅项目官方网站及各个平台的客户端说明（见后面链接）。*

技术栈：

* 服务器后端：Python、Tornado、Cassandra、nginx、Supervisor、Ubuntu Server 等。

年度测评
--------

时间：2015-11 至 2016-01

描述：外包项目。小型 Django 项目。某单位内部系统，为参加年度考核的在职人员提供民主测评功能，区分一般职工、中层干部及领导班子成员、每年度参与及不参与考核人员，管理后台提供每年度测评内容、考核小组、得分计算、考核等级评定及考核归档等，年度测评结束提供测评结果公示。最后提供管理员操作文档和部署文档。

技术栈：Python、Django、Gunicorn、MySQL、Ubuntu Server、nginx、bootstrap、jQuery、SASS 等。

彩乐透 - 广东彩惠智能科技有限公司
---------------------------------

时间：2014-06 至 2015-01

描述：互联网彩票代购系统。中小型 Flask 项目系统。为一般互联网用户提供在线代购福彩和体彩彩票服务，支持大乐透和双色球，集成在线支持功能以及与某彩票购买和出票接口。系统分为两个部分，分别为独立的 Python/Flask 服务器端，其中一部分提供网站功能给一般用户使用，另外一部分为后台管理使用。用户可通过网站注册、登录、充值、下单、支付、查询中奖与否、提款、参与在线活动等。网站还提供资讯信息。后台管理提供各种报表、充值、兑奖、退款等功能。

工作内容：开发维护。

* 增加各种新功能比如虚拟货币体系、在线活动等。
* 完善已有功能比如提款、下单支付、出票流程、各种后台管理功能等。
* 修补系统安全问题，改善系统架构、代码质量等。

技术栈：Python、Flask、SQLAlchemy、jQuery 等。

WIT-FII - 广州远云网络科技有限公司
----------------------------------

时间：2013-06 至 2014-01

描述：路由器产品。包括硬件设备和配套的软件系统。其中公共网站的功能包括：账户和路由器管理等接口服务；中转服务；在线商店等。

工作内容：公共网站的架构及实现。

* 为 iOS 客户端和 Android 客户端提供各种功能的服务接口。
* 在线商店实现了支付宝即时到帐接口，可正常购买产品。

技术栈：

* 公共网站：Python、gevent、SQLAlchemy、Redis 等。

Syncbox - 广州远云网络科技有限公司
----------------------------------

时间：2011-05 至 2013-06

描述：支持多平台的家庭私有存储服务，包括文件服务器端、版本服务器端、web 服务器端和 DDNS 服务器端，以及用于穿透防火墙的 UPnP 服务器端。其中 web 服务器端包括：与文件服务器端和版本服务器端对接（直接基于 TCP 协议，并使用 Proto Buffers 作为数据交换格式），提供 web 页面供在线浏览及文件操作；提供 web 接口供移动终端客户端使用。而其 DDNS 服务为每台连接到互联网和运行着 Syncbox 服务的设备提供动态域名服务。

工作内容：

* web 服务器端：各种文件（PDF、Office、音视频、纯文本等）的预览图、缩略图的获取和生成及文件元数据的获取。推送文件到 Dropbox、Google Drive、SkyDrive、金山快盘、酷盘。为 web 页面、iOS 和 Android 客户端添加了预览图、缩略图服务。
* DDNS 服务器端：接受来自客户端的 IP 地址上报，并用于更新 DDNS 的 A 记录。

技术栈：

* web 服务器端：Python、Tornado、gevent 等。
* DDNS 服务器端：Python、web.py、dnspython、gevent、MySQL 等。

教育
====

本科 - 机械工程及自动化
-----------------------

2001-09 至 2005-07，工学学士，华南理工大学

语言
====

* 英语：大学英语四级考试（CET-4，2004-03）
* 中文：普通话、潮州话、粤语

链接
====

个人的
------

* 网站: https://www.zhangkaizhao.com/
* GitHub: https://github.com/zhangkaizhao
* 领英: https://www.linkedin.com/in/zhangkaizhao

工作的
------

* Safe Family: http://family.mcafee.com/
* 彩乐透: http://www.clt500.com/
* WIT-FII: https://www.witfii.com/index.html
* Syncbox: http://www.syncbox.cn/ 和 http://www.isyncbox.com/
* EveryDo: http://www.everydo.com/

* 广州七乐康药业连锁有限公司: http://www.7lk.com/
* 广州网融网络技术有限公司: http://www.g4b.cn/
* 汕头超声显示器有限公司: http://www.goworld-lcd.com/
