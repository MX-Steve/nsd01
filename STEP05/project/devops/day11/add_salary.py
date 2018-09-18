from dbconnetion import Salary,Session

jan2018_1=Salary(
	date='2018-01-10',
	emp_id=1,
	basic=10000,
	awards=2000
)
jan2018_2=Salary(
	date='2018-01-10',
	emp_id=2,
	basic=10100,
	awards=2100
)
jan2018_3=Salary(
	date='2018-01-10',
	emp_id=3,
	basic=15000,
	awards=5000
)
jan2018_4=Salary(
	date='2018-01-10',
	emp_id=4,
	basic=20000,
	awards=2000
)
jan2018_5=Salary(
	date='2018-01-10',
	emp_id=5,
	basic=13000,
	awards=1000
)

jan2018_6=Salary(
	date='2018-01-10',
	emp_id=6,
	basic=10000,
	awards=2000
)

sals=[jan2018_1,jan2018_2,jan2018_3,jan2018_4,jan2018_5,jan2018_6]

session=Session()
session.add_all(sals)
session.commit()
session.close()
