import csv

comboList = []
with open('12DaysOfCoding.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        comboList.append(line['combo'])

dial = 50
zeroCount = 0
lowerBound = 1
upperBound = 99
exactlyZero = False

def dayOne():
    for i in comboList:

        if i[0] == "L":
            dial -= int(i[1:])
        else:
            dial += int(i[1:])
        if dial % 100 == 0:
            zeroCount += 1
        

    print(zeroCount)

def dayTwo():
    global dial, zeroCount, exactlyZero, upperBound, lowerBound
    for i in comboList:
        #print(i)
        if i[0] == "L":
            dial -= int(i[1:])
        else:
            dial += int(i[1:])
        
        if not exactlyZero:
            if dial > upperBound or dial < lowerBound:
                zeroCount+= 1
                #print("zeroCount ++")
        exactlyZero = False
        if dial%100 == 0:
            exactlyZero = True
        if dial > 0:
            upperBound = ((int(dial / 100))*100)+99
            lowerBound = ((int(dial/100))*100)+1
        else:
            lowerBound = ((int(dial / 100))*100)-99
            upperBound = ((int(dial/100))*100)-1
        #print(dial)
        #input()
        
    print(zeroCount)

dayTwo()