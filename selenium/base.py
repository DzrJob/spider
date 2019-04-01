# coding=utf-8
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
# 设置不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)
# 1.数据Selenium
# 2.百度搜索尚硅谷,按确认按钮,等5秒截图尚硅谷png
driver.get('https://www.baidu.com')
# 获取标题的实际值
aTitle = driver.getTitle()
# 找到输入框
kw = driver.find_element_by_id('kw')
# 输入
kw.send_keys('尚硅谷')
# 找到点击
su = driver.find_element_by_id('su')
# 点击
su.click()

time.sleep(5)
# 截图当前画面
driver.save_screenshot('尚硅谷.png')
# 3.当前页面数据,保存
# 获取源码
text = driver.page_source

with open('尚硅谷.html', 'w', encoding='utf-8') as f:
    f.write(text)

# 4.cookie
# 5.模拟键盘操作,ctrl+a 5秒 ctrl+x 5秒"我爱你中国" 5秒 截图 我爱你中国.png
kw.send_keys(Keys.CONTROL, 'a')
time.sleep(5)
kw.send_keys(Keys.CONTROL, 'x')
time.sleep(5)
kw.send_keys('我爱你中国')
time.sleep(5)

su.click()
driver.save_screenshot('我爱你中国.png')
"""
元素等待
WebDriverWait 显示等待是针对某一个元素进行相关等待判定
driver.implicitly_wait 隐式等待不针对某一个元素进行等待，而是全局元素等待
expected_conditions 判断页面元素
"""                                                          #判断某个元素是否被加到dom树下
element=WebDriverWait(driver,5,0.5).until(expected_conditions.presence_of_element_located((By.ID,"kw")))
# driver:浏览器驱动
# timeout:最长超过时间，默认以秒为单位
# poll_frequency:监测的时间间隔，默认为0.5秒
# ignored_exceptions:超时后的异常信息，默认情况下抛NoSuchElementException异常
# WebDriverWait一般有until和until_not方法配合使用

# time.sleep(5) 强制等待
# driver.implicitly_wait(5) # 隐式等待，整个页面

# 6.设置成无界面模式

# 7.退出浏览器
# driver.close()
driver.quit()


