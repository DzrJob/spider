# RetryMiddleware����Դ��
class RetryMiddleware(object):

    # ����������Exceptionʱ��������
    EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError, ConnectionRefusedError, ConnectionDone, ConnectError, ConnectionLost, TCPTimedOutError, ResponseFailed, IOError, TunnelError)

    def __init__(self, settings):
        '''
        �����漰����settings.py�ļ��еļ�����
        RETRY_ENABLED: ���ڿ����м����Ĭ��ΪTRUE
        RETRY_TIMES: ���Դ���, Ĭ��Ϊ2
        RETRY_HTTP_CODES: ������Щ����״̬����Ҫ����, һ���б�Ĭ��Ϊ[500, 503, 504, 400, 408]
        RETRY_PRIORITY_ADJUST�����������ԭʼ����������������ȼ���Ĭ��Ϊ-1
        '''
        if not settings.getbool('RETRY_ENABLED'):
            raise NotConfigured
        self.max_retry_times = settings.getint('RETRY_TIMES')
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')

    def process_response(self, request, response, spider):
        # ��֮ǰ�����request�п��Լ���meta��Ϣdont_retry�������Ƿ�����    
        if request.meta.get('dont_retry', False):
            return response

        # ���״̬���Ƿ����б��У��ڵĻ��͵���_retry������������
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            # �ڴ˴������Լ��Ĳ�������ɾ�������ô�������־��
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        # ���������Exception�б��еĴ��󣬽�������
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            # �ڴ˴������Լ��Ĳ�������ɾ�������ô�������־��
            return self._retry(request, exception, spider)