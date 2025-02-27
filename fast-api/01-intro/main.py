from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Mi primer api con FastApi"}

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
  return {"message": f"Hola {nombre}"}

@app.get("/suma/{n1}/{n2}")
async def suma(n1: int, n2: int):
  resultado = n1 + n2
  return {"message": f"La suma de {n1} y {n2} es {resultado}"}