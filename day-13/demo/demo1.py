def start():
    print("计算器已经启动！")

def devision(a,b):
    print(a/b)

def end():
    print("AC键关闭，电池扣了！")


try:
    start()
    devision(9,0)

except ZeroDivisionError as e:
    print("捕捉到了被除数不能为0异常！",e)
except Exception as e:
    print("我都能捕捉！",e)
finally: # finally代码块肯定会执行
    end()  # 重要资源关闭的代码
