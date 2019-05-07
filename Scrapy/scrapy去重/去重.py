#-*-coding:utf-8-*- 
# @File    : ȥ��.py
def f():
    pass

"""
������Ӧ���У����ǿ�����request���������ò���dont_filter = True ����ֹȥ�ء���scrapy�������Ĭ��ȥ�صģ����ڲ������ȥ�صġ�
"""
"""
��������Ժ󣬻���ִ��from_settings������
��settings�ļ�����һ��DUPEFILTER_DEBUG�����ã�
��ִ��init��ʼ������������һ������ self.fingerprints = set()��
Ȼ����ִ��request_seen������
�������ǿ����Զ���ȥ�ع���ֻҪ�̳�BaseDupeFilter����
"""
# scrapy���Ĭ�ϵ�ȥ����RFPDupeFilter
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

