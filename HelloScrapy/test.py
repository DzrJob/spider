#-*-coding:GBK-*-
'''
今日头条
js破解_signetrue
'''
from selenium import webdriver
import requests
import time
import json
# from utils.get_proxy import func_proxy
# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
options.set_headless()
options.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"')
# 设置代理
# service_args = ['--proxy={}'.format(func_proxy()['http']), '--proxy-type=socks5']
# brower = webdriver.Chrome(chrome_options=options, service_args=service_args)
brower = webdriver.Chrome(chrome_options=options)
brower.get('https://www.toutiao.com/ch/news_hot/')
sinature = brower.execute_script('return TAC.sign(0)')
print(sinature)
"""获取cookie"""
cookie = brower.get_cookies()
cookie = [item['name'] + "=" + item['value'] for item in cookie]
cookiestr = '; '.join(item for item in cookie)
brower.quit()
print(cookiestr)
header1 = {
    'Host': 'www.toutiao.com',
    'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"',
    'Referer': 'https://www.toutiao.com/ch/news_hot/',
    "Cookie": cookiestr

}
url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&_signature={}'.format(
    sinature)
print(url)
html = requests.get(url, headers=header1, verify=False)
# html = requests.get(url, headers=header1, proxies=func_proxy(), verify=False)
print(html.content.decode('unicode_escape'))
