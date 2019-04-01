# -*- coding: utf-8 -*-
# 项目的目标文件

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 用于封装数据，传递给管道文件，但是必须继承scrapy.Item
class HelloScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    position = scrapy.Field()
    info = scrapy.Field()
    special = scrapy.Field()
    style = scrapy.Field()
    image = scrapy.Field()
