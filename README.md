# Crypto Currency News Site
###### Home Page
![Home Page](https://i.imgur.com/LdPzVGU.png)

###### News Page
![News Page](https://i.imgur.com/vJIfdui.png)

###### Prices Page
![Prices Page](https://i.imgur.com/ls8Q6hN.png)

## URL
In the process of deploying via Digital Ocean

# Setting up Development Environment
## Creating Virtual Environment
```
mkdir -p prj && cd prg
git clone https://github.com/HKSenior/crypto-news.git
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

## Future Upgrades
- [x] Use Celery to auto update database with new articles
- [ ] Add pagination to the home page news cards
- [ ] Allow users to sort news cards by date on news page
- [ ] Allow users to filter news cards by category
- [ ] Style news cards
- [ ] Style nav bar
- [ ] Add charts to price page