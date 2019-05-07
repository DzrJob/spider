#-*-coding:utf-8-*- 
# @File    : middlewares.py
# https://blog.csdn.net/fiery_heart/article/details/82229871
"""
信号用途
直接往redis里记录一下，我今天爬了多少数据
是否和我预期一样
爬虫状态码异常，你怎么查
我的爬虫没任务了它就会退出了，我不想它退出怎么办
爬虫关闭了，我不想看进程，我希望给我来个邮件
怎么办
我现在给你一批url让你去爬，完了，我待会再给你一批。时间不确定
你怎么办？

"""
from scrapy import signals
hahaha = 0
class MyExtension(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.


    """
　　解释：engine_stared 和 engine_stopped 是引擎的开始和结束 ，是整个爬虫爬取任务最开始和结束的地方
　　spider_opend 和 spider_closed  是爬虫开始和结束
　　spider_idle  表示爬虫空闲    spider_error   表示爬虫错误
　　request_scheduled  表示调度器开始调度的时候     request_dropped  表示请求舍弃
　　response_received  表示响应接收到      response_downloaded  表示下载完毕
    """
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(s.spider_error, signal=signals.spider_error)
        crawler.signals.connect(s.spider_idle, signal=signals.spider_idle)

        return s

    # 当spider开始爬取时发送该信号。该信号一般用来分配spider的资源，不过其也能做任何事。
    def spider_opened(self, spider):
        spider.logger.info('spider start crawl: %s' % spider.name)
        print('start','1')


    def item_scraped(self,item, response, spider):
        global hahaha
        hahaha += 1

    # 当某个spider被关闭时，该信号被发送。该信号可以用来释放每个spider在 spider_opened 时占用的资源。
    def spider_closed(self,spider, reason):
        print('-------------------------------all over------------------------------------------')
        global hahaha
        prnit(spider.name,' closed')

    # 当spider的回调函数产生错误时(例如，抛出异常)，该信号被发送。
    def spider_error(self,failure, response, spider):
        code = response.status
        print('spider error')

    # 当spider进入空闲(idle)状态时该信号被发送。空闲意味着:
    #    requests正在等待被下载
    #    requests被调度
    #    items正在item pipeline中被处理
    def spider_idle(self,spider):
        for i in range(10):
            print(spider.name)