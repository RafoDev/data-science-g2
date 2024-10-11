# w - reemplaza el contenido 

# f = open('file.txt', 'w')
f = open('file.txt', 'w+')

f.write('Hola')
f.writelines(['hola\n', 'como\n', 'estas\n'])

f.seek(0)

print(f.read())