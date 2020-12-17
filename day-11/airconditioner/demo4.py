
class Student:
    __num = None
    __name = None
    __age = None
    __sex = None
    __hight = None
    __weight = None
    __grade = None
    __address = None
    __phone_code = None

    def __init__(self,num,name,age,sex,hight,weight,grade,address,phone_code):
        self.__num = num
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__hight = hight
        self.__weight = weight
        self.__grade = grade
        self.__address = address
        self.__phone_code = phone_code

    def setNum(self,num):
        self.__num = num
    def getNum(self):
        return self.__num

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def setHight(self,hight):
        self.__hight = hight
    def getHight(self):
        return self.__hight

    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setGrade(self,grade):
        self.__grade =  grade
    def getGrade (self):
        return self.__grade

    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address

    def setPhone_Code(self,phone_code):
        self.__phone_code = phone_code
    def getPhone_Code(self):
        return self.__phone_code

    def learn(self,time):
        print("我学习了",time,"个小时了！")

    def playGames(self,games_name):
        print("我在玩",games_name)

    def programme(self,lines):
        print("我写了",lines,"行代码！")

    def summation(self,*args):
        sum=0
        for i in args:
            sum+=i
        return sum


class Car:
    __type = None
    __wheels = None
    __color = None
    __weight = None
    __storage = None

    def __init__(self,type,wheels,color,weight,storage):
        self.__type = type
        self.__wheels = wheels
        self.__color = color
        self.__weight = weight
        self.__storage = storage

    def setType(self,type):
        self.__type = type
    def getType(self):
        return self.__type

    def setWheels(self,wheels):
        self.__wheels = wheels
    def getWheels(self):
        return self.__wheels

    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setStorage(self,storage):
        self.__storage = storage
    def getStorage(self):
        return self.__storage

p=Car("宝马",4,"白色","40kg",60)
x=Car("法拉利",4,"红色","20kg",50)
l=Car("铃木",4,"咖色","20kg",50)
h=Car("五菱",4,"黑色","20kg",50)
v=Car("拖拉机",6,"蓝色","20kg",50)
print("车的型号是",p.getType(),"有",p.getWheels(),"个轮胎，颜色是",p.getColor(),"重达",p.getWeight(),"容积是",p.getStorage())
print("车的型号是",x.getType(),"有",x.getWheels(),"个轮胎，颜色是",x.getColor(),"重达",x.getWeight(),"容积是",x.getStorage())
print("车的型号是",l.getType(),"有",l.getWheels(),"个轮胎，颜色是",l.getColor(),"重达",l.getWeight(),"容积是",l.getStorage())
print("车的型号是",h.getType(),"有",h.getWheels(),"个轮胎，颜色是",h.getColor(),"重达",h.getWeight(),"容积是",h.getStorage())
print("车的型号是",v.getType(),"有",v.getWheels(),"个轮胎，颜色是",v.getColor(),"重达",v.getWeight(),"容积是",v.getStorage())

# 笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公

class Notebook:
    __type = None

