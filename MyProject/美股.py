# -*-coding:utf-8-*-
# @File    : 美股.py
"""
「矩阵未来」爬虫（高级）面试题
我们希望你能独立完成下面的任务。结束后给 core@westmatrix.cn（如果被退回请发送至zt2008@qq.com） 发送这个题目的解答，邮件主题请用如下的命名规则：简历平台+面试岗位+姓名+电话。

获取雪球 美国股市涨幅最大的100个股票信息（股票代码，股票名称，当前价，涨跌幅，市值，市盈率） https://xueqiu.com/hq#exchange=US&firstName=3&secondName=3_0&order=desc&orderby=percent

回复邮件请附上代码和数据 - excel或者csv格式

"""
import requests
import json
import time
import pandas as pd
from pandas import DataFrame
"""
分析展示的json数据
https://xueqiu.com/hq#exchange=US&firstName=3&secondName=3_0&order=desc&orderby=percent
https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=1555123209330
https://xueqiu.com/service/v5/stock/screener/quote/list?page=2&size=30&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=1555128002264
"""

unix = time.time()  # 时间戳
size = 100  # 数据量没有限制30，可直接输入参数爬取，避免嵌套for循环降低效率
url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=%d&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=%d'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# 抓取页面
html_code = requests.get(url % (size, unix), headers=headers, verify=False)

# with open('source.html', 'w', encoding='utf-8') as f:
#     f.write(html_code.text)

# 转换字典
data = json.loads(html_code.text)['data']['list']
# print(data)


""""""
df = pd.DataFrame(data, columns=['symbol','name','current','percent','market_capital','pe_ttm'])
# print(df)
df.to_csv('股票信息1.csv',header=['股票代码','股票名称','当前价','涨跌幅','市值','市盈率'],index=False,encoding='utf_8_sig')


""""""
total = 0
for val in data:
    symbol = val['symbol']  # 股票代码
    name = val['name']  # 股票名称
    current = val['current']  # 当前价
    percent = val['percent']  # 涨跌幅
    market_capital = val['market_capital']  # 市值
    pe_ttm = val['pe_ttm']  # 市盈率
    total += 1
    # print(total, symbol, name, current, percent, market_capital, pe_ttm)

    df = DataFrame(
        {
            '股票代码':symbol,
            '股票名称':name,
            '当前价':current,
            '涨跌幅':percent,
            '市值':market_capital,
            '市盈率':pe_ttm
        }, columns=['股票代码', '股票名称','当前价','涨跌幅','市值','市盈率'],index=[total]
    )
    # print(df)

    if total == 1 :
        df.to_csv('股票信息2.csv', encoding='utf_8_sig')
    else:
        df.to_csv('股票信息2.csv',header=False ,mode='a',encoding='utf_8_sig')

