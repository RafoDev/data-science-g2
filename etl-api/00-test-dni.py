import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("APIPERU_TOKEN")

url_dni = "https://apiperu.dev/api/dni"

dni = {
  "dni" : "71040931"
}

headers = {
  "Authorization" : "Bearer " + token,
  "Content-Type" : "application/json"
}

response = requests.post(url_dni, json=dni, headers=headers)

if response.status_code == 200:
  print(response.json())
else:
  print("error: ", response.status_code)