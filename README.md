# Test task (upload image API)

## Технологии и требования
```
Python 3.9+
Django
Django REST Framework
Poetry
```

## Запуск проекта локально
```
1) Скачать проект с гитхаб
2) Установить зависимости c помощью poetry:
устанавливаем potry [документации poetry](https://python-poetry.org/docs/cli/)
- poetry shell
- poetry install
3) Создаем в корне .env и добавляем в него следующие данные:

DB_NAME=       # имя базы данных
POSTGRES_USER=        # логин для подключения к базе данных
POSTGRES_PASSWORD=       # пароль для подключения к БД (установите свой)
DB_HOST=      # название сервиса (контейнера)
DB_PORT=      # порт для подключения к БД

4) Разворачиваем и запускаем проект:
- docker compose up
- docker-compose exec web python manage.py migrate --noinput   # применяем миграции
- docker-compose exec web python manage.py createsuperuser     # создаем суперпользователя
- docker-compose exec web python manage.py collectstatic --no-input     # собираем статику

```

## Регистрация пользователя

```
Производится через API
http://127.0.0.1:8000/api/v1/auth/user/
Необходимые поля:
- username
- email
- password
```

## Загрузка картинки
Производится через API, доступна только авторизованным пользователям
(авторизация через username и password)
Ограничение по размеру картинки: 200кб
```
Производится через API
http://127.0.0.1:8000/api/v1/image/
Поддерживается загрузка нескольких фото одновременно, поэтому необходимо 
указывать нумерацию для поля image, даже если фотография одна:
[0]image, [1]image, ... 
```

## Автодокументация
```
http://127.0.0.1/api/schema/redoc/
```
