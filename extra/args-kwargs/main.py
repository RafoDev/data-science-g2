# *Args y **Kwargs(keyword arguments)

# Son dos maneras adicionales de pasar argumento a una función
# Nos permiten pasar un número variable de argumentos

# ARGS
def test_var_args(arg, *argv):
  print("Argumento normal: ", arg)
  for a in argv:
    print("Argumentos *argv: ", a)

# test_var_args("python", "foo", "bar", "test")

def suma(*numeros):
  total = 0

  for numero in numeros:
    total += numero

  return total

# def suma_2(a,b)
# def suma_3(a,b,c)
# ...
# def suma_l(list = [])

# print(suma(2,3,7,5,3,2,1,6))

# Kwargs

def print_data(**kwargs):
  for key, value in kwargs.items():
    print(key, " = ", value)

# print_data(nombre="Rafael", dni="12323532", grupo = "ds-g2")

# * y ** 

def test_args_kwargs(arg1, arg2, arg3):
  print("arg1: ", arg1)
  print("arg2: ", arg2)
  print("arg3: ", arg3)

args = ("dos", 3, 5)
# test_args_kwargs(*args)

# print()

kwargs = {"arg3": 3, "arg2":"dos", "arg1": 5}
# test_args_kwargs(**kwargs)

l1 = [1, 2, 3]
l2 = [4, 5]

l_concat = [*l1, *l2]
# print(l_concat)

a, *b, c = l_concat

# print(a, b, c)

# funcion (arg_posicionales, *argv, **kwargs)
print()

def funcion(a, b, *argv, **kwargs):
  print("a=", a)
  print("b=", b)

  for arg in argv:
    print("argv = ", arg)
  
  for key, value in kwargs.items():
    print(key, "=", value)

funcion(10, 20, 1,2,3,4, x="hola", y="que", z="tal?")
