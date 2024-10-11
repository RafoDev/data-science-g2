# 1. Máximo de Números: Crea una función que acepte cualquier cantidad de números y devuelva el número más grande. (args)

def max_numero(*args):
  return max(args)

# print(max_numero(3,2,4,5,4,2))

def max_numero_cris(*numeros):
  n_max = numeros[0]
  for num in numeros:
    if num > n_max:
      n_max = num
  return n_max

# numeros = input("Ingresa números separados por comas: ")

# EXTRA: list comprenhension

# num = [int(numero) for numero in numeros.split(",")]
# num = []
# "1,2,3,4,5" después del split -> ["1","2","3","4","5"]
# for numero in numeros.split(","):
#   num.append(int(numero))

# print(max_numero_cris(*num))


# 2. Configuración de Usuario: Escribe una función que acepte el nombre de un usuario y diferentes opciones (por ejemplo, color favorito, altura, idioma, etc.), y luego imprima la configuración completa del usuario.

def config_user(username, **config):
  print(f"Config for {username}:")
  for key, value in config.items():
    print(f"{key} : {value}")

config_rafa = {
  "theme" : "Dark", 
  "terminal" : "hidden", 
  "font_size" : "25"
}

config_user("Rafael", **config_rafa)


# 3. Concatenación de Strings: Crea una función que reciba varios strings como argumentos y los concatene en una sola cadena de texto.

def concatenar_strings(*args):
  return " ".join(args)

print(concatenar_strings("Hola", "mundo", "!"))  # Output: 'Hola mundo !'


# 4. Registrar Pedido en Restaurante: Crea una función que acepte una cantidad variable de platos (con *args) y opciones adicionales (como salsas, tamaño de porción, etc., usando **kwargs), y luego registre el pedido.

def registrar_pedido(*args, **kwargs):
  print("Platos pedidos:")
  for plato in args:
      print(f"- {plato}")

  print("\nOpciones adicionales:")
  for opcion, valor in kwargs.items():
      print(f"{opcion}: {valor}")

registrar_pedido("Pizza", "Ensalada", salsa="BBQ", tamaño="Grande")
# Output:
# Platos pedidos:
# - Pizza
# - Ensalada
#
# Opciones adicionales:
# salsa: BBQ
# tamaño: Grande