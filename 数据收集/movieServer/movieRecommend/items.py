# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovierecommendItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movieId = scrapy.Field()  # 电影编号
    movieNameDouban = scrapy.Field()  # 豆瓣电影名
    director = scrapy.Field()  # 电影导演
    scriptwriter = scrapy.Field()  # 电影编剧
    mainActor = scrapy.Field()  # 电影主演
    filmType = scrapy.Field()  # 电影类型
    countryArea = scrapy.Field()  # 制片国家
    language = scrapy.Field()  # 电影语言
    date = scrapy.Field()  # 上映日期
    filmDuration = scrapy.Field()  # 片长
    filmSummary = scrapy.Field()  # 电影简介
    comments = scrapy.Field()  # 电影评价
    posterUrl = scrapy.Field()  # 海报地址
    posterName = scrapy.Field()  # 海报名称
    morePosterUrl = scrapy.Field()  # 更多海报地址
    referenceUrl = scrapy.Field()  # 信息来源地址

    cookies = scrapy.Field()  # 记录cookies，用来为获取海报提供cookies
    pass
