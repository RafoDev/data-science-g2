from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Mi primer api con FastApi"}