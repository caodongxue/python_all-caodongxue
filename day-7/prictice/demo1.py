li = [1, 4, 7, 5, 82, 1, 3, 4, 5, 9, 7, 6, 1, 10]


'''
for i in range(0,len(li)):
    count = 0 # 计数器
    # 排重
    flag = True # 开关置位开
    for k in range(0,i):
        if li[k] == li[i]:
            flag = False # 一旦发现相同字符，开关置位关闭
            break
    if flag == False: # 判断开关是否是关闭状态，便于判断是否发现是否统计过
        continue # 终止循环，继续下一轮循环
    # 统计
    for j in range(0,len(li)):
        if li[i] == li[j]:
            count += 1
    print(li[i],"出现了",count,"次！")

'''

# 2:
'''
for index,value in enumerate(li):
    if value in  li[:index]:
        continue
    print(value,"出现了",li.count(value))
'''

# 3.使用字典的方式来存：  key:value     数字：次数

d = {}
for i in li:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
