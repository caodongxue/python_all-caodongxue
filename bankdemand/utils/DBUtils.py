
# 读取数据库方法

import pymysql

class MysqlUtils:
    con = None
    cursor = None

    @classmethod
    def read(cls,host="localhost",database="calc",user="root",password="",tablename="num"):
        cls.con = pymysql.connect(host=host,user=user,password=password,database=database,charset="utf8")
        cls.cursor=cls.con.cursor()
        sql='''
            select * from {tablename}
        '''

        cls.cursor.execute(sql.format(tablename=tablename))
        return cls.cursor.fetchall()

# u=MysqlUtils.read()
# print(u)


