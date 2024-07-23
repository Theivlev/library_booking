# Cервис library_booking

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Асинхронность](https://img.shields.io/badge/-Асинхронность-464646?style=flat-square&logo=Асинхронность)]()
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat-square&logo=JWT)]()
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat-square&logo=Alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat-square&logo=SQLAlchemy)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/-Redis-464646?style=flat-square&logo=Redis)](https://redis.io/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat-square&logo=uvicorn)](https://www.uvicorn.org/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)

## Описание

API бронирование книг.

### Доступный функционал

- Регистрация пользователей с помощью библиотеки fastapi-users.
- Аутентификация реализована с помощью JWT-токена.
- Создание объектов разрешено только аутентифицированным пользователям.
- Кеширование с помощью Redis.
- Возможность развернуть проект в Docker-контейнерах.
- slowapi для ограничения количества запросов

#### Локально документация доступна по адресу: <http://127.0.0.1:8000/docs#/>
#### В контейнерах Docker документация доступна по адресу: <http://localhost:7777/docs/>  

#### Технологии

- Python 3.12
- FastAPI
- fastapi-cache2
- Асинхронность
- JWT
- Alembic
- SQLAlchemy
- Docker
- PostgreSQL
- Asyncpg
- Redis
- Uvicorn
- Gunicorn

#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
    git clone <название репозитория>
```

Cоздать и активировать виртуальное окружение:

Команды для установки виртуального окружения на Mac или Linux:

```bash
    python3 -m venv env
    source env/bin/activate
```

Команды для Windows:

```bash
    python -m venv venv
    source venv/Scripts/activate
```

- Перейти в директорию app:

```bash
    cd /app
```

- Создать файл .env по образцу:

```bash
    cp .env.example .env
```

- Установить зависимости из файла requirements.txt:

```bash
    cd ..
    pip install -r requirements.txt
```

- Для создания миграций выполнить команду:

```bash
    alembic init --template async alembic
```

- В папку alembic в env файл вставьте следующий код:

```bash


# import os для работы с sqlite
import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context
from app.core.base import Base
from app.core.config import settings
#from dotenv import load_dotenv для работы с sqlite

config = context.config

# для sqlite
# config.set_main_option('sqlalchemy.url', os.environ['DATABASE_URL_LITE'])

config.set_main_option('sqlalchemy.url', f'{settings.DATABASE_URL}?async_fallback=True')

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
print(target_metadata.tables) # вывод для просмотра FacadeDict, можно убрать

```

- Инициализировать БД:

``` bash
    alembic revision --autogenerate -m "First migration"   
```

- Применить миграцию:

``` bash
    alembic upgrade head 
```

- Запустить проект:

``` bash
    uvicorn main:app --reload    
```

- Запустить Redis:

``` bash
    redis-server.exe 
    redis-cli.exe  
```

#### Запуск в контейнерах Docker

- Предварительно необходимо установить Docker для вашей системы.

- у нас есть alembic и прописаны настройки в файле env.py(код выше)

- Находясь в главной директории проекта:

- Создать файл .env-docker по образцу:

```bash
   cp .env-docker-example .env-docker 
```

- Запустить проект:

``` bash
    docker-compose up -d --build  
```

### В контейнерах Docker документация по адресу: <http://localhost:7777/docs/>


```


#### Примеры некоторых запросов API
Функциональность:

- Регистрация нового пользователя

```

POST - '/auth/register/'

```

- Авторизация пользователя

```

POST - 'auth/jwt/login/'

```


#### - Создание бронирование книги

```
POST - '/bookings/'
```

```
```
#### - Получение списка активных броней

```
GET - '/bookings/active'
```


#### - Получение конкретной брони

```
POST - '/bookings/{booking_id}/'
```

#### - Удаление брони

```
DELETE - '/bookings/{booking_id}/'
```

#### Автор

Ивлев Алексей Константинович 
Python-разработчик (Backend)   
E-mail: theivlev@yandex.ru  

[https://github.com/Theivlev]

