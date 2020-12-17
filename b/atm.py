from card import Card
from user import User
import random
import time


class ATM(object):
    def __init__(self, allUsers):
        self.allusers = allUsers

    def createUser(self):
        # 目标：向用户字典中添加一对键值对（卡号：用户）
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        preMoney = int(input("请输入预存款金额："))
        if preMoney < 0:
            print("预存款输入有误！！开户失败……")
            return 1

        onePasswd = input("请设置密码：")
        # 验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！！开户失败……")
            return 1
        # 所有需要的信息齐全了

        cardStr = self.randomCardId()
        card = Card(cardStr, onePasswd, preMoney)
        user = User(name, idCard, phone, card)
        # 存到字典
        self.allusers[cardStr] = user
        print("开户成功！请牢记卡号(%s)……\n(系统将在 3 秒后自动返回！)" % (cardStr))
        time.sleep(3)

    # 查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        print("账号：%s  余额：%d\n(系统将在 5 秒后自动返回……)" % (user.card.cardId, user.card.cardMoney))
        time.sleep(5)

    # 取款
    def getMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        getNum = int(input("请输入取款金额："))
        user.card.cardMoney -= getNum
        print("取款金额：%d   账户余额：%d   手续费：%d\n(系统将在 5 秒后自动返回……)" % (getNum, user.card.cardMoney, 0))
        time.sleep(5)

    # 存款
    def saveMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1

        getNum = int(input("请输入存款金额："))
        if getNum < 0:
            print("输入有误！！取款失败……")
            return 1
        user.card.cardMoney += getNum
        print("存款金额：%d   账户余额：%d   手续费：%d\n(系统将在 5 秒后自动返回……)" % (getNum, user.card.cardMoney, 0))
        time.sleep(5)

    # 转账
    def transfer(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        tranNum = input("请输入转入账号：")
        tranUser = self.allusers.get(tranNum)
        if not tranUser:
            print("该卡号不存在!!查询失败……")
            return 1
        # 判断是否锁定
        if tranUser.card.cardLock:
            print("该卡已被锁定！！请解锁后重试……")
            return 1
        # 验证密码
        if not self.checkPasswd(tranUser.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定！！请解锁后重试……")
            tranUser.card.cardLock = True
            return 1
        tranMoney = int(input("请输入转账金额："))
        if tranMoney > user.card.cardMoney:
            print("余额不足！！转账失败……")
        # 开始转账
        user.card.cardMoney -= tranMoney
        tranUser.card.cardMoney += tranMoney
        print("转账成功！转账金额：%d\n(系统将在 5 秒后自动返回……)" % (tranMoney))
        time.sleep(5)

    # 改密
    def changePasswd(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1

        while True:
            newPasswd = input("请输入新密码：")
            defPasswd = input("请再次输入新密码：")
            if newPasswd == defPasswd:
                print("密码已确认！请稍候……")
                time.sleep(2)
                user.card.cardPasswd = newPasswd
                return 1

    # 锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if not user:
            print("该卡号不存在!!锁定失败……")
            return 1
        if user.card.cardLock:
            print("该卡号已经锁定，请解锁后重试！！")
            return 1
        cardPasswd = input("请输入您的密码：")
        if cardPasswd != user.card.cardPasswd:
            print("密码输入有误！！锁定失败……")
            return 1
        cardId = input("请输入您的身份证号：")
        if cardId != user.idCard:
            print("身份证输入有误！！锁定失败……")
            return 1
        # 锁定
        user.card.cardLock = True
        print("该卡号已锁定……\n(系统将在 5 秒后自动返回……)")
        time.sleep(5)

    # 解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if not user:
            print("该卡号不存在!!查询失败……")
            return 1
        if not user.card.cardLock:
            print("该卡号已经解锁，无需重复操作……")
            return 1
        cardPasswd = input("请输入您的密码：")
        if cardPasswd != user.card.cardPasswd:
            print("密码输入有误！！解锁失败……")
            return 1
        cardId = input("请输入您的身份证号：")
        if cardId != user.idCard:
            print("身份证输入有误！！解锁失败……")
            return 1
        # 解锁
        user.card.cardLock = False
        print("该卡号已解锁……\n(系统将在 5 秒后自动返回……)")
        time.sleep(5)

    # 补卡
    def newCard(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        newCard = self.randomCardId()
        self.allusers.pop(cardNum)
        self.allusers[newCard] = user
        print("您的新卡号为：%s\n已为您将余额转存入该卡，请妥善保管！" % (newCard))
        print("(系统将在 5 秒后自动返回……)")
        time.sleep(5)

    # 销户
    def killUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在卡号
        user = self.allusers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1

        print("操作成功！请稍候……")
        self.allusers.pop(cardNum)
        time.sleep(2)
        print("该卡号已注销……\n(系统将在 5 秒后自动返回……)")
        time.sleep(5)

    # 验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    # 随机卡号六位数
    def randomCardId(self):
        while True:
            stu = ""
            for a in range(19):
                ch = chr(random.randrange(ord("0"), ord("9") + 1))
                stu += ch
            # 判断是否重复
            if not self.allusers.get(stu):
                return stu

    def checkFunc(self, cardNum, user):
        if cardNum == "t":
            return 1
        if not user:
            print("该卡号不存在!!操作失败……")
            return 1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后重试……")
            return 1
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定！！请解锁后重试……")
            user.card.cardLock = True
            return 1
