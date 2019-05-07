# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy import cmdline
from HelloScrapy.items import HelloScrapyItem


class HellospiderSpider(scrapy.Spider):
    name = 'hellospider'                        # 爬虫名
    allowed_domains = ['www.baidu.com']         # 爬取域名范围
    start_urls = ['http://www.baidu.com/']      # 起始爬取位置，可以多个

    # 自定义请求头（应用评论页cookie）
    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         "authority": "rate.tmall.com",
    #         "method": "GET",
    #         "path": "/list_detail_rate.htm?itemId=564593555827&spuId=927986671&sellerId=2917184910&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvtQvPvpyvUpCkvvvvvjiPR259AjYRPL5vzjrCPmPhlj1nPszU6jibRLFpAjrRRFyCvvpvvvvv9phvHHia1jvxzHi475SrtsQr7gr4NrGBdphvmpvWLU5%2BqvCGCsyCvvpvvvvvCQhvCli4zYMwc3%2Fjvpvhvvpvv8wCvvpvvUmm2QhvCvvvvvvEvpCW2n9Vvvay3w0x9C%2BaWDNBlwethbUfbcc6D70fd3r%2FfaBlaBoAVAYlibmD5dUfbccGgWpwV5im0WFv%2B2Kz8Z0vQRAn%2BbyDCasIAXZTKdyCvm9vvvvvphvv4pvv95BvpvAlvvm2phCvhRvvvUnvphvppvvv951vpvALkphvC99vvOCzBuyCvv9vvUmsuKXyMphCvvOvCvvvphvtvpvhvvvvv86Cvvyv22%2FE9OhvOUG%3D&needFold=0&_ksTS=1545824123814_1162&callback=jsonp1163",
    #         "scheme": "https",
    #         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #         "accept-encoding": "gzip, deflate, br",
    #         "accept-language": "zh-CN,zh;q=0.9",
    #         "cache-control": "no-cache",
    #         "cookie": "cna=zHioFBIdmFQCAXlFUaYbO7/a; lid=%E6%BA%BA%E6%B0%B4%E4%BA%91%E8%8D%92; _m_h5_tk=4b12f64c92e7013124ec1d2d801a5979_1545814244673; _m_h5_tk_enc=2110beddaa008569945ec97a330aa12c; enc=EGg8PEDSYbWizudSsqn62LNfgAL0Bbgz8wauLMSPQkC04XAJPITdmL%2BZfLinJTnPjWSkuGs7nX66APkbhDMKGg%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; uss=""; tk_trace=1; dnk=%5Cu6EBA%5Cu6C34%5Cu4E91%5Cu8352; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D; uc3=vt3=F8dByRMHjwBDBCufxSY%3D&id2=UojXLgEhHTMRnQ%3D%3D&nk2=py%2FzAR8Vm5s%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu6EBA%5Cu6C34%5Cu4E91%5Cu8352; _l_g_=Ug%3D%3D; unb=1936618306; lgc=%5Cu6EBA%5Cu6C34%5Cu4E91%5Cu8352; cookie1=BqtfRptZ4VzVHVOvstybYv4hYkc2iWwri6%2FiA5VdTkc%3D; login=true; cookie17=UojXLgEhHTMRnQ%3D%3D; cookie2=201c535863cea16f79c534bc842c6bb9; _nk_=%5Cu6EBA%5Cu6C34%5Cu4E91%5Cu8352; t=5a9bb7d732b081a10afeb4014e2be80e; sg=%E8%8D%9261; csg=135a06ca; _tb_token_=ee3b1e3e37be5; x5sec=7b22726174656d616e616765723b32223a226638373064313966373030336338326562376439633139333131326634363133434f54696b4f4546454b32387662537739617a4535674561444445354d7a59324d54677a4d4459374d513d3d227d; whl=-1%260%260%260; l=aB9_MI4iysCb39QBCMaTiXJ7h707JOZPVYQY1MaLsTEhN4-o7RXy1jno-VwW2_qC55ky_K-5F; isg=BLy8yuH3zGugvvgwZlk6tCDijVquHXL56ryRNJY9yKeKYVzrvsUwbzLRRcm8KZg3",
    #         "pragma": "no-cache",
    #         "upgrade-insecure-requests": "1",
    #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    #     }
    # }
    # ^(.*): (.*)$
    # "\1":"\2",
    #
    # 重写第一次接收地址的方法
    def start_requests(self):
        for url in self.start_urls:
            cookies = {

            }
            # 表单参数
            formdata = {
                'email': '18610059580',
                'password': '659190'
            }
            # 登录数据提交  dont_filter = True 来阻止去重。而scrapy框架中是默认去重的 (headers\meta\methond\encoding)
            yield scrapy.FormRequest(url, callback=self.parse, cookies=cookies,formdata=formdata,dont_filter=False)

    def parse(self, response):                  # 地址解析
        print(response.body)                    # "<class 'bytes'> 类型网页"
        print(response.text)                    # "<class 'str'> 类型网页"
        print(response.url)                     # 获取当前爬取地址

        with open('百度.html', 'wb') as f:      # 把获得的内容存到本地，方便分析
            f.write(response.body)

        url = response.xpath('//div/a[@id="like"]/@href').extract()               # xpath 解析(伪代码)
        data = response.xpath('//div/a[contains (@id,"like")]/text()').extract()  # xpath 解析(伪代码)

        html = response.text                    # 爬取整个网页
        r = re.compile('a href="(.*?)">(.*?)<') # 正则解析(伪代码)
        data2 = r.findall(html)                 # 查找所有

        json = response.text[7:-1]              # json 解析(伪代码)
        dict = json.loads(json)                 # 获取json数据，转换成字典
        data3 = dict['text'].replace('&quot;', '0')     # 获取字典内容 替换内容

        yield scrapy.Request(url,callback=self.parse_info,meta={'data':data,'data2':data2})      # 携带数据信息 交给下一层级继续解析详情页

    def parse_info(self,response):
        data = response.meta['data']            # 获取携带的信息

        item = HelloScrapyItem()                # 实例化item
        item['data'] = data                     # 封装item
        yield item                              # 数据传递管道文件

    """
    join 按照自定义方法连接列表为字符串
    l = ['a','a','a','a']
    L1 = ''.join(l)   #output is 'aaaa'
    L2 = 'b'.join(l) #output is 'abababa'
    L3 = '5'.join(l)  # output is 'a5a5a5a'
    split 将字符串按自定义方式切割成列表
    L2.split('b')   #result is ['a', 'a', 'a', 'a']
    L3.split('5')   #result is ['a', 'a', 'a', 'a']
    strip 取掉字符两端字符
    l = '222hello22222222'
    l.strip('2')   #output is 'hello'
    l.rstrip('2')  # output is 222hello
    l.lstrip('2')  #output is hello2222222
    startwith 开头
    replice
    re.sub('正则','替换成'，str，次数)
    """
    # 执行该爬虫，并转化为csv文件
    # cmdline.execute(['scrapy', 'crawl', 'hellospider', '-o', 'wiki.csv', '-t', 'csv'])
    # scrapy crawl human -o human.json
    import sys
    from scrapy.cmdline import execute

    if __name__ == '__main__':
        # 方式一
        # 可以直接写    脚本的目录下终端运行  -->  python  脚本名
        # execute(["scrapy","crawl","chouti","--nolog"])

        # #也可以借助sys.argv    在命令行中传参数会被argv捕获（argv为一个列表，第一个参数为脚本的路径，后面是传的参数）
        # #  比如   运行命令 :    python  脚本  参数（chouti）
        # print(sys.argv)
        execute(['scrapy', 'crawl', sys.argv[1], '--nolog'])