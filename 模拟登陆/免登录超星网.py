# -*-coding:utf-8-*-
# @File    : login_requests.py
import requests
# url = 'http://passport2.chaoxing.com/login'
code_url = 'http://passport2.chaoxing.com/num/code?1553701058279'
login_url = 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Ffxlogin.chaoxing.com%2Ffindlogin.jsp%3Fbackurl%3Dhttp%253A%252F%252Fwww.chaoxing.com%252Fchannelcookie%253Ftime%253D1553700990412'
return_url = 'http://i.mooc.chaoxing.com/space/index?t=1553701572714'
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Cookie":"msign_dsr=1553701507253; search_uuid=5df6c806%2de13c%2d4427%2d816a%2dba44a0cb2ea9; UM_distinctid=169bfd38dae508-04571dba8ebcc-b781636-1fa400-169bfd38daf410; chaoxinguser=1; uname=18610059580; _uid=96670250; uf=f9866f9a46b706224fb19f078f19457338671d16e330293316b29334e085223d81b0916a99ee1271c2a6ecfb4a14dc93a8644210e4fd43fffd68be96b6183b1af14b7c176e8f0318310b971a2f9f7b97782233b6f7bf1259; _d=1554212701528; UID=96670250; vc=1A1182A1FEB66604547D8DF136031C18; vc2=DE7E535746448DDC28DD5C5FC723A974; DSSTASH_LOG=C_0-UN_0-US_96670250-T_1554212701529",
"Host":"i.mooc.chaoxing.com",
"Pragma":"no-cache",
"Proxy-Connection":"keep-alive",
"Referer":"http://reg.chaoxing.com/reg/RegisterNew.dll",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

rep = requests.get(return_url,headers=headers)

with open('temp2.html','wb') as f:
    f.write(rep.content)