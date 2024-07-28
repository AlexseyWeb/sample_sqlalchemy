#!/usr/bin/env python3
from sqlalchemy import create_engine, text
from create_table import create_db
from select_db import select

engine = create_engine("sqlite+pysqlite:///:memory:", future=True)

# with engine.connect() as db:
# 	result = db.execute(text("select 'hello DB'"))
# 	print(result.all())

create_db(engine)
select(engine)