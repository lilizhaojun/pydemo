#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 19:10
# @Author  : lizhaojun
# @File    : spider_object.py
'''
面向对象的方式
'''
import requests
import time
import xlwt
import re
import json
from taobao_spider import draw

Data = []
class SpiderTaobao:

    def getdata(self,data_list):
        """
        获取相关数据
        :return:
        """
        for item in data_list:
            temp = {
                'title': item['raw_title'],
                'view_fee': '否' if float(item['view_fee']) else '是',
                'isTmall': '是' if item['shopcard']['isTmall'] else '否',
                'view_price': item['view_price'],
                'item_loc': item['item_loc'],
                'nick': item['nick'],
                'view_sales': item['view_sales'],
                'detail_url': item['detail_url'],
            }
            Data.append(temp)

    def download(self,url):
        """
        下载
        :param url:
        :return:
        """
        response = requests.get(url)
        html = response.text

        return html

    def draw(self):
        """
        绘制
        :return:
        """
        # 分析画图
        # 1、包邮不包邮的比例
        data1 = {'包邮': 0, '不包邮': 0}
        # 2、淘宝与天猫的比例
        data2 = {'淘宝': 0, '天猫': 0}
        # 3、地区选择
        data3 = {}

        for item in Data:
            # print(item)
            if item['view_fee'] == '是':
                data1['包邮'] += 1
            else:
                data1['不包邮'] += 1
            if item['isTmall'] == '是':
                data2['天猫'] += 1
            else:
                data2['淘宝'] += 1
            data3[item['item_loc'].split(' ')[0]] = data3.get(item['item_loc'].split(' ')[0], 0) + 1
        # print(data1)
        # print(data2)
        draw.pie(data1, '是否包邮')
        draw.pie(data2, '是否天猫')
        draw.bar(data3, '地区分布情况')

    def save(self):
        """
        保存
        :return:
        """
        # 持续化，导入xml文件中
        file = xlwt.Workbook(encoding='utf-8')
        sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
        # 写标题
        sheet1.write(0, 0, '标题')
        sheet1.write(0, 1, '价格')
        sheet1.write(0, 2, '地区')
        sheet1.write(0, 3, '店名')
        sheet1.write(0, 4, '购买人数')
        sheet1.write(0, 5, '是否包邮')
        sheet1.write(0, 6, '是否天猫')
        sheet1.write(0, 7, 'url')
        # 写内容
        for i in range(len(Data)):
            sheet1.write(i + 1, 0, Data[i]['title'])
            sheet1.write(i + 1, 1, Data[i]['view_price'])
            sheet1.write(i + 1, 2, Data[i]['item_loc'])
            sheet1.write(i + 1, 3, Data[i]['nick'])
            sheet1.write(i + 1, 4, Data[i]['view_sales'])
            sheet1.write(i + 1, 5, Data[i]['view_fee'])
            sheet1.write(i + 1, 6, Data[i]['isTmall'])
            sheet1.write(i + 1, 7, Data[i]['detail_url'])

        file.save('商品爬虫结果1.xls')

    def spider(self):
        """
        爬虫主体
        :return:
        """
        url = 'https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180305&ie=utf8'
        html = self.download(url)
        #首页数据的清洗
        data_list = json.loads((re.findall(r'g_page_config =(.*?)g_srp_loadCss', html, re.S)[0].strip())[:-1])['mods']['itemlist']['data']['auctions']
        #筛选出需要的数据
        self.getdata(data_list)

        #异步数据
        url2 = 'https://s.taobao.com/api?_ksTS=1520760735896_240&callback=jsonp241&ajax=true&m=customized&stats_click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180311&bcoffset=0&js=1&ie=utf8&rn=4ea860d275f6378bca26c789f2dfa222'
        html2 = self.download(url2)
        data_list2 = json.loads(re.findall(r'{.*}', html2)[0])['API.CustomizedApi']['itemlist']['auctions']
        self.getdata(data_list2)

        #翻页数据
        for i in range(1, 10):
            data_value = 44 * i
            t = time.time()
            ksTs = '%s_%s' % (int(t * 1000), str(t)[-3:])
            callback = 'jsonp%s' % (int(str(t)[-3:]) + 1)
            url = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}&callback={}&q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180311&ie=utf8&bcoffset=4&ntoffset=0&p4ppushleft=1%2C48&s=0'.format(
                data_value, ksTs, callback)
            # print(url)
            html = self.download(url)
            data_list = json.loads(re.findall(r'{.*}', html)[0])['mods']['itemlist']['data']['auctions']
            self.getdata(data_list)

        self.draw()
        self.save()

if __name__ == '__main__':
    spiderTaobao = SpiderTaobao()
    spiderTaobao.spider()