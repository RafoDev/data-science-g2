import os

USERNAME = os.getenv("USERNAME")
print(USERNAME)

PATH = os.getenv("PATH").split(';')

for path in PATH:
  print(path)

print(len(PATH))
