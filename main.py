#!/usr/bin/env python3
from sqlalchemy import create_engine, text
from use_core import use_core_func
from orm_concept import create_user_table, create_address_user


engine = create_engine("sqlite+pysqlite:///test.db", future=True)

# Use core concept
#use_core_func(engine)
create_user_table(engine)
create_address_user(engine)






