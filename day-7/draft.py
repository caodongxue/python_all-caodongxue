import random
bank = {}
bank_name = '中国工商银行昌平支行'
bank_choice= {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项

welcome = '''
*********************************
*          中国工商银行           *
*          账户管理系统           *
*********************************
*              选项              *
'''

welcome_item = '''*            {0}.{1}              *'''


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


def print_welcome():
    print(welcome,end='')
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print('*********************************')

# 输入帮助方法：chose是打印选项
def inputHelp(chose,datatype='str'):
    while True :
        print('请输入', chose, ':')
        i = input('>>>:')
        if len(i) == 0:
            print('该项不能为空，请重新输入！')
            continue
        if datatype != 'str':
            return int(i)
        else:
            return i

def isExists(chose,data):
    if chose in data:
        return True
    return False


def getRandom():
    li = '1234567890qwertyuioopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    string=''
    for i in range(8):
        string = string + li[int(random.random()*len(li))]
    return string

def bank_addUser(username,password,country,province,street,door,money):
    # for i in range(100):
    #      bank["张三"  + str(i)] = {}
    if len(bank) >= 100:
        return 3
    elif username in bank:
        return 2
    else:
        bank[username]= {
            'account':getRandom(),
            'password':password,
            'country':country,
            'province':province,
            'street':street,
            'door':door,
            'money':money,
            'bank_name':bank_name
        }
        return 1






def addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家：")
    province = inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money = inputHelp("银行卡余额", "int")
    status=bank_addUser(username,password,country,province,street,door,money)
    if status == 1:
        user = bank[username]
        print('恭喜开户成功！以下是您的开户信息:')
        print(myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    elif status == 2:
        print('该用户已经存在！请携带证件到其他银行办理！谢谢！！！')
    elif status == 3:
        print('银行库存已满！请携带证件到其他银行办理！谢谢！！！！')


def bank_saveMoney(account,accessamount):
    n=[]
    m=''
    for i in bank.values():
        n.append(i['account'])
        if i['account']== account:
             m=i['money']
    if account not in n:
        return False
    else:
        m += accessamount

def savMoney():
    account = inputHelp('账号')
    accessamount=inputHelp('存款金额','int')
    status2=bank_saveMoney(account,accessamount)
    if status2 == False:
        print('您输入的账号不存在！！！')
    else:
        print('您存入的金额为',accessamount,'现余额为','m')








def bank_drawMoney(account,password,drawamount):
    '''
    bank={
        “在”：{acount:001,password:1234.......},
        "里"：{acount:002,password:1234}

    }



    :param account:
    :param password:
    :param drawamount:
    :return:

    '''
    a=[]# [001,002]
    p=[]
    m=""
    for i in bank.values():
        a.append(i["account"])  #把account存到a里
        p.append(i['password'])
        if i["account"] == account:
            m=i['money']
    if account not in a:
        return 1
    elif password not in p:
        return 2
    elif drawamount > m:
        return 3
    else:
        return 0

def drawMoney():
    account=inputHelp('账号')
    password=inputHelp('密码')
    drawamount=inputHelp('取款金额','int')
    status1 =bank_drawMoney(account,password,drawamount)
    if status1==1:
        print('您输入的账号不存在！！！')
    elif status1==2:
        print('您输入的密码有误！！！')
    elif status1==3:
        print('余额不足！！！')
    else:
        m -= drawamount









# 核心程序
while True :
    print_welcome()
    chose=inputHelp('选项')
    if isExists(chose,bank_choice):
        if chose == '1':
            addUser()
        elif chose == '2':
            savMoney()
        elif chose == '3':
            drawMoney()
        elif chose == '4':
            pass
        elif chose == '5':
            pass
        elif chose == '6':
            print('Bye,Bye您嘞！！！')
            break
    else:
        print('不存在该选项，别瞎弄！')


# age=inputHelp('年龄')
# print(age)


# while True :
#      print_welcome()
#      chose=input('请输入您的选项')




# 字典的使用方法（遍历）
# bank={'1':'开户','2':'存钱','3':'取钱','4':'转账','5':'查询','6':'Bye'}
# a=bank.keys()    #  把键附给a
# for i in a:     # i在a里循环遍历
#      print(bank[i])   # 通过键取值















