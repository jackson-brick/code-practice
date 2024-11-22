from colorama import Fore, Style, Back
import os

os.system('clear')
print("Who is the best person ever?")
print("\n\ta. Jackson\tb. Zoe\tc. Evany\td. Envy")
input()
os.system('clear')
print("Who is the best person ever?")
print(Style.DIM + "\n\ta. Jackson\tb. Zoe" + Style.RESET_ALL + Style.BRIGHT + "\tc. Evany" + Style.RESET_ALL + Style.DIM + "\td. Envy")