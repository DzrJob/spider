#-*-coding:utf-8-*- 
# @File    : get_cookie.py
import requests
import json
import redis
import logging
from .settings import REDIS_URL

# 配置logging基本的设置，然后在控制台输出日志
logger = logging.getLogger(__name__)
##使用REDIS_URL链接Redis数据库, deconde_responses=True这个参数必须要，数据会变成byte形式 完全没法用
redis_connection = redis.Redis.from_url(REDIS_URL, db=15, decode_responses=True)
login_url = 'http://haoduofuli.pw/wp-login.php'


##获取Cookie
def get_cookie(username, password):
    s = requests.Session()
    form = {
        'log': username,
        'pwd': password,
        'rememberme': "forever",
        'wp-submit': "登录",
        'redirect_to': "http://http://www.haoduofuli.pw/wp-admin/",
        'testcookie': "1"
    }
    response = s.post(login_url, data=form)
    cookies = response.cookies.get_dict()
    logger.warning("获取Cookie成功！（账号为:%s）" % username)
    # 如果不序列化，存入Redis后会变成Plain Text格式
    return json.dumps(cookies)

def init_cookie(red, spidername):
    # 获得15库所有的key
    redis_keys = redis_connection.keys()
    for username in redis_keys:
        # 根据key(用户名)获得值(密码)
        password = redis_connection.get(username)
        # 判断这个spider和账号的Cookie是否存在，不存在 则调用get_cookie函数传入从redis中获取到的账号密码的cookie；
        if red.get("%s:Cookies:%s--%s" % (spidername, username, password)) is None:
            cookie = get_cookie(username, password)
            # 保存进redis，Key为spider名字和账号密码，value为cookie。
            red.set("%s:Cookies:%s--%s"% (spidername, username, password), cookie)
            # 还有剩余的更新Cookie  删除无法使用的账号