# Saucedemo Playwright Tests

Автоматизированные UI-тесты для [saucedemo.com](https://www.saucedemo.com) на базе Playwright + pytest.

## 🛠 Стек

- **Python 3.12**
- **Playwright** — управление браузером
- **pytest** — запуск тестов
- **Allure** — отчёты
- **pytest-xdist** — параллельный запуск
- **GitHub Actions** — CI/CD

## 📁 Структура проекта

```
├── pages/          # Page Object Model — локаторы и методы страниц
├── logic/          # Flow — сценарии, Routes — URL константы
├── tests/          # Тест-файлы
├── config.py       # Конфигурация через переменные окружения
├── conftest.py     # Фикстуры и хуки pytest
└── .github/
    └── workflows/
        └── tests.yml  # CI/CD pipeline
```

## 🚀 Запуск локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Tative/saucedemo-playwright-tests.git
cd saucedemo-playwright-tests
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Настроить переменные окружения

Скопировать `.env.example` в `.env` и заполнить:

```bash
cp .env.example .env
```

```env
USER_NAME=standard_user
PASSWORD=secret_sauce
LOCKED_USER=locked_out_user
FIRST_NAME=John
LAST_NAME=Doe
POSTAL_CODE=12345
```

### 4. Запустить тесты

```bash
# Все тесты
pytest

# Только smoke
pytest -m smoke

# Только regression
pytest -m regression

# С Allure-отчётом
pytest --alluredir=allure-results
allure serve allure-results
```

## 📊 Allure-отчёт

Актуальный отчёт после каждого пуша в `main` доступен по ссылке:

🔗 https://tative.github.io/saucedemo-playwright-tests

## ✅ Покрытие

| Страница | Тесты |
|---|---|
| Авторизация | Успешная, невалидные данные, заблокированный пользователь |
| Инвентарь | Добавление товаров, количество товаров в корзине, удаление |
| Корзина | Стоимость, удаление товаров, навигация |
| Оформление заказа | Валидация полей, навигация |
| Обзор заказа | Суммы, налог, итог, навигация |
| Завершение заказа | Текст подтверждения, навигация |
