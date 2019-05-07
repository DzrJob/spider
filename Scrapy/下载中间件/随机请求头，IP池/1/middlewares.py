# -*- coding: utf-8 -*-

import random
import base64
from settings import USER_AGENTS
from settings import PROXIES


class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", useragent)


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)

        if proxy['user_passwd'] is None:
            # 没有代理账户验证的免费代理的使用
            request.meta['proxy'] = "http//" + proxy['ip_port']
        else:
            request.meta['proxy'] = "http//" + proxy['ip_port']
            # 对账户密码进行base64编码转换
            base64_userpasswd = base64.b64decode(proxy['user_passwd'])
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd