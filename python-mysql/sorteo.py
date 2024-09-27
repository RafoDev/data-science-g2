import random
def asignar_tablas(alumnos, tablas):
  for i in range(len(alumnos)):
    print(f"Alumno {alumnos[i]} : {random.choice(tablas)}")

alumnos = ["Alan", "Cristian", "Eduardo", "Fritz", "Henrry", "Hugo", "Juan", "Violeta", "Virna"]
tablas = ["libro", "producto", "vehiculo", "mascota", "juguete", 
  "herramienta", "sumministros_oficina", "instrumentos_musicales"]

asignar_tablas(alumnos, tablas)