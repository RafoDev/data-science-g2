from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel, Field
from pydantic import BaseModel

DATABASE_URI = "mysql+mysqlconnector://root:1234@localhost/ml_db"
engine = create_engine(DATABASE_URI, echo=True)

class Housing(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  rooms: int
  price: float

class HousingCreate(BaseModel):
  rooms: int
  price: float

class HousingCreate(HousingCreate):
  id: int

SQLModel.metadata.create_all(bind=engine)

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