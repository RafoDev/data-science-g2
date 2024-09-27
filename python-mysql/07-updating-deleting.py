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

# Para actualizar un registro

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      
      new_author_name = "Miguel de Cervantes Saavedra"
      old_author_name = "Miguel de Cervantes"

      update_query = f"""
        update book
        set author = "{new_author_name}" where author = "{old_author_name}" 
      """
      
      cursor.execute(update_query)
      db.commit()

      select_author_names = "select distinct author from book"
      cursor.execute(select_author_names)
      
      data = cursor.fetchall()
      print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
      print("Filas consultadas: ", cursor.rowcount)
      
except Exception as error:
  print("Error:", error)

# Para borrar registros

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
    
      drop_record = "delete from book where release_year < 2020"
      
      cursor.execute(drop_record)
      db.commit()

      show_book_table = "select * from book"
      cursor.execute(show_book_table)
      
      data = cursor.fetchall()
      print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
      print("Filas consultadas: ", cursor.rowcount)
      
except Exception as error:
  print("Error:", error)


