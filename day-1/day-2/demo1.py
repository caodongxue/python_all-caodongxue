'''

    变量：变化的量
        可以变化存储数据的量：变量
    python中这些变量随意定义？
    python规则：(法律，一旦违反，直接报错)
        1. 可以使用a~z ,A~Z : 52
        2. 0~9 : 10个数字
        3. _
        总共：63
    python命名规范：（道德，虽然违反，但不犯法。）
        1.数字不能开头
        2.不能使用python中的关键字:help("keywords")35个关键字
        3.python 3虽然提供中文命名法，但是禁止使用。
'''
# help("keywords")  --> 查询又多少关键字
'''
变量 = 6
print(变量)

T_T = 8
print(T_T)
'''
nume=input("请输入姓名")
id=int(input("请输入身份证号"))
year=int(input("请输入年龄"))
gender=input("请输入性别")
stature=int(input("请输入身高"))
weight=int(input("请输入体重"))
print(nume,id,year,gender,stature,weight)
if year> 18:
    print("可以看电影")
else:
    year< 18
    print("年龄不符合")