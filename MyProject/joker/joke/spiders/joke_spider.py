# -*- coding: utf-8 -*-
import re

import scrapy

from joke.items import JokeItem


class JokeSpiderSpider(scrapy.Spider):
    name = 'joke_spider'
    allowed_domains = ['jokeji.cn']
    start_urls = ['http://www.jokeji.cn/list_1.htm']
    url = 'http://www.jokeji.cn/list_%s.htm'
    base_url = 'http://www.jokeji.cn'
    def parse(self, response):
        joke_last_url = response.xpath('//div[@class="next_page"]/a[last()]/@href').extract()[0]
        r = re.compile('list_(\d+).htm')
        max_page_num = r.findall(joke_last_url)[0]
        for page_num in range(int(max_page_num)+1):
            print(page_num)
            url = self.url % (str(page_num))
            yield scrapy.Request(url,callback=self.joke_list)

    def joke_list(self,response):
        joke_list = response.xpath('//div[@class="list_title"]/ul/li')
        for joke in joke_list:
            joke_url = joke.xpath('.//a/@href').extract()[0]
            joke_url = self.base_url + joke_url

            yield scrapy.Request(joke_url,callback=self.joke_info)

    def joke_info(self,response):
        joke_title = response.xpath('//div[@class="left_up"]/h1/text()').extract()[1]
        r = re.compile('-> (.+)')
        # print(joke_title,response.url)
        # print(joke_title[1])
        joke_title = r.findall(joke_title)[0]
        joke_content = response.xpath('//span[@id="text110"]/p/text()').extract()
        if joke_content:
            joke_content = '\n'.join(joke_content)
        item = JokeItem()
        item['joke_title'] = joke_title
        item['joke_content'] = joke_content
        # print(joke_title,joke_content)
        yield item