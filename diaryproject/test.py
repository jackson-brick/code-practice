import random
import os
from colorama import Fore, Style

while True:
    print(Style.BRIGHT + "Test text" + Style.NORMAL + Fore.RESET)
    print("This text should have no style or fore")
    INPUT = input()
    if INPUT == "true":
        print(Fore.RED)
    