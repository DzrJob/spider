#-*-coding:utf-8-*- 
# @File    : get_cookie.py
import requests
import json
import redis
import logging
from .settings import REDIS_URL

# ����logging���������ã�Ȼ���ڿ���̨�����־
logger = logging.getLogger(__name__)
##ʹ��REDIS_URL����Redis���ݿ�, deconde_responses=True�����������Ҫ�����ݻ���byte��ʽ ��ȫû����
redis_connection = redis.Redis.from_url(REDIS_URL, db=15, decode_responses=True)
login_url = 'http://haoduofuli.pw/wp-login.php'


##��ȡCookie
def get_cookie(username, password):
    s = requests.Session()
    form = {
        'log': username,
        'pwd': password,
        'rememberme': "forever",
        'wp-submit': "��¼",
        'redirect_to': "http://http://www.haoduofuli.pw/wp-admin/",
        'testcookie': "1"
    }
    response = s.post(login_url, data=form)
    cookies = response.cookies.get_dict()
    logger.warning("��ȡCookie�ɹ������˺�Ϊ:%s��" % username)
    # ��������л�������Redis�����Plain Text��ʽ
    return json.dumps(cookies)

def init_cookie(red, spidername):
    # ���15�����е�key
    redis_keys = redis_connection.keys()
    for username in redis_keys:
        # ����key(�û���)���ֵ(����)
        password = redis_connection.get(username)
        # �ж����spider���˺ŵ�Cookie�Ƿ���ڣ������� �����get_cookie���������redis�л�ȡ�����˺������cookie��
        if red.get("%s:Cookies:%s--%s" % (spidername, username, password)) is None:
            cookie = get_cookie(username, password)
            # �����redis��KeyΪspider���ֺ��˺����룬valueΪcookie��
            red.set("%s:Cookies:%s--%s"% (spidername, username, password), cookie)
            # ����ʣ��ĸ���Cookie  ɾ���޷�ʹ�õ��˺�