'''
   方法：函数
   def   方法名():
       方法体
    好处：一本万利。写一次，能多次使用
'''


def sum(a,b):   # 申明一个方法，能接受两个数，并对接受的数据进行求和，然后使用return 进行返回
    print("已成功登录火星")
    c=a+b
    print('任务完成，准备返回地球')
    return c

print('准备登陆火星...')
s=sum(1,2)    # 调用sum方法，实现1,2的求和
s=sum(56,71)    # 调用sum方法，实现56,71的求和
s=sum(3,4)

print('返回成功！')
print(s)
# 写一个方法，打印任何传入的数据
def printstr(msg):
    print(msg)

printstr('hello,返回成功')
printstr('吃饭了！')