#-*-coding:utf-8-*- 
# @File    : 前端加密进行爆破.py
from selenium import webdriver
import  execjs

with open ('test.js','r') as f:
    source = f.read()
    phantom = execjs.get('PhantomJS')
    getpass = phantom.compile(source)
    mypass = getpass.call('encrypt', 'admin','admin')
    print(mypass)