import csv


fullUnempCSV = []
with open('education2023.csv','r') as file:
    unemp = csv.DictReader(file)
    for line in unemp:
        fullUnempCSV.append(line)

removeList = []
#for line in fullUnempCSV:
    #if line["IndustryClassification"] != "...":
        #print(line)
    #removeList.append(line)


#for value in removeList:
    #fullUnempCSV.remove(value)
for value in fullUnempCSV:
    value["Year"] = value["Attribute"][-4] + value["Attribute"][-3] + value["Attribute"][-2] + value["Attribute"][-1]
    tempAttribute = ""
    for char in value["Attribute"]:
        if char == ",":
            break
        else:
            tempAttribute += char
    value["Attribute"] = tempAttribute

with open('education2023.csv','w',newline='') as file:
    field_names = ["FIPS Code","State","Area name","Attribute","Value","Year"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in fullUnempCSV:
        writer.writerow(line)

