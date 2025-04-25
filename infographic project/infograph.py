import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from collections import Counter

unemp2023 = []
educ2023 = []
edToIncCA = []
incSince1958 = []
with open('infographic project/unemployment2023.csv','r') as file:
    unemp = csv.DictReader(file)
    for line in unemp:
        unemp2023.append(line)
with open('infographic project/education2023.csv','r') as file:
    educ = csv.DictReader(file)
    for line in educ:
        educ2023.append(line)
with open('infographic project/calieducationtoincome2008-2014.csv','r') as file:
    edToInc = csv.DictReader(file)
    for line in edToInc:
        edToIncCA.append(line)
with open('infographic project/incomesince1958TEST.csv','r') as file:
    incSince = csv.DictReader(file)
    for line in incSince:
        incSince1958.append(line)
educ2023ONLY = []
with open('infographic project/education2023ONLY.csv','r') as file:
    educ = csv.DictReader(file)
    for line in educ:
        educ2023ONLY.append(line)

unemp2023DATA = ""
educ2023DATA = pd.read_csv('education2023.csv')
educ2023DATA4Years = educ2023DATA[educ2023DATA["Attribute"]=="Four years of college or higher"].iloc[:,:]
educ2023DATA4Yearsonly2023 = educ2023DATA4Years[educ2023DATA4Years["Year"]=="2023"].iloc[:,:]
educ2023DATA4Yearsonly2023NoUS = educ2023DATA4Yearsonly2023[educ2023DATA4Yearsonly2023["Area name"] != "United States"].iloc[:,:]


edToIncCADATA = pd.read_csv('calieducationtoincome2008-2014.csv')
edToIncCADATA2014 = edToIncCADATA[edToIncCADATA["Year"] == 2014].iloc[:,:]
edToIncCADATA18plus = edToIncCADATA2014[edToIncCADATA2014["Age"] != "00 to 17"].iloc[:,:]


edToIncCADATA18plusNHSD = edToIncCADATA18plus[edToIncCADATA18plus["Educational Attainment"] == "No high school diploma"].iloc[:,:]
edToIncCADATA18plusHSONLY = edToIncCADATA18plus[edToIncCADATA18plus["Educational Attainment"] == "High school or equivalent"].iloc[:,:]
edToIncCADATA18plusSMCOLLEGE = edToIncCADATA18plus[edToIncCADATA18plus["Educational Attainment"] == "Some college, less than 4-yr degree"].iloc[:,:]
edToIncCADATA18plusBACHELORS = edToIncCADATA18plus[edToIncCADATA18plus["Educational Attainment"] == "Bachelor's degree or higher"].iloc[:,:]

edToIncCADATA18plusNHSDpython = edToIncCADATA18plusNHSD.to_dict(orient='list')
popCount = [0,0,0,0,0,0,0,0]
indices = ["No Income","$5,000 to $9,999","$10,000 to $14,999","$15,000 to $24,999","$25,000 to $34,999","$35,000 to $49,999","$50,000 to $74,999","$75,000 and over"]

for item in range(933,10620):
    try:
        if edToIncCADATA18plusBACHELORS["Personal Income"][item] == "No Income":
            popCount[0] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$5,000 to $9,999":
            popCount[1] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$10,000 to $14,999":
            popCount[2] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$15,000 to $24,999":
            popCount[3] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$25,000 to $34,999":
            popCount[4] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$35,000 to $49,999":
            popCount[5] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$50,000 to $74,999":
            popCount[6] += edToIncCADATA18plusBACHELORS["Population Count"][item]
        elif edToIncCADATA18plusBACHELORS["Personal Income"][item] == "$75,000 and over":
            popCount[7] += edToIncCADATA18plusBACHELORS["Population Count"][item]
    except:
        pass


popCountNew = []
for item in popCount:
    popCountNew.append(item.item())

plot.barh(indices,popCountNew)
plot.xlabel("# of People in California with at least a Bachelor's degree")
plot.ylabel("Personal Income")
plot.title("Personal Income vs. # of People in California with at least a Bachelor's degree")




incSince1958DATA = pd.read_csv('incomesince1958TEST.csv')


states = []
for state in incSince1958DATA["GeoName"]:
    if state not in states:
        states.append(state)

stateIncomes2023 = []
for val in incSince1958:
    if val["GeoName"] != "United States" and val["GeoName"] != "California" and val["GeoName"] != "New York" and val["GeoName"] != "Texas" and val["GeoName"] != "Florida" and val["GeoName"] != "West Virginia":
        if val["Year"] == "2023":
            stateIncomes2023.append(int(val["Value"]))

percentCollege = []
percentPastHS = []

for lcv in educ2023ONLY:
    x=100
    if lcv["Area name"] != "United States" and lcv["Area name"] != "California" and lcv["Area name"] != "New York" and lcv["Area name"] != "Texas" and lcv["Area name"] != "Florida" and lcv["Area name"] != "West Virginia":
        if lcv["Attribute"] == "Percent of adults who are not high school graduates":
            x -= float(lcv["Value"])
            percentPastHS.append(x)
x=0
for lcv in educ2023ONLY:
    if lcv["Area name"] != "United States" and lcv["Area name"] != "California" and lcv["Area name"] != "New York" and lcv["Area name"] != "Texas" and lcv["Area name"] != "Florida" and lcv["Area name"] != "West Virginia": 
        
        if lcv["Attribute"] == "Percent of adults completing some college or associate degree" or lcv["Attribute"] == "Percent of adults with a bachelor's degree or higher":
            x += float(lcv["Value"])
        if lcv["Attribute"] == "Percent of adults with a bachelor's degree or higher":
            percentCollege.append(x)
            
            x= 0


#for item in incSince1958:
    #if item["GeoName"] not in stateIncomes:
        #stateIncomes[item["GeoName"]] = 
collegeToIncomeDF = pd.DataFrame({"avgPersInc":stateIncomes2023,"percCollege":percentCollege})
highSchoolToIncomeDF = pd.DataFrame({"avgPersInc":stateIncomes2023,"percHS":percentPastHS})

j=np.array(stateIncomes2023)
e=np.array(percentCollege)

coefficients = np.polyfit(j, e, 1)
m = coefficients[0] # slope
c = coefficients[1] # intercept
yPredicted = m*j+c
#edToIncCADATA18plusNHSD.plot(kind="bar",x="Personal Income",y="Population Count",title="Educational attainment")

#plot.scatter(stateIncomes2023,percentCollege)
#plot.plot(stateIncomes2023,yPredicted,color='red')
#plot.title("Average Personal Incomes vs. Education Levels, 2023")
#plot.xlabel(f"Average Personal Incomes - Correlation: {collegeToIncomeDF["avgPersInc"].corr(collegeToIncomeDF["percCollege"])}")
#plot.ylabel("Percent That Attended College")
plot.tick_params(axis='x',rotation=30)
plot.ticklabel_format(style="plain",axis="x")
#incSince1958DATA.plot(kind="bar",subplots=True,x="GeoName",y="1958")
#states.remove('United States')
#personalIncome2018.pop(0)
#plot.barh(states,personalIncome2018)
#plot.xlabel("Personal Income")
#plot.ylabel("State")
plot.show()
plot.savefig('figure.png',bbox_inches = "tight")
#print(states)