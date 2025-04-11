import csv
import random
from colorama import Fore, Style
import os
z = os.get_terminal_size()
z = z[0]

wordList = []
with open('wordle.csv','r') as file:
    wordle = csv.DictReader(file)
    for line in wordle:
        wordList.append(line)
word = random.choice(wordList)
word = word['1']+word['2']+word['3']+word['4']+word['5']

newWord = ["","","","",""]
newWord[0] = "X"
print(str(newWord))
newWord[0] = (Fore.RED + Style.BRIGHT + "p" + Style.RESET_ALL)
newWord += Fore.GREEN + Style.BRIGHT + "o" + Style.RESET_ALL
print("control")
print("".join(newWord))
print("control")
a = Fore.GREEN + Style.BRIGHT + "poped" + Style.RESET_ALL
b = Fore.YELLOW + "poped" + Fore.RESET
c = Style.DIM + "poped" + Style.RESET_ALL
print(repr(a).center(z))
print(a.center(z+12))
print(len(a))
print(repr(b).center(z))
print(b.center(z+10))
print(len(b))
print(repr(c).center(z))
print(c.center(z+8))
print(len(c))