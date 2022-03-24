from requests_html import HTMLSession
from bs4 import BeautifulSoup 
import mysql.connector

s = HTMLSession()
url= "https://www.amazon.de/s?k=monitor"

def getdata(url):
	r = s.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	return soup

def getnextpage(soup):
	page = soup.find('ul',{'class': 'a-pagination'})
	if not page.find('li',{'class':'a-disabled a-last'}):
		url ="http://amazon.de"+str(page.find('li',{'class':'a-last'}).find('a')['href'])
		return url
	else:
		return

# while True:
# 	soup = getdata(url)
# 	url = getnextpage(soup)
# 	if not url:
# 		break
# 	print(url)
while url:
	soup = getdata(url)
	url = getnextpage(soup)
	print(url)