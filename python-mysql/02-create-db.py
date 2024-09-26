import os
from mysql import connector
from dotenv import load_dotenv

# Cargar las variables de entorno de .env
load_dotenv()

# Obtenemos las variables de entorno del OS (sistema operativo)
HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

# Configuración mínima para abrir la conexión
config = {
  "host": HOST,
  "user": USER,
  "password": PASSWORD
}

try:
  # Abrimos la conexión hacia MySQL
  with connector.connect(**config) as conn:

    # Queries de creación, borrado y mostrado de base de datos
    create_db = "create database book_ratings"
    drop_db = "drop database book_ratings"
    show_existing_db = "show databases"

    # Abrimos el cursor a partir de la conexión
    with conn.cursor() as cursor:
      try:
        # Borramos la base de datos
        cursor.execute(drop_db)
      except Exception as error:
        print("ERROR:", error)
      # Creamos la base de datos
      cursor.execute(create_db)

      # Mostramos las bases de datos existentes
      cursor.execute(show_existing_db)

      for db in cursor:
        print(db)

except Exception as error:
  print("ERROR:", error)


# Para conectarse a una base de datos en específico 
# algo como USE book_ratings 

config_db = {
  **config,
  "database" : "book_ratings"
}

try:
  with connector.connect(**config_db) as conn:
    print(conn)
    print("Todo bien!")
except Exception as error:
  print("Error: ", error)