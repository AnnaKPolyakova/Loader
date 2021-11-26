# Test task (upload image API)

## Технологии и требования
```
Python 3.9+
Django
Django REST Framework
```

## Запуск проекта локально
```
1) Скачать проект с гитхаб
2) Установить зависимости:
python -m pip install --upgrade pip
pip install -r requirements.txt
3) Применить миграции:
python manage.py migrate
4) Запустить проект:
python manage.py runserver
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
Необходимые поля:
- image
```

## Автодокументация
```
http://127.0.0.1:8000/api/schema/redoc/
```