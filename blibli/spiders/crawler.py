# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        crawler
   Description:
   Author:           wyq19
   Date：            2018/10/31 0031 22:04
   Version:          python3.6
-------------------------------------------------
   Change Activity:
                     2018/10/31 0031 22:04
-------------------------------------------------
"""
__author__ = 'wyq19'
import scrapy
import json
from blibli.items import BlibliItem

class MySpider(scrapy.Spider):
    name = "blibli"
    allowed_domains = ["bilibili.com"]
    start_urls = [
        "https://bangumi.bilibili.com/review/web_api/short/list?media_id=102392&folded=0&page_size=30&sort=0",
    ]
    root_url = 'https://bangumi.bilibili.com/review/web_api/short/list?media_id=102392&folded=0&page_size=30&sort=0&cursor='
    counter = 0

    def parse(self, response):
        js = json.loads(response.text)
        if js['message'] == 'success':
            for li in js['result']['list']:
                item = BlibliItem()
                item['au_avatar'] = li['author']['avatar']
                item['au_mid'] = li['author']['mid']
                item['au_uname'] = li['author']['uname']

                item['content'] = li['content']
                item['likes'] = li['likes']
                item['rating'] = li['user_rating']['score']
                item['ctime'] = li['ctime']
                if 'cursor' in li.keys():
                    yield scrapy.Request(self.root_url+li['cursor'], callback=self.parse)
                yield item