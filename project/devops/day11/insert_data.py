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
cursor=conn.cursor() #创建游标
insert1="INSERT INTO departments(dep_id,dep_name) values(%s,%s)"
data=[(2,'运营部'),(3,'开发部')]
#result = cursor.execute(insert1,(1,'人事部')) #单个插入
result = cursor.executemany(insert1,data) # 插入多个
conn.commit() #增删改要commit
cursor.close()
conn.close()
