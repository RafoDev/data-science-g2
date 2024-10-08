import csv
from prefect import task
from config import config
import requests

@task(name="Extraer info de csv")
def task_extract_csv(filename):
  data = []
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      tmp_data = (row["dni"], row["celular"])
      data.append(tmp_data)
  
  return data

@task(name="Extraer data de dni")
def task_extract_dni(dni):
  token = config.API_TOKEN
  headers = {
    "Authorization" : "Bearer " + token,
    "Content-Type" : "application/json"
  }

  data = {
    "dni" : dni
  }
  url_dni = config.ENDPOINTS["dni"]
  response = requests.post(url_dni, json=data, headers=headers)

  if response.status_code == 200:
    if response.json()["success"]:
      data = response.json()["data"]
      nombres = data["nombres"]
      apellidos = data["apellido_paterno"] + " " + data["apellido_materno"]
      return (nombres, apellidos)
    else:
      # TODO: handle_invalid_dni()
      pass
  else:
    print("error: ", response.status_code)