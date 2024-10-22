<h1 align="center">Django_Celery_Redis</h1>

В рамках данного проекта было создано простое приложение на Django с использованием Celery, Redis и Celery beat. Приложение это минимальны блог в котором можно создать посты от разных пользователей(используется кастомная модель), которых нужно верифицировать через email. Создана задача в Celery, а так же реализовано ежедневное уведомление через Celery beat на почту сколько просмотров у вашего поста.

Цель проекта — хотелось поработать с Celery и Redis'ом как брокер сообщений.
___

<h2 align="center">Установка</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/SergeiMischenko/django_celery.git
    ```

2. **Перейдите в папку проекта:**
    ```bash
    cd django_celery
    ```

3. **Установите виртуальное окружение и активируйте его:**
    ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows
    ```

4. **Установите необходимые зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Откройте файл .env и заполнить его своими данными**
    ```env
    SECRET_KEY = 'your-secret-key'
   
    EMAIL_HOST_USER = "xxxxxxxxxxxxxxxxxxxxxx"
    EMAIL_HOST_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxx"
    ```

6. **Выполните миграции базы данных:**
    ```bash
    python manage.py migrate
    ```

7. **Запустите сервер разработки Redis, Celery, Celery beat:**
    ```bash
    python manage.py runserver
   
    redis-server
   
    celery -A publish worker --loglevel=info              # Для Linux и macOS
    celery -A publish worker -P eventlet --loglevel=info  # Для Windows
   
    celery -A publish beat
    ```

8. **Доступ к приложению:**
   
    После завершения всех вышеуказанных шагов, вам нужно создать несколько постов через админку или shell и приложение будет доступно по адресу [http://127.0.0.1:8000/slug_name_post/](http://127.0.0.1:8000/slug_name_post/).

    `/slug_name_post/` - slug вашего поста.
