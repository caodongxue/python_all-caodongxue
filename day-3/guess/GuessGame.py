# auther: caodongxue
import random

# 1.让系统产生一个随机数
num = int(random.random()*1000)
count = 0 # 猜的计数器
while True:
    guess = int(input("请输入您要猜的数："))
    count = count + 1 #计数器加1
    if num > guess:
        print("小了！")
    elif num < guess:
        print("大了！")
    else:
        print("恭喜你，猜中了，您猜中的数字为",num,"您猜了",count,"次了！")
        break