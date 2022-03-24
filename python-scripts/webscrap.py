from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import mysql.connector


my_url = "https://www.bibliothek.tu-chemnitz.de/uni_biblio/frontdoor.php?source_opus=33385&la=de"

#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html5lib")
print(page_soup)
#grabs each publications
containers = page_soup.findAll("main",{"class":"page-content"})

# filename =   "publishers.csv"
# f = 		 open(filename,'w')
# headers = 	 "tittle, publishers, area\n"
# f.write(headers)


for container in containers:
	# tittle =  		container .div.h4.a.text
	# publishers =	container .div.span.text.strip().replace(",","|")
	# research_area = container .div.p.a
	research_area = container .h1
	#print(research_area)
	# print("tittle : "+tittle+"\n")
	# print("Publishers : "+publishers+"\n")

	# if (not research_area):
	# 	# print("Area : Not Mentaioned!!"+"\n")
	# 	area = "Not Mentaioned"
	# else :
	# 	area = container .div.p.a.text
	# 	# print("Area : "+area+"\n")

	# f.write(tittle + "," + publishers + "," + area + "\n")

#grabs each publications
# containers = page_soup.findAll("div",{"class":"media"})

# for container in containers:
# 	tittle =  container .div.h4.a.text
# 	publishers = container .div.span.text.strip()
# 	research_area = container .div.p.a

# 	if (not research_area):
# 			# print("Area : Not Mentaioned!!"+"\n")
# 			area = "Null"
# 	else :
# 			area = container .div.p.a.text
# 			# print("Area : "+area+"\n")	

# 	db = mysql.connector.connect(host='localhost',database='publication',user='root',password='')
# 	cursor = db.cursor()

# 	add_publications = ("INSERT INTO papers (`tittle`, `publishers`, `research_area`) VALUES (%s, %s, %s)")
# 	data_publications = (tittle,publishers,tittle)

# 	#insertion
# 	cursor.execute(add_publications,data_publications)

# 	db.commit()
# 	cursor.close()
# 	db.close()
