#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 15:44
# @Author  : lizhaojun
# @File    : test_appium.py

from appium import webdriver
import time
import os
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#初始化
desired_caps = {}
#使用哪种移动平台
desired_caps['platforname'] = 'Android'
#版本
desired_caps['platforversion'] = '6.0.1'
#启用哪种设备
desired_caps['devicename'] = 'M92QADPJEYVHR'
#app绝对路径
desired_caps['app'] = PATH('E:\AutoCall_1.0_20171226_prd.apk')

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#使用unicodeKeyboard的编码方式来发送字符串
desired_caps['unicodeKeyboard']=True
#将键盘给隐藏起来
desired_caps['resetKeyboard']=True

driver.find_element_by_id('com.meizu.testdev.vcc:id/edit_number').send_keys('13572400439')

driver.find_element_by_id('com.meizu.testdev.vcc:id/edit_times').send_keys('100')