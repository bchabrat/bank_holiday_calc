from fastapi.testclient import TestClient
from main import app
import pandas as pd

client = TestClient(app)
rota_data = pd.read_csv("rota_schedule.csv")


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == list(rota_data['rota_name'].unique())


def test_calc():
    response = client.get("/calc", params={'rota_name': "Week 1 friday off"})
    assert response.status_code == 200
    assert response.json() == 11

