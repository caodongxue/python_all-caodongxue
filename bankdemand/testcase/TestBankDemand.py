import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from entity.bank import bank_selectUser
from utils.DataRead import DataRead

data1 = DataRead("database",database="bankdemand",tablename="demand",user="root",password="").list

@ddt
class TestBankDemand(unittest.TestCase):
    @data(*data1)
    @unpack
    def testDemand(self,account,password,result):
        re=bank_selectUser(account,password)

        self.assertEqual(str(re),result)









