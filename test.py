from colorama import Style, Fore
import os

screenSize = os.get_terminal_size()
z = screenSize[0]

myList = ["dogs" , "cats" , "goats" , "elephant" , "giraffe"]
wordCounter = 1
for word in range(len(myList)):
    if word == len(myList) - 1:
        print(Style.BRIGHT + myList[0].center(z) + Style.RESET_ALL)
    else: 
        print(myList[-wordCounter].center(z) + Style.RESET_ALL)
    wordCounter += 1
    
wordCounter = 1
for word in range(len(myList)):
    print((Style.BRIGHT + myList[-wordCounter].center(z)) + Style.RESET_ALL)
    wordCounter += 1
        




