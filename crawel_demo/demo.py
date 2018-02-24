#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 9:31
# @Author  : lizhaojun
# @File    : demo.py
import requests
import re
#下载小说的首页
url = 'http://jingcaiyuedu.com/book/41366.html'

#打开文件
fd = open('E:\out_content',mode='w',encoding='utf-8')

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
#print(html)
#提取小说的标题
title = re.findall(r'<meta property="og:title" content="(.*?)"/>',html)[0]

#提取页面所有章节的标题和url
captal = re.findall(r'<dl id="list">.*?</dl>',html,re.S)[0]
captal_title = re.findall(r'href="(.*?)">(.*?)<',captal)

#循环下载每一个章节
for captal_num in captal_title:
    captal_num_title = captal_num[1]
    captal_num_url = 'http://www.jingcaiyuedu.com%s' % captal_num[0]
    #print(captal_num_title,captal_num_url)

    #下载每一章节内容
    captal_response = requests.get(captal_num_url)
    captal_response.encoding = 'utf-8'
    captal_html = captal_response.text
    #print(captal_html)

    #提取内容
    captal_num_article = re.findall(r'<script>a1\(\);</script>(.*?)<script>a2\(\);</script>',captal_html,re.S)[0]

    #清洗数据
    captal_num_article = captal_num_article.replace(' ','')
    captal_num_article = captal_num_article.replace('&nbsp;','')
    captal_num_article = captal_num_article.replace('<br/>','')
    #print(captal_num_article)

    #写入文件
    fd.write(captal_num_title)
    fd.write(captal_num_article)
    fd.write('\n')

fd.close()





