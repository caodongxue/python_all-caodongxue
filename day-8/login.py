'''
    登陆系统：
        业务：
        输入用户名和密码，
        从db.txt文件中匹配是否存在该用户以及
        密码是否正确。若正确则登陆成功！。
        否则弹出友好提示信息！（用户名或密码错误，别瞎弄！）
'''
# 1.将所有数据行提取，存储到字典里（字典：缓冲区。便于快速的修改）
db={}
# 开始读取db.txt文件
f = open("db.txt","r+",encoding="utf-8")
data = f.readlines() # ["张三:root","李四:admin"]
for i in data:
    line = i.split(":") # ["张三","root"] # 通过：号将前后进行切割。
    db[line[0]] = line[1].replace("\n","") # 替换所有密码后面的\n改成""
# 2.开发
name = input("请输入您的用户名：")
password = input("请输入您的密码：")
'''
    1.先判断是否存在该用户名：
        若存在，继续匹配是否密码是否正确
            若密码正确：登陆成功。
            若错误，打印友好提示信息。
        若不存在,该用户不存在。
'''
if name in db:
    if password == db[name]:
        print("登陆成功！")
    else:
        print("密码输入错误！")
else:
    print("改用户不存在！")




'''
    注册：
        输入用户名（非空），密码（非空）。
        之后存到db,然后将db写入db.txt（用户:密码）
'''
