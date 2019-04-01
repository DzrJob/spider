# -*-coding:utf-8-*-
# @File    : redis_mysql.py
import json

import pymysql
import redis

redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
conn = pymysql.Connection(host="localhost", user="root", password="123456",
                          database="lianjia", port=3306, charset='utf8')
cursor = conn.cursor()

while True:
    source, data = redis_client.blpop(["lianjia_spider:items"])
    item = json.loads(data.decode("utf-8"), encoding="utf-8")
    params = (
          item['sale_price']
        , item['name']
        , item['hourse_style']
        , item['floor_num']
        , item['area']
        , item['hourse_style_desc']
        , item['inner_area']
        , item['build_style']
        , item['direction']
        , item['build_year']
        , item['fitting']
        , item['build_style_desc']
        , item['heating']
        , item['one_floor_hours']
        , item['age_limit']
        , item['elevator']
        , item['sale_time']
        ,item['crawled']
        ,item['spider']

    )
    # 使用execute方法执行SQL INSERT语句
    sql = "INSERT INTO lianjia_items(sale_price ，name, hourse_style,floor_num ,area ,hourse_style_desc,inner_area ,build_style," \
          "direction,build_year,fitting,build_style_desc,heating,one_floor_hours,age_limit,elevator,sale_time,crawled,spider) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % params
    cursor.execute(sql)
    # 提交事务
    conn.commit()
