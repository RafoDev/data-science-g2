import requests
import os
from mysql import connector
from dotenv import load_dotenv

load_dotenv()

config = {
  "host" : "localhost",
  "user" : "root",
  "password" : os.getenv("DB_PASSWORD"),
  "database": "db_codigo"
}

def get_pokemon(pokemon_name):
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print("error:", requests.status_code)


def get_pokemons(count):
  url = f"https://pokeapi.co/api/v2/pokemon?limit={count}"

  response = requests.get(url)
  if response.status_code == 200:
    return response.json()["results"]
  else:
    print("error:", requests.status_code)

def insert_pokemons(pokemons):
  with connector.connect(**config) as db:
    with db.cursor() as cursor:
      try:
        cursor.execute(""" 
          create table pokemon(
            id int primary key unique,
            name varchar(100) unique,
            weight int,
            height int,
            base_experience int             
          )
        """)
      except Exception as error:
        print("Error:", error)
    
      for pokemon in pokemons: 
        
        pokemon_data = get_pokemon(pokemon["name"])
        
        id = pokemon_data["id"]
        name = pokemon_data["name"]
        weight = pokemon_data["weight"]
        height = pokemon_data["height"]
        base_experience = pokemon_data["base_experience"]

        try:

          query_insert = """
            insert into pokemon (id, name, weight, height, base_experience) 
            values (%s, %s, %s, %s, %s)
          """
          query_data = (id, name, weight, height, base_experience) 
          
          cursor.execute(query_insert, query_data)
          db.commit()
        except Exception as error:
          print("error: ", error)

# TO-DO! 
# def show_pokemons():

count_pokemons = int(input("Insertar la cantidad de pokemones a extraer: "))
pokemons = get_pokemons(count_pokemons)
insert_pokemons(pokemons)

# show_pokemons()