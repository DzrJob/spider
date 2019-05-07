#-*-coding:utf-8-*- 
# @File    : test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# �����ȸ������,ʵ������
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
# �޽���
chrome_options.headless = False
# # ���ò�����ͼƬ
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)
# 1.����Selenium
# 2.�ٶ������й��,��ȷ�ϰ�ť,��5���ͼ�й��png
driver.get('https://live.kuaishou.com/u/kslangbai666')

time.sleep(5)
# ��ͼ��ǰ����
driver.save_screenshot('test.png')
# 3.��ǰҳ������,����
# ��ȡԴ��
text = driver.page_source

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(text)