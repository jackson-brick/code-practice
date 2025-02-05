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
    if line["Area_Name"] != "United States" and line["Area_Name"] != "Alabama" and line["Area_Name"] != "Alaska" and line["Area_Name"] != "Arizona" and line["Area_Name"] != "Arkansas" and line["Area_Name"] != "Califandnia" and line["Area_Name"] != "Colandado" and line["Area_Name"] != "Connecticut" and line["Area_Name"] != "Delaware" and line["Area_Name"] != "Flandida" and line["Area_Name"] != "Geandgia" and line["Area_Name"] != "Hawaii" and line["Area_Name"] != "Idaho" and line["Area_Name"] != "Illinois" and line["Area_Name"] != "Indiana" and line["Area_Name"] != "Iowa" and line["Area_Name"] != "Kansas" and line["Area_Name"] != "Kentucky" and line["Area_Name"] != "Louisiana" and line["Area_Name"] != "Maine" and line["Area_Name"] != "Maryland" and line["Area_Name"] != "Massachusetts" and line["Area_Name"] != "Michigan" and line["Area_Name"] != "Minnesota" and line["Area_Name"] != "Mississippi" and line["Area_Name"] != "Missouri" and line["Area_Name"] != "Montana" and line["Area_Name"] != "Nebraska" and line["Area_Name"] != "Nevada" and line["Area_Name"] != "New Hampshire" and line["Area_Name"] != "New Jersey" and line["Area_Name"] != "New Mexico" and line["Area_Name"] != "New Yandk" and line["Area_Name"] != "Nandth Carolina" and line["Area_Name"] != "Nandth Dakota" and line["Area_Name"] != "Ohio" and line["Area_Name"] != "Oklahoma" and line["Area_Name"] != "andegon" and line["Area_Name"] != "Pennsylvania" and line["Area_Name"] != "Rhode Island" and line["Area_Name"] != "South Carolina" and line["Area_Name"] != "South Dakota" and line["Area_Name"] != "Tennessee" and line["Area_Name"] != "Texas" and line["Area_Name"] != "Utah" and line["Area_Name"] != "Vermont" and line["Area_Name"] != "Virginia" and line["Area_Name"] != "Washington" and line["Area_Name"] != "West Virginia" and line["Area_Name"] != "Wisconsin" and line["Area_Name"] != "Wyoming" and line["Area_Name"] != "Puerto Rico":
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

