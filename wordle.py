from colorama import Fore, Style
import random
import os
import csv
z = os.get_terminal_size()
z=z[0]
os.system('clear')

wordList = []
win = False
with open('wordle.csv','r') as file:
    wordle = csv.DictReader(file)
    for line in wordle:
        wordList.append(line)
#chosenWord = random.choice(wordList)
#chosenWord = chosenWord['1']+chosenWord['2']+chosenWord['3']+chosenWord['4']+chosenWord['5']
chosenWord = "bunny"
count = [0,0,0,0,0,0]
display = ["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _"]

while True:
    for lcv in range(7):
        os.system('clear')
        if lcv == 7:
            print(Fore.RED + Style.BRIGHT)
            print("Maybe next time!".center(z))
            print(Style.RESET_ALL)
            input("PRESS ENTER TO PLAY AGAIN")
            break
        while True:
            print(chosenWord.center(z))
            for i in range(6):
                print(display[i].center(z+count[i]))
                print("")
            player = input()
            player = player.lower().strip()
            if player == chosenWord:
                os.system('clear')
                print(Fore.GREEN + Style.BRIGHT)
                print("You Win!".center(z))
                print(Style.RESET_ALL)
                input("PRESS ENTER TO PLAY AGAIN".center(z))
                win = True
                break
            if len(player) == 5:
                playerDict = {'1':player[0],'2':player[1],'3':player[2],'4':player[3],'5':player[4]}
                if playerDict in wordList:
                    playerList = list(player)
                    chosenWordList = list(chosenWord)
                    newPlayerList = ["","","","",""]
                    for char in range(len(player)):
                        if chosenWordList[char] == playerList[char]:
                            newPlayerList[char] = (Fore.GREEN + Style.BRIGHT + playerList[char].upper()+Style.RESET_ALL+" ")
                            print(chosenWordList)
                            input()
                            chosenWordList[char] = "!"
                            count[lcv]+=13
                            print(count)
                            print(chosenWordList)
                            print(newPlayerList)
                            input()
                    for char in range(len(player)):
                        if playerList[char] in chosenWordList:
                            newPlayerList[char] = (Fore.YELLOW + playerList[char].upper()+Fore.RESET +" ")
                            chosenWordList[chosenWordList.index(playerList[char])] = "!"
                            count[lcv] += 10

                        else:
                            newPlayerList[char] = (Style.DIM + playerList[char].upper()+Style.RESET_ALL+" ")
                            count[lcv] += 8
                        print(count)
                        print(chosenWordList)
                        print(newPlayerList)
                        print(playerList[char])
                        input()
                    display[lcv] = "".join(newPlayerList)
                    break
                else:
                    os.system('clear')
                    print(Fore.RED + Style.BRIGHT + "Word not in word list")
                    print(Style.RESET_ALL)
            else:
                os.system('clear')
                print(Fore.RED + Style.BRIGHT + "Word not in word list")
                print(Style.RESET_ALL)
        if win == True:
            win = False
            break
        