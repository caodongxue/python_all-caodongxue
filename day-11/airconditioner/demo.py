class Airconditioner:
    __brand = None
    __price = None


    def __init__(self,b,p):
        self.__brand=b
        self.__price=p


    def setBrand(self,b):
        self.__brand = b
    def getBrand(self):
        return self.__brand

    def setPrice(self,p):
        self.__price = p
    def getPrice(self):
        return self.__price

    def startingUp(self):
        print("空调开机了！")

    def shutDown(self,m):
        print("空调将在",m,"分钟后自动关闭")


a=Airconditioner("格力",5000)

print("此空调",a.getBrand(),"造，价格为",a.getPrice(),"一台")

a.startingUp()

a.shutDown(45)

