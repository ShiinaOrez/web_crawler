# PIXIV画作下载工具
**CODER:ShiinaOrez**

|版本|状态|开发者|开源|
|----|----|----|---|
|v2.0|正在开发|ShiinaOrez|√|

-----
## 简介
**pixiv_illust_downloader**是一个在**Linux Python3.6**以上环境下对pixiv网站上的画作进行下载的应用
目前十分简陋，只是简单的**几个文件**而已= =

目前开发的功能只有两个：~~（而且有的时候还会崩溃）~~
+ 根据作品id下载
+ 根据画师id下载热门作品

关于**保存路径**：当前路径/Images/画师名字/作品名称_p0(1,2,3,.....)_Illust_id.jpg(png)

-----

-----
## 准备工作
确保你的终端可以连接到Pixiv官网
使用下面的命令:

	curl -sL www.pixiv.net

如果没有输出，那么可以阅读[这个](https://samzong.me/2017/11/17/howto-use-ssr-on-linux-terminal/)
当然首先你要会用SSR科学上网

-----
## 开始使用
在终端输入以下命令：

	python3 run.py

然后会有**引导** = =~~（当然你不识字我也没有办法）~~

-----
## 版本信息

+ version 1.0   /2018.8.21
	+ 初步开发，开放根据作品ID下载作品
+ version 1.1   /2018.8.21
	+ 增加批量下载画师热门作品
+ version 1.2   /2018.8.22
	+ fix the bug of function 2, change the download tool **urllib** to **requests**
+ version 2.0   /2018.8.22
	+ change the request session, more stable. Change get ID's method from bs4 to JSON.

-----
