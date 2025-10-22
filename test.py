import os
from colorama import Fore, Style, Back
z=os.get_terminal_size()[0]

x = Back.BLUE + "   " + Back.RESET
y = len(Back.BLUE + Back.RESET)
print(f"|{x}|".center(z+y))

print("|   |".center(z))
print(len(Back.BLUE))
print(len(Back.RED))
print(len(Back.GREEN))
print(len(Back.CYAN))