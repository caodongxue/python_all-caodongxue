from userexception.User import User
from userexception.UException import UserException

'''
    比较两个用户：
        若用户的年龄和姓名一样，则判断是同一个人
        否则，则抛出用户异常
'''

u=User()
u.setAge(23)
u.setName("曹东雪")

u1=User()
u1.setAge(23)
u1.setName("曹雪")
try:
    u.compare(u1)
except UserException as e:
    print(e)



