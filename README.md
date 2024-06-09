# Library App

Это приложение для управления библиотекой, написанное на FastAPI и SQLAlchemy.

## Требования

- Python 3.12.2
- [Poetry](https://python-poetry.org/docs/#installation)

## Установка и запуск

### Шаг 1: Клон репозитория

Сначала клонируйте репозиторий и перейдите в директорию проекта:

```sh
git clone <URL репозитория>
cd library_app
```

### Шаг 2: Установка зависимостей

Установите зависимости и активируйте виртуальное окружение

```sh
poetry install
poetry shell
```

### Шаг 3: Запуск приложения

```sh
poetry run uvicorn app.main:app --reload
```