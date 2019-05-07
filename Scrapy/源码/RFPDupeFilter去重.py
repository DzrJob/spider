#-*-coding:utf-8-*- 
# @File    : RFPDupeFilter去重.py
class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None, debug=False):
        self.file = None
        self.fingerprints = set()
        self.logdupes = True
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        if path:
              # 此处可以看到去重其实打开了一个名叫 requests.seen的文件
            # 如果是使用的磁盘的话
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
              # 判断我们的请求是否在这个在集合中
            return True
        # 没有在集合就添加进去
        self.fingerprints.add(fp)
        # 如果用的磁盘队列就写进去记录一下
        if self.file:
            self.file.write(fp + os.linesep)