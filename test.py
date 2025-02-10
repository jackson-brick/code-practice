import csv


fullIncCSV = []
with open('incomesince1958.csv','r') as file:
    inc = csv.DictReader(file)
    for line in inc:
        fullIncCSV.append(line)
print(fullIncCSV)
input()
removeList = []
for line in fullIncCSV:
    if line["Description"] != "Personal dividend income":
        removeList.append(line)
for line in removeList:
    fullIncCSV.remove(line)
print(fullIncCSV)
input()
for lcv in range(1958,2024):
    for line in fullIncCSV:
        #line["Year"] = 
        print("")


with open('education2023.csv','w',newline='') as file:
    field_names = ["FIPS Code","State","Area name","Attribute","Value","Year"]
    writer = csv.DictWriter(file,fieldnames=field_names)

    writer.writeheader()
    for line in fullUnempCSV:
        writer.writerow(line)

