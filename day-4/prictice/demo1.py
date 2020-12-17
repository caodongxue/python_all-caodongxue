A=56
B=78

# 1
'''
A = A + B    #A=134
B = A - B    # B = 56
A = A - B    # A = 78
print(A,B)


# 2
C = A
A = B
B = C
print(A,B)

# 3 ^ 异或
A = A ^ B
B = A ^ B
A = A ^ B

print(A,B)
'''
'''
bai = 3
wan = 2
h = 20
count = 0
high = 0

while True:
    count = count + 1
    high = high + bai
    if high >= h:
        break
    high = high - wan

print("第",count,"天能爬出来！")
'''
'''
# 打印等腰三角形
num = int(input("请输入三角形的层数："))
i = 1
while i <= num:
    j = 1
    while j <= (num-i):
        print(" ",end="")
        j = j + 1
    k = 1
    while k <= i:
        print("* ",end="")
        k =  k + 1
    i = i + 1
    print()
'''


'''
能三角形:(任意两边和大于第三边)  
    直角三角形：3 4 5 : 9 + 16 = 25
    等边三角形: 3 3 3 
    等腰三角形: 3 3 5
    普通三角形: 5 8 7
不能三角型
'''
a = int(input("请输入第一边："))
b = int(input("请输入第二边："))
c = int(input("请输入第三边："))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("等边三角形！")
    elif (a==b or b == c or a == c):
        print("等腰三角型！")
    elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("直角三角形！")
    else:
        print("普通三角形！")
else:
    print("不能形成三角形！")