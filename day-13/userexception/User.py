from userexception.UException import UserException
class User:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    # 比较方法
    def compare(self,n):  #self代表本身，n代表比较的对象
        if self.__name == n.getName() and self.__age == n.getAge():
            print("是同一个人！")
        else:
            raise UserException("用户信息不匹配")


