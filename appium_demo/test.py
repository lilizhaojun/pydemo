#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 15:44
# @Author  : lizhaojun
# @File    : test.py
'''
在虚拟机上执行appium举例
'''
from appium import webdriver
from time import sleep

#apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径(真机时使用）

desired_caps ={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Nexus6'
desired_caps['appPackage'] = 'com.android.dialer'
desired_caps['appActivity'] = '.DialtactsActivity'

#启用app
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.android.dialer:id/floating_action_button').click()
sleep(5)

driver.find_element_by_name('1').click()
driver.find_element_by_name('0').click()
driver.find_element_by_name('0').click()
driver.find_element_by_name('8').click()
driver.find_element_by_name('6').click()
print('拨号完成')

driver.find_element_by_id('com.android.dialer:id/dialpad_floating_action_button').click()
print('呼出')

print("PASS")
driver.quit()

