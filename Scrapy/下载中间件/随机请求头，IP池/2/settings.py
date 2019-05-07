#settings.py
#...
DOWNLOADER_MIDDLEWARES = {
    'newproject.middlewares.RandomHttpProxyMiddleware': 543,
    'newproject.middlewares.RandomUserAgentMiddleware': 550,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
}
HTTP_PROXY_LIST = [
    'http://193.112.216.55:1234',
    'http://118.24.172.34:1234',
]