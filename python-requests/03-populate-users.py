import os
import requests
from mysql import connector
from dotenv import load_dotenv

load_dotenv()

config = {
  "host" : "localhost",
  "user" : "root",
  "password" : os.getenv("DB_PASSWORD"),
  "database": "db_codigo"
}

url_one = "https://randomuser.me/api/" # Nos devuelve 1 usuario random

# EXTRACT
def get_random_users(count = 1):
  url_many = f"https://randomuser.me/api/?results={count}" # Nos devuelve 'count' número de usuarios

  response = requests.get(url_many)
  if response.status_code == 200:
    users = response.json()["results"]
    return users
  else:
    print("error: ", response.status_code)
    return []

def insert_users(users):
  try:
    with connector.connect(**config) as db:
      with db.cursor() as cursor:        
        try:
          cursor.execute("""
          create table user(
            id int auto_increment primary key,
            name varchar(255),
            email varchar(255),
            country varchar(255),
            photo_url varchar(255)
          )
          """)
        except Exception as error:
          print("error: ", error)
        
        # TRANSFORM
        for user in users:
          name = user["name"]["first"] + " " + user["name"]["last"]
          email = user["email"]
          country = user["location"]["country"]
          photo_url = user["picture"]["thumbnail"]

          # LOAD
          insert_query = """
            insert into user(name, email, country, photo_url) 
            values (%s, %s, %s, %s)
          """

          data = (name, email, country, photo_url)

          cursor.execute(insert_query, data)
          db.commit()

  except Exception as error:
    print("error: ", error)

count_users = int(input("Inserte la cantidad de usuarios a extraer: "))
users = get_random_users(count_users)

insert_users(users)