from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	# Create a table with 4 columns
	__tablename__ = 'Users'
	# The first column will be the primary key
	User_id = Column(Integer, primary_key=	True)
	# The second column should be a string representing
	Name = Column(String)
	# the name of the Wiki article that you're referencing
	BirthDay = Column(Integer)
	# The third column will be a string representing the 
	Active = Column(Boolean)
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	def __repr__(self):
		return ("User_Name: {}\n"
				"User_BirthDay: {}\n"
				"Activity: {}\n").format(
				self.Name, self.BirthDay, self.Active)
		
