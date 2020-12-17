'''
# 方法一
# 读取文件
f = open('scores.txt', 'r+', encoding='utf-8')
# 用readlines（）把每一行数据分开
lines=f.readlines()
# 关闭
f.close()
# 初始化
results=[]
# 对每一天数据进行处理，按照空格把姓名，每次分数分隔开
for line in lines:
    data=line.split()  # split（）表示将前后每一个数据按空格进行分割
    sum=0
    for score in data[1:]:
         sum+=int(score)
    result='%s:%d\n'%(data[0],sum)
    results.append(result)
output=open('result.txt','w+',encoding='utf-8')
output.writelines(results)
output.close()
'''


# 方法二
f= open("魔法学院成绩","r+",encoding="utf-8")
dic={}
lines=f.readlines()
f.close()
for line in lines:
    li=line.replace("\n","").split(" ")
    name=li[0]
    scores=li[1:]
    dic[name]= sum([int(i) for i in scores])
print(dic)


