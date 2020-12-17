
'''
    1.类:(类名首字母必须大写，第二个单词开始首字母大写)
        属性
        行为（功能：方法、函数）
    2.对象
        c =  Car()
        句柄 = 类名()
    3.封装：
        3.1 将属性进行私有化
            将属性前面加上__
        3.2 提供方法间接赋值
    类对象：
        1.属性封装
        2.提供setxxxx/getxxx方法，用户进行属性的间接赋值
        3.提供有参构造函数

'''
class person:
    __username = ""
    __age = None
    def setUsername(self,u):
          self.__username = u

    def setAge(self,a):
        if a== None:
            print("年龄非法！")
        elif a > 120 or a < 0:
            print("年龄非法！")
        else:
             self.__age = a

    def show(self):
        print("我叫",self.__username,"，我的年龄为：",self.__age)

p=person()

p.setUsername("何登勇")
p.setAge(45)
p.show()


