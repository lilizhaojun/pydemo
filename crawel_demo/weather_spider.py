#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 下午9:53
# @Author  : lizhaojun
# @Site    : 
# @File    : weather_spider.py
# @Software: PyCharm
'''
爬取中国天气网
'''

import requests
import re
import xlwt

class Spider:
    def __init__(self):
        self.book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        self.sheet = self.book.add_sheet('result', cell_overwrite_ok=True)  # cell_overwrite_ok表示是否可以覆盖单元格

    def download(self,url):
        """
        下载链接的内容
        :param url: 
        :return: 
        """
        response = requests.get(url)
        response.encoding = 'utf-8'
        return response.text


    def close_file(self,load):
        """
        关闭并保存文件
        :return: 
        """
        self.book.save(r'%s' % load)


    def io_file_leng(self,y,data):
        """
        纵向写入
        :return: 
        """
        num = 1
        for i in data:
            self.sheet.write(num, y, i)
            num += 1



    def io_file_cro(self,x,data):
        """
        横向写入
        :return: 
        """
        num = 1
        for i in data:
            self.sheet.write(x,num,i)
            num += 1



    def extract(self,url):
        """
        提取所需内容
        :return: 
        """
        extract = []
        html = self.download(url)
        province = re.findall(r'weather.com.cn" target="_blank">(.*?)</a>',html)[0]
        try:
            city = re.findall(r'<a href="http://www.weather.com.cn/weather/101280101.shtml" target="_blank">(.*?)</a>', html)[0]
        except(ZeroDivisionError, TypeError,IndexError) as e:
            print(e)

        self.sheet.write(0,0,province)

        content = re.findall(r'<ul class="t clearfix">(.*?)</ul>',html,re.S)[0]

        today_time = re.findall(r'<h1>(.*?)</h1>',content)
        extract.append(today_time)

        today_weather = re.findall(r'class="wea">(.*?)</p>',content)
        extract.append(today_weather)

        today_temperature = re.findall(r'<span>(.*?)</span>/<i>(.*?)℃</i>',content)
        tep_high = []
        tep_low = []
        for tep in today_temperature:
            tep_high.append(tep[0])
            tep_low.append(tep[1])
        extract.append(tep_high)
        extract.append(tep_low)
        print(extract)


        #写入文件
        i = 0
        for extract_num in extract:
            self.io_file_leng(i,extract_num)
            i += 1


if __name__ == '__main__':
    spider = Spider()
    url = "http://www.weather.com.cn/weather/101280101.shtml"
    spider.extract(url)
    spider.close_file('test.xls')