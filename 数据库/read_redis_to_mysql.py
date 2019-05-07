# -*-coding:utf-8-*-
import redis
import time
import json
import pymysql

"""
将爬取的数据从redis中存入mysql
"""
# 获取redis连接
redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
# 获取mysql连接
conn = pymysql.Connection(host="localhost", user="root", password="123456",
                          database="toutiao", port=3306, charset='utf8')
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
while True:
    # blpop 先进入先被取出
    # 将多个列表排列，按照从左到右去pop对应列表的元素 列表键名,最左面值
    source, data = redis_client.blpop(["today_top_news_spider3:items"])
    # 把data转换成字典
    item = json.loads(data.decode("utf-8"), encoding="utf-8")
    # print(type(dict_data))
    # 插入的是字典
    # 参数的方式传入
    # source_url= scrapy.Field()
    #     # 文章标题
    #     title= scrapy.Field()
    #     # 文章内容
    #     content= scrapy.Field()
    #     # 文章里面的图片链接
    #     image_url= scrapy.Field()
    #
    #     # 增加爬虫的名称和时间戳
    #     crawled = scrapy.Field()
    #     spider = scrapy.Field()
    params = (item['source_url'], item['channel'], item['title'], item['content'], item['image_url'],
              item['crawled'], item['spider'])
    # 使用execute方法执行SQL INSERT语句
    sql = "INSERT INTO toutiao_items(source_url , channel,title ,content ,image_url  ,crawled ,spider) VALUES ('%s','%s',  '%s', '%s', '%s', '%s', '%s')" % params
    cursor.execute(sql)
    # 提交事务
    conn.commit()
