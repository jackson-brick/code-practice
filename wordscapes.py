import os
import csv
import random


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
def manualEdit():
    for i in range(len(wordList)):
        print(wordList[i+count])
        action = input()
        if action.lower().strip() == "del":
            wordList.pop(i + count)
            count -= 1
        elif action.lower().strip() == "finish":
            wordList[i+count] += "LAST FINISHED HERE"
            break
    print(wordList)

def removeDupes():
    for i in wordList:
        while True:
            if wordList.count(i) > 1:
                wordList.remove(i)
                print(f"removed" + i)
            else:
                break

def removeLongWords():
    for i in wordList:
        while True:
            if len(i) > 8:
                wordList.remove(i)
                print(f"removed" + i)
            break

def removeShortWords():
    for i in wordList:
        while True:
            if len(i) < 3:
                wordList.remove(i)
                print(f"removed" + i)
            break

def editWords():
    with open('wordscapesEditingTxt.txt','w') as file:
        for i in wordList:
            file.write(i)
            file.write("\n")
        file.write("END")


while True:
    wordChoice = random.choice(wordList)
    if len(wordChoice) >= 7:
        break
wordIterations = []
print(wordChoice)
for i in range(len(wordChoice)):
    tempWord = wordChoice[:i] + wordChoice[i+1:]
    input()
