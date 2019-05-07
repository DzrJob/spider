#-*-coding:utf-8-*- 
# @File    : test.py
import time
import os
while True:
    print('the first spider')
    os.system("scrapy crawl human -o human.json")
    print('the second spider')
    os.system("scrapy crawl nbgov -o nbgov.json")
    time.sleep(86400)# 24hours