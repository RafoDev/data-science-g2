
# file = open("file.txt", 'r')
# r: leer 
# r+: leer y escribir 
file = open("file.txt", 'r+')

# Para leer TODO el contenido del archivo
# content = file.read()
# print(content)

# Para leer UNA línea por vez
# line = file.readline()
# print(line)

# si un string está vacío es falsy
# Si es falsy, al evaluarlo va a resolver en false

# while True:
#   line = file.readline()
#   if len(line) > 0:  
#     print(line, end='')
#   else:
#     break

# lines = file.readlines()

# for line in lines:
#   print(line)

# for line in file:
#   print(line)

file.close()

# lectura bajo contexto (no es necesario cerrar el archivo)

# with open('file.txt') as file:
#   for line in file.readlines():
#     print(line, end='')

with open('file.txt') as file:
  print(file.read())


# r(read) - sólo leer
# r+ -> leer y escribir

# w(write) - sólo escribir
# w+ -> escribir y leer