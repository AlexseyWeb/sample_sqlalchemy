#!/usr/bin/env python3
from sqlalchemy import create_engine, text
from create_table import create_db
from select_db import select

engine = create_engine("sqlite+pysqlite:///:memory:", future=True)


try:
	first_numb = int(input("Enter x number please: "))
	second_numb = int(input("Enter y number please: "))
except:
	print("Undefined error")


create_db(engine, first_numb, second_numb)
select(engine)