# -*- coding: utf-8 -*-
from time import sleep

import scrapy
from selenium import webdriver
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk')

class KuaishouSpiderSpider(scrapy.Spider):
    name = 'kuaishou_spider'
    allowed_domains = ['kuaishou.com']
    # start_urls = ['http://live.kuaishou.com/']

    url = 'http://live.kuaishou.com/u/%s'
    user_id = '3xsey959k2h932y'

    x = 0
    y = 6

    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #         "Cache-Control": "no-cache",
    #         "Connection": "keep-alive",
    #         "Cookie": "clientid=3; did=web_64cb48f000e7cfdde6996f8e8d441a79; client_key=65890b29; userId=594924662; userId=594924662; kuaishou.live.bfb1s=ac5f27b3b62895859c4c1622f49856a4; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAVCSToNcItH-VosbHyz_CmQBgq14HI-vx3J3UOX3m1h-mmdxsrucYvYfHXnmHuQ3x775zNwuU5Yw5qdCoPh9YofVGJtWuI6bpdMr5u-zA8rPzgdgn-ZcC2pOLok3cae9ISCLjUv-gjCh2uCE706aCgcrkDogVff_j-qATVQr257s1iTPzYfseIEC-jdAQqx4ZD76T0BfE5XT7UclW6yD-XgaEtjNYCqMvUVZmp6WeyTUfct3aCIgc3F1fSCGuDkT4pTPHz8y-zkZLj6mezwZzhSa9xvDyYMoBTAB; kuaishou.live.web_ph=029eb9a1a52a1533309f5c71b6871dbec929",
    #         "Host": "live.kuaishou.com",
    #         "Pragma": "no-cache",
    #         "Upgrade-Insecure-Requests": "1",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    #     }
    # }

    def __init__(self):
        """
        在初始化对象时，创建driver. 设置无界面模式
        """
        super(KuaishouSpiderSpider, self).__init__(name='kuaishou_spider')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = False
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


    def start_requests(self):
        self.driver.get(self.url % (self.user_id))
        yield scrapy.Request(self.url % (self.user_id), callback=self.parse,dont_filter=True)

    def parse(self, response):

        xpath_str = '//li[@class="chat-info"][position()>'+str(self.x)+ 'and position()<'+str(self.y)+']'
        print(xpath_str)
        datas = response.xpath(xpath_str)
        print(len(datas))
        for data in datas:
            if data.xpath('./div[@class="gift-comment"]'):
                giver = data.xpath('./div[@class="gift-comment"]/span[@class="username"]/text()').extract()[0].strip()
                gift = data.xpath('./div[@class="gift-comment"]/img/@src').extract()[0]
                print(giver, '赠送了:', gift)

            if data.xpath('./div[@class=""]/span[@class="comment"]'):
                commentator = data.xpath('./div/span[@class="username"]/text()').extract()[0].strip()
                comment = data.xpath('./div[@class=""]/span[@class="comment"]//text()').extract()[0].strip()
                print(commentator, '评论了:', comment)

        self.x += len(datas)
        self.y += len(datas)
        yield scrapy.Request(self.url % (self.user_id), callback=self.parse,dont_filter=True)