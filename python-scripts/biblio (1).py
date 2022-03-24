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
faculty_soup = soup(page_html,"html.parser")

#grabs each departments
faculty_containers = faculty_soup.findAll("main",{"class":"page-content"})
faculty_container =  faculty_containers[0].findAll("li")

#CSV File
filename =   "final.csv"
f = 		 open(filename,'w', encoding='utf-8')
headers = 	 "Tittle, Authors, Research Area, Publication Type, Source, Link\n"
f.write(headers)

for faculty_contain in faculty_container:
	faculty =  		faculty_contain .a['href']
	
	#create faculty links
	faculty_urls = "https://www.bibliothek.tu-chemnitz.de"+faculty
	#print(faculty_urls)
	
	#html parsing
	subject_soup = soup(uReq(faculty_urls), "html.parser")
	
	#grabs each faculty subject
	subject_containers = subject_soup.findAll("main",{"class":"page-content"})
	subject_container =  subject_containers[0].findAll("li")

	for subject_contain in subject_container:
		subject =  		subject_contain .a['href']
		
		#create subject urls
		subjects_urls = "https://www.bibliothek.tu-chemnitz.de"+subject
		subjects_url =  subjects_urls.replace("Lines_Displayed=20","Lines_Displayed=999")
		#print(subjects_url+"\n")

		#html parsing
		publications_soup = soup(uReq(subjects_url), "html5lib")
		
		#grabs each publications page url
		publications_containers = publications_soup.findAll("main",{"class":"page-content"})
		publications_container =  publications_containers[0].findAll("td",{"valign":"TOP"})

		for publications_contain in publications_container:		
			publications_urls = publications_contain .a
			
			if(not publications_urls) :
				next
			else :
				publications_url =   publications_contain .a['href']
				publication_url =    "https://www.bibliothek.tu-chemnitz.de"+publications_url
				publication_url_en = publication_url.replace("la=de","la=en")
				
				#html5lib parsing
				publication_page_content_soup = soup(uReq(publication_url_en), "html5lib")
				
				author             = ""
				publication_tittle = ""
				
				#grabs each publication authors
				publication_page_containers = publication_page_content_soup.findAll("main",{"class":"page-content"})

				publication_author_list =    publication_page_containers[0].findAll("b")
				publication_tittle = 	     publication_page_containers[0] .h3.text.replace(",","|")  #header01
				publication_contents_table = publication_page_containers[0].findAll("table")

				publication_content_table =  publication_contents_table[1].findAll("tr")

				for publication_authors in publication_author_list:
					publication_author = publication_authors .a
					if(not publication_author) :
						break
					else :
						author = author + publication_authors .a.text.strip().replace(","," ") #header 02
						author = author+"|"

				publication_expertise_area = ""
				publication_document_type =  ""
				publication_source        =  ""

				for publication_content in publication_content_table:
					file_header = publication_content .td.b.text
					file_header_data = publication_content .td.find_next_sibling('td').find_next_sibling('td').text
					#print(header+"\n")

					#key_words = header_data.find("Freie Schlagwörter")
					if("Freie Schlagwörter" in file_header):
						publication_expertise_area = publication_expertise_area + file_header_data.replace(",","|") #header 03
						#print(expertise_area+"\n")

					elif ("Dokumentart" in file_header):
						publication_document_type =  publication_document_type + file_header_data.replace(",","|") #header 04
						#print(document_type+"\n")

					elif ("Quelle" in file_header):
						publication_source =         publication_source + file_header_data.replace(",","|") #header 05
						#print(source+"\n")
				f.write(publication_tittle + "," + author + "," + publication_expertise_area + "," + publication_document_type + "," + publication_source + "," + publication_url +"\n")