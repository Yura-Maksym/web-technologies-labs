# Confectionery API (Лабораторна робота №2)

Це REST API для каталогу кондитерської продукції, створене за допомогою FastAPI та SQLAlchemy.

## 🛠 Технологічний стек
* **Python 3.11+**
* **FastAPI** (веб-фреймворк)
* **SQLAlchemy** (ORM для роботи з БД)
* **SQLite** (база даних)
* **Uvicorn** (ASGI сервер)

## 📦 Встановлення та запуск

1. Клонуйте репозиторій.
2. Встановіть залежності:
   pip install fastapi "uvicorn[standard]" sqlalchemy
3. Запустіть сервер:
   uvicorn main:app --reload
4. Відкрийте документацію API у браузері: http://127.0.0.1:8000/docs