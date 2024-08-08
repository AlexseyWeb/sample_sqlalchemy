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
	jack = Person(name="Jack", age=28)
	alex = Person(name="Alex", age=23)
	db.add(tom)
	db.add(jack)
	db.add(alex)
	db.commit()
	print(tom.id)

with Session(autoflush=False, bind=engine):
	people = db.query(Person).all()
	for i in people:
		print(f"{i.id}.{i.name} {i.age}")