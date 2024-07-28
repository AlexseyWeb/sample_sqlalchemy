from sqlalchemy import text

def select(engine):
	with engine.connect() as con:
		result = con.execute(text("SELECT * FROM some_table"))
		for item in result:
			print(item)