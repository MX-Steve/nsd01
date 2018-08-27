from dbconnetion import Departments,Employees,Salary,Session
session=Session()

# q 1
#qset=session.query(Departments).order_by(Departments.dep_id)
#print(qset)
#for dep in qset: # 向qset取值时，得到一个个实例
#	print("%s:%s"%(dep.dep_id,dep.dep_name))

# q 2
#qset=session.query(Employees.emp_name,Employees.phone)
#print(qset)
#for name,phone in qset: #qset执行后返回的是一个元祖
#	print("%s:%s" %(name,phone))
#qset = session.query(Departments.dep_name.label('部门'))
#print(qset)
#for row in qset:
#	print(row.部门)

#qset=session.query(Employees.emp_name,Employees.email).\
#	order_by(Employees.emp_id)[3:6]  #[3:6]代表切片,切片后变成元祖组成的列表

# qset = session.query(Employees.emp_name).filter(Employees.dep_id==2).filter(Employees.gender=="m")
# print(qset)
#for name in qset:
#	print(name)

#qset=session.query(Employees.emp_name).filter(Employees.emp_name.like("z%"))
#print(qset)
#for name in qset:
#	print(name)

#qset = session.query(Employees.emp_name).filter(Employees.emp_name.in_(['zhangsan','zhanghong']))
#print(qset)
#for name in qset:
#	print(name)

qset = session.query(Employees.emp_name).filter(~Employees.emp_name.in_(['zhangsan','zhanghong'])) #qset是一个sql语句，filter函数内加~代表取反，配合in_，表示不在集合中
print(qset)
for name in qset:
        print(name)

#qset = session.query(Employees.emp_name).filter(Employees.emp_name.isnot(None)) #qset是一个sql语句 安装emp_name列进行查询
#print(qset) 
#for name in qset: # for循环时则执行查询操作
#	print(name)

session.close()
