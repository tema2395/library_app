# Library App

Это приложение для управления библиотекой, написанное на FastAPI и SQLAlchemy.

## Требования

- Python 3.12.2
- [Poetry](https://python-poetry.org/docs/#installation)
- PostgreSQL 16.2

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

### Шаг 3: Создание env.py

В корневой директории проекта создать файл env.py со следующей структурой:
```
HOST = 'localhost'
PORT = 5432
USER = 'user_name'
PASSWORD = 'psw'
```
 - `HOST` - Хост бд
 - `PORT` - Порт бд
 - `USER` - Ваш юзернейм бд
 - `PASSWORD` - Ваш пароль от бд

### Шаг 4: Запуск приложения

```sh
poetry run uvicorn app.main:app --reload
```