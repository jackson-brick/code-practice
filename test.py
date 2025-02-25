from colorama import Fore, Style
import os
import random
import time
z=os.get_terminal_size()
z=z[0]

keyboard_characters = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', ' ', '\t', '\n', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', '~', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

colors = ['red','yellow','green','magenta','blue','cyan']

def unencryption():
    print(Style.BRIGHT)
    for lcv in range(150):
        lineLen = random.randint(3,50)
        color = random.choice(colors)
        if color == 'red':
            for i in range(lineLen):
                print(Fore.RED + random.choice(keyboard_characters),end="")
        elif color == 'yellow':
            for i in range(lineLen):
                print(Fore.YELLOW + random.choice(keyboard_characters),end="")
        elif color == 'green':
            for i in range(lineLen):
                print(Fore.GREEN + random.choice(keyboard_characters),end="")
        elif color == 'blue':
            for i in range(lineLen):
                print(Fore.BLUE + random.choice(keyboard_characters),end="")
        
        time.sleep(0.05)
        

while True:
    os.system('clear')
    print(Style.DIM)
    print(("Computer Information: " + Style.NORMAL + Style.BRIGHT + Fore.RED +"LOCKED").center(z))
    print(Fore.GREEN)
    print("\n\n\n")
    code = input()
    unencryption()
    if code == "barackobAma":
        print("")
        print(Style.BRIGHT + Fore.GREEN)
        print("Code success. Press ENTER to continue.")
        input()
        os.system('clear')
        break
    else:
        print("")
        print(Style.BRIGHT + Fore.RED)
        print("Code failure. Press ENTER to try again.")
        input()
        os.system('clear')
        
print("Secret message")

