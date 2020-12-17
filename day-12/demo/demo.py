class Oldphone:
    phoneNumber = None
    voice = None

    def call(self,number):
        print(self.phoneNumber,"正在给",number,"打电话........")



class Newphone(Oldphone):
    place = None
    picture = None
    ps = None

    def call(self,number):
        super().call(number)
        print("归属地：",self.place,"图片：",self.picture,"备注：",self.ps)

phone = Newphone()
phone.phoneNumber = "16738478249"
phone.voice = "爱情买卖"
phone.place = "河北"
phone.picture = "小猪佩奇"
phone.ps = "旺财来电"
phone.call("16467248785")