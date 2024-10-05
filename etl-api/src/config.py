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

config = Config()