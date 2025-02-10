import csv


fullIncCSV = []
with open('incomesince1958.csv','r') as file:
    inc = csv.DictReader(file)
    for line in inc:
        fullIncCSV.append(line)
incKeys = fullIncCSV[0].keys()
removeKeys = []
for key in incKeys:
    if key.isdigit():
        removeKeys.append(key)



removeList = []
for line in fullIncCSV: 
    if line["Description"] != " Personal dividend income ":
        removeList.append(line)
for line in removeList:
    fullIncCSV.remove(line)
newIncCSV = []
x=0
for lcv in range(1958,2024): 
    for line in fullIncCSV:
        newIncCSV.append(line)
        newIncCSV[x]["Year"] = str(lcv)
        newIncCSV[x]["Value"] = line[str(lcv)]
        x+=1
print(newIncCSV[0]['1958'])
print(removeKeys)
print(newIncCSV[0][removeKeys[0]])


for key in removeKeys:
    for entry in newIncCSV:
        del entry[str(key)]


with open('incomesince1958TEST.csv','w',newline='') as file:
    field_names = ["GeoFIPS","GeoName","Region","LineCode","Description","Unit","Year","Value"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in newIncCSV:
        writer.writerow(line)

