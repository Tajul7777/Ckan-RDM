from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import mysql.connector

my_url = "https://www.bibliothek.tu-chemnitz.de/uni_biblio/abfrage_browsen.php?la=de&fbclid=IwAR0blaTxfbFI8WpL_ay6uM70FrP3TsKI7-dXFvgWCnHk3DCZ0_SaveQZ32E"
index = 0;
#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grabs each departments
containerss = page_soup.findAll("main",{"class":"page-content"})
containers = containerss[0].findAll("li")

filename =   "final.csv"
f = 		 open(filename,'w', encoding='utf-8')
headers = 	 "Tittle, Authors, Key Words, Document Type, Source, Link\n"
f.write(headers)


for container in containers:
	departments =  		container .a['href']

	urls = "https://www.bibliothek.tu-chemnitz.de"+departments
	# print(urls)

	soups = soup(uReq(urls), "html.parser")
	#grabs each departments
	facultyss = soups.findAll("main",{"class":"page-content"})
	facultys = facultyss[0].findAll("li")

	for faculty in facultys:
		facult =  		faculty .a['href']
		facult_link = "https://www.bibliothek.tu-chemnitz.de"+facult

		#display all the papers (upto 1000)
		facult_links = facult_link.replace("Lines_Displayed=20","Lines_Displayed=999")
		
		content_soup = soup(uReq(facult_links), "html5lib")
		#print(content_soup)
		#grabs each paper page link
		paperss = content_soup.findAll("main",{"class":"page-content"})
		papers = paperss[0].findAll("td",{"valign":"TOP"})
		
		for paper in papers:		
			page_link = paper .a
			#print(page_link)
			if(not page_link) :
				next
			else :
				page_links = paper .a['href']
				paper_page_link = "https://www.bibliothek.tu-chemnitz.de"+page_links.replace("la=de","la=en")
				#print(paper_page_link+"\n")
				paper_page_content_soup = soup(uReq(paper_page_link), "html5lib")
				
				author = ""
				tittle = ""
				#grabs each paper authors
				publication_paperss = paper_page_content_soup.findAll("main",{"class":"page-content"})
				authors_list = publication_paperss[0].findAll("b")
				tittle = publication_paperss[0] .h3.text.replace(",","|")  #header01
				data_tables = publication_paperss[0].findAll("table")

				data_table_contents = data_tables[1].findAll("tr")


				for authorss in authors_list:
					authors = authorss .a
					if(not authors) :
						break
					else :
						author = author+authorss .a.text.strip().replace(","," ") #header 02
						author = author+"|"
					#author = author+"|"

				
				expertise_area = ""
				document_type =  ""
				source         = ""
				for data_table_content in data_table_contents:
					header = data_table_content .td.b.text
					header_data = data_table_content .td.find_next_sibling('td').find_next_sibling('td').text
					#print(header+"\n")

					#key_words = header_data.find("Freie Schlagwörter")
					if("Freie Schlagwörter" in header):
						expertise_area = expertise_area + header_data.replace(",","|") #header 03
						#print(expertise_area+"\n")

					elif ("Dokumentart" in header):
						document_type = document_type + header_data.replace(",","|") #header 04
						#print(document_type+"\n")

					elif ("Quelle" in header):
						source = source + header_data.replace(",","|") #header 05
						#print(source+"\n")
				#f.write(tittle + "," + author + "," + expertise_area + "," + document_type + "," + source + "," + paper_page_link +"\n")
			
				
						



				


	