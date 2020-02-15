import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="wmjrc@qq.com"    #用户名
mail_pass="naznzovfynuiddff"   #口令 
 
 
sender = 'wmjrc@qq.com'
receivers = ['1436375972@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('查询到新的信息', 'plain', 'utf-8')
message['From'] = Header("sim_sign.py", 'utf-8')
message['To'] =  Header("admin", 'utf-8')
 
subject = '最新查询信息'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")