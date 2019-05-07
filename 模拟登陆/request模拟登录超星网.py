# -*-coding:utf-8-*-
# @File    : login_requests.py
import requests
# url = 'http://passport2.chaoxing.com/login'
code_url = 'http://passport2.chaoxing.com/num/code?1553701058279'
login_url = 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Ffxlogin.chaoxing.com%2Ffindlogin.jsp%3Fbackurl%3Dhttp%253A%252F%252Fwww.chaoxing.com%252Fchannelcookie%253Ftime%253D1553700990412'
return_url = 'http://i.mooc.chaoxing.com/space/index?t=1553701572714'
form = {
    "pid": "-1",
    "pidName": "",
    "fid": "-1",
    "fidName": "",
    "allowJoin": "0",
    "isCheckNumCode": "1",
    "f": "0",
    "productid": "",
    "uname": "***************",
    "password": "***************",
    "numcode": "5536",
    "verCode": "",
}
headers = {
"Host":"passport2.chaoxing.com",
"Connection":"keep-alive",
"Pragma":"no-cache",
"Cache-Control":"no-cache",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
}
session = requests.session()
session.headers = headers

valcode = session.get(code_url)

print(session.cookies)

temp = open("valcode.png", "wb")
temp.write(valcode.content)
temp.close()

valc = input("input:")
form["numcode"] = str(valc)
print(session.cookies)
resp = session.post(login_url,data=form)

print(session.cookies)

# 把返回的页面写入temp_1.html
temp = open("temp_1.html", "wb")
temp.write(resp.content)
temp.close()
ret = session.get(return_url)
temp = open("temp_1.html", "wb")
temp.write(ret.content)
temp.close()