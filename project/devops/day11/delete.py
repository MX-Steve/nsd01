from dbconnetion import Departments,Session

#xz=Departments(dep_id=5,dep_name='行政')

session=Session()
#session.add(xz)
xz=session.query(Departments).get(5)
session.delete(xz)


session.commit()
session.close()
