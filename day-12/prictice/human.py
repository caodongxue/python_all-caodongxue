class Human:
    __age = None
    __sex = None
    __name = None

    def __init__(self,age,sex,name):
        self.__age = age
        self.__sex = sex
        self.__name = name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def _setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

class Worker(Human):

    def __init__(self,age,sex,name):
        super().__init__(age,sex,name)

    def work(self):
        print("我叫",self.getName(),self.getSex(), "，今年",self.getAge(), "岁!每天的工作就是搬砖")


w=Worker(23,"女","曹东雪")
w.work()

class Student(Human):
    __num = None
    def __init__(self,age,sex,name,num):
        super().__init__(age, sex, name)
        self.__num = num

    def learn(self):
        print("我叫",self.getName(),self.getSex(), "，今年",self.getAge(),"岁！学号是",self.__num, "每天的学习就是读书")

    def sing(self):
        print("我叫",self.getName(),self.getSex(), "，今年",self.getAge(),"岁！学号是",self.__num, "我每天都会唱歌")

s=Student(19,"女","刘莹莹",4)
s.learn()
s.sing()





