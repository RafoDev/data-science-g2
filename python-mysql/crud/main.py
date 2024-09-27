import os
from MySQLDatabase import *
from AlumnoHandler import *
from dotenv import load_dotenv

load_dotenv()

config = {
  "host": os.getenv("DB_HOST"),
  "user": os.getenv("DB_USER"),
  "password": os.getenv("DB_PASSWORD"),
  "database": "db_codigo"
}

db = MySQLDatabase(**config)

def create_alumno_tbl(conn):
  try:
    with conn.cursor() as cursor:
      cursor.execute("""
        create table alumno(
          id int primary key auto_increment,
          nombre varchar(100),
          email varchar(100),
          celular varchar(100)
        )
      """)
  except Exception as error:
    print("Error: ", error)

# create_alumno_tbl(db.conn)

alumnoHandler = AlumnoHandler(db.conn)

def menu():
  options = [
    ("[1]", "Registrar Alumno"),
    ("[2]", "Mostrar Alumnos"),
    ("[3]", "Actualizar Alumno"),
    ("[4]", "Eliminar Alumno"),
    ("[5]", "Salir"),
  ]

  print(tabulate(options))

opcion = 0

while opcion != 5:
  print()
  menu()
  print()
  opcion = int(input("Ingrese una opción: "))

  if opcion == 1:
    print("[1] Registrar alumno")
    data = {}
    data["nombre"] = input("Nombre: ")
    data["email"] = input("Email: ")
    data["celular"] = input("Celular: ")

    alumnoHandler.insertar_alumno(**data)
  elif opcion == 2:
    print("[2] Mostrar alumnos")
    alumnoHandler.mostrar_alumnos()
  elif opcion == 3:
    print("[3] Actualizar alumno")
    data = {}
    data["id"] = input("ID: ")
    data["nombre"] = input("Nombre: ")
    data["email"] = input("Email: ")
    data["celular"] = input("Celular: ")
    alumnoHandler.actualizar_alumno(**data)
  elif opcion == 4:
    print("[4] Borrar alumno")
    id = input("id: ")
    alumnoHandler.borrar_alumno(id)
  elif opcion == 5:
    print("[5] Salir")

db.close_conn()
