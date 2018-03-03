#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 下午9:11
# @Author  : lizhaojun
# @Site    : 
# @File    : main.py
# @Software: PyCharm
'''
12306爬取买票
'''

import requests


def check():
    """
    查询余票
    :return: 
    """
    response = requests.get(
        'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-03-03&leftTicketDTO.from_station'
        '=CDW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT')
    result = response.json()
    return result['data']['result']

'''
3 = 车次
8 = 出发时间
9 = 到达时间
23 = 软卧
26 = 硬卧
28 = 硬座
29 = 无座
'''
j = 0
for i in check():
    tmp_list = i.split('|')
    '''for num in tmp_list:
        if tmp_list[3] != 'G574':
            break
        print(j,num)
        j += 1'''
    #以上来判断出各索引号代表的值
    if tmp_list[32] == '无' or tmp_list[32] == '':
        print(tmp_list[3],'该车次无软卧票')
    else:
        print(tmp_list[3],'该车次软卧票{}张'.format(tmp_list[32]))

