from colorama import Fore, Style
import random
import os
import csv
z = os.get_terminal_size()
z=z[0]
os.system('clear')

wordList = []
with open('test.csv','r') as file:
    wordle = csv.DictReader(file)
    for line in wordle:
        wordList.append(line)
chosenWord = random.choice(wordList)
chosenWord = chosenWord['1']+chosenWord['2']+chosenWord['3']+chosenWord['4']+chosenWord['5']
display = ["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _"]

for lcv in range(6):
    for i in display:
        print(i.center(z))
        print("")
    player = input()
    if player.lower() == chosenWord:
        os.system('clear')
        print("You Win!".center(z))
        quit()
    if len(player) == 5:
        playerDict = {'1':player[0],'2':player[1],'3':player[2],'4':player[3],'5':player[4]}
        if playerDict in wordList:
            for char in range(len(player)):
                if chosenWord[char] == player[char].lower():
                    display[char] = player[char].upper()
        else:
            os.system('clear')
        print(Fore.RED + Style.BRIGHT + "Word not in word list")
        print(Style.RESET_ALL)
    else:
        os.system('clear')
        print(Fore.RED + Style.BRIGHT + "Word not in word list")
        print(Style.RESET_ALL)