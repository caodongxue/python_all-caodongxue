# sum = 0
# for i in range(1,21):
#     sum1 = 1
#     for i in range(1,i+1):
#         sum1 = sum1 * i
#     sum = sum1 + sum
# print(sum)
'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。

max = 0
sum = 0

for i in range(10):
    num = int(input("请输入数据："))
    if num > max:
        max = num
    sum = sum +  num
print("最大值为：",max,"，和为：",sum,"平均数为：",(sum / 10))
'''





'''
for i in range(0,10):# 控制层走向
    for j in range(0,10-i):
        print(" ",end="")

    for k in  range(0,i+1): # range(0,5)
        print("* ",end="")

    print()
'''



a = 451050
b = 5643
# 任何数 % 10 ：取得最后一个数
print(a % 10)
print(a // 10)# 5643   564
