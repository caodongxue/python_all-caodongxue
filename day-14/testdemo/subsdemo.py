import unittest
from testdemo.cal import Calc

class TestCalc1(unittest.TestCase):

    def testSubs(self):
        a = 1
        b = 2
        sum = -1
        c = Calc()
        s = c.subs(a, b)

        # 断言
        self.assertEqual(sum, s)