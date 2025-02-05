import csv

fullUnempCSV = []
with open('unemployment2023.csv','r') as file:
    unemp = csv.DictReader(file)
    for line in unemp:
        fullUnempCSV.append(line)

print(fullUnempCSV[100]["State"])
for line in fullUnempCSV:
    if line["Attribute"][-2] != "2" and line["Attribute"][-1] != "3":
        fullUnempCSV.remove(line)

with open('unemployment2023.csv','w',newline='') as file:
    field_names = ["FIPS_Code","State","Area_Name","Attribute","Value"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in fullUnempCSV:
        writer.writerow(line)

