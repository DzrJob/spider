# -*- coding: utf-8 -*-

# Scrapy settings for jd project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd'

SPIDER_MODULES = ['jd.spiders']
NEWSPIDER_MODULE = 'jd.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "authority": "www.jd.com",
   "method": "GET",
   "path": "/",
   "scheme": "https",
   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   "accept-encoding": "gzip, deflate, br",
   "accept-language": "zh-CN,zh;q=0.9",
   "cache-control": "no-cache",
   "cookie": "shshshfpa=5298db10-4f9c-f3af-9cc8-b4737c9ef4a6-1545994879; shshshfpb=iIxAbhcmKaHPOPG6CZmgHBw%3D%3D; o2Control=webp|lastvisit=13; pinId=ktRu68LA7BJgYYxWfbkPFrV9-x-f3wj7; unpl=V2_ZzNtbUpVRBx9DhRXeRhcB2JRFw4RBxYWIFgUUH0aD1VvBhYIclRCFX0UR1FnGF4UZwQZXERcRhRFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdWQFvCxdURF5AHXcLR1R5GFoMYgMibUVncyV2DE5ccxxsBFcCIh8WC0sScwhAGXsdWQFvCxdURF5AHXcLR1R5GFoMYgMiXHJU; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_936897c230134c4bbad2dac572ba945d|1554278862296; areaId=1; PCSYCityID=1; ipLoc-djd=1-72-2799-0; __jdu=1545994878293201307841; user-key=2d8b338c-01fd-4c33-befb-6245ba0e97a5; cn=0; mt_xid=V2_52007VwMWV1lQWl8WTxBfDWUAE1JfWVRTGkkpXwNuAxpTWFlOWEtAGkAANwNBTlRZW1wDHBgLA2YEFQEJCgVcL0oYXA17AhdOXFpDWR9CGFQOYgAiUG1YYlkdSxBdAWALEmJdXVRd; shshshfp=28f65b8f9c4d124b257eaebbf9db349e; __jda=122270672.1545994878293201307841.1545994878.1554365056.1554371216.22; TrackID=1ERY3UQQ0FKgYo1D9guTxC3PERBQUKiNTyFVVaqqc9ww4nEG00qWkQyORqtPmzikj8EyvHir1zo7054KPrxRkx7coxwa_xQt8V953vXwrkDQ; thor=A88F5552D99B0B04515C28B2A55F41794EB75781B1DB258A9AC82FCB12D2C5FFE62BE9A25A01C4DC5E642C5D33ADA0CB8AA36E7349C63ED4A310DC383DC9482F3538A57A7168A167C99393FB3340E6A404B2BA605B2149EF76DAFC997A9F8FC12C255233272FA0A2D03A321843AFDF4498507E1556483C8A26EBB9C67CE8CAAFBDA08256969CF5424C7D9984F8B598738DF2FE7392D6AFF738241FA77E2C7507; pin=jd_6d0140cc90785; unick=%E6%BA%BA%E6%B0%B4%E4%BA%91%E8%8D%92; ceshi3.com=201; _tp=7YHwXC88znjkmLJCNVwDc1yL4VQjf1eG2cGQ%2FcKp7BQ%3D; _pst=jd_6d0140cc90785; 3AB9D23F7A4B3C9B=EKPH5I35ZWPDI5BGQRMHNDQN2ISFRVBMT7O7LT3DZQ5ES4HGZEXAWJXVFSAQDNVRCSGNWIEN2YTGVSYPCE5S6FOOBM; __jdb=122270672.18.1545994878293201307841|22.1554371216; shshshsID=c52319532e91ab744204ff110645e568_6_1554371403316",
   "pragma": "no-cache",
   "referer": "https://search.jd.com/Search?keyword=%E6%89%8B%E8%A1%A8&enc=utf-8&spm=a.0.0&wq=&pvid=45efb033b2fd416799c496494293bb91",
   "upgrade-insecure-requests": "1",
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd.middlewares.JdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载中间件
# DOWNLOADER_MIDDLEWARES = {
#     # 'jd.middlewares.JdDownloaderMiddleware': 543,
#     'jd.middlewares.JDScrapyDownloaderRandomUser': 543, # 使用随机请求头和IP
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,  # 把系统的禁用掉
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'jd.pipelines.JDPipeline': 300,  # 数据存储成json文件
   'jd.pipelines.JDMongoDBPipeline': 301, # 存储到MongoDB
   'jd.pipelines.ExamplePipeline': 303,  # 添加爬取的时间和爬虫的名称
   'jd.pipelines.JDsqlite3Pipeline': 304,  # 存储到sqlite
   'scrapy_redis.pipelines.RedisPipeline': 400,  # 将数据存到redis数据库 (优先级要比其他管道低(数值高))
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
"""------------------------MONGODB------------------------"""
# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
DB_NAME = "jd"
# 存放数据的表名称
SHEET_NAME = "jd"
"""-------------------------------------------------------"""
"""------------------------redis分布式------------------------"""
# scrapy_redis去重组件(scrapy去重保存为内存，停止后会失效)
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 启用Redis调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 不调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
# 不清空redis队列 可中途暂停, 不清空信息
SCHEDULER_PERSIST = True
# 默认Scrapy队列模式, 优先级
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列模式, 先进先出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈模式, 先进后出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
# redis主机
# REDIS_HOST = "127.0.0.1"
# REDIS_PORT = 6379
# REDIS_PASS = 'redisP@ssw0rd'
# REDIS_ENCODING = "utf-8"
REDIS_URL = "redis://127.0.0.1:6379"
"""-------------------------------------------------------"""
