# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HellocrawlspiderSpider(CrawlSpider):
    name = 'hellocrawlspider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/?&start=0']

    rules = (
        # 规则元祖
        # LinkExtractor 提取链接,
        # callback 请求后成功回调callback指定的函数
        # follow=True 深度爬取(所有符合规则地址)，follow=False 当前页的链接
        # 找到所有start后的值
        Rule(LinkExtractor(allow=r'start=(\d+)'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i


