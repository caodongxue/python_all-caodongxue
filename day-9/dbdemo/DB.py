
import xlrd
import pymysql
data=xlrd.open_workbook("D:\\测试开发技术\\a.xlsx")
sheet=data.sheet_by_name("用户管理")
rows=sheet.nrows  # 获取所有行数
cols=sheet.ncols  #获取所有列

con = pymysql.connect(host="localhost",user="root",password="",database="db",charset="utf8")
cursor=con.cursor()#获取游标
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(str(sheet.cell_value(i,j)).replace(".0",""))
    string=",".join(a)
sql="insert into person values([string])".format(string=string)
s=cursor.execute(sql)
print(s)
con.commit()
cursor.close()
con.close()
'''
# 0~100质数
num=[]
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)


# 0~100斐波那契数列
f1 = 0
f2 = 1
fn = 1
print(0)
while fn < 100:
    print(f2)
    fn = f2 + f1
    f1,f2 = f2,fn
'''






