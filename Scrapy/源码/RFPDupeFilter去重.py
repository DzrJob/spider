#-*-coding:utf-8-*- 
# @File    : RFPDupeFilterȥ��.py
class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None, debug=False):
        self.file = None
        self.fingerprints = set()
        self.logdupes = True
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        if path:
              # �˴����Կ���ȥ����ʵ����һ������ requests.seen���ļ�
            # �����ʹ�õĴ��̵Ļ�
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
              # �ж����ǵ������Ƿ�������ڼ�����
            return True
        # û���ڼ��Ͼ���ӽ�ȥ
        self.fingerprints.add(fp)
        # ����õĴ��̶��о�д��ȥ��¼һ��
        if self.file:
            self.file.write(fp + os.linesep)