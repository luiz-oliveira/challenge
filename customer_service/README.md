# Get a token as admin

curl -X POST -d "grant_type=password&username=admin&password=123456@a" -u"WhBJZN9m8dJ63cF30U0NeU7hMO0cG84yj2SHZA12:YM19g9A3E87ia1zDiPNvyr3nUvmDhZHNl2KrnEKAuudKNXLnQVHzYsnYBaVSknVUZVJB27L73VPWyoYtTd1aKhLgcTDCNW7fg02y6bGO3Lda6PnRPaFR3DguwdkIXZqU" http://localhost:8000/api/v1/auth/token/

## Response:

{"access_token": "bg6Ikaf2LHSzTu4TZl5aYIFWRNWeH8", "expires_in": 36000, "token_type": "Bearer", "scope": "read write", "refresh_token": "nGbj3vPEZZoGe1A3sXwkFUkygWYd2K"}


# Get the customers list

curl -X GET -H "Authorization: Bearer bg6Ikaf2LHSzTu4TZl5aYIFWRNWeH8" "http://localhost:8000/api/v1/customers/"

# Get a specif customer

curl -X GET -H "Authorization: Bearer bg6Ikaf2LHSzTu4TZl5aYIFWRNWeH8" "http://localhost:8000/api/v1/customers/{{id}}/"