from email.text import MIMEText
from email.header import Header
message=MIMEText("Python EMAIL","plain","utf-8")
message['From']=Header('zzg','utf-8')
message['To']=Header('lh','utf-8')
subject='Python SMTP 邮件测试'
message['Subject']=Header(subject,'utf-8')
