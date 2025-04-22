import json
import time
import random
import os
from colorama import Fore, Style, Back
z = os.get_terminal_size()
z = z[0]
os.system('clear')
saidNoOnce = 0
#You are trapped in a computer, the narrator is trying to keep you in











while True:
    print("Would you like to launch the program?".center(z))
    print((Fore.GREEN + Style.BRIGHT + "YES\t\t" + Fore.RED + Style.DIM + "no").center(z + 10))
    print(Style.RESET_ALL)
    startInput = input()
    if "yes" in startInput.lower().strip():
        break
    else:
        noWord = ""
        os.system('clear')
        noList = ["Ughh, let's try this agai--","Maybe say yes next time--","This is getting old--","JUST LAUNCH THE PROGRA--","I WILL REMEMBER THI--","PLEASE, JUST DO IT--","The program is not launched."]
        
        for letter in noList[saidNoOnce]:
            os.system('clear')
            noWord += letter
            print(noWord.center(z))
            
            time.sleep(0.05)
        if saidNoOnce <=5:
            saidNoOnce += 1
        print("")
        time.sleep(0.3)
        os.system('clear')

os.system('clear')



