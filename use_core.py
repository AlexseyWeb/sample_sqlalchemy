""" Use core concept to sqlalchemy """
from create_table import create_db
from select_db import select 
from create_session import create_session

def use_core_func(engine):

	try:
		first_numb = int(input("Enter x number please: "))
		second_numb = int(input("Enter y number please: "))
	except:
		print("Undefined error")


	create_db(engine, first_numb, second_numb)
	list_run = [select, create_session,]

	for run in list_run:
		run(engine)
