import csv

fullUnempCSV = []
with open('unemployment2023.csv','r') as file:
    unemp = csv.DictReader(file)
    for line in unemp:
        fullUnempCSV.append(line)

removeList = []
print(fullUnempCSV[100]["State"])
state = fullUnempCSV[0]["State"]
for line in fullUnempCSV:
    if line["Attribute"][-2] != "2":
        removeList.append(line)
    elif line["Attribute"][-1] != "3":
        removeList.append(line)        
    if line["State"] != state:
        print(f"Done with {state}")
        state = line["State"]

for value in removeList:
    fullUnempCSV.remove(value)



with open('unemployment2023.csv','w',newline='') as file:
    field_names = ["FIPS_Code","State","Area_Name","Attribute","Value"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in fullUnempCSV:
        writer.writerow(line)

