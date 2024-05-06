from Authentication import authentication
from GetExternalContacts import getExternalContacts
from DeleteExternalContacts import deleteExternalContacts

access_token = authentication()
pageNumber = 1
getExternalContacts_json = getExternalContacts(access_token, pageNumber)
pageCount = getExternalContacts_json["pageCount"]
deleteExternalContacts(getExternalContacts_json, access_token)

for i in range(pageCount-1):
    pageNumber = i+2
    getExternalContacts_json = getExternalContacts(access_token, pageNumber)
    deleteExternalContacts(getExternalContacts_json, access_token)
    