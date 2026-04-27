# Використовуємо офіційний образ Python
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо всі файли проєкту в контейнер
COPY . /app

# Встановлюємо залежності
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic

# Відкриваємо порт 8000
EXPOSE 8000

# Команда для запуску сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]