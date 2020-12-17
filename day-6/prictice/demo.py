# 笔试的高频率题目
# 给一个字符串：'hello world'，求每个字符出现次数。
# 写一个冒泡排序，选择排序

# 统计字符出现的次数

'''
string=('this is a dog,that is a monky!')
li=list(string)        # 将字符转换成列表
for i in range(0,len(li)):
    count=0       # 计数器
    # 排重
    flag=True       # 开关置位开
    for k in range(0,i):
        if li[k]==li[i]:
            flag=False      # 一旦发现相同字符，开关置位关闭
            break

    if flag==False:        # 判断开关是否是关闭状态，便于判断是否发现是否统计过
        continue         # 中止循环，继续下一轮循环
    # 统计
    for j in range(0,len(li)):
        if li[i]==li[j]:
            count += 1
    print(li[i],'出现了',count,'次！')

'''



# 选择排序
'''
a = [1,5,21,30,15,9,30,24]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            a[j],a[i]=a[i],a[j]
print(a)
'''

# 冒泡排序
'''
a = [1,5,21,30,15,9,30,24]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
'''

'''
list = [1,2,3,4,5,6,7,8,9]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[j]>list[i]:
            list[j],list[i]=list[i],list[j]
print(list)
'''

list = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]

for index,a in enumerate(list):
    if a in list[:index]:
        continue
    print(a,'出现了',list.count(a),'次')

'''
d={}
for i in list:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

'''
'''
def num(a,b):
    c=a+b
    return (c)

c=num(4,6)
print(c)
'''
'''
def showinfo(name,age,*args ):
    print(name,'-------',age)
    print(args)


showinfo('刘莹莹',23,'女',3454,'4235676432')
'''
# 
# def showinfo(name,age,*args ):
#     print(name,'-------',age)
#     for i in args:
#         print(i)
#
# showinfo('刘莹莹',23,'女',3454,'4235676432')


# def num(*args):
#     for i in args:
#         c=num[i]+num[i+1]
#         return c
#
# num(2,4,5,6,7,2,3)





