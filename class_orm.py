from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

Session = sessionmaker(autoflush=False, bind=engine)

with Session(autoflush=False, bind=engine) as db:
	tom = Person(name="Tom", age=32)
	db.add(tom)
	db.commit()
	print(tom.id)