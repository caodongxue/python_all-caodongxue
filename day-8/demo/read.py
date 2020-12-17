g=open('1998.jpg', 'rb')# 读取
j=open('1997.jpg','wb')# 写入

# 读取一个图片
p=g.read()
# 将读取数据写入到另一个文件中
j.write(p)
# 关闭读取和写入资源
g.close()
j.close()





