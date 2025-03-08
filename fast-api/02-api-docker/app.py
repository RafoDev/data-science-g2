from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
  return {"message": "🐋 Dockerized FastAPI v1.0"}