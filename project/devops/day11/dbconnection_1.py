from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

engin = create_engine(
	'mysql+pymysql://root:tedu.cn@localhost/tarena',
	encoding='utf8',
	echo=True
)
