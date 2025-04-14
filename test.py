import csv
import random
from colorama import Fore, Style
import os
z = os.get_terminal_size()
z = z[0]

wordList = []
with open('wordle.csv','r') as file:
    word = csv.DictReader(file)
    for line in word:
        wordList.append(line)
wordleUsedList = []
with open('wordleUsed.csv','r') as file:
    word = csv.DictReader(file)
    for line in word:
        wordleUsedList.append(line)

for line in wordleUsedList:
    del line['occurrence']
    del line['day']


    







