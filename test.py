import csv
import pandas as py
import numpy as np
import random
import os
os.system('clear')

countyData = []
with open('statsfinal.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        countyData.append(line)

ca = []
wa = []
ore = []
ct = []
de = []
fl = []
ga = []
me = []
ml = []
ma = []
nh = []
nj = []
ny = []
nc = []
ri = []
sc = []
va = []


for i in countyData:
    if "California" in i["County"]:
        ca.append(i)
    elif "Washington" in i["County"]:
        wa.append(i)
    elif "Oregon" in i["County"]:
        ore.append(i)
    elif "Connecticut" in i["County"]:
        ct.append(i)
    elif "Delaware" in i["County"]:
        de.append(i)
    elif "Florida" in i["County"]:
        fl.append(i)
    elif "Georgia" in i["County"]:
        ga.append(i)
    elif "Maine" in i["County"]:
        me.append(i)
    elif "Maryland" in i["County"]:
        ml.append(i)
    elif "Massachusetts" in i["County"]:
        ma.append(i)
    elif "New Hampshire" in i["County"]:
        nh.append(i)
    elif "New Jersey" in i["County"]:
        nj.append(i)
    elif "New York" in i["County"]:
        ny.append(i)
    elif "North Carolina" in i["County"]:
        nc.append(i)
    elif "Rhode Island" in i["County"]:
        ri.append(i)
    elif "South Carolina" in i["County"]:
        sc.append(i)
    elif "Virginia" in i["County"]:
        va.append(i)

WCcountyList = [ca,ore,wa]
ECcountyList = [ct,de,fl,ga,me,ml,ma,nh,nj,ny,nc,ri,sc,va]

sumx = 0
sumy = 0
print("West Coast")
for i in range(10):
    while True:
        x = random.choice(random.choice(WCcountyList))
        if x["County"][-13:-3] == "California" or x["County"][-13:-3] == "Washington" or x["County"][-9:-3] == "Oregon":
            break
    print(x["County"] + " : " + x["Average Annual Count"])
    if x["Average Annual Count"].replace(" ","").isdigit():
        sumx += float(x["Average Annual Count"].replace(" ",""))
    elif x["Average Annual Count"] == "3 or fewer":
        sumx += 2
print(f"Average: {sumx/10}")

print("")
print("East Coast")
for i in range(10):
    while True:
        y = random.choice(random.choice(ECcountyList))
        if y["County"][-13:-3] != "California" and y["County"][-13:-3] != "Washington" and y["County"][-9:-3] != "Oregon":
            break
    print(y["County"] + " : " + y["Average Annual Count"])
    if y["Average Annual Count"].replace(" ","").isdigit():
        sumy += float(y["Average Annual Count"].replace(" ",""))
    elif y["Average Annual Count"] == "3 or fewer":
        sumy += 2
    
print(f"Average: {sumy/10}")







"""
Created by statecancerprofiles.cancer.gov on 05/09/2025 4:58 pm.

"Alaska Census Area Name Change: please note that Wade Hampton Census Area, AK (FIPS code=02270) was renamed effective July 1, 2015, and the new name is Kusilvak Census Area

"South Dakota County Name Change: please note that Shannon County, SD (FIPS code=46113) was renamed effective May 1, 2015, and the new name is Oglala Lakota County (FIPS Code

State Cancer Registries may provide more current or more local data.


Trend
   Rising when 95% confidence interval of average annual percent change is above 0.
   Stable when 95% confidence interval of average annual percent change includes 0.
   Falling when 95% confidence interval of average annual percent change is below 0.

"[rate note] Incidence rates (cases per 100,000 population per year) are age-adjusted to the 2000 US standard population [http://www.seer.cancer.gov/stdpopulations/stdpop.19ages.html] (19
"[trend note] Incidence data come from different sources. The Average Annual Percent Change (AAPC) is based on the APCs calculated by Joinpoint. Due to data availability issues, the time

Rates and trends are computed using different standards for malignancy. For more information see malignant.html.

"^ All Stages refers to any stage in the Surveillance, Epidemiology, and End Results (SEER) Summary/Historic Combined Summary Stage (2004+) [ https://seer.cancer.gov/tools/ssm/ ]."
"[rank note]Results presented with the CI*Rank statistics help show the usefulness of ranks. For example, ranks for relatively rare diseases or less populated areas may be essentially meaningless because of
[rural urban note] Rural-Urban Continuum Codes provided by the USDA [ https://www.ers.usda.gov/data-products/rural-urban-continuum-codes ].
Puerto Rico is treated as urban because over 90% of the population lives in urban areas.
"* Data has been suppressed to ensure confidentiality and stability of rate estimates.  Counts are suppressed if fewer than 16 records were reported in a specific area-sex-race category. If an average
Data not available [http://statecancerprofiles.cancer.gov/datanotavailable.html] for this combination of data selections.
"1 Source: National Program of Cancer Registries [ https://www.cdc.gov/cancer/npcr/index.htm ] and Surveillance, Epidemiology, and End Results [ http://seer.cancer.gov ] SEER
"6 Source: National Program of Cancer Registries SEER*Stat Database - United States Department of Health and Human Services, Centers for Disease Control and Prevention (based on the 2023 submission).  [ https
7 Source: SEER November 2023 submission.
"8 Source: Incidence data provided by the SEER Program. ( http://seer.cancer.gov ) AAPCs are calculated by the Joinpoint Regression Program ( https://surveillance.cancer.gov/joinpoint/ )

"Note: This website still uses Connecticut counties instead of planning regions for consistency of geographies across data topics. If/when all data sources have new planning regions, then this website will switch

Data for the United States does not include data from Indiana.
Data for the United States does not include Puerto Rico.
"""
