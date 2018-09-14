# Get a token as admin

curl -X POST -d "grant_type=password&username=admin&password=123456@a" -u"u2zRtWvBiwrPwWewVd5aJVQAbyRfxURTqPSxiHkn:hsRxzLj0AKV8dbPUVakXMvs0iXoGw551Xw7ZNcNpJNuonSrpCns2vNiRmbSweu90tws16ye7T7JcaaFPxjkoTMFgwQNcokZQzetiLa0jKLhAd78CPA38lOshlPe8Pzym" http://localhost:8000/api/v1/auth/token/

## Response:

{"access_token": "ASQpBMYOdLKQY64jFTZd0YhsB4FPdn", "expires_in": 36000, "token_type": "Bearer", "scope": "read write", "refresh_token": "0n8MKz9aHLWlUXf7YM0TskrNFvQ5k1"}


# Get the customers list

curl -X GET -H "Authorization: Bearer ASQpBMYOdLKQY64jFTZd0YhsB4FPdn" "http://localhost:8000/api/v1/customers/"

# Get a specif customer

curl -X GET -H "Authorization: Bearer ASQpBMYOdLKQY64jFTZd0YhsB4FPdn" "http://localhost:8000/api/v1/customers/{{id}}/"