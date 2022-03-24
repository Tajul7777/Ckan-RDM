# Python program to convert
# JSON file to CSV
 
 
import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('jsonData.json') as json_file:
    data = json.load(json_file)
 
publications_data = data['Publications']
 
# now we will open a file for writing
data_file = open('jsonData.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for publication_data in publications_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = publication_data.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(publication_data.values())
 
data_file.close()