#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 10:40
# @Author  : lizhaojun
# @File    : draw.py
'''
使用matplotlib绘制饼图
'''
import numpy as np
import matplotlib.pyplot as plt

#设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def pie(data,image_name):
    """
    绘制饼状图
    :param data:
    :param image_name:
    :return:
    """
    fig = plt.figure(figsize=(8,8))
    cities = data.keys()
    values = [x for x in data.values()]
    print(values)

    ax1 = fig.add_subplot(111)
    ax1.set_title('饼图')

    labels = ['{}:{}'.format(city,value) for city,value in zip(cities,values)]

    #设置饼状的突出显示
    explode = [0,0.1]

    #画饼状图，指定标签和对应的颜色
    #指定阴影效果
    ax1.pie(values,labels=labels,explode=explode,shadow=True)

    plt.savefig('%s.png'% image_name)
    plt.show()

def bar(data,image_name):
    """
    绘制柱状图
    :param data:
    :param image_name:
    :return:
    """
    data_key = list(data.keys())
    data_value = list(data.values())
    plt.bar(range(len(data_value)),data_value,color='rgb',tick_label=data_key)

    plt.savefig('%s.png'% image_name)
    plt.show()

