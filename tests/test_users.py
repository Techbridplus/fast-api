import pytest
from app import schemas

def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == "test@example.com"
    assert "id" in response.json()

def test_get_user(client):
    # First create a user
    response = client.post(
        "/users/",
        json={"email": "testget@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    
    user_id = response.json()["id"]
    
    # Then get the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    user = schemas.UserOut(**response.json())
    assert user.email == "testget@example.com"
    assert user.id == user_id

def test_get_user_not_exist(client):
    response = client.get("/users/999")
    assert response.status_code == 404
