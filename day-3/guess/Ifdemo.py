# age=10
# if age>=18:
#     print("hello!!!")
# else:
#     print("gun!!!")

i=0 # 输入三次分数并判断
while i < 3:
    score = int(input("请输入您本次考试分数："))
    if score <= 100 and score > 90:
        print("excellent!")
    elif score <= 90 and score > 80:
        print("good!")
    elif score <= 80 and score >= 70:
        print("just so so!")
    elif score < 60 and score > 0:
        print("恭喜你，你的试卷已经在路上了！")
    else:
        print("输入非法！！")
    i = i + 1







