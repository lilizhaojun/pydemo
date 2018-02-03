'''
导出报告
'''
__author__ = 'lizhaojun'

import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('init by setup')

    def tearDown(self):
        print('this is the tearDown')

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


if __name__ == '__main__':
    # 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTest(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    # 生成测试报告
    print('testsRun:%s' % test_result.testsRun)
    print('failures:%s' % test_result.failures)
    print('errors:%s' % test_result.errors)
    print('skipped:%s' % test_result.skipped)
