# -*- coding: utf-8 -*-
import scrapy
from HelloScrapy.items import AtguiguItem


# 爬虫
# 类名规则：在爬虫名称的基础上首字母大写把下划线去掉+Spider
# 继承scrapy.Spider ，这是一个基本爬虫
# scrapy.CrawlSpider,规则爬虫
class AtguiguTeacherSpider(scrapy.Spider):
    # 爬虫的识别名称，必须唯一
    name = 'atguigu_teacher'
    # 是搜索的域名范围，
    # 也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = ['www.atguigu.com']
    # 爬取的URL元祖/列表。
    # 爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
    # 不受上面约束限制可以多个包括其他路径(www.baidu.com)
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    # 解析的方法，
    # 每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
    # 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
    # 生成需要下一页的URL请求。
    # 当start_urls所有的地址请求成功的时候，引擎会把数据封装在Response这个类中并把数据传递给response变量
    def parse(self, response):
        print("response.url====", response.url)
        print(response.body)
        # 保存数据
        with open('尚硅谷首页.html', 'wb') as f:
            f.write(response.body)

        # 使用xpath解析数据,并封装到Item,使用yield把数据返回到管道文件
        teacher_list = response.xpath('//div[@class="con"]/ul/li')

        for teacher in teacher_list:
            # .extract() 把对象装换成unicode编码中utf-8
            name = response.xpath('./div[@class="t-info"]/h5/b[1]/text()').extract()[0]
            position = response.xpath('./div[@class="t-info"]/h5/b[2]/text()').extract()[0]
            info = response.xpath('')
            special = response.xpath('')
            style = response.xpath('')
            image = response.xpath('')

            # 实例化item
            item = AtguiguItem()

            item['name'] = name
            item["position"] = position

            # 把数据传递管道文件用yield
            # return会导致结束
            yield item
