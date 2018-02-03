'''
pyunit框架的使用
'''
import unittest

import requests


class TestStringMethds(unittest.TestCase):

    def setUp(self):
        """
        测试案例执行前准备
        :return: 
        """
        print('fixture setup')

    def tearDown(self):
        """
        测试案例执行后
        :return: 
        """
        print('fixture Down')

    def test_upper(self):
        """
        测试用例
        :return: 
        """
        self.assertEqual('abc'.upper(), 'ABC')

    def test_isupper(self):
        """
        测试大小写是否异常
        :return: 
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('sIjjjj'.isupper())

    def test_split(self):
        """
        测试hello world
        :return: 
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_baidu_api(self):
        """
        baidu接口测试
        :return: 
        """
        url='http://www.baidu.com'
        res=requests.get(url)
        self.assertEqual(res.status_code,200)



if __name__ == '__main__':
    unittest.main
