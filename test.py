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

countyPops = []
with open('countypopulations.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        countyPops.append(line)

def poop():
    for i in countyData:
        try:
            if i["County"][i["County"].index(","):-3].replace(", ","") == "Hawaii":
                print("Hawaii")
                countyData.remove(i)
            elif i["County"][i["County"].index(","):-3].replace(", ","") == "Alaska":
                print("Alaska")
                countyData.remove(i)
        except:
            print(i["County"])
            input()



    with open('statsfinal.csv','w',newline='') as file:
        field_names = ["County","FIPS","2023 Rural-Urban Continuum Codes([rural urban note])","Age-Adjusted Incidence Rate([rate note]) - cases per 100,000","Lower 95% Confidence Interval","Upper 95% Confidence Interval","CI*Rank([rank note])","Lower CI (CI*Rank)","Upper CI (CI*Rank)","Average Annual Count","Recent Trend","Recent 5-Year Trend ([trend note]) in Incidence Rates","Lower 95% Confidence Interval","Upper 95% Confidence Interval"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for line in countyData:
            writer.writerow(line)

def fart():
    wcStates = ["California", "Washington","Oregon","Utah","Nevada","Arizona","Idaho","Montana","Wyoming","Colorado","New Mexico","Texas","Oklahoma","Kansas","Nebraska","South Dakota","North Dakota","Minnesota","Iowa","Missouri","Arkansas","Louisiana","Wisconsin","Illinois"]
    ecStates = ["Connecticut","Delaware","Florida", "Georgia","Maine","Maryland","Massachusetts","New Hampshire","New Jersey","New York","North Carolina","Rhode Island","South Carolina","Virginia","Vermont","Pennsylvania","West Virginia","Alabama","Tennessee","Kentucky","Ohio","Michigan","Indiana","Mississippi"]

    eastCoast = []
    westCoast = []

    for i in countyData:
        if i["County"][i["County"].index(","):-3].replace(", ","") in wcStates:
            westCoast.append(i)
        elif i["County"][i["County"].index(","):-3].replace(", ","") in ecStates:
            eastCoast.append(i)

    finalWest = []
    finalEast = []
    westPropSum = 0
    eastPropSum = 0


    for i in range(1):
        x = random.choice(westCoast)
        if x["Average Annual Count"] != "data not available":
            if x["Average Annual Count"] == "3 or fewer":
                x["Average Annual Count"] = 2
            for lcv in countyPops:
                try:
                    if lcv["Geographic Area"].replace(".","") == x["County"][:-3]:
                        tempPop = int(lcv["2023"].replace(",",""))
                except:
                    print("didnt work " + x)
            westPropSum += (int(x["Average Annual Count"])/tempPop)
            finalWest.append(f"{x["County"]} : {x["Average Annual Count"]}")
            westCoast.remove(x)
    westPropSum/=100

    print("")

    for i in range(1):
        x = random.choice(eastCoast)
        if x["Average Annual Count"] != "data not available":
            if x["Average Annual Count"] == "3 or fewer":
                x["Average Annual Count"] = 2
            for lcv in countyPops:
                try: 
                    if lcv["Geographic Area"].replace(".","") == x["County"][:-3]:
                        tempPop = int(lcv["2023"].replace(",",""))
                except:
                    print("didnt work " + x)
            eastPropSum += (int(x["Average Annual Count"])/tempPop)
            finalEast.append(f"{x["County"]} : {x["Average Annual Count"]}")
            eastCoast.remove(x)
    eastPropSum/=100

    print("West Coast:")
    print("")
    for i in finalWest:
        print(i)
    print(f"Average proportion: {westPropSum}")

    print("")
    print("East Coast")
    print("")
    for i in finalEast:
        print(i)
    print(f"Average proportion: {eastPropSum}")

fart()


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
