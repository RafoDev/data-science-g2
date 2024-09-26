import os

from mysql import connector
from dotenv import load_dotenv

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
    create_book_tbl = """
      create table book(
        id int primary key auto_increment,
        title varchar(100),
        author varchar(100),
        genre varchar(100),
        release_year smallint
      )
    """
    
    with db.cursor() as cursor:

      try:
        cursor.execute(create_book_tbl)
        # IMPORTANTE: Confirmar la transacción
        db.commit()
      except Exception as error:
        print("Error: ", error)
      
      # Describir la tabla
      describe_book_tbl = "describe book"
      cursor.execute(describe_book_tbl)

      book_tbl = cursor.fetchall()
      
      for column in book_tbl:
        print(column)

except Exception as error:
  print("Error: ", error)

