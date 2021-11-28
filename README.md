# Squid Room
Platform for 1 on 1 battles of Splatoon.

## Requirement
* Python 3.9.6
* Django 3.2.9

## Installation
```
pip install -r requirements.txt
```

## Usage
1. Clone repository.
```
git clone https://github.com/ishikawa16/squidroom.git
```

2. Generate secret key.
```
cd squidroom/config
python generate_secretkey_setting.py > local_settings.py
```

3. Initialize databases.
```
cd ..
python manage.py makemigrations accounts
python manage.py makemigrations rooms
python manage.py migrate
```

4. Set up server.
```
python manage.py runserver
```
