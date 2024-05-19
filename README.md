# Online Auctioning System

Simple Online auctioning rest api system 

## Rest APIs implemented:
```
User can register at: /authentication/register/
User can request token: /authentication/token/
User can refresh token: /authentication/token/refresh/
User can revoke token: /authentication/token/revoke/

User can create an item to auction/List all auction items: /api/item/
User can bid on an item: /api/bid/
```
## Setup steps:

create a virtual env with python3:

```commandline
python3 -m pip install venv
python3 -m venv venv310
```

Use virtual env:

```commandline
source venv310/bin/activate
```

Clone the repo:
```commandline
git clone https://github.com/itzmestar/auction_system
```

Install requirements:
```commandline
cd auction_system
python -m pip install -r requirements.txt
```

Create DB:
```commandline
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:
```commandline
python manage.py createsuperuser
```

## To Run local server:
```commandline
python manage.py runserver
```

this will run the webapp on localhost on port 8000

Access the API swagger docs here: http://127.0.0.1:8000/docs
