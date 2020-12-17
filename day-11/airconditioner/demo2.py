class Student:
    __name = None
    __age = None

    def __init__(self,n,a):
        self.__name = n
        self.__age = a

    def setName(self,n):
        self.__name = n
    def getName(self):
        return self.__name

    def setAge(self,a):
        self.__age = a
    def getAge(self):
        return self.__age

    def introduce(self):
        print("大家好，我叫",d.getName(),"今年",d.getAge(),"岁了！")

    def compare(self):
        if d.getAge()>f.getAge():
            print("我比同桌大",d.getAge()-f.getAge(),"岁！")
        elif d.getAge()<f.getAge():
            print("我比同桌小",f.getAge()-d.getAge(),"岁！")
        else:
            print("我和同桌一样大")


d=Student("曹东雪",23)
f=Student("于锌",24)
d.introduce()
d.compare()


