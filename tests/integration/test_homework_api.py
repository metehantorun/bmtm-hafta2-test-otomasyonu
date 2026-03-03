import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_abs(client):
    res = client.get('/api/absolute/-10')
    assert res.status_code == 200
    assert res.json['result'] == 10

def test_api_fact(client):
    res = client.get('/api/factorial/5')
    assert res.status_code == 200
    assert res.json['result'] == 120

def test_api_fact_neg(client):
    res = client.get('/api/factorial/-1')
    assert res.status_code == 422

def test_api_fact_invalid(client):
    res = client.get('/api/factorial/abc')
    assert res.status_code == 422

def test_api_stability(client):
    client.get('/api/factorial/-1')
    res = client.get('/api/absolute/5')
    assert res.status_code == 200