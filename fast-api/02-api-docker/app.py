from fastapi import FastAPI
from housing_predictor.housing_predictor import HousingModel
from pydantic import BaseModel

app = FastAPI()
housing_model = HousingModel()

class HousingInput(BaseModel):
  rooms: int

@app.get("/")
async def index():
  return {"message": "🐋 Dockerized FastAPI v1.1"}
  
@app.post("/housing")
async def housing_predictor(input: HousingInput):
  rooms = input.rooms
  price = housing_model.predict(rooms)
  return {"rooms": rooms, "price": price}
