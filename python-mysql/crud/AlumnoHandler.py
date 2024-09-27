from tabulate import tabulate

class AlumnoHandler:
  def __init__(self, db):
    self.db = db

  # Insertar
  def insertar_alumno(self, nombre, email, celular):
    try:
      with self.db.cursor() as cursor:
        query = "insert into alumno (nombre, email, celular) values (%s, %s, %s)"
        cursor.execute(query, (nombre, email, celular))

        self.db.commit()
        
        print("[INFO] Alumno Creado")
    except Exception as error:
      print("Error: ", error)

  # Mostrar
  def mostrar_alumnos(self):
    try:
      with self.db.cursor() as cursor:
        query = "select * from alumno"
        cursor.execute(query)

        data = cursor.fetchall()
        print(tabulate(data, headers=cursor.column_names, tablefmt="github"))
    except Exception as error:
      print("Error: ", error)

  # Actualizar
  def actualizar_alumno(self, nombre, email, celular, id):
    try:
      with self.db.cursor() as cursor:
        query = "update alumno set nombre = %s, email = %s, celular = %s where id = %s"
        cursor.execute(query, (nombre, email, celular, id))

        self.db.commit()
        
        print("[INFO] Alumno Actualizado")
    except Exception as error:
      print("Error: ", error)

  # Borrar
  def borrar_alumno(self, id):
    try:
      with self.db.cursor() as cursor:
        query = "delete from alumno where id = %s"
        cursor.execute(query, (id,))

        self.db.commit()
        
        print("[INFO] Alumno Borrado")
    except Exception as error:
      print("Error: ", error)