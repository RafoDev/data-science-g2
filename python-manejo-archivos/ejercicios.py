
# Función que solicite al usuario ingresar varias lineas 
# de texto y guarde ese contenido en un archivo nuevo

with open('salida.txt', 'w') as file:
  while True:
    linea = input("Ingresa una línea de texto (o escribe 'salir' para terminar): ")
    if linea.lower() == 'salir':
      break
    file.write(linea + '\n')
  # file.close()

# Copiar contenido entre 2 archivos

with open('archivo.txt', 'r') as fuente:
    with open('copia.txt', 'w') as destino:
        for linea in fuente:
            destino.write(linea)