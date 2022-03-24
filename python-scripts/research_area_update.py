from urllib.request import urlopen as uReq
import json
import requests
import re

u = 'http://localhost:5000/api/3/action/datastore_upsert'
ckan_api_key = '71e2aebb-f605-4ad3-8d63-aa32f5be0bae'
resource_id = '143dde40-25a1-4c69-86bd-041bbad6d773'

r = requests.get('http://localhost:5000/api/3/action/datastore_search?resource_id=143dde40-25a1-4c69-86bd-041bbad6d773&limit=35000')

response_data = r.json()
jsondata = response_data["result"]["records"]

def unique_list(l):
	ulist = []
	[ulist.append(x) for x in l if x not in ulist]
	return ulist
    
for i in jsondata:
     title = i["Title"]
     authors = i["Authors"]
     research = i["Research Area"]
     types = i["Publication Type"]
     source = i["Source"]
     year = i["Year"]
     link = i["Link"]
     
     ra = i["Research Area"]   
     flag = ra
     if ((ra == "Not Mentioned" or ra == "" or ra == " ") or (re.search("^.*Not Mentioned.*$", ra))) :
         raw_data = title+" "+source
         remove_sc = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", raw_data)         
         research_data = remove_sc.replace(' ','').split(" ") #list 01
         #research = " ".join(research_data)
         
         all_authors = authors
         if(type(all_authors) is not None):
         	author_data = all_authors.split("|")
         	get_ra = ""
         	for authorList in jsondata:
         		authors_split = authorList["Authors"]
         		research_datas = authors_split.split("|")
         	
         		if(author_data[0] in research_datas):
         			get_ra = (authorList["Research Area"]+" "+get_ra).strip() #list02
         #research = get_ra
         #save_data = [""]
         	save_data = ""
         	if(get_ra != ""):
         		get_ra_split = get_ra.replace(' ','').split("|")
         		flags = 0
         		for if_get in get_ra_split:
         			for if_reserach in research_data:
         				if ((if_get in if_reserach) or (re.search("^.*if_get.*$", if_reserach))):
         					save_data = if_get+" | "+save_data
         					#print(save_data)
         					flags = 1
         				if(re.search("^.*web.*$", title) or (re.search("^.*web.*$", source)) or(re.search("^.*Gaedke.*$", title))):
         					save_data = save_data+"Web engineering"
         					#print(save_data)
         					flags = 2
         		
         	research = ' '.join(unique_list(save_data.split()))
         	if(flags == 0):
         		research = str(source) + str(title)
     	 
         
         
     else:
         reserach = "Empty"


     records = [{
     'Title': title,
     'Authors': authors,
     'Research Area': research,
     'Publication Type': types,
     'Source': source,
     'Year': year,
     'Link': link,     
     }]
     
     if ((flag == "Not Mentioned" or flag == "") or (re.search("^.*Not Mentioned.*$", flag))) :
         r = requests.post(u, headers={"X-CKAN-API-Key": ckan_api_key,"Accept": "application/json",'Content-Type': 'application/json'},
         data=json.dumps({
        "resource_id": resource_id,
        "method": "upsert",
        "records": records,
  	}))
     
            
 






























