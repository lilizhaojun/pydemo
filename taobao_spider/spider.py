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
import xlwt
import matplotlib
import re


url = 'https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180305&ie=utf8'
response = requests.get(url)
html = response.text

content = re.findall(r'g_page_config =(.*?)g_srp_loadCss',html,re.S)[0]
print(content)