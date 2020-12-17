'''
  //: 保留整数部分
  /：带有小数部分
  int("3.6") --> 3
'''

# print(int("3.6"))
print(3 < 5)
name1 = input("请输入姓名：")
number1 = input("请输入身份证号：")
age1 = int(input("请输入年龄："))
sex1 = input("请输入性别：")
height1 = input("请输入身高：")
weight1 = input("请输入体重：")
print("姓名    身份证号          年龄      性别      身高       体重 ")
print("----".center(70, "-"))
print(name1, "", number1, "          ", age1, "      ", sex1, "     ", height1, "     ", weight1)
if age1 > 18:
    print("可以去看电影了")
else:
    print("年龄不符合")
