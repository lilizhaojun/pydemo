#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 12:15
# @Author  : lizhaojun
# @File    : test_demo.py
'''
在widonws上可正常执行
'''
from uiautomator import Device
import time

d = Device('M92QADPJEYVHR')

def test_login(mobile,pas):
    """
    登录flyme账号
    :param mobile:
    :param pas:
    :return:
    """
    try:
        d(text='手机号/Flyme 账号').set_text(mobile)
        d(resourceId='com.meizu.account:id/edtPwd').set_text(pas)
        d(resourceId='com.meizu.account:id/btnLogin').click()
        time.sleep(5)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_login('13572400439','lzj13572400439')

