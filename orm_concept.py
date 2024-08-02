from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData 



def create_user_table(engine):
	""" Create user table in database"""

	metadata_obj = MetaData()

	user_table = Table(
		"user_account",
		metadata_obj,
		Column("id", Integer, primary_key=True),
		Column("name", String(30)),
		Column("fullname", String),
		)
	metadata_obj.create_all(engine)

def create_address_user(engine):
	metadata_obj = MetaData()

	address_table = Table(
		"address account",
		metadata_obj,
		Column("id", Integer, primary_key=True),
		Column("street", String(150)),
		Column("number_street", Integer),
		Column("fulladdress", String(200))
		)
	metadata_obj.create_all(engine)

def create_product(engine):
	metadata_obj = MetaData()
	product_table = Table(
		"product",
		metadata_obj,
		Column("id", Integer, primary_key=True),
		Column("name_product", String(180)),
		Column("contry", String(100)),
		Column("color", String(50)),
		Column("year", Integer)
		)


