import unittest

from prictice.bank import bank_selectUser
from prictice.bank import bank

class TestInquire(unittest.TestCase):
    def testQuire(self):
        account = "dmin"
        password = "dmin"
        result = "该用户不存在！"
        u = bank_selectUser(account,password)

        self.assertEqual(result,u)


    def testQuire1(self):
        account = "admin"
        password = "dmin"
        result = "用户密码错误!"
        u = bank_selectUser(account,password)

        self.assertEqual(result,u)


    def testQuire2(self):
        account = "admin"
        password = "admin"
        result = bank["张三"]
        u = bank_selectUser(account,password)

        self.assertEqual(result,u)







