#-*-coding:utf-8-*- 
# @File    : middlewares.py
# https://blog.csdn.net/fiery_heart/article/details/82229871
"""
�ź���;
ֱ����redis���¼һ�£��ҽ������˶�������
�Ƿ����Ԥ��һ��
����״̬���쳣������ô��
�ҵ�����û���������ͻ��˳��ˣ��Ҳ������˳���ô��
����ر��ˣ��Ҳ��뿴���̣���ϣ�����������ʼ�
��ô��
�����ڸ���һ��url����ȥ�������ˣ��Ҵ����ٸ���һ����ʱ�䲻ȷ��
����ô�죿

"""
from scrapy import signals
hahaha = 0
class MyExtension(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.


    """
�������ͣ�engine_stared �� engine_stopped ������Ŀ�ʼ�ͽ��� ��������������ȡ�����ʼ�ͽ����ĵط�
����spider_opend �� spider_closed  �����濪ʼ�ͽ���
����spider_idle  ��ʾ�������    spider_error   ��ʾ�������
����request_scheduled  ��ʾ��������ʼ���ȵ�ʱ��     request_dropped  ��ʾ��������
����response_received  ��ʾ��Ӧ���յ�      response_downloaded  ��ʾ�������
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

    # ��spider��ʼ��ȡʱ���͸��źš����ź�һ����������spider����Դ��������Ҳ�����κ��¡�
    def spider_opened(self, spider):
        spider.logger.info('spider start crawl: %s' % spider.name)
        print('start','1')


    def item_scraped(self,item, response, spider):
        global hahaha
        hahaha += 1

    # ��ĳ��spider���ر�ʱ�����źű����͡����źſ��������ͷ�ÿ��spider�� spider_opened ʱռ�õ���Դ��
    def spider_closed(self,spider, reason):
        print('-------------------------------all over------------------------------------------')
        global hahaha
        prnit(spider.name,' closed')

    # ��spider�Ļص�������������ʱ(���磬�׳��쳣)�����źű����͡�
    def spider_error(self,failure, response, spider):
        code = response.status
        print('spider error')

    # ��spider�������(idle)״̬ʱ���źű����͡�������ζ��:
    #    requests���ڵȴ�������
    #    requests������
    #    items����item pipeline�б�����
    def spider_idle(self,spider):
        for i in range(10):
            print(spider.name)