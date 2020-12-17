import datetime
from bank.tools import tools# 从bank文件导入tools类

class User:
    '''
    账号（int）、姓名(Str)、密码(6位数字)、地址、存款余额(double)
    、注册时间(date)、开户行（银行的名称（String））
    '''
    __account = None # 系统自动产生，不需要提供set方法，可以提供get方法
    __username = None
    __password = None
    __address = None
    __money = None
    __reg_date = None # 不需要提供set方法，可以提供get方法
    __bankname = None # 不需要提供set方法，提供get方法，应该去银行那边取数据

    def __init__(self,username,password,address,money):
        self.__username = username
        self.__password = password
        self.__address = address
        self.__money = money
        self.__account = tools().getRandom() # 从tools类里获取随机码
        self.__bankname = "中国工商银行昌平支行"
        self.__reg_date = datetime()

    def getAccount(self):
        return self.__account
    def setUsername(self,username):
        if len(tools.bank) >= 100:
            return 3
        elif username in tools.bank:
            return 2
        else:
             self.__username = username
        return 1
    def getUsername(self):
        return self.__username
    def setPassword(self,password):
        self.__password = password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money
    def getReg_Data(self):
        return self.__reg_date
    def getBankname(self):
        return self.__bankname






def  addUser():
    username = tools.inputHelp("用户名")
    password = tools.inputHelp("密码")
    country = tools.inputHelp("居住地址：1.国家：")
    province =  tools.inputHelp("省份")
    street = tools.inputHelp("街道")
    door = tools.inputHelp("门牌号")
    money =  tools.inputHelp("银行卡余额","int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = User(username,password,country,province,street,door,money)
    # 判断1   2   3
    if status == 1:
        user = tools.bank[username]
        print("恭喜开户成功！以下是您的开户信息：")
        print(tools.myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")
























