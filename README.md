# Test task (upload image API)

## Технологии и требования
```
Python 3.9+
Django
Django REST Framework
Poetry
```

## Запуск проекта 
```
1) Скачать проект с гитхаб
2) Создаем в корне .env и добавляем в него следующие данные:

DB_NAME=       # имя базы данных
POSTGRES_USER=        # логин для подключения к базе данных
POSTGRES_PASSWORD=       # пароль для подключения к БД (установите свой)
DB_HOST=db      # название сервиса (контейнера)
DB_PORT=5432      # порт для подключения к БД

4) Разворачиваем и запускаем проект:
- docker compose up
- docker-compose exec web python manage.py migrate --noinput   # применяем миграции
- docker-compose exec web python manage.py createsuperuser     # создаем суперпользователя
- docker-compose exec web python manage.py collectstatic --no-input     # собираем статику

```

## Регистрация пользователя

```
Производится через API
http://127.0.0.1/api/v1/auth/user/
Необходимые поля:
- username
- email
- password
```

## Загрузка картинок
Производится через API, доступна только авторизованным пользователям
(авторизация через username и password)
Ограничение по размеру картинки: 200кб
```
Производится через API
http://127.0.0.1/api/v1/image/
Поддерживается загрузка нескольких фото одновременно, поэтому необходимо 
указывать нумерацию для поля image, даже если фотография одна:
[0]image, [1]image, ... 
```

## Автодокументация
```
http://127.0.0.1/api/schema/redoc/
```
## Тесты
```
- docker-compose exec pytest

Тесты можно запустить локально без docker, для этого необходимо создать и 
активировать venv с помощью poetry:
- python -m venv venv
- source venv/bin/activate
- устанавливаем poetry (документации с информацией по установке https://python-poetry.
  org/docs/cli/)
- poetry install
- pytest
```
