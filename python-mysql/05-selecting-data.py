import os

from mysql import connector
from dotenv import load_dotenv
from tabulate import tabulate

# Cargar las variables de entorno de .env
load_dotenv()

# Obtenemos las variables de entorno del OS (sistema operativo)
config = {
  "host": os.getenv("DB_HOST"),
  "user": os.getenv("DB_USER"),
  "password": os.getenv("DB_PASSWORD"),
  "database": "book_ratings"
}

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      select_all = "select * from book"
      cursor.execute(select_all)

      # Para pedir que el cursor traiga toda la tabla
      tbl_rows = cursor.fetchall()

      print(tabulate(tbl_rows, headers=["id", "title", "author", "genre", "release_date"]))

      # for row in tlb_rows:
      #   print(row)


except Exception as error:
  print("Error: ", error)
