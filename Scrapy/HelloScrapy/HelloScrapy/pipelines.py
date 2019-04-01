# -*- coding: utf-8 -*-
# 项目的管道文件

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

class ExamplePipeline(object):

    def process_item(self,item,spider):
        item["crawled"] = datetime.utcnow()  # 爬取的时间 格林威治时间
        item["spider"] = spider.name + "_windows_dzr"  # 爬虫的名称，#mycrawler_redis
        return item

class HelloscrapyPipeline(object):

    def open_spider(self, spoder):      # 开始时候调用
        self.file = open("teachers.json", "w", encoding="utf-8")
    def close_spider(self, spider):     # 结束的时候调用
        self.file.close()               # 关闭文件

    # 处理数据,对数据 进行处理,添加字段,删除字段,存储数据
    def process_item(self, item, spider):
        # 转换成字典
        dict_item = dict(item)
        # 把字典转换成字符串
        str_item = json.dumps(dict_item, ensure_ascii=False) + '\n'
        return item

