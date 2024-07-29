from sqlalchemy import  text

def create_db(engine, numb_x, numb_y):
	with engine.begin() as conn:
		conn.execute(text("CREATE TABLE some_table(x int, y int)"))
		conn.execute(
			text("INSERT INTO some_table (x, y) VALUES(:x, :y)"),
			[{"x": numb_x, "y": numb_y}]
			)
		
