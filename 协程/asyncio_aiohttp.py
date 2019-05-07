#-*-coding:utf-8-*- 
# @File    : asyncio_aiohttp.py

import requests

def func(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    cookies = {'Cookie': ''}
    # 这里暂时懒得用session, verify参数忽略https网页的ssl验证
    r = requests.get(url, headers=headers, timeout=10, cookies=cookies, verify=False)
    r.encoding = r.apparent_encoding  # 自动识别网页编码避免中文乱码，但会拖慢程序
    return r.text  # 或r.content

func('http://www.sina.com')

########################################################################################

import asyncio
import aiohttp


async def html(url: str) ->str:
    code = 'utf-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        # 老版本aiohttp没有verify参数，如果报错卸载重装最新版本
        async with session.get(url, headers=headers, timeout=10, verify_ssl=False) as r:
            # text()函数相当于requests中的r.text，r.read()相当于requests中的r.content
            return await r.text()


loop = asyncio.get_event_loop()
loop.run_until_complete(html('http://www.sina.com'))
# 对需要ssl验证的网页，需要250ms左右等待底层连接关闭
loop.run_until_complete(asyncio.sleep(0.25))
loop.close()

# https://www.jianshu.com/p/0efdc952e8ca
# https://www.jianshu.com/p/5f41d9fb6b12