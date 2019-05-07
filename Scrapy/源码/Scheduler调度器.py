#-*-coding:utf-8-*- 
# @File    : Scheduler������.py
"""
CHEDULER����Ҫ������� push Request pop Request �� ȥ�صĲ�����

����queue ���������ڴ��������ɵġ�

queuelib.queue�ͻᷢ�ֻ����ڴ�ģ�deque��

"""
class Scheduler(object):

    def __init__(self, dupefilter, jobdir=None, dqclass=None, mqclass=None,
                 logunser=False, stats=None, pqclass=None):
        self.df = dupefilter
        self.dqdir = self._dqdir(jobdir)
        self.pqclass = pqclass
        self.dqclass = dqclass
        self.mqclass = mqclass
        self.logunser = logunser
        self.stats = stats
        # ע����scrpy������ע������������˷�����һ������ ���ڷ��ʵ�ǰ���������
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        # ��ȡȥ���õ��� Ĭ�ϣ�scrapy.dupefilters.RFPDupeFilter
        dupefilter_cls = load_object(settings['DUPEFILTER_CLASS'])
        # ��ȥ�����������from_settings �� scrapy.dupefilters.RFPDupeFilter 43��
        # ���ֵ��÷�ʽ����IDE��ת���Ǻܺ�  ������Ҫ�Լ�ȥ��
        # @classmethod
        # def from_settings(cls, settings):
        #     debug = settings.getbool('DUPEFILTER_DEBUG')
        #     return cls(job_dir(settings), debug)
        # �������from_settings���� ��ʵ�������ù���Ŀ¼ ���Ƿ���debug
        dupefilter = dupefilter_cls.from_settings(settings)
        # ��ȡ���ȼ����� ����� Ĭ�ϣ�queuelib.pqueue.PriorityQueue
        pqclass = load_object(settings['SCHEDULER_PRIORITY_QUEUE'])
        # ��ȡ���̶��� �����SCHEDULERʹ�ô��̴洢 �������ᶪʧ��
        dqclass = load_object(settings['SCHEDULER_DISK_QUEUE'])
        # ��ȡ�ڴ���� �����SCHEDULERʹ���ڴ�洢 �����ᶪʧ��
        mqclass = load_object(settings['SCHEDULER_MEMORY_QUEUE'])
        # �Ƿ���debug
        logunser = settings.getbool('LOG_UNSERIALIZABLE_REQUESTS', settings.getbool('SCHEDULER_DEBUG'))
        # ����Щ�������ݸ� __init__����
        return cls(dupefilter, jobdir=job_dir(settings), logunser=logunser,
                   stats=crawler.stats, pqclass=pqclass, dqclass=dqclass, mqclass=mqclass)


    def has_pending_requests(self):
      """����Ƿ���û���������"""
        return len(self) > 0

    def open(self, spider):
      """Engine�������֮�������������"""
        self.spider = spider
        # ����һ�������ȼ����ڴ���� ʵ��������
        # self.pqclass Ĭ���ǣ�queuelib.pqueue.PriorityQueue
        # self._newmq �᷵��һ���ڴ���е� ʵ�������� ��110  111 ��
        self.mqs = self.pqclass(self._newmq)
        # ���self.dqdir ������ �ʹ���һ�����̶��� ����self.dqs Ϊ��
        self.dqs = self._dq() if self.dqdir else None
        # ���һ��ȥ��ʵ������ open �����Ǵ�BaseDupeFilter�̳е�
        # �������ǿ�����self.df��ȥ����
        return self.df.open()

    def close(self, reason):
      """��ȻEngine�ر�ʱ"""
          # ����д��̶��� ��������dump�󱣴浽active.json�ļ���
        if self.dqs:
            prios = self.dqs.close()
            with open(join(self.dqdir, 'active.json'), 'w') as f:
                json.dump(prios, f)
        # Ȼ��ر�ȥ��
        return self.df.close(reason)

    def enqueue_request(self, request):
      """���һ��Requests�����ȶ���"""
          # self.df.request_seen�Ǽ�����Request�Ƿ��Ѿ�������� ����л᷵��True
        if not request.dont_filter and self.df.request_seen(request):
              # ���Request��dont_filter����û�����ã�Ĭ��ΪFalse���� �Ѿ�������ȥ��
            # ��push������
            self.df.log(request, self.spider)
            return False
        # �ȳ��Խ�Request push�����̶���
        dqok = self._dqpush(request)
        if dqok:
              # ����ɹ� ���ڼ�¼һ��״̬
            self.stats.inc_value('scheduler/enqueued/disk', spider=self.spider)
        else:
              # ������ӽ����̶��������ӽ��ڴ����
            self._mqpush(request)
            self.stats.inc_value('scheduler/enqueued/memory', spider=self.spider)
        self.stats.inc_value('scheduler/enqueued', spider=self.spider)
        return True

    def next_request(self):
      """�Ӷ����л�ȡһ��Request"""
          # ���ȴ��ڴ�����л�ȡ
        request = self.mqs.pop()
        if request:
            self.stats.inc_value('scheduler/dequeued/memory', spider=self.spider)
        else:
              # ���ܻ�ȡ��ʱ��Ӵ��̶��ж����ȡ
            request = self._dqpop()
            if request:
                self.stats.inc_value('scheduler/dequeued/disk', spider=self.spider)
        if request:
            self.stats.inc_value('scheduler/dequeued', spider=self.spider)
        # ����ȡ�ĵ�Request���ظ�Engine
        return request

    def __len__(self):
        return len(self.dqs) + len(self.mqs) if self.dqs else len(self.mqs)

    def _dqpush(self, request):
        if self.dqs is None:
            return
        try:
            reqd = request_to_dict(request, self.spider)
            self.dqs.push(reqd, -request.priority)
        except ValueError as e:  # non serializable request
            if self.logunser:
                msg = ("Unable to serialize request: %(request)s - reason:"
                       " %(reason)s - no more unserializable requests will be"
                       " logged (stats being collected)")
                logger.warning(msg, {'request': request, 'reason': e},
                               exc_info=True, extra={'spider': self.spider})
                self.logunser = False
            self.stats.inc_value('scheduler/unserializable',
                                 spider=self.spider)
            return
        else:
            return True

    def _mqpush(self, request):
        self.mqs.push(request, -request.priority)

    def _dqpop(self):
        if self.dqs:
            d = self.dqs.pop()
            if d:
                return request_from_dict(d, self.spider)

    def _newmq(self, priority):
        return self.mqclass()

    def _newdq(self, priority):
        return self.dqclass(join(self.dqdir, 'p%s' % priority))

    def _dq(self):
        activef = join(self.dqdir, 'active.json')
        if exists(activef):
            with open(activef) as f:
                prios = json.load(f)
        else:
            prios = ()
        q = self.pqclass(self._newdq, startprios=prios)
        if q:
            logger.info("Resuming crawl (%(queuesize)d requests scheduled)",
                        {'queuesize': len(q)}, extra={'spider': self.spider})
        return q

    def _dqdir(self, jobdir):
        if jobdir:
            dqdir = join(jobdir, 'requests.queue')
            if not exists(dqdir):
                os.makedirs(dqdir)
            return dqdir