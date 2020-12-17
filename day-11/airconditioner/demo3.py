class Human:
    __name = None
    __sex = None
    __age = None
    __remaining_money = None
    __brand = None
    __battery_capacity = None
    __size = None
    __duration = None
    __integral = None

    def __init__(self,name,sex,age,remaining_money,brand,battery_capacity,size,duration,integral):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__remaining_money = remaining_money
        self.__brand = brand
        self.__battery_capacity = battery_capacity
        self.__size = size
        self.__duration = duration
        self.__integral = integral

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setRemaining_money(self,remaining_money):
        self.__remaining_money = remaining_money
    def getRemaining_money(self):
        return self.__remaining_money

    def setBrand(self,brand):
        self.__name = brand
    def getBrand(self):
        return self.__brand

    def setBattery_capacity(self,battery_capacity):
        self.__battery_capacity = battery_capacity
    def getBattery_capacity(self):
        return self.__battery_capacity

    def setSize(self,size):
        self.__size = size
    def getSize(self):
        return self.__size

    def setDuration(self,duration):
        self.__duration = duration
    def getDuration(self):
        return self.__duration

    def setIntegral(self,integral):
        self.__integral = integral
    def getIntegral(self):
        return self.__integral

    def messages(self):
        print("我叫",y.__name,y.__sex,y.__age,"岁了","我的手机剩余话费有",y.__remaining_money,
              "元！，手机品牌是",y.__brand,"电池容量是",y.__battery_capacity,"屏幕大小为",y.__size,"英寸",
              "待机时长",y.__duration,"小时，剩余积分为",y.__integral)

    def Phone(self):
        h=input("请输入电话号码：")
        c=int(input("请输入通话时长："))
        if len(h)==0:
            print("电话号码不能为空！")
        elif y.__remaining_money < 1:
            print("话费不足，请及时充值！")
        else:
            if 10>=c>0:
                y.__remaining_money-=c*1
                y.__integral+=c*15
                print(y.messages())
            elif 10>c>=20:
                y.__remaining_money-=c*0.8
                y.__integral+=c*39
                print(y.messages())
            else:
                y.__remaining_money-=c*0.65
                y.__integral+=c*48
                print(y.messages())




y=Human("曹东雪","女",18,130,"苹果8","1821mah",4.7,24,367)
y.messages()
y.Phone()
