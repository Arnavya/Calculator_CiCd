import pytest
from app.calculator import add, subtract, multiply, divide
from app import create_app


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_api_calculate():
    app = create_app()
    client = app.test_client()

    response = client.post("/calculate", json={"a": 8, "b": 4, "operation": "divide"})

    assert response.status_code == 200
    assert response.get_json()["result"] == 2
