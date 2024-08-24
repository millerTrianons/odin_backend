# 
# INTEGRATION TESTS
# 

from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_ping_pong():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


