# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from jd.settings import MONGODB_HOST, MONGODB_PORT, DB_NAME, SHEET_NAME
class JDMongoDBPipeline(object):
    def open_spider(self, spider):
        # mongodb客户端
        self.client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT, )
        # 创建mongodb数据库
        db_name = self.client[DB_NAME]
        # 创建集合
        self.sheet_name = db_name[SHEET_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 转换成字典
        item_dict = dict(item)
        # 插入输入到mongodb数据库
        self.sheet_name.insert(item_dict)
        return item

import json
class JDPipeline(object):
    def open_spider(self, spider):
        self.f = open('京东.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        # 把字典转换成字符串
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

from datetime import datetime
class ExamplePipeline(object):

    def process_item(self,item,spider):
        item["crawled"] = datetime.utcnow()  # 爬取的时间 格林威治时间
        item["spider"] = spider.name + "_windows_dzr"  # 爬虫的名称，#mycrawler_redis
        return item

import os
import sqlite3
class JDsqlite3Pipeline(object):

    def __init__(self):
        self.path = './data.sqlite'
        if os.path.exists(self.path):
            os.remove(self.path)
        # 创建数据库连接
        self.conn = sqlite3.connect(self.path)
        # 获取游标
        self.cursor = self.conn.cursor()
        sql = """
                    create table jd_item_info(
                        id integer primary key autoincrement not null,
                        item_id text not null,
                        item_url text not null,
                        item_name text not null,
                        item_price text not null,
                        crawled text not null,
                        spider text not null
                    );
              """
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()
        # self.f = open('天猫.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        # self.f.close()
        pass
    def process_item(self, item, spider):
        sql = "insert into jd_item_info(item_id,item_url,item_name,item_price,crawled,spider) values('%s','%s','%s','%s','%s','%s')" % (
            item['item_id'], item['item_url'], item['item_name'], item['item_price'], item['crawled'], item['spider'])
        self.cursor.execute(sql)
        self.conn.commit()
        # self.f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item