import os
import time
import random
import math
from colorama import Fore, Style

screenSize = os.get_terminal_size()
z = int(screenSize[0])

gameType = "Phrases"
fontColor = "Default"
fontEmp = "Finished"
mode = "Easy"

def loading_sequence(seconds_to_load):
    loadingList = ["fun paragraphs" , "challenging words" , "all the code" , "security measures" , "eye-tracking software" , "the CIA's confidential files" , "your address" , "my shopping list" , "all the answers to the algebra test"]
    usedLoadingList = []
    for lcv in range(seconds_to_load):
        usedLoadingList.append(random.choice(loadingList))
        loadingList.remove(f"{usedLoadingList[lcv]}")
    os.system('clear')
    time.sleep(0.5)
    while seconds_to_load > 0:
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}".center(z))
        time.sleep(0.5)
        os.system('clear')
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}  .".center(z))
        time.sleep(0.5)
        os.system('clear')
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}  .  .".center(z))
        time.sleep(0.5)
        os.system('clear')
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}  .  .  .".center(z))
        time.sleep(1)
        os.system('clear')
        seconds_to_load -= 1
    while len(usedLoadingList) > 0:
        loadingList.append(usedLoadingList[-1])
        usedLoadingList.pop(-1)





def welcome():
    global playerInput
    print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))
    print("+                                  +".center(z))
    print("+            Type Racer            +".center(z))
    print("+                                  +".center(z))
    print("+              Welcome             +".center(z))
    print("+                                  +".center(z))
    print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))
    print("")
    print("Welcome to Type Racer! Challenge your typing accuracy, precision, and speed with either a longer paragraph or a string of words. Visit SETTINGS to change your preferences. Type START when ready to begin!\n\n".center(z))
    playerInput = input("")
    os.system('clear')

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
                print(Style.RESET_ALL + settingSentence[0].center(z))
                print(Style.RESET_ALL + Style.BRIGHT + settingSentence[1].center(z) + Style.RESET_ALL)
                print(Style.RESET_ALL + Style.BRIGHT + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "red":
                print(Style.RESET_ALL + Fore.RED + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.RED +  settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.RED + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "green":
                print(Style.RESET_ALL + Fore.GREEN + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.GREEN + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.GREEN + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "yellow":
                print(Style.RESET_ALL + Fore.YELLOW + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.YELLOW + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.YELLOW + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "blue":
                print(Style.RESET_ALL + Fore.BLUE + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.BLUE + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.BLUE + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "magenta":
                print(Style.RESET_ALL + Fore.MAGENTA + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.MAGENTA + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.MAGENTA + settingSentence[2].center(z) + Style.RESET_ALL)
            elif fontColor.lower() == "cyan":
                print(Style.RESET_ALL + Fore.CYAN + settingSentence[0].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.CYAN + settingSentence[1].center(z) + Style.RESET_ALL)
                print( Style.BRIGHT + Fore.CYAN + settingSentence[2].center(z) + Style.RESET_ALL)
    elif gameType.lower() == "words":
        wordCounter = 1
        if fontEmp.lower() == "finished":
            if fontColor.lower() == "default":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "red":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + Fore.RED + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(Fore.RED + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "green":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + Fore.GREEN + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(Fore.GREEN + settingWord[ele].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "yellow":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + Fore.YELLOW + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(Fore.YELLOW + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "blue":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + Fore.BLUE + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(Fore.BLUE + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "magenta":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + Fore.MAGENTA + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(Fore.MAGENTA + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "cyan":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.BRIGHT + Fore.CYAN + settingWord[0].center(z) + Style.RESET_ALL)
                    else: 
                        print(Fore.CYAN + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
        elif fontEmp.lower() == "unfinished":
            if fontColor.lower() == "default":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + (settingWord[0]).center(z))
                    else: 
                        print(Style.BRIGHT + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "red":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + Fore.RED + settingWord[0].center(z))
                    else: 
                        print(Style.BRIGHT + Fore.RED + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "green":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + Fore.GREEN + settingWord[0].center(z))
                    else: 
                        print(Style.BRIGHT + Fore.GREEN + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "yellow":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + Fore.YELLOW + settingWord[0].center(z))
                    else: 
                        print(Style.BRIGHT + Fore.YELLOW + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "blue":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + Fore.BLUE + settingWord[0].center(z))
                    else: 
                        print(Style.BRIGHT + Fore.BLUE + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "magenta":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + Fore.MAGENTA + settingWord[0].center(z))
                    else: 
                        print(Style.BRIGHT + Fore.MAGENTA + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
            elif fontColor.lower() == "cyan":
                for word in range(len(settingWord)):
                    if word == len(settingWord) - 1:
                        print(Style.RESET_ALL + Fore.CYAN + settingWord[0].center(z))
                    else: 
                        print(Style.BRIGHT + Fore.CYAN + settingWord[-wordCounter].center(z) + Style.RESET_ALL)
                    wordCounter += 1
    print("")
    
    global settingInput
    print(Fore.WHITE + f"Game type:   {gameType}".center(z))
    print("")
    print(Fore.WHITE + f"Font color:   {fontColor}".center(z))
    print("")
    print(Fore.WHITE + f"Font emphasis:   {fontEmp}".center(z))
    print("")
    print(Fore.WHITE + f"Mode:   {mode}".center(z))

    settingInput = input(Fore.WHITE + Style.BRIGHT + "To change a setting, type the name of the setting".center(z) + "Type BACK to return to the start screen:".center(z) + "\n" + Style.RESET_ALL)
    os.system('clear')
    if settingInput.lower() == "game type":
        if gameType.lower() == "phrases":
            gameType = "Words"
            
        elif gameType.lower() == "words":
            gameType = "Phrases"
            
    elif settingInput.lower() == "font color":
        print(("Default   " + Fore.RED + "Red   " + Style.RESET_ALL + Fore.YELLOW + "Yellow   " + Style.RESET_ALL + Fore.GREEN + "Green   " + Style.RESET_ALL + Fore.BLUE + "Blue   " + Style.RESET_ALL + Fore.MAGENTA + "Magenta   " + Style.RESET_ALL + Fore.CYAN + "Cyan" + Style.RESET_ALL).center(z))
        colorPreference = input()
        if colorPreference.lower() == "red":
            fontColor = "Red"
            os.system('clear')
        elif colorPreference.lower() == "yellow":
            fontColor = "Yellow"
            os.system('clear')
        elif colorPreference.lower() == "green":
            fontColor = "Green"
            os.system('clear')
        elif colorPreference.lower() == "blue":
            fontColor = "Blue"
            os.system('clear')
        elif colorPreference.lower() == "magenta":
            fontColor = "Magenta"
            os.system('clear')
        elif colorPreference.lower() == "cyan":
            fontColor = "Cyan"
            os.system('clear')
        elif colorPreference.lower() == "default":
            fontColor = "Default"
            os.system('clear')
    elif settingInput.lower() == "font emphasis":
        if fontEmp.lower() == "finished":
            fontEmp = "Unfinished"
            
        elif fontEmp.lower() == "unfinished":
            fontEmp = "Finished"
            
    elif settingInput.lower() == "mode":
        if mode.lower() == "easy":
            mode = "Hard"
            
        elif mode.lower() == "hard":
            mode = "Easy"
            
        else:
            pass
            
    
def print_paragraph():
    global checkParagraph
    global usedParagraph
    paragraph = [["Do nothing out of selfish ambition or vain conceit.","Rather, in humility value others above yourselves,","not looking to your own interests","but each of you to the interests of the others."] , ["The only people for me are the mad ones,","the ones who are mad to live, mad to talk, mad to be saved,","desirous of everything at the same time, the ones who never yawn or say a commonplace thing,","but burn, burn, burn like fabulous yellow roman candles","exploding like spiders across the stars."] , ["And he humbled you and let you hunger and fed you with manna,","which you did not know, nor did your fathers know,","that he might make you know that man does not live by bread alone,","but man lives by every word that comes from the mouth of the Lord."] , ["I must not fear. Fear is the mind-killer.","Fear is the little-death that brings total obliteration. I will face my fear.","I will permit it to pass over me and through me.","And when it has gone past I will turn the inner eye to see its path.","Where the fear has gone there will be nothing. Only I will remain."] , ["I am an invisible man.","No, I am not a spook like those who haunted Edgar Allan Poe;","nor am I one of your Hollywood-movie ectoplasms.","I am a man of substance, of flesh and bone, fiber and liquids—","and I might even be said to possess a mind.","I am invisible, understand, simply because people refuse to see me."] , ["For whoever would save his life will lose it,","but whoever loses his life for my sake and the gospel’s will save it.","For what does it profit a man to gain","the whole world and forfeit his soul?"] , ["What then shall we say to these things?","If God is for us, who can be against us?","He who did not spare his own Son but gave him up for us all,","how will he not also with him graciously give us all things?"] , ["For God has not destined us for wrath,","but to obtain salvation through our Lord Jesus Christ,","who died for us so that whether we are awake or asleep we might live with him."] , ["For we do not have a high priest who is unable to sympathize with our weaknesses,","but one who in every respect has been tempted as we are, yet without sin.","Let us then with confidence draw near to the throne of grace,","that we may receive mercy and find grace to help in time of need."]]
    usedParagraph = random.choice(paragraph)
    if fontEmp.lower() == "finished":
        if fontColor.lower() == "default":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
        elif fontColor.lower() == "red":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + Fore.RED + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(Fore.RED + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
        elif fontColor.lower() == "green":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + Fore.GREEN + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(Fore.GREEN + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
        elif fontColor.lower() == "yellow":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + Fore.YELLOW + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(Fore.YELLOW + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
        elif fontColor.lower() == "blue":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + Fore.BLUE + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(Fore.BLUE + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
        elif fontColor.lower() == "magenta":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + Fore.MAGENTA + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(Fore.MAGENTA + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
        elif fontColor.lower() == "cyan":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.BRIGHT + Fore.CYAN + usedParagraph[ele].center(z) + Style.RESET_ALL)
                else: 
                    print(Fore.CYAN + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
    elif fontEmp.lower() == "unfinished":
        if fontColor.lower() == "default":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + (usedParagraph[ele]).center(z))
                else: 
                    print(Style.BRIGHT + usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
        elif fontColor.lower() == "red":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + Fore.RED + usedParagraph[ele].center(z))
                else: 
                    print(Style.BRIGHT + Fore.RED + usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
        elif fontColor.lower() == "green":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + Fore.GREEN + usedParagraph[ele].center(z))
                else: 
                    print(Style.BRIGHT + Fore.GREEN + usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
        elif fontColor.lower() == "yellow":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + Fore.YELLOW + usedParagraph[ele].center(z))
                else: 
                    print(Style.BRIGHT + Fore.YELLOW + usedParagraph[ele].center(z) + Style.RESET_ALL)
                
        elif fontColor.lower() == "blue":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + Fore.BLUE + usedParagraph[ele].center(z))
                else: 
                    print(Style.BRIGHT + Fore.BLUE + usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
        elif fontColor.lower() == "magenta":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + Fore.MAGENTA + usedParagraph[ele].center(z))
                else: 
                    print(Style.BRIGHT + Fore.MAGENTA + usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
        elif fontColor.lower() == "cyan":
            for ele in range(len(usedParagraph) - 1):
                if ele == 0:
                    print(Style.RESET_ALL + Fore.CYAN + usedParagraph[ele].center(z))
                else: 
                    print(Style.BRIGHT + Fore.CYAN + usedParagraph[ele].center(z) + Style.RESET_ALL)
                    
    print("")
        
def print_wordSequence():
    wordSequence = [["dog" , "cat" , "goat" , "cow" , "elephant" , "fish" , "giraffe" , "eagle" , "cheetah" , "chicken" , "horse" , "shark" , "dolphin" , "parrot" , "sheep" , "pig"]]


print("Press ENTER to launch Type Racer\n\n".center(z))
input()
os.system('clear')

#loading_sequence(4)

while True:
    welcome()
    if playerInput.lower() == "start":
        print_paragraph()
        global timeStart
        timeStart = time.time()
        print("\n")
        response = input()
        if response == 0:
            break
        else:
            print("You've made a mistake! Try again. Press ENTER to start.")
            input()
    elif playerInput.lower() == "settings":
        while True:
            settings()
            if settingInput.lower() == "back":
                break
        
    


 

