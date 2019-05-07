#-*-coding:utf-8-*- 
# @File    : 分布式.py
import io
import re
import sys

import scrapy.cmdline
from jd.items import JdItem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码

from scrapy_redis.spiders import RedisSpider
class JdSpiderSpider(RedisSpider):
    name = 'jd_spider2'
    allowed_domains = ['jd.com']
    # start_urls = ['https://www.jd.com/']
    # psort 0综合(默认) 1价格(降序) 2价格 3销量 4评论 5新品
    url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=%d&s=%s&click=0'
    next_url = 'https://search.jd.com/s_new.php?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=%d&scrolling=y&s=%s&psort&show_items=%s'

    # 关键字
    keyword = "apple"
    # 开始页数
    page = 1
    # 产品展示参数
    s = 0

    # lpush JdSpiderSpider:start_urls https://search.jd.com/Search?keyword=apple&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=1&s=0&click=0
    redis_key = 'JdSpiderSpider:start_urls'

    # def start_requests(self):
    #     # 重写start_urls 加入参数
    #     yield scrapy.Request(self.url % (self.keyword, self.page, self.s), callback=self.parse)

    def parse(self, response):
        ids = []
        # with open('html_code.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # 有预售 class="gl-item gl-item-presell"
        data_list = response.xpath('//li[contains(@class,"gl-item")]')
        # 测试查看每页数据书否30
        # print(len(data_list), self.page, response.url)

        for data in data_list:
            item = JdItem()
            # 产品多款data-pid 单款data-sku
            item_id = data.xpath('./@data-pid').extract()
            if not item_id:
                item_id = data.xpath('./@data-sku').extract()

            item_name = data.xpath('.//div[contains(@class,"p-name")]//em/text()[1]').extract()
            item_price = data.xpath('.//div[@class="p-price"]//i/text()').extract()
            if item_id:
                item['item_id'] = item_id[0]
                item_url = 'https://item.jd.com/' + item_id[0] + '.html'
                item['item_url'] = item_url
            if item_name:
                item['item_name'] = item_name[0]
            if item_price:
                item['item_price'] = item_price[0]
            # item['page'] = self.page
            yield item
        headers = {'referer': response.url}
        self.page += 1
        self.s += 30
        url = self.next_url % (self.keyword, self.page, self.s, ','.join(ids))
        yield scrapy.Request(url, callback=self.next_parse, headers=headers)

    def next_parse(self, response):
        data_list = response.xpath('//li[contains(@class,"gl-item")]')

        # print(len(data_list), self.page, response.url)

        for data in data_list:
            item = JdItem()
            item_id = data.xpath('./@data-pid').extract()
            if not item_id:
                item_id = data.xpath('./@data-sku').extract()

            item_name = data.xpath('.//div[contains(@class,"p-name")]//em/text()[1]').extract()
            item_price = data.xpath('.//div[@class="p-price"]//i/text()').extract()
            if item_id:
                item['item_id'] = item_id[0]
                item_url = 'https://item.jd.com/' + item_id[0] + '.html'
                item['item_url'] = item_url
            if item_name:
                item['item_name'] = item_name[0]
            if item_price:
                item['item_price'] = item_price[0]
            # item['page'] = self.page
            yield item

        if self.page < 200:
            self.page += 1
            self.s += 30
            url = self.url % (self.keyword, self.page, self.s)
            yield scrapy.Request(url, callback=self.parse)

# scrapy.cmdline.execute(['scrapy', 'crawl', 'jd_scrapy_redis', '-o', 'wiki.csv', '-t', 'csv'])