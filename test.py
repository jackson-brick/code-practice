from colorama import Fore, Style, Back
import os

os.system('clear')
print("Who is the best person ever?")
print(Style.BRIGHT + "\n\ta. Jackson\tb. Benji\tc. Evany\td. Envy" + Style.DIM)
input()
os.system('clear')
print("Who is the best person ever?")
print(Style.DIM + "\n\ta. Jackson\tb. Zoe" + Style.RESET_ALL + Style.BRIGHT + "\tc. Evany" + Style.RESET_ALL + Style.DIM + "\td. Envy")