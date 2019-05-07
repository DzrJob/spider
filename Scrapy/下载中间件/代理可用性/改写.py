class MyRetryMiddleware(RetryMiddleware):
    logger = logging.getLogger(__name__)

    def delete_proxy(self, proxy):
        if proxy:
            # delete proxy from proxies pool


    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            # ɾ���ô���
            self.delete_proxy(request.meta.get('proxy', False))
            time.sleep(random.randint(3, 5))
            self.logger.warning('����ֵ�쳣, ��������...')
            return self._retry(request, reason, spider) or response
        return response


    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            # ɾ���ô���
            self.delete_proxy(request.meta.get('proxy', False))
            time.sleep(random.randint(3, 5))
            self.logger.warning('�����쳣, ��������...')

            return self._retry(request, exception, spider)