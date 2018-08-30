import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.header import Header

# 邮件头部设置
mail_host='smtp.qq.com'
mail_user='2513556525@qq.com'
#mail_pass = getpass()
mail_pass = "rzscpnnylwixebfe"
message=MIMEText("Python EMAIL TEXT","plain","utf-8") # 设置标题与邮件格式
message['From']=Header('2513556525@qq.com','utf-8')# 发送者
message['To']=Header('2513556525@qq.com','utf-8') # 收件人
subject='Python SMTP 邮件测试python1803' # 邮件正文
message['Subject']=Header(subject,'utf-8') #插入邮件正文

sender='2513556525@qq.com'
receivers=["2513556525@qq.com"] #抄送
# 创建发送对象:主机 端口 主机名
smtp_obj=smtplib.SMTP()
smtp_obj.connect(mail_host)
smtp_obj.login(mail_user,mail_pass)
# message.as_string()将前面的message字典转换为字符串发送
smtp_obj.sendmail(sender,receivers,message.as_string())
smtp_obj.quit()
