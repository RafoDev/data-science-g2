import csv

filename = "data.csv"

with open(filename) as csv_file:
  # Reader construye listas por cada fila
  csv_reader = csv.reader(csv_file, delimiter=",")
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print("Columnas: ", row)
      line_count+=1
    else:
      print(row)
  
with open(filename) as csv_file:
  # DictReader construye diccionarios por cada fila 
  # a partir de los nombres de las columnas
  csv_reader = csv.DictReader(csv_file, delimiter=",")
  for row in csv_reader:
    print(row)