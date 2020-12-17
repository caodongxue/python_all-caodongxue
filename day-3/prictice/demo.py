name1=input("请输入姓名：")
number1=input("请输入身份证号：")
age1=input("请输入年龄：")
sex1=input("请输入性别：")
height1=input("请输入身高：")
weight1=input("请输入体重：")
#print("姓名    身份证号          年龄      性别      身高       体重 ")
# print("----".center(70,"-"))
# print(name1,"",number1,"          ",age1,"      ",sex1,"     ",height1,"     ",weight1)

info='''
[----体检登记表：----]
姓名：{name}
身份证号：{number}
年龄：{age}
性别：{sex}
身高：{height}
体重：{weight}
 ------------------
'''
print(info.format(
    name=name1,
    number=number1,
    age=age1,
    sex=sex1,
    height=height1,
    weight=weight1
))