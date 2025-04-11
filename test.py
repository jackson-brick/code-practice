import csv
import random

wordList = []
with open('wordle.csv','r') as file:
    wordle = csv.DictReader(file)
    for line in wordle:
        wordList.append(line)
word = random.choice(wordList)
word = word['1']+word['2']+word['3']+word['4']+word['5']
player = input()
newDict = {'1':player[0],'2':player[1],'3':player[2],'4':player[3],'5':player[4]}
print(newDict in wordList)