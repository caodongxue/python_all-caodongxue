import pymysql
'''
    1.获取数据库连接(host地址，user用户，password密码，database数据库，charset编码集)
    2.获取游标(所有sql语句等数据库的操作必须经过游标)
    3.书写sql 语句
    4.使用游标执行sql语句
        4.1 若做的是增删改，没有返回结果
        4.2 若做的是查询操作，有返回结果
    5.处理执行后的结果
    6.关闭游标
    7.关闭连接
'''


# 查询数据

# 1. 获取数据库 连接
con = pymysql.connect(host="localhost",user="root",password="",database="lttest",charset="utf8")

# 2.通过连接来获取游标
cursor = con.cursor()

# 3.书写sql
sql = "select * from  person"

# 4.通过游标执行sql语句
s = cursor.execute(sql)
print(s)

# 提取游标内的查询数据
one = cursor.fetchmany(6)
print(list(one))

# 4.1 提交刚才执行操作，提交给数据
con.commit()

# 5.关闭资源
cursor.close()
con.close()





