## Описание API

API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности:

- Подписка и отписка от авторизованного пользователя;
- Создание, просмотр, удаление и изменение постов;
- Просмотр сообществ;
- Комментирование, просмотр, удаление и обновление комментариев;
- Фильтрация по полям.

## Установка

1. Клонировать репозиторий:

   ```bash
   git clone git@github.com:OlgaSHp/api_final_yatube.git
   ```

2. Перейти в папку с проектом:

   ```bash
   cd api_final_yatube/
   ```

3. Установить виртуальное окружение для проекта:

   ```bash
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```bash
   # для OS Lunix и MacOS
   source venv/bin/activate

   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```bash
   cd yatube_api
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Запустить проект:

   `python manage.py runserver`

## Как работает

- Для аутентификации используются JWT-токены.
- Для незарегистрированных пользователей доступ к API только на чтение
- Исключение — эндпоинт /follow/: доступ к нему возможен только аутентифицированным пользователям.  
- Аутентифицированным пользователям разрешено изменение и удаление своего контента;
  в остальных случаях доступ предоставляется только для чтения.


## Примеры запросов

Получение токена

Отправить POST-запрос на адрес `api/v1/jwt/create/` и передать 2 поля:

1. `username` - имя пользователя.
2. `password` - пароль пользователя.

Получить все посты

Отправить GET-запрос на адрес `api/v1/posts/`

Опубликовать пост

Отправить POST-запрос на адрес `api/v1/posts/`

1. Запрос:

   ```json
   {
     "text": "Новый текст"
   }
   ```

2. Ответ:

   ```json
   {
     "id": 2,
     "author": "Автор",
     "text": "Новый текст",
     "pub_date": "2019-08-24T14:15:22Z",
     "image": "строка",
     "group": 0
   }
   ```

Внесение обновлений в пост

Отправить POST-запрос на адрес `api/v1/posts/{post_id}/ и передать обязательные поля `id` и `text`, в заголовке указать `Authorization`:`Bearer <токен>`.

1. Запрос:

   ```json
   {
   "id": 1,
   "text": "текст",
   "image": "текст",
   "group": 0
   }
   ```

2. Ответ:

   ```json
   {
   "id": 1,
   "author": "текст",
   "text": "текст",
   "pub_date": "2019-08-24T14:15:22Z",
   "image": "текст",
   "group": 0
   }
   ```

## Подробная информация
http://localhost:8000/redoc/
