from datetime import datetime
import requests

def deleteExternalContacts(getExternalContacts_json, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token }
    for i in range(len(getExternalContacts_json["entities"])):
        try:
            lastagent_datetime = getExternalContacts_json["entities"][i]["customFields"]["lastagent_datetime"].split("T")
            lastagent_datetime_delta = datetime(int(lastagent_datetime[0].split("-")[0]), int(lastagent_datetime[0].split("-")[1]), int(lastagent_datetime[0].split("-")[2]), int(lastagent_datetime[1].split(":")[0]), int(lastagent_datetime[1].split(":")[1]), int(lastagent_datetime[1].split(":")[2].split(".")[0]))
            #print(lastagent_datetime_delta)
            if((datetime.now()-lastagent_datetime_delta).days>30):
                print("Deleting External Contact")
                firstName = getExternalContacts_json["entities"][i]["firstName"]
                print(firstName)
                id = getExternalContacts_json["entities"][i]["id"]
                print(id)
                requests.delete("https://api.mypurecloud.com/api/v2/externalcontacts/contacts/"+str(id), headers= headers)
        except KeyError: pass