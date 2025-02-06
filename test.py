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
    value["Year"] = value["Attribute"][-1] + value["Attribute"][-2] + value["Attribute"][-3] + value["Attribute"][-4]
    value["Attribute"].replace(f", {value["Year"]}","")


with open('education2023.csv','w',newline='') as file:
    field_names = ["Year","Age","Gender","Educational Attainment","Personal Income","Population Count"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in fullUnempCSV:
        writer.writerow(line)

