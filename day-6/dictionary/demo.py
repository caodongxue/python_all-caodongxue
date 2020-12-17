'''
   字典：其实就是键值对的存储关系
   a={
      key1:value1
      key2:value2
      ......        
   }
''' ,
'''  
   a=dict({})
   特性：
       不允许存储重复的键。
   常用api：
       get(key)  获取值
       clear()  清空所有集合
       keys()  获取所有键
       values()  获取所有值
'''
a = {
    "北京":"昌平",
    "上海":"浦东",
    "天津":"滨海新区"
}

# 1遍历
keys = list(a.keys())

for key in keys:
    print(key ,"=",a.get(key))

# 2

values = list(a.values())
for index,key in enumerate(keys):
    print(keys[index],"=",values[index])



