from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item_without_query():
    response = client.get("/items/42")

    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


def test_read_item_with_query():
    response = client.get("/items/5", params={"q": "taco"})

    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "taco"}


def test_read_item_rejects_non_integer_id():
    response = client.get("/items/abc")

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["path", "item_id"]


def test_unknown_route_returns_404():
    response = client.get("/nao-existe")

    assert response.status_code == 404
