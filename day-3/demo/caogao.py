
# a = int(input("请输入一个数字："))
# b = int(input("请输入一个数字："))
# c = int(input("请输入一个数字："))
# if a + b > c and a + c > b and b + c > a:
#     while True:
#         if a == b and b == c:
#             print("等边三角形！")
#             break
#         elif a == b or b == c or c == a:
#             print("等腰三角形！")
#             break
#         else:
#             print("普通三角形")
#             break
# else:
#     print("无法构成三角形")



i = 0
while i <= 2:
    password = 123456
    num = int(input("请输入密码："))
    if num != password:
       print("输入密码错误！")
    else:
        print("输入密码正确！")
        break
    i = i + 1

# num = int(input("请输入您要的层数："))
# i = 1
# while i <= num:
#     print("第",i,"层",end="")
#     j = 1
#     while j <= i:
#         print(j,"x",i,"=",(j*i),"\t",end="")
#         j = j + 1
#     print()
#     i = i + 1


# 九九乘法表倒序
# i = 9
# while i >= 1:
#     print("第",i,"层",end="")
#     j = 1
#     while j <= i:
#         print(j,"x",i,"=",(j*i),"\t",end="")
#         j = j + 1
#     print()
#     i = i - 1

# i = 0
# while i <= 2:
#     password = 123456
#     num = int(input("请输入密码："))
#     if num != password:
#        print("输入密码错误！")
#     else:
#         print("输入密码正确！")
#         break
#     i = i + 1
# else:
#     print("密码被冻结！")

# A=56
# B=78
# A=A+B
# B=A-B
# A=A-B
# print(A,B)

# num = int(input("请输入您要的层数："))
# i = 1
# while i <= num:
#     print("第",i,"层",end="")
#     j = 1
#     while j <= i:
#         print(j,"x",i,"=",(j*i),"\t",end="") # end="" 不换行
#         j = j + 1
#     print() # 换行
#     i = i + 1






# ......*
# .....* *
# ....* * *
# ...* * * *
# ..* * * * *
# .* * * * * *
# * * * * * * *

# print("* ".center(6))
# print("* * ".center(5))
#
# i=1
# while i<=7:
#     j=1
#     while j<=7-i:
#         print(' ',end='')
#         j+=1
#     k=1
#     while k<=i:
#         print('*'.center(2),end='')
#         k+=1
#     print()
#     i+=1

# high=20  #井高
# up=3  #向上
# down=2  #下滑
# day=0  #天数
# climb=0  #爬的高度
# while True :
#     day=day+1
#     climb=climb+3
#     if climb>=high:
#         print("小青蛙出来了，用了",day,"天！")
#         break
#     climb=climb-2

#为什么要用while True来定义？？？
#因为while True是死循环，没有break就一直循环


# sum=1
# x=0
# for i in range(1,21):
#     sum=sum*i
#     x+=sum
# print(x)

# m=0
# for j in range(1,21):
#     num = 1
#     for i in range(1, j + 1):
#         num = num * i
#     m=m+num
# print(m)
'''
for i in range(1,11):
      a=int(input('请输入数字：'))
      print(a)
'''















