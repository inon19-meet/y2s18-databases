from User_model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///User.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_User():
	user = session.query(
		User).first()
	return user
print(add_User)

def add_all_Users():
	user = session.query(
		User).all()
	return user
print(add_all_Users)
	pass

def add_User_by_name(Name):
	user = session.query(
		User).filter_by(
		Name=Name).first()
	return user
print(add_User_by_name("inon"))

def delete_User_by_name(Name):
	session.query(User).filter_by(
		Name=Name).delete()
	session.commit()
delete_User_by_name("inon")

def delete_all_Users():
	session.query(User).all(.delete()
	session.commit()

delete_all_Users()

#def edit_User_name():
	#pass
