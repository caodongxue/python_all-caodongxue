# 1.将所有数据行提取，存储到字典里（字典：缓冲区。便于快速的修改）
db={}
# 开始读取db.txt文件
f = open("db.txt","r+",encoding="utf-8")
data = f.readlines() # ["张三:root","李四:admin"]
for i in data:
    line = i.split(":") # ["张三","root"] # 通过：号将前后进行切割。
    db[line[0]] = line[1].replace("\n","") # 替换所有密码后面的\n改成""
f.close()
'''
    注册：
        输入用户名（非空），密码（非空）。
        之后存到db,然后将db写入db.txt（用户:密码）
'''
while True:
    name = input("请输入用户名：").strip() # strip()代表请输入用户名非空
    password = input("请输入密码：").strip()  # strip()代表请输入密码非空
    if len(name) != 0 and len(password) != 0:
        if name in db:
            print("该用户已经存在！")
        else:
            # 正常注册
            db[name] = password   # 将用户名和密码存入到db字典里
            break
    else:
        print("输入不能为空！")
# 更新db 到db.txt
# 1.遍历db
w = open("db.txt","w+",encoding="utf-8")
for key in db:
    w.write("{name}:{password}\n".format(name=key,password=db[key]))
w.close()
















'''

db={}
f=open('db.txt','r+',encoding='utf_8')
data=f.readlines()
for i in data:
    line=i.split(':')
    db[line[0]]=line[1].replace('\n','')
f.close()
while True:
    name=input('请输入用户名：').strip()
    password=input('请输入用户密码：').strip()
    if len(name) !=0 and len(password) !=0:
        if name in db:
            print('用户已存在！！！')
        else:
            db[name]=password
            break
    else:
        print('输入不能为空！！！')

w=open('db.txt','w+',encoding='utf-8')
for key in db:
    w.write("{name}:{password}\n".format(name=key,password=db[key]))
w.close()


'''






