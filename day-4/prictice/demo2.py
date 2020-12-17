'''
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(j, "x", i, "=", (i * j), "\t", end="")
    print()
'''
'''
name = "jason"
password = "138456"

for i in range(3):
    n = input("请输入用户名：")
    p = input("请输入密码：")
    if n == name and p == password:
        print("恭喜，登陆成功！")
        break
    else:
        print("密码输入失败！")
        if i == 2:
            print("三次密码输入错误！系统已锁定，请在30分钟后重新登陆！")
            break
'''

'''
    for [变量]  in  range(100):  0~100

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",(i*j),"\t",end="")
    print()


# 打印1~10之间的跳数
for i in range(1,11,2):
    print(i)

'''
'''
 1~10相加的和:
 
sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)
'''





#for循环写九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,'=',(i*j),"\t",end='')
    print()

'''
#从1到10相加
'''
sum=0
for i in range(1,11):
    sum=sum+i
print('和:',sum)
'''
'''
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(j,'x',i,'=',(i*j),'\t',end='')
    print()
'''
'''
for i in range(1,10,+1):
    for j in range(1,i+1):
        print(j,'x',i,'=',(i*j),'\t',end="")
    print()
'''
# 1!=1              1
# 2!=1*2            2
# 3!=1*2*3          6
# 4!=1*2*3*4        24
#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# a=0
# for i in range(1,21):
#     num=1
#     for j in range(1,i+1):
#         num=num*j
#     a=a+num
# print(a)

'''
m=0
for j in range(1,21):
    num = 1
    for i in range(1, j + 1):
        num = num * i
    m=m+num
print(m)
'''
# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
max = 0
sum = 0
for i in range(10):
    num=int(input('请输入数据：'))
    if num > max:
        max=num
    sum=sum+num
print('最大值为：',max,'，和为：','平均数为：',(sum/10))










