from sqlalchemy.orm import Session
from sqlalchemy import text

def create_session(engine):
	stmp = text("SELECT x, y FROM some_table WHERE x = :x ORDER BY x, y")
	with Session(engine) as session:
		result = session.execute(stmp, {"x": 33})
		for row in result:
			print(f"X = 33 output -> {row}")
