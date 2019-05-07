#-*-coding:utf-8-*- 
# @File    : 西刺代理.py
import requests
import re
url = 'https://www.xicidaili.com/nn/'
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Host":"www.xicidaili.com",
"Pragma":"no-cache",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}


def re_parse_html(html_code):
    pass

response = requests.get(url=url,headers=headers)
# print(response.text)
# <a href="/nn/3639">3639</a> <a href="/nn/3640">3640</a>
page_max = re.findall(r'<a href="/nn/\d+">(\d+)</a>',response.text)[1]
for page in range(1,int(page_max)):  #不要最后一页
    spider_url = url+str(page)
    html_code=requests.get(spider_url,headers=headers).text
    print(html_code)
    # re_list_ip = re.findall(r'<td>\d*\.\d*\.\d*\.\d*</td>', html_code)
    # re_list_port = re.findall(r'<td>[\d]*</td>', html_code)
    # re_list_live_time = re.findall(u'<td>\d*[小时分钟天]+</td>', html_code)
    # print(re_list_ip)
    # print(re_list_port)
    # print(re_list_live_time)