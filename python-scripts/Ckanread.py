from urllib.request import urlopen as uReq
import json
import requests

datastore_url = 'http://localhost:5000/api/3/action/datastore_upsert'
auth_key = '71e2aebb-f605-4ad3-8d63-aa32f5be0bae'
resource_id = 'd8145740-8291-486e-9b81-cc3f8095dea4'
header = {"X-CKAN-API-Key": auth_key,"Accept": "application/json",'Content-Type': 'application/json'}
r = requests.get('http://localhost:5000/api/3/action/datastore_search?resource_id=d8145740-8291-486e-9b81-cc3f8095dea4&limit=5')


response_data = r.json()
jsondata = response_data["result"]["records"]

for i in jsondata:
 title = (i["Title"])
 authors = (i["Authors"])
 ra = (i["Research Area"])
 research = ""
 if ra == "Not Mentioned":
 	research = title
 else:
 	reserach = ra
 types = (i["Publication Type"])
 source = (i["Source"])
 year = (i["Year"])
 
 link = (i["Link"])
 upsert_records = [{"Title":title,"Authors":authors,"Research Area":research,"Publication Type":types,
 "Source":source,"Year":year,"Link":link}]
 
 jsonData = requests.post(datastore_url, headers=header,  data=json.dumps({
        "resource_id": resource_id,
        "method": "upsert",
        "records": upsert_records,
  }))



