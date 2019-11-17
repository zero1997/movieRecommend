import scrapy
from movieRecommend.items import MovierecommendItem
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import requests

import pandas as pds
import os
from time import sleep
import random


class movieSpider(scrapy.Spider):
    name = 'movieSpider'

    def start_requests(self):
        # 读取电影信息
        # df_movies = pds.read_csv('/Users/cm/course/云计算与大数据平台/movieRecommend/ml-20m/movies.csv')
        # mac 命令行文件名
        # filename = os.path.abspath('..') + r'/ml-20m/movies.csv' #获取存储电影信息的文件名

        # 从命令中获取开始和结束的电影index
        start = int(getattr(self, 'start', None))
        end = int(getattr(self, 'end', None))
        cookiesChange = int(getattr(self, 'cookiesChange', None))
        # start, end, cookiesChange = [int(x) for x in os.sys.argv[1:]]
        print('*' * 15 + '\n抓取{}到{}的电影...'.format(start, end))

        # 其他方式运行的文件名
        filename = os.path.abspath('') + r'/movies.csv'  # 获取存储电影信息的文件名
        df_movies = pds.read_csv(filename)

        # 读取ip池
        # ipList = []
        # with open('ip.txt') as f_ip:
        #     for line in f_ip:
        #         ip = line.strip()
        #         ipList.append(ip)
        # f_ip.close()

        # 获取一个ip随机的driver
        # driver = self.get_random_driver(ipList=ipList)

        # 新建Firefox driver
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        # 用request获取一个cookies
        cookies = self.get_cookies()

        # 设置最长等待时间
        max_timeOut = 60

        with open('success.csv', 'a') as f_success:
            for index in df_movies.index[start:end]:  # 爬取start到end的电影数据
                movieId = int(df_movies.loc[index, 'movieId'])  # pds直接读出来是int64，不能转成json，要改成int
                movieName = df_movies.loc[index, 'title']
                print("正在抓取movieId={}的地址...".format(movieId))
                # 用selenium爬取电影网页地址
                sleep(random.randint(2, 4))
                driver.get('https://movie.douban.com')
                # 设置等待时间
                WebDriverWait(driver, max_timeOut).until(
                    EC.visibility_of(driver.find_element_by_name('search_text'))).send_keys(movieName)
                sleep(1)
                WebDriverWait(driver, max_timeOut).until(
                    EC.visibility_of(driver.find_element_by_xpath('//input[@type="submit"]'))).click()
                try:  # 检查有没有爬取到电影链接
                    url = WebDriverWait(driver, max_timeOut).until(
                        EC.visibility_of(driver.find_element_by_class_name('cover-link'))).get_property('href')
                except:
                    print('{}抓取不成功！'.format(movieId))
                    continue
                else:
                    if (url.split('/')[-3] == 'subject'):  # 判断抓到的url是不是电影的url
                        print("movieId={}的电影地址抓取成功！".format(movieId))
                        f_success.write('{},{},{}\n'.format(movieId, movieName, url))
                    else:
                        print('{}抓取不成功！'.format(movieId))
                        continue
                # 根据爬到的url进一步爬取电影信息
                request = scrapy.Request(url=url, callback=self.parse, cookies=cookies)
                request.meta['movieId'] = movieId
                request.meta['url'] = url
                request.meta['cookies'] = cookies
                yield request

                # 切换cookies
                if index % cookiesChange == 0:
                    driver = self.change_cookies(driver)
                    cookies = self.get_cookies()

        driver.close()

    def parse(self, response):
        item = MovierecommendItem()  # 初始化item实例

        item['movieId'] = response.meta['movieId']  # 接收传入的movieId
        item['referenceUrl'] = response.meta['url']  # 电影信息来源地址
        item['cookies'] = response.meta['cookies']  # 记录cookies

        print('正在获取ID为{}的数据...'.format(item['movieId']))

        article = response.css('div.article')  # 所有有待提取的片段，包括卡片和下面的影评
        indent_clearfix = response.css('div.indent.clearfix')  # 只包含上面电影卡片内容

        info = indent_clearfix.css('#info')  # 提取与电影信息有关的内容

        # 提取豆瓣电影名
        item['movieNameDouban'] = ''.join(response.css('#content h1 span::text').extract())

        # 提取导演  如果超过一个人会有' / '，需要删除
        item['director'] = info.xpath('span/span[contains(text(),"导演")]/following-sibling::*//text()').extract()
        if len(item['director']) > 1:
            item['director'] = list(set(item['director']))
            item['director'].remove(' / ')

        # 提取编剧
        item['scriptwriter'] = info.xpath('span/span[contains(text(),"编剧")]/following-sibling::*//text()').extract()
        if len(item['scriptwriter']) > 1:
            item['scriptwriter'] = list(set(item['scriptwriter']))
            item['scriptwriter'].remove(' / ')

        # 提取主演
        item['mainActor'] = info.xpath('span/span[contains(text(),"主演")]/following-sibling::*//text()').extract()
        if len(item['mainActor']) > 1:
            item['mainActor'] = list(set(item['mainActor']))
            item['mainActor'].remove(' / ')

        # 提取类型
        item['filmType'] = info.xpath(
            'span[contains(text(),"类型")]/following-sibling::node()[position()< {}]//text()'.format(
                len(info.xpath('span[contains(text(),"类型")]/following-sibling::node()'))
                - len(info.xpath('span[contains(text(),"制片国家/地区")]/following-sibling::node()')))).extract()

        # 提取制片国家/地区 string
        item['countryArea'] = info.xpath('span[contains(text(),"制片国家/地区")]/following-sibling::node()').extract_first()

        # 提取语言
        item['language'] = info.xpath('span[contains(text(),"语言")]/following-sibling::node()').extract_first()

        # 提取上映日期
        item['date'] = info.xpath(
            'span[contains(text(),"上映日期")]/following-sibling::*[position()=1]//text()').extract_first()

        # 提取片长
        item['filmDuration'] = info.xpath(
            'span[contains(text(),"片长")]/following-sibling::*[position()=1]//text()').extract_first()

        # 提取电影简介
        item['filmSummary'] = article.xpath('//span[@property="v:summary"]//text()').extract_first()

        # 提取电影评价
        item['comments'] = article.css('#hot-comments .short::text').extract()

        # 爬取海报
        mainpic = indent_clearfix.css('#mainpic')  # 电影卡片海报模块
        item['morePosterUrl'] = mainpic.css(' ::attr(href)').extract_first()
        item['posterUrl'] = mainpic.css(' img::attr(src)').extract_first()
        item['posterName'] = str(item['movieId'])

        yield item

    def get_random_driver(self, ipList):
        '''构造ip随机的driver'''
        # 利用options实现headless
        options = Options()
        options.headless = True
        while True:
            # tempIp = random.choice(ipList)
            tempIp = '119.142.206.251:4241'
            options.add_argument('--proxy-server=http://' + tempIp)  # 随机设置ip
            driver = webdriver.Firefox(options=options)
            driver.get('https://movie.douban.com')
            try:
                driver.find_element_by_name('search_text')
            except NoSuchElementException:
                print(tempIp + '不可用，正在测试下一个ip...')
                ipList.remove(tempIp)  # 删除这个不可用的ip
                driver.close()
                if len(ipList) == 0:
                    print('*' * 20 + '\n无可用ip')
            else:
                print(tempIp + '可用，下面抓取电影url...')
                return driver

    def change_cookies(self, driver):
        '''为传入的driver换一个新的cookies'''
        options = Options()
        options.headless = True
        newDriver = webdriver.Firefox(options=options)
        newDriver.get('http://movie.douban.com')
        try:
            newDriver.find_element_by_name('search_text')
        except NoSuchElementException:
            print("没有获取有效cookies！")
            newDriver.close()  # 关闭新建的Firefox窗口
            return None
        else:
            print('获取新cookies成功！')
            newCookies = newDriver.get_cookies()
            driver.get('http://movie.douban.com')
            driver.delete_all_cookies()  # 删除现有cookies
            for cookie in newCookies:
                driver.add_cookie(cookie)  # 添加新的cookies
            newDriver.close()  # 关闭新建的Firefox窗口
            return driver

    def get_cookies(self):
        '''获取一个cookies，为爬具体的电影网页准备cookies'''
        return requests.get('https://movie.douban.com').cookies.get_dict()
