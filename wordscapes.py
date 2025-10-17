import os
import csv


z = os.get_terminal_size()[0]

word = "pumpkin"
wordList = []
tempWord = ""
with open('wordscapesEditingTxt.txt','r') as file:
    for line in file.read():
        if line != "\n":
            if line == " ":
                wordList.append(tempWord)
                tempWord = ""
            else:
                tempWord += line
        else:
            wordList.append(tempWord)
            tempWord = ""


dictList = []
with open('wordscapesDict.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        dictList.append(line["word"])


count = 0
for i in range(len(dictList)):
    print(dictList[i+count])
    action = input()
    if action.lower().strip() == "del":
        dictList.pop(i + count)
        count -= 1
    elif action.lower().strip() == "finish":
        dictList[i+count] += "LAST FINISHED HERE"
        break
print(wordList)

with open('wordscapesEditingTxt.txt','w') as file:
    for i in dictList:
        file.write(i)
        file.write("\n")
    file.write("END")