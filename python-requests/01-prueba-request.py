import requests
import json

# Documentación oficial: https://requests.readthedocs.io/en/latest/

url = "https://randomuser.me/api/"

# métodos: get, post, patch, delete
response = requests.get(url)

if response.status_code == 200:
  print("[Success - 200]")
  # print(response.json())

  data = response.json()
  user = data["results"][0]
  
  
  print(user["gender"])
  print(user["name"]["first"])
  print(user["location"]["country"])
  
  # Para imprimir la data en forma de json
  print(json.dumps(data, indent=4))

else:
  print("error: ", response.status_code)

