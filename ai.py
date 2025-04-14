import csv
import os

z = os.get_terminal_size()
z=z[0]

wordList = []
with open('dictionary.csv','r') as file:
    word = csv.DictReader(file)
    for line in word:
        wordList.append(line)

wordListNew = []
checkedWords = []
for line in wordList:
    print(line['word'])
    if line['word'] not in checkedWords:
        wordListNew.append(line)
        checkedWords.append(line['word'])

with open('dictionary.csv','w',newline="") as file:
    field_names = ["word","pos","definitions","synonyms"]
    writer = csv.DictWriter(file,fieldnames=field_names)
    writer.writeheader()
    for line in wordListNew:
        writer.writerow(line)
