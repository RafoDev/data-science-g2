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

# Insertar un registro

insert_single_record = """
  insert into book(title, author, genre, release_year)
  values(%s, %s, %s, %s)
"""

single_record = ("Quien Pierde Paga", "Stephen King", "Suspenso", 2020)

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      cursor.execute(insert_single_record, single_record)
      db.commit()
      print("Filas insertadas: ", cursor.rowcount)

except Exception as error:
  print("Error: ", error)

# Insertar múltiples registros

insert_record = """
  insert into book(title, author, genre, release_year)
  values(%s, %s, %s, %s)
"""

multiple_records = [
  ("Don Quijote", "Miguel de Cervantes", "Parodia", 1605),
  ("Historia de dos ciudades", "Charles Dickens", "Novela", 1859),
  ("El señor de los anillos", "J.R.R Tolkien", "Fantasía", 1954),
]

try:
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      cursor.executemany(insert_record, multiple_records)
      db.commit()
      print("Filas insertadas: ", cursor.rowcount)

except Exception as error:
  print("Error: ", error)