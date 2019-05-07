#-*-coding:utf-8-*- 
# @File    : selenium淘宝滑动验证码.py
import asyncio
import time,random
from selenium import webdriver
from retrying import retry

async def main(username,pwd,url):
    chrome_options = webdriver.ChromeOptions()
    # 无界面
    chrome_options.headless = False
    # 设置不加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.execute_script(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    driver.execute_script('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    driver.execute_script('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    driver.execute_script('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    userdriver.find_element_by_id('TPL_username_1')
    driver.find_element_by_id('TPL_password_1').send_keys(username)
