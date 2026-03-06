import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_absolute_success(client):
    """Mutlak deger basarili calisma"""
    res = client.get('/api/absolute/-10')
    assert res.status_code == 200
    assert res.json['result'] == 10

def test_api_absolute_invalid(client):
    """Absolute hata blogunu tetikleyen test (Except bloguna girer)"""
    res = client.get('/api/absolute/gecersiz_veri')
    assert res.status_code == 400

def test_api_factorial_success(client):
    """Faktöriyel basarili calisma"""
    res = client.get('/api/factorial/5')
    assert res.status_code == 200
    assert res.json['result'] == 120

def test_api_factorial_negative(client):
    """Factorial hata blogunu tetikleyen test (Negatif sayi)"""
    res = client.get('/api/factorial/-1')
    assert res.status_code == 422

def test_api_factorial_invalid(client):
    """Factorial hata blogunu tetikleyen test (Gecersiz tip)"""
    res = client.get('/api/factorial/abc')
    assert res.status_code == 422

def test_api_stability(client):
    """Hatalardan sonra API'nin calismaya devam etmesi"""
    client.get('/api/factorial/-1') 
    res = client.get('/api/absolute/5') 
    assert res.status_code == 200