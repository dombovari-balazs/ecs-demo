from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.items.router import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_read_main():
    item_id = 2

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.text == '{"item_id":'+str(item_id)+',"q":null}'
    