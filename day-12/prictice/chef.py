class Chef:
    __name = None
    __age = None

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def steamRice(self):
        print("先放水再放米")

class Xchef(Chef):

    def aFriedDish(self):
        print("先放油再放菜")

class Xxchef(Xchef):
    def steamRice(self):
        super().steamRice()


    def aFriedDish(self):
        super().aFriedDish()


x=Xxchef("曹东雪",18)
print(x.getName(),x.getAge())
x.steamRice()
x.aFriedDish()

