import time
print(time.time())
print(time.struct_time.tm_year)
t1 =print(time.localtime())
print(time.localtime().tm_mday)
print(time.gmtime()) #0时区的九元组
# time.mktime(t1)
time.asctime()
time.ctime()
time.ctime(0)
# time.asctime(t1)
# print(time.struct_time("%Y-%m-%d %H:%M:%S"))
# print(time.asctime())
# from time import datetime
from datetime import datetime,timedelta
t1 = datetime.now()
print(t1.year)
print(t1.month)
t2 = datetime.today()
print(t2)
# datetime.strftime("2018-8-20",'%Y-%m-%d')

# print(aa)
dt = timedelta(days=100)
print(t1 -dt)
print(t1+dt)
