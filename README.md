Краткое описание финального проекта по API
API для Yatube - это учебный проект по API приложения Yatube

Используемые технологии и библиотеки:
DRF

sqlite

djoser

requests

pytest

Установка и настройки:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/yandex-praktikum/api_final_yatube.git
cd api_final_yatube
Cоздание и активация виртуального окружения:

python -m venv env
source venv/Scripts/activate
Установка зависимостей из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Применение миграций:

python3 manage.py migrate
Запуск django сервера:

python manage.py runserver
Заполнение базы данных из CSV:
Перейти в диреторию postman_collection и запустить bash-скрипт

set_up_data.sh
Документация:
Документация API доступна по адресу:

http://127.0.0.1:8000/redoc/
Примеры запросов к API:
Получение публикаций
Получить список всех публикаций.

GET-запрос на эндпоинт:

http://127.0.0.1:8000/api/v1/posts/
Создание публикации
Добавление новой публикации в коллекцию публикаций.

POST-запрос на эндпоинт:

http://127.0.0.1:8000/api/v1/posts/
Получение публикации
Получение публикации по id.

GET-запрос на эндпоинт:

http://127.0.0.1:8000/api/v1/posts/{id}/
Обновление публикации
Обновление публикации по id.

PUT-запрос на эндпоинт:

http://127.0.0.1:8000/api/v1/posts/{id}/
Подписки
Возвращает все подписки пользователя, сделавшего запрос.

GET-запрос на эндпоинт:

http://127.0.0.1:8000/api/v1/follow/
Разработчики:
Нижегородова Людмила

https://github.com/LyudmilaN-3# qa_python_sprint_5
