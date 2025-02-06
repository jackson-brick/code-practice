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

unemp2023DATA = ""
educ2023DATA = ""
edToIncCADATA = pd.read_csv('calieducationtoincome2008-2014.csv')
incSince1958DATA = ""

edToIncCADATA.plot(x="Educational Attainment",y="Population Count",title="Educational attainment")
plot.savefig('figure.png')