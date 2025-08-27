import pytest
from app import schemas


def test_get_all_todos(authorized_client, test_todos):
    res = authorized_client.get("/todos/")

    def validate(todo):
        return schemas.Todo(**todo)
    todos_map = map(validate, res.json())
    todos_list = list(todos_map)

    assert len(res.json()) == len(test_todos)
    assert res.status_code == 200

def test_unauthorized_user_get_all_todos(client, test_todos):
    res = client.get("/todos/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_todo(client, test_todos):
    res = client.get(f"/todos/{test_todos[0].id}")
    assert res.status_code == 401

def test_get_one_todo_not_exist(authorized_client, test_todos):
    res = authorized_client.get(f"/todos/88888")
    assert res.status_code == 404


def test_get_one_todo(authorized_client, test_todos):
    res = authorized_client.get(f"/todos/{test_todos[0].id}")
    todo = schemas.Todo(**res.json())
    assert todo.id == test_todos[0].id
    assert todo.description == test_todos[0].description
    assert todo.title == test_todos[0].title

@pytest.mark.parametrize("title, description", [
    ("awesome new title", "awesome new content"),
    ("favorite pizza", "i love pepperoni"),
    ("tallest skyscrapers", "wahoo"),
])
def test_create_todo(authorized_client, test_user, test_todos, title, description):
    res = authorized_client.post(
        "todos/", json={"title": title, "description": description})

    created_todo = schemas.Todo(**res.json())
    assert res.status_code == 201
    assert created_todo.title == title
    assert created_todo.description == description
    assert created_todo.owner_id == test_user['id']


def test_create_todo_default_published_true(authorized_client, test_user, test_todos):
    res = authorized_client.post(
        "todos/", json={"title": "arbitrary title", "description": "aasdfjasdf"})

    created_todo = schemas.Todo(**res.json())
    assert res.status_code == 201
    assert created_todo.title == "arbitrary title"
    assert created_todo.description == "aasdfjasdf"
    assert created_todo.owner_id == test_user['id']


def test_unauthorized_user_create_todo(client, test_user, test_todos):
    res = client.post(
        "todos/", json={"title": "arbitrary title", "description": "aasdfjasdf"})
    assert res.status_code == 401


def test_unauthorized_user_delete_todo(client, test_user, test_todos):
    res = client.delete(
        f"todos/{test_todos[0].id}")
    assert res.status_code == 401


def test_delete_todo_success(authorized_client, test_user, test_todos):
    res = authorized_client.delete(
        f"todos/{test_todos[0].id}")

    assert res.status_code == 204


def test_delete_todo_non_exist(authorized_client, test_user, test_todos):
    res = authorized_client.delete(
        f"todos/8000000")

    assert res.status_code == 404


def test_delete_other_user_todo(authorized_client, test_user, test_todos):
    res = authorized_client.delete(
        f"todos/{test_todos[3].id}")
    assert res.status_code == 403


def test_update_todo(authorized_client, test_user, test_todos):
    data = {
        "title": "updated title",
        "description": "updatd content",
        "id": test_todos[0].id

    }
    res = authorized_client.put(f"todos/{test_todos[0].id}", json=data)
    updated_todo = schemas.Todo(**res.json())
    assert res.status_code == 200
    assert updated_todo.title == data['title']
    assert updated_todo.description == data['description']


def test_update_other_user_todo(authorized_client, test_user, test_user2, test_todos):
    data = {
        "title": "updated title",
        "description": "updatd content",
        "id": test_todos[3].id

    }
    res = authorized_client.put(f"todos/{test_todos[3].id}", json=data)
    assert res.status_code == 403


def test_unauthorized_user_update_todo(client, test_user, test_todos):
    res = client.put(
        f"todos/{test_todos[0].id}")
    assert res.status_code == 401


def test_update_todo_non_exist(authorized_client, test_user, test_todos):
    data = {
        "title": "updated title",
        "description": "updatd content",
        "id": test_todos[3].id

    }
    res = authorized_client.put(
        f"todos/8000000", json=data)

    assert res.status_code == 404