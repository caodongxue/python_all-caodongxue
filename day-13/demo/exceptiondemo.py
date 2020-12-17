def devide(a,b):
    if b == 0:
        raise IndexError("被除数不能为0！")
    else:
        print(a/b)   # ZeroDevisionError

try:
    devide(6,0)

except ZeroDivisionError as e:
    print("我处理了第一个异常",e)  # 第一个异常的处理
except IndexError as e:
    print("我处理了第二个异常",e)   # 第二个异常的处理
except Exception as e:
    print("所有异常我都能捕捉！！",e)  # 我们捕捉所有异常