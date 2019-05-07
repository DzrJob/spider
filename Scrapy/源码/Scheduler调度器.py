#-*-coding:utf-8-*- 
# @File    : Scheduler调度器.py
"""
CHEDULER的主要是完成了 push Request pop Request 和 去重的操作。

而且queue 操作是在内存队列中完成的。

queuelib.queue就会发现基于内存的（deque）

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
        # 注意在scrpy中优先注意这个方法，此方法是一个钩子 用于访问当前爬虫的配置
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        # 获取去重用的类 默认：scrapy.dupefilters.RFPDupeFilter
        dupefilter_cls = load_object(settings['DUPEFILTER_CLASS'])
        # 对去重类进行配置from_settings 在 scrapy.dupefilters.RFPDupeFilter 43行
        # 这种调用方式对于IDE跳转不是很好  所以需要自己去找
        # @classmethod
        # def from_settings(cls, settings):
        #     debug = settings.getbool('DUPEFILTER_DEBUG')
        #     return cls(job_dir(settings), debug)
        # 上面就是from_settings方法 其实就是设置工作目录 和是否开启debug
        dupefilter = dupefilter_cls.from_settings(settings)
        # 获取优先级队列 类对象 默认：queuelib.pqueue.PriorityQueue
        pqclass = load_object(settings['SCHEDULER_PRIORITY_QUEUE'])
        # 获取磁盘队列 类对象（SCHEDULER使用磁盘存储 重启不会丢失）
        dqclass = load_object(settings['SCHEDULER_DISK_QUEUE'])
        # 获取内存队列 类对象（SCHEDULER使用内存存储 重启会丢失）
        mqclass = load_object(settings['SCHEDULER_MEMORY_QUEUE'])
        # 是否开启debug
        logunser = settings.getbool('LOG_UNSERIALIZABLE_REQUESTS', settings.getbool('SCHEDULER_DEBUG'))
        # 将这些参数传递给 __init__方法
        return cls(dupefilter, jobdir=job_dir(settings), logunser=logunser,
                   stats=crawler.stats, pqclass=pqclass, dqclass=dqclass, mqclass=mqclass)


    def has_pending_requests(self):
      """检查是否有没处理的请求"""
        return len(self) > 0

    def open(self, spider):
      """Engine创建完毕之后会调用这个方法"""
        self.spider = spider
        # 创建一个有优先级的内存队列 实例化对象
        # self.pqclass 默认是：queuelib.pqueue.PriorityQueue
        # self._newmq 会返回一个内存队列的 实例化对象 在110  111 行
        self.mqs = self.pqclass(self._newmq)
        # 如果self.dqdir 有设置 就创建一个磁盘队列 否则self.dqs 为空
        self.dqs = self._dq() if self.dqdir else None
        # 获得一个去重实例对象 open 方法是从BaseDupeFilter继承的
        # 现在我们可以用self.df来去重啦
        return self.df.open()

    def close(self, reason):
      """当然Engine关闭时"""
          # 如果有磁盘队列 则对其进行dump后保存到active.json文件中
        if self.dqs:
            prios = self.dqs.close()
            with open(join(self.dqdir, 'active.json'), 'w') as f:
                json.dump(prios, f)
        # 然后关闭去重
        return self.df.close(reason)

    def enqueue_request(self, request):
      """添加一个Requests进调度队列"""
          # self.df.request_seen是检查这个Request是否已经请求过了 如果有会返回True
        if not request.dont_filter and self.df.request_seen(request):
              # 如果Request的dont_filter属性没有设置（默认为False）和 已经存在则去重
            # 不push进队列
            self.df.log(request, self.spider)
            return False
        # 先尝试将Request push进磁盘队列
        dqok = self._dqpush(request)
        if dqok:
              # 如果成功 则在记录一次状态
            self.stats.inc_value('scheduler/enqueued/disk', spider=self.spider)
        else:
              # 不能添加进磁盘队列则会添加进内存队列
            self._mqpush(request)
            self.stats.inc_value('scheduler/enqueued/memory', spider=self.spider)
        self.stats.inc_value('scheduler/enqueued', spider=self.spider)
        return True

    def next_request(self):
      """从队列中获取一个Request"""
          # 优先从内存队列中获取
        request = self.mqs.pop()
        if request:
            self.stats.inc_value('scheduler/dequeued/memory', spider=self.spider)
        else:
              # 不能获取的时候从磁盘队列队里获取
            request = self._dqpop()
            if request:
                self.stats.inc_value('scheduler/dequeued/disk', spider=self.spider)
        if request:
            self.stats.inc_value('scheduler/dequeued', spider=self.spider)
        # 将获取的到Request返回给Engine
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