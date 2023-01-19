from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi import status
from main import app

app = FastAPI()

client = TestClient(app)

def test_read_main():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"msg": " "}
    return{"msg":" ","data": []}