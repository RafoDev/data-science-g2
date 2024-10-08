import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  MYSQL_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : os.getenv("DB_PASSWORD"),
    "database" : "db_codigo"
  }

  ENDPOINTS = {
    "dni" : "https://apiperu.dev/api/dni",
    "ruc" : "https://apiperu.dev/api/ruc"
  }

  API_TOKEN = os.getenv("APIPERU_TOKEN")

config = Config()