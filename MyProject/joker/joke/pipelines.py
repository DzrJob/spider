# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from datetime import datetime

import pymysql

class JokePipeline(object):

    def open_spider(self,spider):
        # 获取mysql连接
        self.conn = pymysql.Connection(host="localhost", user="root", password="123456",
                                  database="djangoscrapy", port=3306, charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()

    def close_spider(self,spider):
        pass

    def process_item(self, item, spider):
        createDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(type(createDate))
        sql = "insert into joke_jokes(joke_title,joke_content,createDate) values('%s','%s','%s')" % (
            item['joke_title'], item['joke_content'],createDate)
        # print(item['joke_title'])
        # print(item['joke_content'])
        # print(createDate)
        self.cursor.execute(sql)
        self.conn.commit()
        return item
