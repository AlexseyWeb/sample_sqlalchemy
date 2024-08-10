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

# with Session(autoflush=False, bind=engine) as db:
# 	tom = Person(name="Tom", age=32)
# 	jack = Person(name="Jack", age=28)
# 	alex = Person(name="Alex", age=23)
# 	db.add(tom)
# 	db.add(jack)
# 	db.add(alex)
# 	db.commit()
# 	print(tom.id)
print("\t\t\tid name age")
with Session(autoflush=False, bind=engine) as db:
	people = db.query(Person).all()
	for i in people:
		print(f" Получение данных всех {i.id}.{i.name} {i.age}")

with Session(autoflush=False, bind=engine) as db:
	first_person = db.get(Person, 1)
	print(f" Получение по id через Get {first_person.name} - {first_person.age}")

with Session(autoflush=False, bind=engine):
	people = db.query(Person).filter(Person.age > 30).first()
	print(f" Фильтрация запроса id = {i.id} name = {i.name} age = {i.age}")

with Session(autoflush=False, bind=engine) as db:
	remove_people = db.query(Person).filter(Person.id == 1).first()
	db.delete(remove_people)
	db.commit()

