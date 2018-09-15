# SCORE SERVICE - API

## Running In Development

After you clone this repository you should configure you database settings in `microservice\settings.py` by changing the lines bellow:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_C_NAME', 'database_c'),
        'USER': os.environ.get('DATABASE_C_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_C_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_C_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_C_PORT', '5432'),
    }
}

mongoengine.connect(
    db=os.environ.get('MONGODB_C_NAME', 'database_c'),
    host=os.environ.get('MONGODB_C_HOST', 'localhost')
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
> curl -X POST -d "grant_type=password&username=admin&password=123456@a" -u"u2zRtWvBiwrPwWewVd5aJVQAbyRfxURTqPSxiHkn:hsRxzLj0AKV8dbPUVakXMvs0iXoGw551Xw7ZNcNpJNuonSrpCns2vNiRmbSweu90tws16ye7T7JcaaFPxjkoTMFgwQNcokZQzetiLa0jKLhAd78CPA38lOshlPe8Pzym" http://localhost:8000/api/v1/auth/token/
> ```
>
>**Response**
>```json
>{
>    "access_token": "AUDgAyqX49cEpXtoDB10n5DQPos7SX", 
>    "expires_in": 36000, 
>    "token_type": "Bearer", 
>    "scope": "read write", 
>    "refresh_token": "ReOy4LwgEiEJCw1KkduGq01cqOKa41"
>}
