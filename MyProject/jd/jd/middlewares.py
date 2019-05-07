# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json

from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware


import redis
from jd.get_cookie import init_cookie
class CookieMiddleware(RetryMiddleware):

    def __init__(self, settings, crawler):
        # 重载父类
        RetryMiddleware.__init__(self, settings)
        # decode_responses 设置取出的编码为str
        # settings['REDIS_URL'] 访问scrapy的settings
        self.redis_connection = redis.from_url(settings['REDIS_URL'], db=14, decode_responses=True)
        # 往redis中添加cookie。第二个参数就是spidername的获取方法（其实就是字典啦！）
        init_cookie(self.redis_connection, crawler.spider.name)

    # 静态方法 优于init
    # 如果存在该函数，from_crawler会被调用使用crawler来创建中间器对象，必须返回一个中间器对象，
    # 通过这种方式，可以访问到crawler的所有核心部件，如settings、signals等。
    # 访问settings的方法
    @classmethod
    def from_crawler(cls, crawler):
        # init中两个参数
        return cls(crawler.settings, crawler)

    def process_request(self, request, spider):
        redisKeys = self.redis_connection.keys()
        while len(redisKeys) > 0:
            elem = random.choice(redisKeys)
            if spider.name + ':Cookies' in elem:
                cookie = json.loads(self.redis_connection.get(elem))
                request.cookies = cookie
                request.meta["accountText"] = elem.split("Cookies:")[-1]
                break


import random
from fake_useragent import UserAgent
class JDScrapyDownloaderRandomUser(object):

    def __init__(self):
        self.ua = UserAgent()
        with open('ip.txt', 'r+') as f:
            self.user_agent_list = f.read().split("\n")

    def process_request(self, request, spider):
        print('随机配置生效')
        user_agent = self.ua.random
        print('随机浏览器========', user_agent)
        request.headers.setdefault('User-Agent', user_agent)

        proxy_ip = random.choice(self.user_agent_list)
        print('随机代理==========', proxy_ip)
        request.meta['proxy'] = 'http://' + proxy_ip


class JdSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JdDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
