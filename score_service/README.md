# Get a token as admin

curl -X POST -d "grant_type=password&username=admin&password=123456@a" -u"TxwppGEWeZIYQu0c3urTeTg3tDYx2LXpROGm9K70:g8p9wpIrPuzI817iMU61fQNhlhVb9SQCAyzGtuPaqOFPFayOG3gp0w5cEBmWgaD8G1cy9tDer4Rwz5awuMJ90Oon00z9w811AXP25OK3sMA7Vr63WebIWizZ1PVCA3gg" http://localhost:8000/api/v1/auth/token/

## Response:

{"access_token": "rHsoOQWPnJfXw0S24la3HlBJk6YLdr", "expires_in": 36000, "token_type": "Bearer", "scope": "read write", "refresh_token": "2CrgldBvZQbG1HbS9dLIFAkiE8ns3X"}


# Get the customers list

curl -X GET -H "Authorization: Bearer rHsoOQWPnJfXw0S24la3HlBJk6YLdr" "http://localhost:8000/api/v1/customers/"

# Get a specif customer

curl -X GET -H "Authorization: Bearer rHsoOQWPnJfXw0S24la3HlBJk6YLdr" "http://localhost:8000/api/v1/customers/{{id}}/"