# -*- coding: utf-8 -*-
# 项目的设置文件
"""
    设置浏览器头
    设置middlewares.py
    设置pipelines.py
"""
# Scrapy settings for HelloScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 项目名称
BOT_NAME = 'HelloScrapy'
# 爬虫模块的位置
SPIDER_MODULES = ['HelloScrapy.spiders']
# 新爬虫模块的位置
NEWSPIDER_MODULE = 'HelloScrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'HelloScrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 是否要遵循爬虫协议，不遵循设置为Fasle或者注释掉即可
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 爬虫的并发量，默认是16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延迟配置，默认是0,以后可以设置2或者1.5都行
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# 每个域的并发请求
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 每个IP 16个并发请求
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否启用cookie,默认是启用，要设置不起来，防止别人知道我们
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用telnet控制台（默认启用）
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
# 爬虫中间件，一般用不着
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'HelloScrapy.middlewares.HelloscrapySpiderMiddleware': 543,
# }
# 下载中间件，以后下载的时候可以用，后面的值是优先级，数字越小优先级越高
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'HelloScrapy.middlewares.HelloscrapyDownloaderMiddleware': 543,
    'LianJia.middlewares.LianjiaSpiderRandomUser': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,  # 把系统的禁用掉
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 配置管道文件
ITEM_PIPELINES = {
    'HelloScrapy.pipelines.HelloscrapyPipeline': 300,
    'TodayTopNews.pipelines.ExamplePipeline': 302,  # 添加爬取的时间和爬虫的名称
    'scrapy_redis.pipelines.RedisPipeline': 400,  # 把爬取的数据添加到redis数据
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True

# The initial download delay
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
# 在高延迟情况下要设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 日志级别
# LOG_LEVEL = 'DEBUG'
# 下载延迟
# DOWNLOAD_DELAY = 1
# 下载超时
# DOWNLOAD_TIMEOUT = 10
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

ITEM_PIPELINES = {
    'LianJia.pipelines.LianjiaPipeline': 300,
    'LianJia.pipelines.MyredisspiderPipeline': 302,  # 添加爬取的时间和爬虫的名称
    'scrapy_redis.pipelines.RedisPipeline': 400,  # 将数据存到redis数据库 (优先级要比其他管道低(数值高))
}
"""redis分布式"""
# scrapy_redis去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# scrapy_redis调度器组件
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
