'''
    方法：函数
    好处：一本万利，一次书写，处处使用。
    def  【方法名】(参数列表):
        方法体
        [return]
    方法名：  多个单词组成，第二个单词开始，首字母就要大写。 totalStudentNumber : 驼峰式命名法
    参数列表：
        1.单值传输
        2.*args:元组：能不定数量的接受参数
        3.**kwargs:字典
        4.注意：3个参数列表的为位置是禁止调换。
'''

# 就用方法来打印1~100以内的数据：(方法的递归(循环)调用)
'''
i = 1

def  printNum(i):
    if i <= 100:
        print(i)
        i = i + 1
        printNum(i)

printNum(i)

def getSum(a,b):
    c=a+b
    print(c)
getSum(2,9)
'''
def showInfo(name,age,*args,**kwargs):
    print(age,'-----',name)
    for i in args:
       print(i)
    keys=list(kwargs.keys())
    for key in keys:
        print(key,':',kwargs.get(key))

showInfo('曹东雪','24','女','160','45kg',telephon=15097321703,address='河北省邯郸市邯山区')
























