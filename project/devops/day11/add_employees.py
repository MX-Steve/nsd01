from dbconnetion import Employees,Session

# 目前只是在内存中有
zs = Employees(emp_id=1,emp_name='zhangsan',gender='m',phone='18262629610',email='steve@163.com',dep_id=1)
xh = Employees(emp_id=2,emp_name='xiaohong',gender='f',phone='18262629611',email='xh@163.com',dep_id=1)
lh = Employees(emp_id=3,emp_name='lihong',gender='f',phone='18262629612',email='lh@163.com',dep_id=2)
zh = Employees(emp_id=4,emp_name='zhanghong',gender='m',phone='18262629613',email='zh@163.com',dep_id=3)
ll = Employees(emp_id=5,emp_name='lilin',gender='m',phone='18262629614',email='ll@163.com',dep_id=3)
ss = Employees(emp_id=6,emp_name='songshi',gender='m',phone='18262629614',email='ss@163.com',dep_id=2)
emps = [xh,lh,zs,zh,ll,ss]

session = Session()
session.add_all(emps)
session.commit()
session.close()
