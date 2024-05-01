from fastapi import FastAPI

# Documentation: https://fastapi.tiangolo.com/tutorial/first-steps/

app = FastAPI()


@app.get("/")
async def root():
  return {
    "ok": True,
    "message": "Hello World",
  }

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {
    "ok": True,
    "item_id": item_id,
  }
