'''
组织测试方式
'''
import unittest


class Widget(object):
    def __init__(self, name):
        self.name = name
        self.width = 50
        self.height = 40

    def size(self):
        """
        计算面积
        :return: 
        """
        return self.height * self.width

    def resize(self, width, height):
        """
        重新调整大小
        :param width: 
        :param height: 
        :return: 
        """
        self.width = width
        self.height = height
        return self.width * self.height

    def dispose(self):
        """
        :return: 
        """
        print('dispose the width')


class SimpleWidgeTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The Widget')

    def tearDown(self):
        self.widget.dispose()

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), 2000, 'incorrect default size')

    def test_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), 15000, 'wrong size after resize')

    @unittest.skip('用于skip装饰器的示例')
    def test_skip(self):
        self.assertTrue(True)


def suit():
    """
    组织测试套件
    :return: 
    """
    suite = unittest.TestSuite()
    suite.addTest(SimpleWidgeTestCase('test_default_widget_size'))
    suite.addTest(SimpleWidgeTestCase('test_resize'))
    return suite


if __name__ == '__main__':
    test_suit = suit()
    result = unittest.TextTestRunner(verbosity=2).run(test_suit)
