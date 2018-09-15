# CUSTOMER SERVICE - API

## Running In Development

After you clone this repository you should configure you database settings in `microservice\settings.py` by changing the lines bellow:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_A_NAME', 'database_a'),
        'USER': os.environ.get('DATABASE_A_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_A_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_A_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_A_PORT', '5432'),
    }
}
```

To start your Django Framework:

  * Run `pip3 install -r requirements.txt`;
  * Install PosgreSQL and create the database configured;
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
> curl -X POST -d "grant_type=password&username=admin&password=123456@a" -u"WhBJZN9m8dJ63cF30U0NeU7hMO0cG84yj2SHZA12:YM19g9A3E87ia1zDiPNvyr3nUvmDhZHNl2KrnEKAuudKNXLnQVHzYsnYBaVSknVUZVJB27L73VPWyoYtTd1aKhLgcTDCNW7fg02y6bGO3Lda6PnRPaFR3DguwdkIXZqU" http://localhost:8000/api/v1/auth/token/
> ```
>
>**Response**
>```json
>{
>    "access_token": "vnKHstGVI78DpzJW7nBZaOvRFJLJ5s", 
>    "expires_in": 36000, 
>    "token_type": "Bearer", 
>    "scope": "read write", 
>    "refresh_token": "5SLIsGoeiYmVpNYTOPeZblKuPumjLU"
>}

---

### Get the customers list

```
POST /api/v1/customers/
```

You can filter by the fields using like these : `?cpf=111222444555`

>**Curl**
> 
> ```shell
> curl -X GET -H "Authorization: Bearer bg6Ikaf2LHSzTu4TZl5aYIFWRNWeH8" "http://localhost:8000/api/v1/customers/"
> ```
>
>**Response**
>```json
>[
>    {
>        "id":1,"full_name":"Luiz Carlos",
>        "cpf":"12345678950",
>        "email":"luiz@luiz.com"
>    },
>    {
>        "id":2,
>        "full_name":"Maria Lucia",
>        "cpf":"12547896325",
>        "email":"maria@maria.com"
>    },
>    {
>        "id":3,
>        "full_name":"João Pedro",
>        "cpf":"12698745236",
>        "email":"joao@joao.com"
>    },
>    {
>        "id":4,
>        "full_name":"Guilherme Damasceno",
>        "cpf":"12544102369",
>        "email":"guilherme@guilherme.com"
>    }
>]

---

### Get a customer

```
POST /api/v1/customers/{{id}}
```

>**Curl**
> 
> ```shell
> curl -X GET -H "Authorization: Bearer bg6Ikaf2LHSzTu4TZl5aYIFWRNWeH8" "http://localhost:8000/api/v1/customers/1/"
> ```
>
>**Response**
>```json
>{
>    "debts":[
>        {
>            "amount":"1000.00",
>            "date_debt":"2018-09-13"
>        }
>    ],
>    "full_name":"Luiz Carlos",
>    "address":"Rua do Correio, 140, Rio de Janeiro",
>    "cpf":"12345678950",
>    "email":"luiz@luiz.com",
>    "phone":"5524988754123",
>    "created_at":"2018-09-13T21:58:32.584460Z",
>    "update_at":"2018-09-13T21:58:32.584485Z"
>}
>