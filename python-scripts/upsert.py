from urllib.request import urlopen as uReq
import json
import requests
import re

u = 'http://localhost:5000/api/3/action/datastore_upsert'
ckan_api_key = '71e2aebb-f605-4ad3-8d63-aa32f5be0bae'
resource_id = '019e8492-3363-4db6-beee-adfb1ca0b365'

r = requests.get('http://localhost:5000/api/3/action/datastore_search?resource_id=019e8492-3363-4db6-beee-adfb1ca0b365&limit=30999')

response_data = r.json()
jsondata = response_data["result"]["records"]

for i in jsondata:
     title = i["Title"]
     authors = i["Authors"]
     research = i["Research Area"]
     types = i["Publication Type"]
     source = i["Source"]
     year = i["Year"]
     year_flag = year
     link = i["Link"]
     ra = i["Research Area"]   
     flag = ra
     if (ra == "Not Mentioned" or ra == "") :
         research = title
     else:
         reserach = ra
     if (year == 0):
     	if(re.search("^.*2021.*$", title)):
     		year = 2021
     	elif(re.search("^.*2020.*$", title)):
     		year = 2020
     	elif(re.search("^.*2019.*$", title)):
     		year = 2019
     	elif(re.search("^.*2018.*$", title)):
     		year = 2018
     	elif(re.search("^.*2017.*$", title)):
     		year = 2017
     	elif(re.search("^.*2016.*$", title)):
     		year = 2016
     	elif(re.search("^.*2016.*$", title)):
     		year = 2016
     	elif(re.search("^.*2015.*$", title)):
     		year = 2015
     	elif(re.search("^.*2014.*$", title)):
     		year = 2014
     	elif(re.search("^.*2013.*$", title)):
     		year = 2013
     	elif(re.search("^.*2012.*$", title)):
     		year = 2012
     	elif(re.search("^.*2011.*$", title)):
     		year = 2011
     	elif(re.search("^.*2010.*$", title)):
     		year = 2010
     	elif(re.search("^.*2013.*$", title)):
     		year = 2013
     	elif(re.search("^.*2009.*$", title)):
     		year = 2009
     	elif(re.search("^.*2008.*$", title)):
     		year = 2008
     	elif(re.search("^.*2007.*$", title)):
     		year = 2007
     	elif(re.search("^.*2006.*$", title)):
     		year = 2006
     	elif(re.search("^.*2005.*$", title)):
     		year = 2005
     	elif(re.search("^.*2004.*$", title)):
     		year = 2004
     	elif(re.search("^.*2003.*$", title)):
     		year = 2003
     	elif(re.search("^.*2002.*$", title)):
     		year = 2002
     	elif(re.search("^.*2001.*$", title)):
     		year = 2001
     	elif(re.search("^.*2000.*$", title)):
     		year = 2000
     	elif(re.search("^.*1999.*$", title)):
     		year = 1999

     records = [{
     'Title': title,
     'Authors': authors,
     'Research Area': research,
     'Publication Type': types,
     'Source': source,
     'Year': year,
     'Link': link,     
     }]
     
     if ((flag == "Not Mentioned" or flag == "") or (year_flag == 0)) :
         r = requests.post(u, headers={"X-CKAN-API-Key": ckan_api_key,"Accept": "application/json",'Content-Type': 'application/json'},
         data=json.dumps({
        "resource_id": resource_id,
        "method": "upsert",
        "records": records,
  	}))
     
            
 






























