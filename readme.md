# worldbankapi

worldbankapi is a Python 3 + Django Project designed and built for managing the world's most populous
countries data provided by worldbank.com.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Installing

### Clone the project

Run, in the CLI:
```bash
git clone https://github.com/ezequielsalas/worldbankapi.git
```

Then, move to the project:
```bash
cd worldbankapi
```

Install dependencies
```bash
pip install -r requirements.txt
```

Prepare the database
```bash
python manage.py migrate
```

## Deployment

```bash
python manage.py runserver 8080
```


## Built With

* [Django REST framework](https://github.com/encode/django-rest-framework) - Web Framework


## Authors

**Ezequiel Salas**

