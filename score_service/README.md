# SCORE SERVICE - API

## Running In Development

After you clone this repository you should configure you database settings in `microservice\settings.py` by changing the lines bellow:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_B_NAME', 'database_b'),
        'USER': os.environ.get('DATABASE_B_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_B_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_B_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_B_PORT', '5432'),
    }
}

mongoengine.connect(
    db=os.environ.get('MONGODB_B_NAME', 'database_b'),
    host=os.environ.get('MONGODB_B_HOST', 'localhost')
)
```

To start your Django Framework:

  * Run `pip3 install -r requirements.txt`;
  * Install PosgreSQL and create the database configured;
  * Install MongoDB and create the database configured;
  * Run `python3 manage.py migrate`;
  * Run `python3 manage.py runserver`;

## Testing

  * To run the unit test use `python3 manage.py test`;
  * To run the coverage test use `coverage run --source="." manage.py test && coverage report`;

## Code quality

  * To run the prospector test use `prospector --uses django apps/`;
  * To run the pylint test use `pylint --load-plugins pylint_django apps/`;

## Some exemples with curls

### Get a token

```
POST /api/v1/auth/token/
```

>**Curl**
> 
> ```shell
> curl -X POST -d "grant_type=password&username=admin&password=123456@a" -u"TxwppGEWeZIYQu0c3urTeTg3tDYx2LXpROGm9K70:g8p9wpIrPuzI817iMU61fQNhlhVb9SQCAyzGtuPaqOFPFayOG3gp0w5cEBmWgaD8G1cy9tDer4Rwz5awuMJ90Oon00z9w811AXP25OK3sMA7Vr63WebIWizZ1PVCA3gg" http://localhost:8000/api/v1/auth/token/
> ```
>
>**Response**
>```json
>{
>    "access_token": "rHsoOQWPnJfXw0S24la3HlBJk6YLdr", 
>    "expires_in": 36000, 
>    "token_type": "Bearer", 
>    "scope": "read write", 
>    "refresh_token": "2CrgldBvZQbG1HbS9dLIFAkiE8ns3X"
>}
