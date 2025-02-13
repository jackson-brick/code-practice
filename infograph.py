import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

unemp2023 = []
educ2023 = []
edToIncCA = []
incSince1958 = []
with open('unemployment2023.csv','r') as file:
    unemp = csv.DictReader(file)
    for line in unemp:
        unemp2023.append(line)
with open('education2023.csv','r') as file:
    educ = csv.DictReader(file)
    for line in educ:
        educ2023.append(line)
with open('calieducationtoincome2008-2014.csv','r') as file:
    edToInc = csv.DictReader(file)
    for line in edToInc:
        edToIncCA.append(line)
with open('incomesince1958.csv','r') as file:
    incSince = csv.DictReader(file)
    for line in incSince:
        incSince1958.append(line)
educ2023ONLY = []
with open('education2023ONLY.csv','r') as file:
    educ = csv.DictReader(file)
    for line in educ:
        educ2023ONLY.append(line)

unemp2023DATA = ""
educ2023DATA = pd.read_csv('education2023.csv')
educ2023DATA4Years = educ2023DATA[educ2023DATA["Attribute"]=="Four years of college or higher"].iloc[:,:]
educ2023DATA4Yearsonly2023 = educ2023DATA4Years[educ2023DATA4Years["Year"]=="2023"].iloc[:,:]
educ2023DATA4Yearsonly2023NoUS = educ2023DATA4Yearsonly2023[educ2023DATA4Yearsonly2023["Area name"] != "United States"].iloc[:,:]



edToIncCADATA = pd.read_csv('calieducationtoincome2008-2014.csv')
edToIncCADATA2008 = edToIncCADATA[edToIncCADATA["Year"]==2008].iloc[:,:]
edToIncCADATA2008NHSD = edToIncCADATA2008[edToIncCADATA2008["Educational Attainment"] == "No high school diploma"].iloc[:,:]
persInc = []
for item in edToIncCADATA2008NHSD["Personal Income"]:
    persInc.append(item)
popCount = []
for item in edToIncCADATA2008NHSD["Population Count"]:
    popCount.append(item)



incSince1958DATA = pd.read_csv('incomesince1958.csv')


states = []
for state in incSince1958DATA["GeoName"]:
    if state not in states:
        states.append(state)

stateIncomes2023 = []
for val in incSince1958DATA:
    if val["Year"] == "2023":
        stateIncomes2023.append(val["Value"])

percentCollege = []
percentPastHS = []

for lcv in educ2023ONLY:
    x=100
    if lcv["Attribute"] == "Percent of adults who are not high school graduates":
        x -= lcv["Value"]
    percentPastHS.append(x)
for lcv in educ2023ONLY:
    x=0
    if lcv["Attribute"] == "Percent of adults completing some college or associate degree":
        x += lcv["Value"]
    elif lcv["Attribute"] == "Percent of adults with a bachelor's degree or higher":
        x += lcv["Value"]
    percentCollege.append(x)

#for item in incSince1958:
    #if item["GeoName"] not in stateIncomes:
        #stateIncomes[item["GeoName"]] = 


#edToIncCADATA2008NHSD.plot(kind="scatter",subplots=True,x="Personal Income",y="Population Count",title="Educational attainment")
#plot.barh(persInc,popCount)
#plot.title("Income for People With No High School Diploma, 2008")
#plot.xlabel("# of People")
#plot.ylabel("Personal Income")
#incSince1958DATA.plot(kind="bar",subplots=True,x="GeoName",y="1958")
#states.remove('United States')
#personalIncome2018.pop(0)
#plot.barh(states,personalIncome2018)
#plot.xlabel("Personal Income")
#plot.ylabel("State")
plot.savefig('figure.png',bbox_inches = "tight")
#print(states)