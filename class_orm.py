from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String 
from sqlalchemy import create_engine


sqlite_database = "sqlite:///restaurant"

engine = create_engine(sqlite_database)


class Base(DeclarativeBase): pass 

class Person(Base):
	__tablename__ = "people"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	age = Column(Integer)
	sallary = Column(Integer)

Base.metadata.create_all(bind=engine)

print("Database restaraunt is created...")