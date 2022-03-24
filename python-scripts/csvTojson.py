#Convert CSV to JSON 
import json
import csv

with open ("processed_tagsV1.csv" , "r") as f:
	reader = csv.reader(f)
	next(reader)
	data = {"Publications": []}
	for row in reader:
		# print(row[0]) id
		# print(row[1]) title
		# print(row[2]) authors
		# print(row[3]) ra
		# print(row[4]) year
		# print(row[5]) pt
		# print(row[6]) source
		# print(row[7]) link
		# print(row[8]) tags
 		data["Publications"].append({"Title":row[1],"Authors":row[2],"Research Area":row[3],"Publication Type":row[5],"Source":row[6],"Year":row[4],"Link":row[7], "Tags":row[8]})
 		#data["Publications"].append({"Title":row[0],"Authors":row[1],"Research Area":row[2],"Publication Type":row[3],"Source":row[4],"Year":row[5],"Link":row[6]})


with open ("processed_tagsV1.json", "w") as f:
	json.dump(data, f, indent=4)