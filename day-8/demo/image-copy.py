f = open("../景甜.jpg","rb")
w = open("D:/旺财.jpg","wb")

data =  f.read()
w.write(data)

f.close()
w.close()
