import requests
import json

# Get External Contact

def getExternalContacts(access_token, pageNumber):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token }
    getExternalContacts_response = requests.get("https://api.mypurecloud.com/api/v2/externalcontacts/contacts?pageSize=100&pageNumber="+str(pageNumber)+"&sortOrder=firstName", headers= headers)
    getExternalContacts_json = json.loads(getExternalContacts_response.text)
    return getExternalContacts_json