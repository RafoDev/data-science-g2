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

# Para mostrar tabla filtrada

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      year = 2000
      query = "select author from book where release_year > {}".format(year)
      
      cursor.execute(query)

      data = cursor.fetchall()
      print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
      print("Filas consultadas: ", cursor.rowcount)
      
except Exception as error:
  print("Error:", error)

# Para mostrar tabla ordenada

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      query = "select * from book order by release_year desc"
      
      cursor.execute(query)

      data = cursor.fetchall()
      print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
      print("Filas consultadas: ", cursor.rowcount)
      
except Exception as error:
  print("Error:", error)

# Limit

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      query = "select * from book limit 3"
      
      cursor.execute(query)

      data = cursor.fetchall()
      print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
      print("Filas consultadas: ", cursor.rowcount)
      
except Exception as error:
  print("Error:", error)