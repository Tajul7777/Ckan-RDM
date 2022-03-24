from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import mysql.connector

root_url= "https://www.researchgate.net/profile/"

professors_list = open('professors.txt')
line = professors_list.readlines()

for lines in line:
	url = root_url+lines
	print(url)

	#Opening up connection, grabbing the page
	webpage = uReq(url).read()
	uClient.close()