# ToDo App

### Используемые технологии:
- Django
- SQLite3

### Перед запуском выполните:
- Склонировать репозиторий в локальную директорию:
```
git clone git@github.com:olga3ok/todoapp.git
```
- Активация виртуального окружения и установка зависимостей из requirements.txt:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
cd todoapp
```
```
pip install -r requirements.txt
```
- Cоздание миграций, а также их применение:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- Запуск:
```
python manage.py runserver
```
