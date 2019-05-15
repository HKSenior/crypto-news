<h2 align="center">Crypto Currency News Site</h2>

![Home Page](https://i.imgur.com/DMICJcQ.jpg)

## URL
<https://www.hassani-cryptonews.com>

# Setting up Development Environment
## Creating Virtual Environment
```
mkdir -p prj && cd prg
git clone -b dashboard https://github.com/HKSenior/crypto-news.git
virtualenv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

###### To exit the Virtual Environment
```
deactivate
```

## Starting Workers and the Beat (Celery)
```
celery -A {your project} worker -l info -B
```

This method of starting the workers and beat is solely for development
purposes. In production, daemonization is the prefered solution.

## Collecting static files
```
python manage.py collectstatic
```

## Starting the server
```
python manage.py runserver
```

# Setting up .env config file
###### Django Configuration
- SECRET_KEY
- ALLOWED_HOSTS
- DEBUG

###### Database Configuration (PostgreSQL)
- DB_ENGINE
- DB_USER
- DB_HOST
- DB_PASSWORD
- DB_ENGINE

###### Celery Configuration
- CELERY_ENABLE_UTC
- CELERY_BROKER_URL
- CELERY_TIMEZONE
- CELERY_TASK_SERIALIZER
- CELERY_RESULT_SERIALIZER