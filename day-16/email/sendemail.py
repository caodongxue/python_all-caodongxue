# 授权码zwdevromkoaddiab
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = '2398710377@qq.com'
receivers = [
             '1402162946@qq.com'
             ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_host = 'smtp.qq.com'
password = 'zwdevromkoaddiab'
tester = '曹东雪'
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = '2398710377@qq.com'
message['To'] = Header("曹东雪的邮件", 'utf-8')
subject = '第一轮计算器的单元测试报告 -- [' + tester + ']'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('详情请见附件消息！', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
f = open('计算器测试报告.html', 'r+',encoding="utf-8").read() # 先读取报告文件
att1 = MIMEText(f, 'base64', 'utf-8')  # 添加到附件里
att1["Content-Type"] = 'application/octet-stream' # 添加属性头
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="bank_reporting.html"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(sender,password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件",e)






