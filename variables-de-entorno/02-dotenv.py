import os
from dotenv import load_dotenv

load_dotenv()

MYVAR = os.getenv("MYVAR")
PASSWORD = os.getenv("DB_PASSWORD")

print(MYVAR)
print(PASSWORD)