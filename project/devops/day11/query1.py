from dbconnetion import Departments,Employees,Salary,Session
session=Session()

#qset=session.query(Departments).order_by(Departments.dep_id)
#print(qset)
#for dep in qset: # 向qset取值时，得到一个个实例
#	print("%s:%s"%(dep.dep_id,dep.dep_name))

#qset=session.query(Employees.emp_name,Employees.phone)
#print(qset)
#for name,phone in qset:
#	print("%s:%s" %(name,phone))
qset = session.query(Departments.dep_name.label('部门'))
print(qset)
for row in qset:
	print(row.部门)

session.close()
