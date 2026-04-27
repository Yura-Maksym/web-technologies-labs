from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Запуск автоматичного скрапера...")

# Налаштування браузера (автоматично завантажить потрібний драйвер)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 1. Відкриваємо сторінку
    driver.get("http://127.0.0.1:8000/")
    time.sleep(2)  # Чекаємо, поки завантажиться

    # 2. Авторизація
    print("Вводимо логін та пароль...")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)  # Чекаємо переходу на сторінку каталогу

    # 3. Зчитуємо дані
    print("\n--- Зібрані дані з каталогу ---")
    products = driver.find_elements(By.TAG_NAME, "li")

    if not products:
        print("Каталог порожній.")
    else:
        for p in products:
            print("-", p.text)
    print("-------------------------------")

finally:
    time.sleep(2)
    driver.quit()  # Закриваємо браузер
    print("Скрапінг завершено.")