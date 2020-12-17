import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from entity.Calc import Calc
from utils.DataRead import DataRead
# 数据源
data1 = DataRead("database",database="calc",tablename="num",user="root",password="").list
# data2 = DataRead("excel",filename="D:\\Users\\PycharmProjects\\day-16\\testcase
#                                       \\asdf.xlsx",sheetname="0").list

@ddt
class TestCalc(unittest.TestCase):
    @data(*data1)# @data(*data2)
    @unpack
    def testAdd(self,a,b,c):
        ca = Calc()
        s = ca.add(a,b)
        self.assertEqual(s,c)

