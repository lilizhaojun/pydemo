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


url = 'https://list.tmall.com/search_product.htm?q=python&type=p&' \
      'spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
response = requests.get(url)
html = response.text