#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 9:46
# @Author  : lizhaojun
# @File    : bs4_demo.py
'''
演示beautifulsoup的应用
'''
from bs4 import BeautifulSoup
import html5lib

def get_html_data():
    html_doc = """
    <html>
    <head>
    <title>WuXiaolong</title>
    </head>
    <body>
    <p>分享 Android 技术，也关注 Python 等热门技术。</p>
    <p>写博客的初衷：总结经验，记录自己的成长。</p>
    <p>你必须足够的努力，才能看起来毫不费力！专注！精致！
    </p>
    <p class="Blog"><a href="http://wuxiaolong.me/">WuXiaolong's blog</a></p>
    <p class="WeChat"><a href="https://open.weixin.qq.com/qr/code?username=MrWuXiaolong">公众号：吴小龙同学</a> </p>
    <p class="GitHub"><a href="http://example.com/tillie" class="sister" id="link3">GitHub</a></p>
    </body>
    </html>   
    """
    soup = BeautifulSoup(html_doc,'html5lib')
    tag = soup.head
    print(tag)
    print(tag.name)
    print(tag.title)
    #多个匹配时，只显示第一个，比如P标签
    print(soup.p)
    print(soup.a['href'])
    print(soup.find('p'))
    print(soup.find('p',class_= 'WeChat'))
    print('************')

    for p in soup.find_all('p'):
        print(p.string)

if __name__ == '__main__':
    get_html_data()
