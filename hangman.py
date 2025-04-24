import os

z = os.get_terminal_size()[0]

print("1 or 2 players?".center(z))
numPlayers=input()

while True:
    failCount = 0
    word = "bunny"
    wordList = list(word)
    blankList = list("_"*len(word))

    fail1 = "|         "
    fail2 = "|         "
    fail3 = "|         "
    fail4 = "|         "
    fail5 = "|         "
    fail6 = "|         "
    while True:
        if failCount == 1:
            fail1 = "|      ( )"
        elif failCount == 2:
            fail2 = "|       |"
        elif failCount == 3:
            fail3 = "|      /|"
        elif failCount == 4:
            fail4 = "|      /|\\"
        elif failCount == 5:
            fail5 = "|      / "
        elif failCount == 6:
            fail6 = "|      / \\"
        print(",-------,".center(z))
        print("|       |".center(z))
        print(fail1.center(z))
        if failCount <= 2:
            print(fail2.center(z))
        elif failCount == 3:
            print(fail3.center(z))
        else:
            print(fail4.center(z))
        if failCount <= 5:
            print(fail5.center(z))
        else:
            print(fail6.center(z))
        print("|         ".center(z))
        print("|_________".center(z))
        print("")
        if failCount < 6:
            if "_" in blankList:
                print(("Word: " + " ".join(blankList)).center(z))
                guess = input()
            else:
                os.system('clear')
                print("You win! Press ENTER to play again!".center(z))
                print("")
                print("Type QUIT to close the program".center(z))
                win = input()
                if win.lower().strip() == "quit":
                    quit()
                break
        else:
            print("You lose! Press ENTER to play again!".center(z))
            print("")
            print("Type QUIT to close the program!".center(z))
            lose = input()
            if lose.lower().strip() == "quit":
                quit()
            break
        if guess.lower().strip() == word:
            os.system('clear')
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
            
        else:
            failCount+=1

        