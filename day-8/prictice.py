# 请编程写出一个登陆程序，从文件中校验用户名是否存在，若不存在则报错：不存在该用户，否则登陆成功!,若密码输入错误，打印密码输入错误！

nn = {}
f = open('nn.txt', 'r+', encoding='utf-8')
data = f.readlines()
for i in data:
    line = i.split(",")
    # nn[line[0]] = line[3].replace("\n", "")
    # nn[line[0]] = line[2]
    nn[line[0]] = line[1].replace("\n", "")
name = input("请输入您的用户名：")
password = input("请输入您的密码：")
# age=input('请输入您的年龄:')
# sex=input('请输入您的性别:')
if name in nn:
    if password == nn[name]:
        print("登陆成功！")
    else:
        print("密码输入错误！")
else:
    print("不存在该用户！")




















