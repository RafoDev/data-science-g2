def divide(a, b):
  try:
    result = a/b
  except Exception as error:
    print(f"error: {error}")
  else:
    return result

divide(a = 4, b = "aaa")

print("hola")
print(divide(4,1))

try:
  file = open('archivo.txt')
except:
  print("Un error inesperado!!")