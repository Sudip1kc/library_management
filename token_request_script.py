
import requests

# Access Token received from the token endpoint
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMzQ2NTgyLCJpYXQiOjE3NDEzNDYyODIsImp0aSI6ImMwZDhkNDRjNTQ1YzQwZTA4ZTAxNTU1ZDEwYzhhYWFmIiwidXNlcl9pZCI6MX0.wXhZJHHSxap5FQJe7d5yUqKTmzzLqZK2T4A2omXR77I"
refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MTQzMjY4MiwiaWF0IjoxNzQxMzQ2MjgyLCJqdGkiOiIyZDhmMzgxMGRmN2Q0OGVkOTI5ODFkYTRiMmQwNmYwNSIsInVzZXJfaWQiOjF9.Hr9CmUXYmvO3VCxeF5zD478PLWf2Kv8mXsGtNWZrQkU"

# The API endpoint you want to interact with
url = "http://127.0.0.1:8000/api/books/"

# Setting the Authorization header with Bearer token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make a GET request to the /api/books/ endpoint
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Failed to access. Status code: {response.status_code}")

# If access token expired, use the refresh token to obtain a new access token
refresh_url = "http://127.0.0.1:8000/api/token/refresh/"

refresh_response = requests.post(refresh_url, data={"refresh": refresh_token})

if refresh_response.status_code == 200:
    tokens = refresh_response.json()
    print(f"New Access Token: {tokens['access']}")
else:
    print(f"Failed to refresh token. Status code: {refresh_response.status_code}")
