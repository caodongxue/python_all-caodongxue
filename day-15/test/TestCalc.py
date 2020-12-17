import unittest
from  testdemocalc.Calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    [2,4,6],
    [3,-2,1],
    [-8,4,-4],
    [23,45,68]
]

@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,q,w,e):
        a = q
        b = w
        y = e
        u = Calc()
        sum = u.add(a,b)
        self.assertEqual(y,sum)



data2=[
    [4,3,1],
    [-2,-3,1],
    [-5,4,-9],
    [3,-4,7],
    [89,45,44]
]
@ddt
class TestCalcSub(unittest.TestCase):
    @data(*data2)
    @unpack
    def testSub(self,q,w,e):
        a = q
        b = w
        y = e
        u = Calc()
        sum = u.sub(a,b)
        self.assertEqual(y,sum)


data3=[
    [2,3,6],
    [4,-5,-20],
    [-6,7,-42],
    [-8,-9,72],
    [100,100,10000]
]
@ddt
class TestCalcMul(unittest.TestCase):
    @data(*data3)
    @unpack
    def testMul(self,q,w,e):
        a = q
        b = w
        y = e
        u = Calc()
        sum = u.mul(a, b)
        self.assertEqual(y, sum)


data4 = [
    [4,2,2],
    [-8,4,-2],
    [64,-2,-32],
    [-6,-3,2]
]
@ddt
class TestCalcDiv(unittest.TestCase):
    @data(*data4)
    @unpack
    def testDiv(self,q,w,e):
        a = q
        b = w
        y = e
        u = Calc()
        sum = u.div(a, b)
        self.assertEqual(y, sum)









