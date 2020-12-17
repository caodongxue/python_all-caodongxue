data = {
    "北京":{
        "昌平":{
            "天通苑":["海底捞","呷哺呷哺"],
            "龙泽":["永辉超市","永旺超市"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["清华","北大"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        }
    },


    '河北':{
        '邯郸':{
             '磁县':['花官营','吴庄'],
             '峰峰':['白村','左良']
             },
        '石家庄':{
             '晋州':['梨','苹果'],
             '无极':['轮胎','牛肉']
               },
        '张家口':{
             '承德':['西官营','烤全羊'],
             '坝上':['骑马','牛肉干']
                }
         }

}



# 方法显示当前地区的子列表
def print_place(choice):
    for i in choice:
        print("\t\t",i)

while True:
    ###########城市
    for con in data:
        print(con)
    choice1 = input("请输入城市：choice1:>>>:")
    if choice1 in data:
        if choice1 == 'q' or choice1 == 'Q':
            print("欢迎下次光临！！")
            break
        print_place(data[choice1])
        choice2 = input("请输入区：choice2:>>>:")
        if choice2 == 'q' or choice2 == 'Q':
            print("欢迎下次光临！！")
            break
        if choice2 in data[choice1]:
            print_place(data[choice1][choice2])
            choice3 = input("请输入具体地区：choice3:>>>>:")
            if choice3 == 'q' or choice3 == 'Q':
                print("欢迎下次光临！！")
                break
            if choice3 in data[choice1][choice2]:
                print_place(data[choice1][choice2][choice3])
                print("是否继续观光浏览？？？")
                yes = input("是？否？")
                if yes != '是':
                    break
