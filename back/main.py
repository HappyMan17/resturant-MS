from fastapi import FastAPI
from config.env import env

# Documentation: https://fastapi.tiangolo.com/tutorial/first-steps/

app = FastAPI()


@app.get("/")
async def root():
  return {
    "ok": True,
    "message": "Hello World",
  }

@app.get("/port")
async def port():
  return {
    "ok": True,
    "message": f"running on port: { env['PORT'] }",
  }

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {
    "ok": True,
    "item_id": item_id,
  }
