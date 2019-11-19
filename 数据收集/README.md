# 基于Scrapy框架采集电影信息

## 进度安排
### 11.01 测试好爬虫环境
### 11.12 完成所有数据的爬取
### 11.15 完成数据入库


## 环境
- scrapy+selenium+firefox

### 命令
- conda install scrapy
- conda install selenium
- 下载和安装 geckodriver
- wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
- mv /tmp/geckodriver-v0.26.0-linux64_orig.tar ./
- tar -xvf geckodriver-v0.26.0-linux64.tar.gz 
- sudo mv geckodriver /usr/local/bin/
- sudo yum install firefox
- sudo yum install unzip

## 运行
- 进入movieServer文件夹，直接运行movie.sh文件，带有两个参数，第一参数为开始电影序号，第二个参数为截止电影序号。
例如./movie.sh 0 10000，抓起0～10000电影的数据。
- 可以修改movie.sh脚本中关于每批数量、休眠时间等参数。
- 运行结束会在movirServer中创建posters文件夹和moviInfo.json文件，分别存储电影海报以及电影其他信息。
