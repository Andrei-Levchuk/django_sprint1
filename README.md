# Автор

Андрей Левчук


# Название проектa

Blogicum

Краткое описание проекта:

Социальная сеть для публикации личных дневников.

Это сайт, на котором пользователь может создать свою страницу 
и публиковать на ней сообщения («посты»).

Пользователь может перейти на страницу любой категории и 
увидеть все посты, которые к ней относятся.

Пользователи могут заходить на чужие страницы, 
читать и комментировать чужие посты.


## Как развернуть локально

1. Склонировать репозиторий:

    git clone https://github.com/username/repository.git

2. Установить зависимости:

    pip install -r requirements.txt

3. Настроить базу данных (при наличии):

    python manage.py migrate

4. Запустить локальный сервер:

    python manage.py runserver
