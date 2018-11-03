# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlibliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    au_avatar = scrapy.Field()
    au_mid = scrapy.Field()
    au_uname = scrapy.Field()

    content = scrapy.Field()
    rating = scrapy.Field()
    ctime = scrapy.Field()
    likes = scrapy.Field()


