# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup
# import mysql.connector


my_url = "https://vsr.informatik.tu-chemnitz.de/research/publications/"

#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

# #grabs each publications
# containers =  page_soup.findAll("main",{"class": "page-content"})
# contents =    containers[0].findAll("h2", {"class":"linie"})

# for container in containers:
# 	tittle =  container .div.h4.a.text
# 	publishers = container .div.span.text.strip()
# 	research_area = container .div.p.a

# 	print("tittle : "+tittle+"\n")
# 	print("Publishers : "+publishers+"\n")

# 	if (not research_area):
# 		print("Area : Not Mentaioned!!"+"\n")
# 	else :
# 		area = container .div.p.a.text
# 		print("Area : "+area+"\n")

#grabs each publications
containers = page_soup.findAll("div",{"class":"media"})

contents =  page_soup.findAll("main",{"class": "page-content"})
content =    contents[0].findAll("h2", {"class":"linie"})

filename =   "publishers.csv"
f = 		 open(filename,'w')
headers = 	 "Year, Tittle, Publishers, Research Area\n"
f.write(headers)

# nextSibling = content[0].text
# print(nextSibling)
for container in containers:
	tittle =  container .div.h4.a.text
	publishers = container .div.span.text.strip()
	research_area = container .div.p.a

	years = container.find_previous_sibling("h2")

	if (not years):
			# print("Area : Not Mentaioned!!"+"\n")
			years = "Null"
	else :
			years = container.find_previous_sibling("h2").text
			# print("Area : "+area+"\n")

	if (not research_area):
			# print("Area : Not Mentaioned!!"+"\n")
			area = "Null"
	else :
			area = container .div.p.a.text
			# print("Area : "+area+"\n")	

	f.write(years + "," + tittle + "," + publishers + "," + area + "\n")

	db = mysql.connector.connect(host='localhost',database='publication',user='root',password='')
	cursor = db.cursor()

	add_publications = ("INSERT INTO paper (`years`,`tittle`,`publishers`,`research_area`) VALUES (%s, %s, %s, %s)")
	data_publications = (years,tittle,publishers,area)

	#insertion
	cursor.execute(add_publications,data_publications)

	db.commit()
	cursor.close()
	db.close()
