from personexception.PException import AgeException
class Person:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        if age<=0:
            raise AgeException("数据非法！！！")
        else:
            self.__age = age
    def getAge(self):
        return self.__age


