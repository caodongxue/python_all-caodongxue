class Oldphone:
    __brand = None

    def __init__(self,brand):
        self.__brand = brand

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def call(self,string):
        print("正在给",string,"打电话")



class Newphone(Oldphone):
    def __init__(self,brand):
        super().__init__(brand)

    def call(self,string):
        super().call(string)
        print("语音拨号中......")

    def show(self):
        print("品牌为：",self.getBrand(),"的手机很好用！")

n=Newphone("三星")
n.call("曹东雪")
n.show()