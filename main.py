#!/usr/bin/env python3
from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as db:
	result = db.execute(text("select 'hello DB'"))
	print(result.all())
