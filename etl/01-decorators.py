import time

# DRY -> DON'T REPEAT YOURSELF
# DECORATOR: Función que acepta otra función como argumento y modifica su comportamiento sin alterar su estructura.

def logger(func):
  def wrapper():
    print(f"{time.ctime()} | INFO | Function run - Created function '{func.__name__}'")
    func()
    print(f"{time.ctime()} | INFO | Function run - Finished function '{func.__name__}'")

  return wrapper

@logger
def saludar():
  print("Hola!")

saludar()


def decorador_general(function):
  def wrapper(*args, **kwargs):
    print("Antes de la función")
    value = function(*args, **kwargs)
    print("Después de la función")
    return value
  return wrapper

@decorador_general
def suma_dos(a, b):
  print("Dentro de la función...")
  return a + b

@decorador_general
def suma_tres(a,b,c):
  return a + b + c

result = suma_dos(1,2)
print(result)

result = suma_tres(1,2,3)
print(result)