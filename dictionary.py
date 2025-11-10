import csv
import os

dictList = []
with open('gamesandmisc/dictionary.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line["word"])
        dictList.append(line)

while True:
    os.system('clear')
    word = input("What word do you need?\n")
    word = word.lower().strip()
    for i in dictList:
        if word == i["word"].lower().strip():
            print(word.capitalize())
            definitionList = []
            tempWord = ""
            for letter in range(len(i["definitions"])):
                
                if i["definitions"][letter] == "[":
                    continue
                if i["definitions"][letter] == "]":
                    definitionList.append(tempWord)
                    continue
                if i["definitions"][letter] == ",":
                    if i["definitions"][letter-1] == "\'" and i["definitions"][letter+2] == "\'":
                        definitionList.append(tempWord)
                        tempWord = ""
                        continue
                tempWord += i["definitions"][letter]
            for j in range(len(definitionList)):
                print(f"{j+1}. {definitionList[j]}")
            input()
            break