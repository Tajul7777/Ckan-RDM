#Convert CSV to JSON 
import re
import json
import csv

with open ("bibliothek.csv" , "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"Publications": []}
    for row in reader:
        source = row[4]
        if(re.search("^.*2021.*$", source)):
            year = 2021
        elif(re.search("^.*2020.*$", source)):
            year = 2020
        elif(re.search("^.*2019.*$", source)):
            year = 2019
        elif(re.search("^.*2018.*$", source)):
            year = 2018
        elif(re.search("^.*2017.*$", source)):
            year = 2017
        elif(re.search("^.*2016.*$", source)):
            year = 2016
        elif(re.search("^.*2015.*$", source)):
            year = 2015
        elif(re.search("^.*2014.*$", source)):
            year = 2014
        elif(re.search("^.*2013.*$", source)):
            year = 2013
        elif(re.search("^.*2012.*$", source)):
            year = 2012
        elif(re.search("^.*2011.*$", source)):
            year = 2011
        elif(re.search("^.*2010.*$", source)):
            year = 2010
        elif(re.search("^.*2009.*$", source)):
            year = 2009
        elif(re.search("^.*2008.*$", source)):
            year = 2008
        elif(re.search("^.*2007.*$", source)):
            year = 2007
        elif(re.search("^.*2006.*$", source)):
            year = 2006
        elif(re.search("^.*2005.*$", source)):
            year = 2005
        else:
            year = 0000
        data["Publications"].append({"Title":row[0],"Authors":row[1],"Research Area":row[2],"Publication Type":row[3],"Source":row[4],"Year":year,"Link":row[5]})


with open ("bibliothek.json", "w") as f:
    json.dump(data, f, indent=4)
