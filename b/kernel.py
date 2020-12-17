import time
from admin import Admin
from atm import ATM
import pickle
import os


def main():
    # 界面对象
    admin = Admin()
    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return 1  # returnz之后就结束程序了，不执行下面的程序

    absPath = os.getcwd()  # 获取当前文件所在的绝对路径
    filepath = os.path.join(absPath, "D:\\Users\\PycharmProjects\\b\\allusers.txt")
    f = open(filepath, "rb")
    allUsers = pickle.load(f)
    # 提款机对象
    atm = ATM(allUsers)
    print(type(atm.allusers))

    while True:
        # 登录成功打印系统功能界面
        admin.printSysFunctionView()
        # 等待用户的操作
        option = input("请输入您想办理的业务：")
        if option == "1":
            atm.createUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            atm.saveMoney()
        elif option == "5":
            atm.transfer()
        elif option == "6":
            atm.changePasswd()
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            atm.newCard()
        elif option == "10":
            atm.killUser()
        elif option == "t":
            admin.printSysFunctionView()
        elif option == "q":
            if not admin.adminOption():
                # 将当前用户信息保存到文件中
                f = open(filepath, "wb")
                pickle.dump(atm.allusers, f)
                f.close()
                return 1


if __name__ == '__main__':
    main()
