#-*-coding:utf-8-*- 
# @File    : ǰ�˼��ܽ��б���.py
from selenium import webdriver
import  execjs

with open ('test.js','r') as f:
    source = f.read()
    phantom = execjs.get('PhantomJS')
    getpass = phantom.compile(source)
    mypass = getpass.call('encrypt', 'admin','admin')
    print(mypass)