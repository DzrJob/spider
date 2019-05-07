# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    item_id = scrapy.Field()
    item_url = scrapy.Field()
    item_name = scrapy.Field()
    item_price = scrapy.Field()
    page = scrapy.Field()

    # 增加爬虫的名称和时间戳
    crawled = scrapy.Field()
    spider = scrapy.Field()