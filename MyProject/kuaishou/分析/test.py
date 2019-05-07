#-*-coding:utf-8-*- 
# @File    : test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 驱动谷歌浏览器,实例对象
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
# 无界面
chrome_options.headless = False
# # 设置不加载图片
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)
# 1.数据Selenium
# 2.百度搜索尚硅谷,按确认按钮,等5秒截图尚硅谷png
driver.get('https://live.kuaishou.com/u/kslangbai666')

time.sleep(5)
# 截图当前画面
driver.save_screenshot('test.png')
# 3.当前页面数据,保存
# 获取源码
text = driver.page_source

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(text)