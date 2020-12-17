# -*- codig:utf-8 -*-
# author:jason
# center，自动居中，空缺部分可以自定义进行补全
#  香蕉的数据
id1 = input("请输入商品编号：")
name1 = input("请输入商品名称：")
price1 = int(input("请输入商品价格："))
count1 = int(input("请输入商品的数量："))
quanlity1 = input("请输入商品的品质：")
#  苹果的数据
id2 = 2
name2 = "苹果"
price2 = 2.9
count2 = 1200
quanlity2 = "B+"
#  橘子的数据
id3 = 3
name3 = "橘子"
price3 = 6.1
count3 = 2500
quanlity3 = "A+"
print("欢迎来到Jason水果商城".center(70,"-"))
print("----".center(70,"-"))
print("编号           名称            单价           库存量            品质")
print("----".center(70,"-"))
print(id1,"              ",name1,"            ",price1,"            ",count1,"              ",quanlity1)
print(id2,"              ",name2,"            ",price2,"            ",count2,"              ",quanlity2)
print(id3,"              ",name3,"            ",price3,"            ",count3,"              ",quanlity3)
print("----".center(70,"-"))
print("本次消费总金额：",(price1 * count1 +  price2 * count2 + price3 * count3) , "￥")
