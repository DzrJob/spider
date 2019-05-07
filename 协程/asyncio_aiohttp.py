#-*-coding:utf-8-*- 
# @File    : asyncio_aiohttp.py

import requests

def func(url: str) ->str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    cookies = {'Cookie': ''}
    # ������ʱ������session, verify��������https��ҳ��ssl��֤
    r = requests.get(url, headers=headers, timeout=10, cookies=cookies, verify=False)
    r.encoding = r.apparent_encoding  # �Զ�ʶ����ҳ��������������룬������������
    return r.text  # ��r.content

func('http://www.sina.com')

########################################################################################

import asyncio
import aiohttp


async def html(url: str) ->str:
    code = 'utf-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        # �ϰ汾aiohttpû��verify�������������ж����װ���°汾
        async with session.get(url, headers=headers, timeout=10, verify_ssl=False) as r:
            # text()�����൱��requests�е�r.text��r.read()�൱��requests�е�r.content
            return await r.text()


loop = asyncio.get_event_loop()
loop.run_until_complete(html('http://www.sina.com'))
# ����Ҫssl��֤����ҳ����Ҫ250ms���ҵȴ��ײ����ӹر�
loop.run_until_complete(asyncio.sleep(0.25))
loop.close()

# https://www.jianshu.com/p/0efdc952e8ca
# https://www.jianshu.com/p/5f41d9fb6b12