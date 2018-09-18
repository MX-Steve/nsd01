#!/usr/local/env python3
import pymysql
conn=pymysql.connect(
	host="127.0.0.1",
	port=3306,
	user='root',
	passwd='tedu.cn',
	db='tedu',
	charset='utf8'
)
cursor=conn.cursor() #创建游标,和指针一样，会往后移动
update1="update departments set dep_name=%s where dep_name=%s"
cursor.execute(update1,('人力资源部','人事部'))

delete1 = "delete from departments where dep_id=%s"
cursor.execute(delete1,3)



conn.commit()
cursor.close()
conn.close()
