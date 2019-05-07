#-*-coding:utf-8-*- 
# @File    : test.py
import redis   # pip install redis
# 创建redis连接
r = redis.StrictRedis(host='localhost',         # Redis服务器地址
                      port=6379,                # Redis端口号
                      decode_responses=True,    # True键值对中的value为str类型,False是字节类型
                      db=10)                    # db库
r.set('name', 'dzr')  # key是"name" value是"dzr" 将键值对存入redis缓存
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))

# 创建连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=11)
r = redis.StrictRedis(connection_pool=pool)
r.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
print(r.get('gender'))      # gender 取出键male对应的值

import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 默认的情况下，管道里执行的命令可以保证执行的原子性，
# 执行pipe = r.pipeline(transaction=False)可以禁用这一特性。
pipe = r.pipeline() # 创建一个管道

pipe.set('name', 'jack')
pipe.set('role', 'sb')
pipe.sadd('faz', 'baz')
pipe.incr('num')    # 如果num不存在则vaule为1，如果存在，则value自增1
pipe.execute()

print(r.get("name"))
print(r.get("role"))
print(r.get("num"))