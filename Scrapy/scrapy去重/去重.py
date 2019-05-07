#-*-coding:utf-8-*- 
# @File    : 去重.py
def f():
    pass

"""
在爬虫应用中，我们可以在request对象中设置参数dont_filter = True 来阻止去重。而scrapy框架中是默认去重的，那内部是如何去重的。
"""
"""
请求进来以后，会先执行from_settings方法，
从settings文件中找一个DUPEFILTER_DEBUG的配置，
再执行init初始化方法，生成一个集合 self.fingerprints = set()，
然后在执行request_seen方法，
所以我们可以自定制去重规则，只要继承BaseDupeFilter即可
"""
# scrapy框架默认的去重类RFPDupeFilter
class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None, debug=False):
        self.file = None
        self.fingerprints = set()
        self.logdupes = True
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        if path:
            self.file = open(os.path.join(path, 'requests.seen'), 'a+')
            self.file.seek(0)
            self.fingerprints.update(x.rstrip() for x in self.file)

    @classmethod
    def from_settings(cls, settings):
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(job_dir(settings), debug)

    def request_seen(self, request):
        fp = self.request_fingerprint(request)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)

    def request_fingerprint(self, request):
        return request_fingerprint(request)

    def close(self, reason):
        if self.file:
            self.file.close()

    def log(self, request, spider):
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request: %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False

        spider.crawler.stats.inc_value('dupefilter/filtered', spider=spider)

