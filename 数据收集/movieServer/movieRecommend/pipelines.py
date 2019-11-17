# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
import os
from linecache import getline
from random import randint


class MovierecommendPipeline(object):
    def process_item(self, item, spider):
        # 构造基本信息字典
        dict_movieInfo = {'movieId': item['movieId'],
                          'movieNameDouban': item['movieNameDouban'],
                          'director': item['director'],
                          'scriptwriter': item['scriptwriter'],
                          'mainActor': item['mainActor'],
                          'filmType': item['filmType'],
                          'countryArea': item['countryArea'],
                          'language': item['language'],
                          'date': item['date'],
                          'filmDuration': item['filmDuration'],
                          'filmSummary': item['filmSummary'],
                          'comments': item['comments'],
                          'posterUrl': item['posterUrl'],
                          'morePosterUrl': item['morePosterUrl'], }
        if (dict_movieInfo['director']):
            print('{}抓取成功，电影名为：{}'.format(dict_movieInfo['movieId'], dict_movieInfo['movieNameDouban']))
        json_movieInfo = json.dumps(dict_movieInfo)

        # 写入json文件
        filename = os.path.abspath('') + '/movieInfo.json'
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json_movieInfo)
            f.write('\n')
        return item


class ImageSavePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # tempIP = getline('ip.txt', random.randint(1, 1000)).strip()
        yield Request(url=item['posterUrl'], meta={'imgname': item['posterName']}, cookies=item['cookies'])

    def file_path(self, request, response=None, info=None):
        filename = u'{}.jpg'.format(request.meta['imgname'])
        return filename
