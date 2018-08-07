from User_model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///User.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_User(Name, BirthDay, Active):
	user_object = 	User(
		Name = 	Name,
		BirthDay = BirthDay,
		Active = Active)
	session.add(user_object)
	session.commit()
#add_User("inon", 20/7/2001, True )
#add_User("solar", 12/8/2002, False )	
def query_User():
	user = session.query(
		User).first()
	return user
#print(query_User())

def query_all_Users():
	user = session.query(
		User).all()
	return user
print(query_all_Users())
	

def query_User_by_name(Name):
	user = session.query(
		User).filter_by(
		Name=Name).first()
	return user
#print(query_User_by_name("inon"))

def delete_User_by_name(Name):
	delete_User = session.query(User).filter_by(
		Name=Name).delete().all()
	session.commit()
	return delete_User
#delete_User_by_name("inon")

def delete_all_Users():
	delete_Users = session.query(User).delete()
	session.commit()
	return delete_Users

def query_User_by_Activity():
	activity = session.query(User).filter_by(
		Active=True).all()
	return activity

def delete_User_by_Activity():
	delete_non_Active = session.query(User).filter_by(
		Active=False).all()
	return delete_non_Active

def User_Rating():
	rating = session.query(User).filter_by(
		Rating = Rating).all()
	return rating



#print(query_User_by_Activity())
print(delete_all_Users())
#print(query_all_Users())

#def edit_User_name():
	#pass
