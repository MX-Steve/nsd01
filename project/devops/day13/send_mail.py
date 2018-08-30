import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮件头部设置
message=MIMEText("Python EMAIL TEXT","plain","utf-8") # 设置标题与邮件格式
message['From']=Header('root@localhost','utf-8')# 发送者
message['To']=Header('bob@localhost','utf-8') # 收件人
subject='Python SMTP 邮件测试' # 邮件正文
message['Subject']=Header(subject,'utf-8') #插入邮件正文

sender="root@tedu.cn"
receivers=['bob@localhost','alice@localhost'] #抄送
# 创建发送对象:主机 端口 主机名
smtp_obj=smtplib.SMTP("localhost")
# message.as_string()将前面的message字典转换为字符串发送
smtp_obj.sendmail(sender,receivers,message.as_string())
