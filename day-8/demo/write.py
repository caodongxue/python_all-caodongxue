
# r=open('a.txt', 'w+', encoding='utf-8')
#
# r.write('鹅鹅鹅\n',)
# r.write('曲项向天歌\n',)
# r.write('白毛浮绿水\n',)
# r.write('红掌拨清波\n',)
#
# r.close()

'''
    1.写入到文件:a.txt
    2.写入的数据："万能的测试开发"
    文件操作模式：
        w:写，
        r:读
        +:可读可写
        a:只能写（可以在原来的基础上附加数据）
        b:字节读写。wb（写入字节：写入一个图片，mp3，mp4）
    读取：
        read()读取所有数据，弊端：直接加载所有数据，若数据太大，机器太卡
        readlines() : 读取所有行，并将每一行放入到列表
        readline():  单独读取一行。
'''

f = open("a.txt","r+",encoding="utf-8")

print(f.readline())
print(f.readline())
print(f.readline())

f.close()





'''
# 1.打开文件，并获取文件句柄（把柄）
f = open("a.txt","w",encoding="utf-8")

# 2. 写入数据

f.write("万能的测试开发！！！\n")  # 用到C语言底层资源
f.writelines("\t静夜思(李白)\n")
f.writelines("床前明月光，疑是地上霜。\n")
f.writelines("举头望明月，低头思故乡！\n")

# 3.关闭资源（）
f.close()
'''