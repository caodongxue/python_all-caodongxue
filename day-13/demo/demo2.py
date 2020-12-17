def devision(a,b):
    try:
        print(a/b)                      # 3  3  除法正常处理
        return "除法正常处理！"           # 3 执行最终代码块！ 3
    except IndexError as e:             # 除法正常处理 3 执行最终代码块！ 3
        print("角标异常！")              #
        return 1
    except ZeroDivisionError as e:
        print("被除数不能为0异常！")
        return 2
    finally:
        print("执行最终代码块！")
        return 3

s = devision(9,3)
print(s)
'''
    被除数不能为0异常！执行最终代码块！
    被除数不能为0异常！被除数不能为0异常！
    被除数不能为0异常！执行最终代码块！2
    被除数不能为0异常！执行最终代码块！
'''