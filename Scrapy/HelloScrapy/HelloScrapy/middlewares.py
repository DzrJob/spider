# -*- coding: utf-8 -*-
"""
下载中间件是scrapy提供用于用于在爬虫过程中可修改Request和Response，用于扩展scrapy的功能；比如：

可以在请求被Download之前，请求头部加上某些信息；
完成请求之后，回包需要解压等处理；
明确：
请求是引擎发出来的，不是爬虫发出来的
引擎从爬虫拿url，给调度器去重，同时会从调度器的任务队列里取出一个任务，给下载器
下载器下载完以后，下载器把response返回给引擎
"""
# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from fake_useragent import UserAgent
from scrapy import signals

class HelloscrapyDownloaderRandomUser(object):

    def __init__(self):
        self.ua = UserAgent()
        with open('ip.txt', 'r+') as f:
            self.user_agent_list = f.read().split("\n")

    # 每个Request对象经过下载中间件时会被调用，优先级越高的中间件，越先调用
    def process_request(self, request, spider):
        print('随机配置生效')
        user_agent = self.ua.random
        print('随机浏览器========', user_agent)
        request.headers.setdefault('User-Agent', user_agent)

        proxy_ip = random.choice(self.user_agent_list)
        print('随机代理==========', proxy_ip)
        request.meta['proxy'] = 'http://' + proxy_ip

    # 当每个Response经过下载中间件会被调用，优先级越高的中间件，越晚被调用，与process_request()相反；
    # 获取的响应是从下载器到引擎的，所以response经过中间件的顺序刚好与request相反
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 当process_exception()和process_request()抛出异常时会被调用，应该返回以下对象
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    # 如果存在该函数，from_crawler会被调用使用crawler来创建中间器对象，必须返回一个中间器对象，
    # 通过这种方式，可以访问到crawler的所有核心部件，如settings、signals等。
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

class HelloscrapySpiderMiddleware(object):
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


class HelloscrapyDownloaderMiddleware(object):
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
