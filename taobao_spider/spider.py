#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 下午10:23
# @Author  : lizhaojun
# @Site    : 
# @File    : spider.py
# @Software: PyCharm
'''
淘宝中数据爬虫
'''


import requests
import time
import xlwt
import matplotlib
import re
import json

Data = []

def getdata(data_list):
    """
    获取相关数据
    :return: 
    """
    for item in data_list:
        temp = {
            'title': item['title'],
            'view_price': item['view_price'],
            'item_loc': item['item_loc'],
            'nick': item['nick'],
            'view_sales': item['view_sales'],
            'detail_url': item['detail_url']
        }
        Data.append(temp)


url = 'https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180305&ie=utf8'
response = requests.get(url)
html = response.text

#提取、清洗
content = re.findall(r'g_page_config =(.*?)g_srp_loadCss',html,re.S)[0].strip()

#格式化数据
content = content[:-1]
#print(content)
content = json.loads(content)
data_list = content['mods']['itemlist']['data']['auctions']
#print(data_list)

#筛选出需要的数据
getdata(data_list)

#首页12条异步加载的数据
url2 = 'https://s.taobao.com/api?_ksTS=1520760735896_240&callback=jsonp241&ajax=true&m=customized&stats_click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180311&bcoffset=0&js=1&ie=utf8&rn=4ea860d275f6378bca26c789f2dfa222'
response2 = requests.get(url2)
html2 = response2.text
data_list2 = json.loads(re.findall(r'{.*}',html2)[0])['API.CustomizedApi']['itemlist']['auctions']

getdata(data_list2)

#翻页
for i in range(1,10):
    data_value = 44*i
    t = time.time()
    ksTs = '%s_%s'% (int(t*1000),str(t)[-3:])
    callback = 'jsonp%s'% (int(str(t)[-3:])+1)
    url = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}&callback={}&q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180311&ie=utf8&bcoffset=4&ntoffset=0&p4ppushleft=1%2C48&s=0'.format(data_value,ksTs,callback)
    #print(url)
    response = requests.get(url)
    html = response.text
    data_list = json.loads(re.findall(r'{.*}', html)[0])['mods']['itemlist']['data']['auctions']

    getdata(data_list)

print(len(Data))