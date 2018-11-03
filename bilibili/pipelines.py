# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from datetime import datetime

TABLE_NAME = 'bilibili'

class BlibliPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='***', passwd='***', db='***', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into ' + TABLE_NAME + ' (mid,name,avatar,rating,likes,ctime,content,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, (
                item['au_mid'], item['au_uname'], item['au_avatar'], item['rating'], item['likes'], item['ctime'] , item['content'], datetime.now()))
        except pymysql.err.IntegrityError:
            pass
        self.conn.commit()

        return item

    def close_sppider(self):
        self.conn.close()