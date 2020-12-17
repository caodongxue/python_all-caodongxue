from bankexception.BException import BalanceException
class Bank:
    __balance = None

    def setBalance(self,balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance

    def takeOut(self):
        b = 3000
        self.__balance=int(input("请输入取款金额："))
        if self.__balance>b:
            raise BalanceException("余额不足！！！")
        else:
            print("取款成功！！！","现在余额为",b-self.getBalance(),"元！")









