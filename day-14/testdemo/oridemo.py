'''
    单元测试框架：unittest
        使用这个框架能大大的提高测试效率，节省时间
        1.写一个测试类：继承unittest
            1.1 测试类命名规范：TestXxxx
        2.断言：期望值，和实际值穿进去

    测试集：
        能将所有的测试用例，先加载进测试集里，然后统一执行。
'''

import unittest
from testdemo.cal import Calc
class TestCal(unittest.TestCase):
    def testAdd(self):
        a = 1
        b = 2
        sum = 3
        c = Calc()
        s = c.add(a, b)

        # 断言
        self.assertEqual(sum, s)

    def testAdd1(self):
        a = -1
        b = -2
        sum = -3
        c = Calc()
        s = c.add(a,b)

        #断言
        self.assertEqual(sum,s)


