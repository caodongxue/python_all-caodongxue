import time

class Animal(object):
    __color = ""
    __weight = ""
    __age = None

    def __init__(self,color,weight,age):
        self.__age = age
        self.__color = color
        self.__weight = weight

    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

class Dog(Animal):
    __brand = ""

    def __init__(self,color,age,weight,brand):
        super().__init__(color,age,weight)
        self.__brand = brand

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def show(self):
        for i in range(3):
            print("汪~",end="")
            time.sleep(1)
        print()
        print("我是",self.getColor(),"的狗，我的最高寿命",self.getAge(),
              "我的体重",self.getWeight(),"我属于",self.getBrand())

class Cat(Animal):
    __brand = ""

    def __init__(self,color,age,weight,brand):
        super().__init__(color,age,weight)
        self.__brand = brand
    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def show(self):
        for i in range(3):
            print("喵~",end="")
            time.sleep(1)
        print()
        print("我是",self.getColor(),"的猫，我的最高寿命",self.getAge(),
              "我的体重",self.getWeight(),"我属于",self.getBrand())

c=Cat("灰色",2,15,"猫科")
c.show()
d=Dog("黄色",5,10,"犬科")
d.show()
