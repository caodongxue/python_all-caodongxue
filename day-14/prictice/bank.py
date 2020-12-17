bank = {}
bank_name = "中国工商银行昌平支行"

myinfo='''
\033[0;32;40m
------------账户信息------------
账号：{account}
姓名：{username}
密码：{password}
地址：
    国家：{country}
    省份：{province}
    街道：{street}
    门牌号：{door}
账户余额：{money}
注册银行名：{bank_name}
-------------------------------
\033[0m
'''

# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
    return None

# 银行的查询功能
def bank_selectUser(account,password):

    uname = findByAccount(account)

    if uname != None and len(uname) != 0:
        if password == bank[uname]["password"]:
            user = bank[uname]
            return bank["张三"]
        else:
            return "用户密码错误!"
    else:
        return"该用户不存在！"
#
# # 查询账户方法
# def selectUser():
#     account = inputHelp("账号")
#     password = inputHelp("密码")
#
#     bank_selectUser(account,password)
#
bank["张三"] = {"account":"admin","money":2000,
                  "country":"中国","province":"安徽省",
                  "street":"幸福大道","door":"s001","password":"admin","bank_name":bank_name}
bank["李四"] = {"account":"admin1","money":2000,
                  "country":"中国","province":"福建省",
                  "street":"幸福大道","door":"s002","password":"admin","bank_name":bank_name}
#
# selectUser()











