import os
from mysql import connector
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

config = {
  "host" : HOST,
  "user" : USER,
  "password": PASSWORD
}
# Mala práctica
#conn = connector.connect(**config)
#conn.close()
try:
  with connector.connect(**config) as conn:
    print(conn)
except Exception as error:
    print("[ERROR]: ", error)
  