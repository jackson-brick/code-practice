from colorama import Fore, Style
import random
import os
import csv
z = os.get_terminal_size()
z=z[0]
os.system('clear')

wordList = []
wordUsedList = []
win = False
with open('wordle.csv','r') as file:
    wordle = csv.DictReader(file)
    for line in wordle:
        wordList.append(line)
with open('wordleUsed.csv','r') as file:
    wordle = csv.DictReader(file)
    for line in wordle:
        wordUsedList.append(line)
wordUsedList = [{'word':'optic'}]
#whore, tongs, liver

while True:
    colorCount = 0
    chosenWord = random.choice(wordUsedList)
    chosenWord = chosenWord['word'].upper()
    count = [0,0,0,0,0,0]
    display = ["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _"]
    for lcv in range(7):
        os.system('clear')
        if lcv == 6:
            print(Fore.RED )
            print(chosenWord.center(z))
            print("")
            print("Maybe next time!".center(z))
            print(Style.RESET_ALL)
            print("WORDLE".center(z))
            print("")
            for i in range(6):
                if colorCount != 1 and colorCount != 3:
                    print(display[i].center(z+len(display[i])-8))
                else:
                    print(display[i].center(z+len(display[i])-9))
                    colorCount = 0
            print("")
            print("PRESS ENTER TO PLAY AGAIN".center(z))
            input()
            break
        while True:
            print("WORDLE".center(z))
            print("")
            for i in range(6):
                if colorCount != 1 and colorCount != 3:
                    print(display[i].center(z+len(display[i])-8))
                else:
                    print(display[i].center(z+len(display[i])-9))
                    colorCount = 0
                
            player = input()
            player = player.upper().strip()
            if player == chosenWord:
                os.system('clear')
                print(Fore.GREEN )
                print("You Win!".center(z))
                print(Style.RESET_ALL)
                print("PRESS ENTER TO PLAY AGAIN".center(z))
                input()
                win = True
                break
            if len(player) == 5:
                playerDict = {'word':player}
                if playerDict in wordList:
                    playerList = list(playerDict['word'])
                    chosenWordList = list(chosenWord)
                    checkList = ["","","","",""]
                    newPlayerList = ["","","","",""]
                    for char in range(len(player)):
                        if chosenWordList[char] == playerList[char]:
                            newPlayerList[char] = (Fore.GREEN  + playerList[char].upper()+Style.RESET_ALL)
                            checkList[char] = "!"
                            chosenWordList[char] = "!"
                            if char != 4:
                                newPlayerList[char] += " "



                    for char in range(len(player)):
                        if checkList[char] != "!":
                            if playerList[char] in chosenWordList:
                                newPlayerList[char] = (Fore.YELLOW + playerList[char].upper()+Style.RESET_ALL)
                                checkList[char] = "!"
                                chosenWordList[chosenWordList.index(player[char])] = "!"
                                if char != 4:
                                    newPlayerList[char] += " "



                    for char in range(len(player)):
                        if newPlayerList[char] == "":
                            newPlayerList[char] = (Style.DIM + playerList[char].upper()+Style.RESET_ALL)
                            if char != 4:
                                newPlayerList[char] += " "

                    display[lcv] = "".join(newPlayerList)
                    break
                else:
                    os.system('clear')
                    print(Fore.RED)
                    print("Word not in word list".center(z))
                    print(Style.RESET_ALL)
            else:
                os.system('clear')
                print(Fore.RED) 
                print("Word not in word list".center(z))
                print(Style.RESET_ALL)
        if win == True:
            win = False
            break
        