from sqlalchemy import  text

def create_db(engine):
	with engine.begin() as conn:
		conn.execute(text("CREATE TABLE some_table(x int, y int)"))
		conn.execute(
			text("INSERT INTO some_table (x, y) VALUES(:x, :y)"),
			[{"x": 1, "y": 1}, {"x": 2, "y": 4}]
			)
		
