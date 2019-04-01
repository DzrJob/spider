#-*-coding:utf-8-*- 
# @File    : 简单加密无验证码.py
import requests
import json
login_url='https://passport.cnblogs.com/user/signin'
return_url='https://home.cnblogs.com/u/-E6-/'#我的主页
session=requests.session()

#获取VerificationToken
login_page=session.get(login_url)
p=login_page.text.find('VerificationToken')+len('VerificationToken')+4
token=login_page.text[p:login_page.text.find("'",p)]

headers={'Content-Type': 'application/json; charset=UTF-8',
          'X-Requested-With': 'XMLHttpRequest',
          'VerificationToken':token}
session.headers.update(headers)
#可以通过抓包获取加密后的用户名和密码，我将在附录部分介绍如何在Python中加密
data={"input1":"。。。省略。。。",
      "input2":"。。。省略。。。",
      "remember":True}

#模拟登录
response=session.post(login_url,data=json.dumps(data))
print(response.text)
#{"success":true}
#登录成功

#跳转到主页
home_page=session.get(return_url)
#获取主页标题
p=home_page.text.find('<title>')+len('<title>')
title=home_page.text[p:home_page.text.find('</title>',p)]
print(title)
#E6的主页 - 博客园
#如果登录失败，跳转到主页时返回的结果没有title标签，home_page.text将为'需要登陆'