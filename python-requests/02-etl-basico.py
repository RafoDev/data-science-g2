import requests
import json

# Documentación oficial: https://requests.readthedocs.io/en/latest/

url = "https://randomuser.me/api/"

# EXTRACT: de una api

# métodos: get, post, patch, delete
response = requests.get(url)

if response.status_code == 200:
  print("[Success - 200]")
  # print(response.json())
  data = response.json()
  user = data["results"][0]

  # TRANSFORM
  dic_user = {
    "name" : user["name"]["first"] + " " + user["name"]["last"],
    "country" : user["location"]["country"],
    "email": user["email"],
    "photo_url": user["picture"]["thumbnail"]
  }

  for key, value in dic_user.items():
    # print(f"{key} : {value}")
    print(key, " : ", value)

  # LOAD

  data_dir_path = "users/data/"
  user_filename = dic_user["name"].replace(" ", "_")

  with open(data_dir_path + user_filename + ".json", "w") as user_file:
    user_file.write(json.dumps(dic_user, indent=4))

else:
  print("error: ", response.status_code)