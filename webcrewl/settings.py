# -*- coding: utf-8 -*-

# Scrapy settings for webCrewl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'coupons'

SPIDER_MODULES = ['webcrewl.spiders']
NEWSPIDER_MODULE = 'webcrewl.spiders'

ROOT_URL = 'http://www.newsmth.net'
BASE_URL = 'http://www.newsmth.net/nForum/board/CouponsLife'

AM_ROOT_URL = 'https://www.amazon.cn/'
AM_BASE_URL = 'https://www.amazon.cn/gp/goldbox/all-deals'
AMZ_PAGE_URL = 'https://www.amazon.cn/gp/goldbox/ref=gbps_ftr_s-4_68d9_page_2?gb_f_GB-SUPPLE=page:2,sortOrder:BY_SCORE,dealsPerPage:18&pf_rd_p=fd0b439a-1761-4f65-859a-d880c95c68d9&pf_rd_s=slot-4&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=JAMNNEB0MEJEE42CJ40N'

KEYS = ['亚马逊', '白条', '亚麻', '闪付', 'ofo', '摩拜', '手慢无', '物美', '翼支付', '菜鸟', '大毛', '小毛', '超市', 'jd', '华夏','z秒']
AUTHOR = ['keeker'] 
EXCLUDE = ['吗', '?','？', '为什么','求','如何', '怎么样', '咨询', '为啥']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webCrewl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'webCrewl.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'webcrewl.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'webcrewl.pipelines.SomePipeline': 300,
#}
ITEM_PIPELINES = {
    'webcrewl.pipelines.TagPipeline': 100,
    'webcrewl.pipelines.MongoDBPipeline':300
                  }

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "coupons"
MONGODB_COLLECTION = "items"
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
