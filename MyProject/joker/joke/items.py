# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JokeItem(scrapy.Item):
    # define the fields for your item here like:
    joke_title = scrapy.Field()
    joke_content = scrapy.Field()
