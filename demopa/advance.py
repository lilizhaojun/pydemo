'''
进阶部分知识
'''
from time import sleep

import requests

from mypack import mymodule


def while_for():
    """
    监控程序
    :return: 
    """
    while True:
        res = requests.get('http://www.baidu.com')
        print(res.status_code)
        sleep(1)


def for_demo():
    """
    for循环
    :return: 
    """
    name_list = 'lizhaojun'

    print('序列索引迭代')
    for name in name_list:
        print(name)

    print('序列项迭代')
    for index in range(len(name_list)):
        print(name_list[index])


def exception_demo():
    """
    异常捕捉
    :return: 
    """
    while True:
        try:
            print('run this try')
            a = 4
            b = a / 0
            c = 2
            print(c)
        except BaseException as e:
            print('run in except')
            print(e)
        finally:
            print('finally')
        sleep(1)


def fun_demo_0():
    """
    返回0个值
    :return: 
    """
    print('返回0个值')


def fun_demo_1():
    """
    返回一个值
    :return: 
    """
    print('返回一个值')
    return 1


def fun_demo_more():
    """
    返回多个值
    :return: 
    """
    print('返回多个值')
    return 1, 2, 4


def parameter_default_demo(a=100):
    """
    默认参数
    :param a: 
    :return: 
    """
    print('a=%s' % a)


def parameter_default_demo1():
    """
    默认参数无参数
    :return: 
    """
    print('默认')


def parameter_args_demo(*args):
    """
    单星号传值
    :param args: 
    :return: 
    """
    print('*args')
    for name in args:
        print(name)


def parameter_kwargs_demo(**kwargs):
    """
    双星号传值
    :param kwargs: 
    :return: 
    """
    print('**kwargs')
    name = kwargs.get('name', None)
    value = kwargs.get('age', None)
    print('name is %s,age is %s' % (name, value))


def parameter_use_arg_demo():
    """
    使用星号传值
    :return: 
    """
    mytuple = (1, 2, 3, 4, 5)
    parameter_args_demo(*mytuple)  # 正确的调用方法
    parameter_args_demo(mytuple)  # 错误的调用方法

    mydic = {'name': 'lili', 'age': '20'}
    '''mydic2={
        'A':{
        'name':'jiji','age':'23'},
        'B':{
            'name':'okok','age':'22'}
        }'''
    parameter_kwargs_demo(**mydic)


def module_demo():
    """
    调用包
    :return: 
    """
    print(mymodule.author)


if __name__ == '__main__':
    # while_for()
    # for_demo()
    # exception_demo()
    # print(fun_demo_0())
    # print(fun_demo_1())
    # print(fun_demo_more())
    # parameter_default_demo(200)
    # parameter_use_arg_demo()
    module_demo()
