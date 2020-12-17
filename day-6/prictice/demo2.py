
'''
string=('this is a dog,that is a monky!')
# 身份运算符 in     not in
print('is' in string[:12])# 判断is 是否在前面12个字符串里出现过

for i,j in enumerate(string): # 枚举每一个字符出现的角标  +  字符
    if j in string[:i]:  # 通过切片来判断是否之前是否出现过
        continue
    print(j,'出现了',string.count(j))# 通过count（）方法来统计全文出现次数
'''

    # 姓名    年龄 性别   编号 任职公司 薪资 部门编号
names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营","19","女","210","Oracle",600,"60"],
    ["李汉聪","45","男","230","Tencent",700 ,"10"]
]
#统计每个人的平均薪资
'''
m=0
i=0
for n in range(len(names)):
    m+=names[n][5]
    i=m/len(names)
print(i)
#统计每个人的平均年龄
m=0
i=0
for n in range(len(names)):
    m+=int(names[n][1])
    i=m/len(names)
print(i)
'''
'''
#公司新来一个员工，张佳伟，45，男，220，alibaba，500,30，添加到列表中
names.append(['张佳伟','45','男','220','alibaba',500,'30'])
print(names)
#统计公司男女人数
for i in range(0,len(names)):
    count=0
    flag=True
    for k in range(0,i):
        if names[k][2]==names[i][2]:
            flag=False
            break
    if flag==False:
        continue
    for j in range(0,len(names)):
        if names[i][2]==names[j][2]:
            count += 1
    print(names[i][2],'有',count,'人！')

#每个部门的人数
for i in range(0,len(names)):
    count=0
    flag=True
    for k in range(0,i):
        if names[k][6]==names[i][6]:
            flag=False
            break
    if flag==False:
        continue
    for j in range(0,len(names)):
        if names[i][6]==names[j][6]:
            count += 1
    print(names[i][6],'部门有',count,'人！')
'''

#
a=[
	[10, 14,  9,  15],
	[ 7,  4,  8,  10],
	[ 6,  8,  4,   9],
	[ 8, 51, 10,  23]
  ]
max = a[0][0]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i][j] >= max:
           max = a[i][j]
           continue



















