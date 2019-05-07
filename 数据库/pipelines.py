# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

import pymongo





#把数据存储到mongodb数据中
from Sina.settings import MONGODB_HOST, MONGODB_PORT, DB_NAME,SHEET_NAME

from datetime import datetime

class ExamplePipeline(object):

    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()#爬取的时间
        item["spider"] = spider.name+"_windows_afu"#爬虫的名称，#mycrawler_redis
        return item



class SinaMongodbPipeline(object):
    def open_spider(self, spider):
        #mongodb客户端
        self.client = pymongo.MongoClient( host=MONGODB_HOST,port=MONGODB_PORT,)

        #创建mongodb数据库
        db_name = self.client[DB_NAME]

        #创建集合
        self.sheet_name = db_name[SHEET_NAME]


    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        #转换成字典
        item_dict = dict(item)

        #插入输入到mongodb数据库
        self.sheet_name.insert(item_dict)



        return item







class SinaPipeline(object):
    def open_spider(self,spider):
        self.file = open("新浪.json","w",encoding="utf-8")

    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):

        content = item["tiezi_content"]

        #http://sports.sina.com.cn/go/2018-12-18/doc-ihqhqcir7914429.shtml
        #-->sports.sina.com.cn/go/2018-12-18/doc-ihqhqcir7914429
        #-->sports_sina_com_cn_go_2018-12-18_doc-ihqhqcir7914429.txt
        name =item["tiezi_url"]
        name = name[7:name.rfind(".")].replace(".","_").replace("/","_")+".txt"

        print("name============================",name)

        #把帖子的内容保存到文件里面
        file_name = item["save_path"]+"/"+name

        with open(file_name,"w",encoding="utf-8") as f:
            f.write(content)



        #把帖子保存的文件的绝对路径添加到tiez_path

        item["tiez_path"] = file_name









        self.file.write(json.dumps(dict(item),ensure_ascii=False)+"\n")
        return item
