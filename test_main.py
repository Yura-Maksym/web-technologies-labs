from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


# 1. Unit-тест: Перевірка отримання списку продуктів
def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 2. Performance-тест + Складний сценарій
def test_complex_scenario_performance():
    start_time = time.time()

    # Крок А: Створюємо категорію
    cat_response = client.post("/categories/", json={"name": "Тестова Категорія"})
    assert cat_response.status_code == 201
    category_id = cat_response.json()["id"]  # Беремо результат першого запиту

    # Крок Б: Використовуємо ID категорії як вхідні дані для створення продукту
    prod_response = client.post("/products/", json={
        "name": "Тестова Цукерка",
        "price": 50.5,
        "category_id": category_id
    })
    assert prod_response.status_code == 201

    end_time = time.time()
    execution_time = end_time - start_time

    # Перевіряємо, що весь складний ланцюжок запитів виконався швидше ніж за 1 секунду
    assert execution_time < 1.0