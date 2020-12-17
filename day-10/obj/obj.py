'''
    类：class



'''
'''
# 模板的编写
class  car:
    num = 0
    color = ""
    brand = ""

    def run(self):
        print("在大马路上跑来跑去！溜了溜了！！！！")
# 造车
c = car() # 车造完了
# 给车加各种属性
c.num = 4
c.color = "宝色蓝"
c.brand = "BMW"
# 让车跑起来
c.run() # 跑起来
print("我的车有",c.num,"个轮胎，车身是",c.color,"颜色，总之我的车是",c.brand,"牌子的车！")
'''





class ren:
    skin_color = ""
    head = 0
    hair = ""
    arm = 0
    leg = 0
    def eat(self):
        print("饿了吃火锅！！！")

c=ren()

c.head = 1
c.hair = "黑色"
c.skin_color = "黄皮肤"
c.arm = 2
c.leg = 2
print("人类有",c.head,"个脑袋，",c.arm,"个胳膊，",c.leg,"条腿",c.hair,"的头发",c.skin_color)
c.eat()