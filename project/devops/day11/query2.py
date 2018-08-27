from dbconnetion import Departments,Employees,Salary,Session
#Session:创建TCP连接，用来对数据库数据增删改查
from sqlalchemy import and_ , or_

session = Session()
#qset = session.query(Employees.emp_name).filter(and_(Employees.dep_id==2,Employees.gender=='m'))
#print(qset)
#for name in qset:
#	print(name)
#qset = session.query(Employees.emp_name).filter(or_(Employees.dep_id==2,Employees.gender=='m')) #filter()函数就相当于sql语句中的where条件，对查询进行过滤
#print(qset)
#for name in qset:
#        print(name)

#qset = session.query(Employees.emp_name,Employees.phone)
#print(qset.all())# 返回列表
#print(qset.first())# 返回满足条件的第一个值
#print(qset.one()) ==>>报错，多于一行
#qset = session.query(Employees.emp_name,Employees.phone).filter(Employees.emp_id==1)
#print(qset.one()) # 查询必须只有一项，否则报错
#print(qset.scalar()) # 调用one()，返回第一列的值

#qset=session.query(Employees)
#print(qset.count())

qset=session.query(Employees.emp_name,Departments.dep_name).join(Departments,Employees.dep_id==Departments.dep_id) # 前Employees,join后面就要是Departments
print(qset)
print(qset.all())

session.close()
