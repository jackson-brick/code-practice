import os
import random
import csv

wordOptions = []
with open('gamesandmisc/hangman.csv','r') as file:
    csvWord = csv.DictReader(file)
    for i in csvWord:
        wordOptions.append(i['word'])


z = os.get_terminal_size()[0]

while True:
    os.system('clear')
    print("1 or 2 players?".center(z))
    numPlayers=input()
    if numPlayers.strip() == "1":
        numPlayers = 1
        break
    elif numPlayers.strip() == "2":
        numPlayers = 2
        break

while True:
    os.system('clear')
    letterBank = []
    failCount = 0
    if numPlayers == 1:
        word = random.choice(wordOptions)
    else:
        while True:
            os.system('clear')
            print("Without the other player looking, choose a word".center(z))
            print("(Phrases are not supported yet, only one word please)".center(z))
            word = input()
            if " " not in word.strip():
                if word.strip().isalpha():
                    if len(word.strip()) >3 and len(word) <41:
                        word = word.strip().lower()
                        break
    wordList = list(word)
    blankList = list("_"*len(word))

    fail1 = "|         "
    fail2 = "|         "
    fail3 = "|         "
    fail4 = "|         "
    fail5 = "|         "
    fail6 = "|         "
    fail7 = "|         "
    fail8 = "|         "
    fail9 = "|         "
    fail10 = "|         "
    while True:
        os.system('clear')
        if failCount == 1:
            fail1 = " |      ( ) "
        elif failCount == 2:
            fail2 = " |      ( )\\"
        elif failCount == 3:
            fail3 = " |     /( )\\"
        elif failCount == 4:
            fail4 = "|       |"
        elif failCount == 5:
            fail5 = "|      /|"
        elif failCount == 6:
            fail6 = "|      /|\\"
        elif failCount == 7:
            fail7 = " |      /  "
        elif failCount == 8:
            fail8 = " |      / \\ "
        elif failCount == 9:
            fail9 = " |     _/ \\ "
        elif failCount == 10:
            fail10 = " |     _/ \\_"
        
        print(",-------,".center(z))
        print("|       |".center(z))
        if failCount <2:
            print(fail1.center(z))
        elif failCount == 2:
            print(fail2.center(z))
        else:
            print(fail3.center(z))
        if failCount == 4:
            print(fail4.center(z))
        elif failCount == 5:
            print(fail5.center(z))
        else:
            print(fail6.center(z))
        if failCount == 7:
            print(fail7.center(z))
        elif failCount == 8:
            print(fail8.center(z))
        elif failCount == 9:
            print(fail9.center(z))
        else:
            print(fail10.center(z))
        print("|         ".center(z))
        print("|_________".center(z))
        print("")
        print(f"Guessed Letters: {', '.join(letterBank)}".center(z))
        print("")
        if failCount <= 10:
            if "_" in blankList:
                print(("Word: " + " ".join(blankList)).center(z))
                guess = input()
            else:
                os.system('clear')
                print(" ".join(list(word.upper())).center(z))
                print("")
                print("You win! Press ENTER to play again!".center(z))
                print("")
                print("Type QUIT to close the program".center(z))
                win = input()
                if win.lower().strip() == "quit":
                    quit()
                break
        else:
            print(" ".join(list(word.upper())).center(z))
            print("")
            print("You lose! Press ENTER to play again!".center(z))
            print("")
            print("Type QUIT to close the program!".center(z))
            lose = input()
            if lose.lower().strip() == "quit":
                quit()
            break
        if guess.lower().strip() == word:
            os.system('clear')
            print(" ".join(list(word.upper())).center(z))
            print("")
            print("You win! Press ENTER to play again!".center(z))
            print("")
            print("Type QUIT to close the program".center(z))
            win = input()
            if win.lower().strip() == "quit":
                quit()
            break
        if len(guess.strip()) == 1:
            if guess.lower() in word:
                for i in range(len(wordList)):
                    if guess.lower() == wordList[i]:
                        blankList[i] = wordList[i].upper()
                        wordList[i] = "!"
            else:
                failCount+=1
                if guess.strip().upper() not in letterBank:
                    letterBank.append(guess.strip().upper())
            
        else:
            failCount+=1

        