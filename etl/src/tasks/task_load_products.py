import os
from dotenv import load_dotenv
from mysql import connector
from prefect import task

load_dotenv()

config = {
  "host":"localhost",
  "user":"root",
  "password": os.getenv("DB_PASSWORD"),
  "database": "db_codigo"
}

@task(name="Limpieza y carga de productos en la bd")
def task_load_products_baseline(products):
	with connector.connect(**config) as db:
		with db.cursor() as cursor:
			try:
				cursor.execute("drop table if exists product")
				db.commit()

				cursor.execute("""
					create table if not exists product(
						id int primary key auto_increment,
						title varchar(200) unique,
						price float,
            discount int,
						free_shipping bool,
						rating float,
						reviews int,
						variations int,
						best_seller bool
					)
				""")
				db.commit()
			except Exception as error:
				print("error: ", error)

			query_insert = """
				insert into product(title, price, discount, free_shipping, rating, reviews, variations, best_seller)
				values (%s,%s,%s,%s,%s,%s,%s,%s)
			"""
			try:
				cursor.executemany(query_insert, products)
				db.commit()
			except Exception as error:
				print("error: ", error)
				
@task(name="Cargar nuevos productos en la bd")
def task_load_products_update(products):
	with connector.connect(**config) as db:
		with db.cursor() as cursor:
			query_insert = """
				insert into product(title, price, discount, free_shipping, rating, reviews, variations, best_seller)
				values (%s,%s,%s,%s,%s,%s,%s,%s)
			"""
			for product in products:
				try:
					cursor.execute(query_insert, product)
					db.commit()
				except Exception as error:
					print("error: ", error)