'''
   自定义异常：
       1.继承异常体系中的父类
       2.重写__init__方法，传入msg异常信息

'''
class UserNotExistExeption(Exception):  # UserNotExistExeption:自定义异常

    def __init__(self,msg):
        self.msg = msg

raise UserNotExistExeption("用户信息不匹配！！")















