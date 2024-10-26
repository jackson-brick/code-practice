from colorama import Style, Fore
import os

screenSize = os.get_terminal_size()
z = screenSize[0]

gameType = "Words"
fontColor = "Red"
fontEmp = "Unfinished"
mode = "Easy"

def settings():
    print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))
    print("+                                  +".center(z))
    print("+             Settings             +".center(z))
    print("+                                  +".center(z))
    print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))
    print("")
    global gameType
    global fontColor
    global fontEmp
    global mode
    settingSentence = ["Two roads diverged in a wood, and I-" , "I took the one less traveled by," , "And that has made all the difference."]
    settingWord = ["dogs" , "cats" , "goats" , "giraffes" , "elephants" , "groundhogs" , "killer whales" , "sharks" , "eagles" , "penguins" , "bears" , "camels"]
    if gameType.lower() == "phrases":
        if fontEmp.lower() == "finished":
            if fontColor.lower() == "default":
                print(Style.BRIGHT + settingSentence[0].center(z) + Style.RESET_ALL)
                print(settingSentence[1].center(z) + Style.RESET_ALL)
                print(settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "red":
                print(Style.BRIGHT + Fore.RED + settingSentence[0].center(z) + Style.RESET_ALL)
                print(Fore.RED + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Fore.RED + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "green":
                print(Style.BRIGHT + Fore.GREEN + settingSentence[0].center(z) + Style.RESET_ALL)
                print(Fore.GREEN + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Fore.GREEN + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "yellow":
                print(Style.BRIGHT + Fore.YELLOW + settingSentence[0].center(z) + Style.RESET_ALL)
                print(Fore.YELLOW + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Fore.YELLOW + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "blue":
                print(Style.BRIGHT + Fore.BLUE + settingSentence[0].center(z) + Style.RESET_ALL)
                print(Fore.BLUE + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Fore.BLUE + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "magenta":
                print(Style.BRIGHT + Fore.MAGENTA + settingSentence[0].center(z) + Style.RESET_ALL)
                print(Fore.MAGENTA + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Fore.MAGENTA + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "cyan":
                print(Style.BRIGHT + Fore.CYAN + settingSentence[0].center(z) + Style.RESET_ALL)
                print(Fore.CYAN + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Fore.CYAN + settingSentence[2].center(z) + Style.RESET_ALL)
        elif fontEmp.lower() == "unfinished":
            if fontColor.lower() == "default":
                print(settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "red":
                print(Fore.RED + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.RED +  settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.RED + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "green":
                print(Fore.GREEN + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.GREEN + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.GREEN + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "yellow":
                print(Fore.YELLOW + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.YELLOW + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.YELLOW + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "blue":
                print(Fore.BLUE + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.BLUE + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.BLUE + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "magenta":
                print(Fore.MAGENTA + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.MAGENTA + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.MAGENTA + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "cyan":
                print(Fore.CYAN + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.CYAN + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.CYAN + settingSentence[2].center(z) + Style.RESET_ALL)
    elif gameType.lower() == "words":
        wordCounter = 1
        if fontEmp.lower() == "finished":
            if fontColor.lower() == "default":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "red":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + Fore.RED + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((Fore.RED + settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "green":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + Fore.GREEN + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((Fore.GREEN + settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "yellow":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + Fore.YELLOW + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((Fore.YELLOW + settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "blue":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + Fore.BLUE + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((Fore.BLUE + settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "magenta":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + Fore.MAGENTA + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((Fore.MAGENTA + settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "cyan":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Style.BRIGHT + Fore.CYAN + settingWord[0]).center(z) + Style.RESET_ALL)
                    else: 
                        print((Fore.CYAN + settingWord[-wordCounter]).center(z) + Style.RESET_ALL)
                    wordCounter += 1
        elif fontEmp.lower() == "unfinished":
            if fontColor.lower() == "default":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
            elif fontColor.lower() == "red":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Fore.RED + settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + Fore.RED + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
            elif fontColor.lower() == "green":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Fore.GREEN + settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + Fore.GREEN + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
            elif fontColor.lower() == "yellow":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Fore.YELLOW + settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + Fore.YELLOW + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
            elif fontColor.lower() == "blue":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Fore.BLUE + settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + Fore.BLUE + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
            elif fontColor.lower() == "magenta":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Fore.MAGENTA + settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + Fore.MAGENTA + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
            elif fontColor.lower() == "cyan":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print((Fore.CYAN + settingWord[0]).center(z))
                    else: 
                        print((Style.BRIGHT + Fore.CYAN + settingWord[-wordCounter]).center(z))
                    wordCounter += 1
    print("")
    while True:
        print(Fore.WHITE + f"Game type:   {gameType}".center(z))
        print("")
        print(Fore.WHITE + f"Font color:   {fontColor}".center(z))
        print("")
        print(Fore.WHITE + f"Font emphasis:   {fontEmp}".center(z))
        print("")
        print(Fore.WHITE + f"Mode:   {mode}".center(z))
        settingInput = input(Fore.WHITE + Style.BRIGHT + "To change a setting, type the name of the setting".center(z) + "Type BACK to return to the start screen:".center(z) + "\n")


#print(Fore.RED + "hello")
settings()

(                                                                                          )
(                                                                                          )
(                                                                                   )
(                                                                                   )