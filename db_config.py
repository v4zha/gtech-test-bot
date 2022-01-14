import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import os

db_key=os.environ["DB_KEY"]
engine=sqlalchemy.create_engine(db_key)
Base=declarative_base()

#creat table data :)
class User(Base):
	__tablename__='users'
	u_id=sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
	u_name=sqlalchemy.Column(sqlalchemy.String(length=80))

Base.metadata.create_all(engine)

#Create session
Session=sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session=Session()

def add_user(name):
	#create new user instance	
	n_usr=User(u_name=name)
	session.add(n_usr)
	session.commit()

def user_exist(name):
	#check if user exists
	users=session.query(User).filter_by(u_name=name).count()
	if users!=0:
		return True
	else:
		return False

def get_users():
	#get all users from db
	return session.query(User).all()
