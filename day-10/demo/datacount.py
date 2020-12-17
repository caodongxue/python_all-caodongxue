f=open("baidu_x_system.log","r+",encoding="utf-8")
dic = {}  # {ip:次数}
lines = f.readlines()
for line in lines:
    ip = line.split(" ")[0]
    if ip in dic:
        dic[ip] = dic[ip]+1
    else:
        dic[ip]= 1
print(dic)







