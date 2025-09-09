from fastapi import FastAPI
from src.items.router import router as item_router

app = FastAPI()
app.include_router(item_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


