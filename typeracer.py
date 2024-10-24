import os
import time
import random

screenSize = os.get_terminal_size()
z = int(screenSize[0])



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



print("Press ENTER to launch Type Racer\n\n".center(z))
input()
os.system('clear')

loading_sequence(4)

print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))
print("+                                  +".center(z))
print("+            Type Racer            +".center(z))
print("+                                  +".center(z))
print("+              Welcome             +".center(z))
print("+                                  +".center(z))
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))

paragraphLists = [[""]]
usedParagraph = random.choice(paragraphLists)

wordAcrossScreen = 0
emptySpaceCounter = 0
for word in usedParagraph:
    wordAcrossScreen += int(len(word))
    if wordAcrossScreen > z:
        wordAcrossScreen -= int(len(word))
        for i in range(z-wordAcrossScreen):
            print(" ", end = "")
        wordAcrossScreen = 0
    else:
        print(word, end = "")
    









