import redis

import time
import json

import pymongo


# 读取redis数据库的数据
# 写入到mongodb数据库中，写入的时候要是字段

redis_client = redis.StrictRedis(host='192.168.18.48', port=6379,db=0)

mongodb_client = pymongo.MongoClient(host="localhost",port=27017,)


#创建数据库
db_name = mongodb_client["sina"]

#创建表
sheet_name = db_name["sina_item"]


while True:

	# time.sleep(1)
	#blpop 先进入先被取出
	#
	source,data = redis_client.blpop(["sina_item:items"])
	# print("source==",source)
	# print("data===",data)
	# print(type(data))

	#把data转换成字典
	dict_data = json.loads(data.decode("utf-8"),encoding="utf-8")
	# print(type(dict_data))
	#插入的是字典
	sheet_name.insert(dict_data)

	print(dict_data)

