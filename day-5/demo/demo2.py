# a = [2,5,4,3,6]
# sum = 0
#
# for i in a: # 不携带角标
#     sum += i # sum +=   i    a +=  n     a =  a + n
# print(sum)
'''
    列表：[]
    常用的api:
        len() 求长度
        append() 可以向列表最后一位添加一条数据
        remove（） 删除一个数
        pop
        切片：
        枚举：列举出每一种可能出现的情况。enumerate()  index,value


'''

import  random
names = ["刘日成","张佳伟","李晗聪","李晓帅","陆佳琪","刘营营","曹东雪","何登勇","张岩","洪晓雅"]
# 切片：[start:end]  ,start  ~  end - 1

print(names[0:3:2])

names.append("贾生")
names.remove("张佳伟")
num =  int(random.random() * len(names))
name = names[num]
print("恭喜你，",name,"被点名！")
print(names)
