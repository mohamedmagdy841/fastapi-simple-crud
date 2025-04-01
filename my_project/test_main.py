from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", data={"username": "test", "password": "test"})
    assert response.status_code == 200
    json = response.json()
    assert "access_token" in json
    assert json["token_type"] == "bearer"

def test_create_article():
    auth = client.post("/login", data={"username": "test", "password": "test"})
    assert auth.status_code == 200
    access_token = auth.json().get("access_token")
    assert access_token

    response = client.post("/articles/", 
        json={
            "title": "Test article",
            "content": "Test content",
            "is_published": True,
            "user_id": 1
            },
            headers= {
            "Authorization": "bearer " + access_token
        }
    )

    assert response.status_code == 200
    assert response.json().get("title") == "Test article"
