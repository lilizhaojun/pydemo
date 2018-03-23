#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 17:14
# @Author  : lizhaojun
# @File    : demo_object.py
'''
利用面向对象的思想实现简单爬虫
'''
import requests
import re

class Crawel:

    #下载内容
    def download(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        return response.text

    def spider(self,url):
        html = self.download(url)
        title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html)[0]
        fd = open('E:\%s' % title, mode='w', encoding='utf-8')
        captal = re.findall(r'<dl id="list">.*?</dl>', html, re.S)[0]
        captal_title = re.findall(r'href="(.*?)">(.*?)<', captal)

        for captal_num in captal_title:
            captal_num_title = captal_num[1]
            captal_num_url = 'http://www.jingcaiyuedu.com%s' % captal_num[0]


            # 下载每一章节内容
            captal_html = self.download(captal_num_url)


            # 提取内容
            captal_num_article = \
            re.findall(r'<script>a1\(\);</script>(.*?)<script>a2\(\);</script>', captal_html, re.S)[0]

            # 清洗数据
            captal_num_article = captal_num_article.replace(' ', '')
            captal_num_article = captal_num_article.replace('&nbsp;', '')
            captal_num_article = captal_num_article.replace('<br/>', '')


            # 写入文件
            fd.write(captal_num_title)
            fd.write(captal_num_article)
            fd.write('\n')
        fd.close()


if __name__ == '__main__':
    crawel = Crawel()
    url = 'http://jingcaiyuedu.com/book/41366.html'
    crawel.spider(url)
