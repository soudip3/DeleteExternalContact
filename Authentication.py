import requests
import json

def authentication():
    the_data = {"client_id": "", "client_secret": "", "grant_type": "client_credentials"}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # Get Access Token
    response = requests.post("https://login.mypurecloud.com/oauth/token", data=the_data, headers=headers)
    response_json = json.loads(response.text)
    access_token = "Bearer "+response_json["access_token"]
    return access_token