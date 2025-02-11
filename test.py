import csv
import os
import ast
#os.system('clear')

fullEducCSV = []
with open('education2023.csv','r') as file:
    educ = csv.DictReader(file)
    for line in educ:
        if line["Year"] == "2023":
            fullEducCSV.append(line)
incKeys = fullEducCSV[0].keys()
removeKeys = []
for key in incKeys:
    if key.isdigit():
        removeKeys.append(key)



        
input()

with open('education2023.csv','w',newline='') as file:
    field_names = ["FIPS Code","State","Area name","Attribute","Value","Year"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in fullEducCSV:
        writer.writerow(line)

