import csv
from prefect import task

@task(name="Extraer info de csv")
def task_extract_csv(filename):
  data = []
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      tmp_data = (row["dni"], row["celular"])
      data.append(tmp_data)
  
  return data