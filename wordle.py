from colorama import Fore, Style
import random
import os
z = os.get_terminal_size()
z=z[0]
#os.system('clear')

word_list = ["great","laugh","smart","crazy"]

chosenWord = random.choice(word_list)
display = "_ _ _ _ _".center(z) + "\n\n"
newDisplay = ""

for lcv in range(6):
    print(newDisplay)
    print((display.center(z))* (6-lcv))
    player = input()
    if player.lower() == chosenWord:
        print("You Win!".center(z))
        quit()
    if len(player) == 5:
        for char in range(len(player)):
            if chosenWord[char] == player[char].lower():
                display[char] = player[char].upper()