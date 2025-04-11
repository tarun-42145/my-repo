import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home_route(client):
    res = client.get('/')
    assert res.status_code == 200

def test_calculator_route(client):
    res = client.get('/calculator/')
    assert res.status_code == 200
