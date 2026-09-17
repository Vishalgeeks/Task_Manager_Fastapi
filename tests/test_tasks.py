from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Task Management API" in response.json()["message"]


def test_register():
    response = client.post("/auth/register/", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login():
    response = client.post("/auth/login/", data={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_task():
    client.post("/auth/register/", json={
        "username": "taskuser",
        "email": "task@example.com",
        "password": "password123"
    })
    login_resp = client.post("/auth/login/", data={
        "username": "taskuser",
        "password": "password123"
    })
    token = login_resp.json()["access_token"]
    
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "A test task"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"


def test_read_tasks():
    client.post("/auth/register/", json={
        "username": "readuser",
        "email": "read@example.com",
        "password": "password123"
    })
    login_resp = client.post("/auth/login/", data={
        "username": "readuser",
        "password": "password123"
    })
    token = login_resp.json()["access_token"]
    
    response = client.get(
        "/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)