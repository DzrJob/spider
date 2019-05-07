# middlewares.py
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.exceptions import NotConfigured
from collections import defaultdict
from urllib.parse import urlparse
from faker import Faker  # 引入Faker，pip install faker下载
import random


class RandomHttpProxyMiddleware(HttpProxyMiddleware):

    def __init__(self, auth_encoding='latin-1', proxy_list=None):
        if not proxy_list:
            raise NotConfigured
        self.proxies = defaultdict(list)
        for proxy in proxy_list:
            parse = urlparse(proxy)
            self.proxies[parse.scheme].append(proxy)  # 生成dict，键为协议，值为代理ip列表

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('HTTP_PROXY_LIST'):
            raise NotConfigured

        http_proxy_list = crawler.settings.get('HTTP_PROXY_LIST')  # 从配置文件中读取
        auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'latin-1')

        return cls(auth_encoding, http_proxy_list)

    def _set_proxy(self, request, scheme):
        proxy = random.choice(self.proxies[scheme])  # 随机抽取选中协议的IP
        request.meta['proxy'] = proxy


class RandomUserAgentMiddleware(object):

    def __init__(self):
        self.faker = Faker(local='zh_CN')
        self.user_agent = ''

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request, spider):
        self.user_agent = self.faker.user_agent()  # 获得随机user_agent
        request.headers.setdefault(b'User-Agent', self.user_agent)