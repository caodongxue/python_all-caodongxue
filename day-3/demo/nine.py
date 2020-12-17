'''
1x1=1
1x2=2   2x2=4
1x3=3   2x3=6   3x3=9
1x4=4   2x4=8   3x4=12  4x4=16
....
1x9=9   2x9=18  3x9=27  4x9=36  5x9=45  ........ 9x9=81
'''
# num = int(input("请输入您要的层数："))
# i = 1
# while i <= num:
#     print("第",i,"层",end="")
#     j = 1
#     while j <= i:
#         print(j,"x",i,"=",(j*i),"\t",end="") # end="" 不换行
#         j = j + 1
#     print() # 换行
#     i = i + 1

i=1
while i<=7:
    j=1
    while j<=7-i:
        print(' ',end='')
        j+=1
    k=1
    while k <= i:
        print('*'.center(2),end='')
        k+=1
    print()
    i+=1

#倒三角
'''
i=1
while i<=7:
    k = 1
    while k <= i:
        print(' ', end='')
        k += 1
    j = 1
    while j<=7-i:
        print('*'.center(2),end='')
        j+=1
    print()
    i+=1
'''
'''
i=int(input('请输入数字：'))
while True:
    if i==1:
        n = int(input("请输入您要的层数："))
        i = 1
        while i <= n:
            print("第", i, "层", end="")
            j = 1
            while j <= i:
                print(j, "x", i, "=", (j * i), "\t", end="")
                j = j + 1
            print()
            i = i + 1
        break
    elif i==2:
        m = int(input("请输入三角形的层数："))
        i = 1
        while i <= m:
            j = 1
            while j <= (m - i):
                print(" ", end="")
                j = j + 1
            k = 1
            while k <= i:
                print("* ", end="")
                k = k + 1
            i = i + 1
            print()
        break
    else:
        i=int(input('输入有误！请重新输入数字：'))
'''















