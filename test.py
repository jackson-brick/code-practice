import csv
import random
from colorama import Fore, Style
import os
z = os.get_terminal_size()
z = z[0]

word = []
word.append(Fore.GREEN + "PooP"+Style.RESET_ALL)
word.append(Fore.YELLOW + "pEE"+Style.RESET_ALL)
word.append(Style.DIM + "fart" + Style.RESET_ALL)
word = "".join(word)
print(word)
print(len(word))
print(word.center(z))
print(word.center(z+len(word)-11))
print("XXX".center(z))

    







