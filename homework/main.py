from sqlalchemy import create_engine, Column, Integer, String, Float 
from sqlalchemy.orm import DeclarativeBase, Session
from enter_product import enter_data

url_database = "sqlite:///test.db"
engine = create_engine(url_database)

class Base(DeclarativeBase): pass 
class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True)
    title_of_product = Column(String(100))
    price = Column(Float)

Base.metadata.create_all(bind=engine)

product = enter_data()


with Session(autoflush=False, bind=engine) as db:
    data = Product(title_of_product=product[1], price=product[2])
    db.add(data)
    db.commit()
    db.refresh(data)
    print(data.id)