import os
from colorama import Back, Fore, Style

z=os.get_terminal_size()
z=z[0]
print(Back.BLACK)
os.system('clear')
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+".center(z))
print("|                                     |".center(z))
print("|            Tic-Tac-Toe              |".center(z))
print("|                                     |".center(z))
print("|              Welcome                |".center(z))
print("|                                     |".center(z))
print("|                                     |".center(z))
print("|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|".center(z))
print("|                                     |".center(z))
print("|                                     |".center(z))
print("|      1     |     2     |      3     |".center(z))
print("| ----------------------------------- |".center(z))
print("|      4     |     5     |      6     |".center(z))
print("| ----------------------------------- |".center(z))
print("|      7     |     8     |      9     |".center(z))
print("|                                     |".center(z))
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+".center(z))


print("Press ENTER to begin!".center(z))
input()


winner = 0

tl = "1"
tr = "3"
top = "2"
bl = "7"
br = "9"
bot = "8"
left = "4"
right = "6"
mid = "5"
os.system('clear')
print("\n\n")
print(f" {tl} | {top} | {tr} ".center(z))
print("-----------".center(z))
print(f" {left} | {mid} | {right} ".center(z))
print("-----------".center(z))
print(f" {bl} | {bot} | {br} ".center(z))

while winner == 0:
    print("Player 1's move: ".center(z))
    move1 = input()
    while move1 != "1" and move1 != "2" and move1 != "3" and move1 != "4" and move1 != "5" and move1 != "6" and move1 != "7" and move1 != "8" and move1 != "9":
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "1" and tl.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "2" and top.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "3" and tr.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "4" and left.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "5" and mid.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "6" and right.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "7" and bl.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "8" and bot.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    while move1 == "9" and br.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 1's move: ".center(z))
        move1 = input()
    if move1 == "1":
        tl = "X"
    elif move1 == "2":
        top = "X"
    elif move1 == "3":
        tr = "X"
    elif move1 == "4":
        left = "X"
    elif move1 == "5":
        mid = "X"
    elif move1 == "6":
        right = "X"
    elif move1 == "7":
        bl = "X"
    elif move1 == "8":
        bot = "X"
    elif move1 == "9":
        br = "X"

    os.system('clear')
    print("\n\n")
    print(f" {tl} | {top} | {tr} ".center(z))
    print("-----------".center(z))
    print(f" {left} | {mid} | {right} ".center(z))
    print("-----------".center(z))
    print(f" {bl} | {bot} | {br} ".center(z))

    if tl == "X" and top == "X" and tr == "X":
        winner = 1
        break
    elif left == "X" and mid == "X" and right == "X":
        winner = 1
        break
    elif bl == "X" and bot == "X" and br == "X":
        winner = 1
        break
    elif tl == "X" and mid == "X" and br == "X":
        winner = 1
        break
    elif tr == "X" and mid == "X" and bl == "X":
        winner = 1
        break
    elif tl == "X" and left == "X" and bl == "X":
        winner = 1
        break
    elif top == "X" and mid == "X" and bot == "X":
        winner = 1
        break
    elif tr == "X" and right == "X" and br == "X":
        winner = 1
        break
    elif tl.isalpha() and tr.isalpha() and top.isalpha() and mid.isalpha() and left.isalpha() and right.isalpha() and br.isalpha() and bl.isalpha() and bot.isalpha():
        winner = 3
        break

    print("Player 2's move: ".center(z))
    move2 = input()
    while move2 != "1" and move2 != "2" and move2 != "3" and move2 != "4" and move2 != "5" and move2 != "6" and move2 != "7" and move2 != "8" and move2 != "9":
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "1" and tl.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "2" and top.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "3" and tr.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "4" and left.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "5" and mid.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "6" and right.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "7" and bl.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "8" and bot.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    while move2.lower() == "9" and br.isalpha():
        print("That is not a valid move!".center(z))
        print("Player 2's move: ".center(z))
        move2 = input()
    if move2.lower() == "1":
        tl = "O"
    elif move2.lower() == "2":
        top = "O"
    elif move2.lower() == "3":
        tr = "O"
    elif move2.lower() == "4":
        left = "O"
    elif move2.lower() == "5":
        mid = "O"
    elif move2.lower() == "6":
        right = "O"
    elif move2.lower() == "7":
        bl = "O"
    elif move2.lower() == "8":
        bot = "O"
    elif move2.lower() == "9":
        br = "O"
    os.system('clear')
    print("\n\n")
    print(f" {tl} | {top} | {tr} ".center(z))
    print("-----------".center(z))
    print(f" {left} | {mid} | {right} ".center(z))
    print("-----------".center(z))
    print(f" {bl} | {bot} | {br} ".center(z))

    if tl == "O" and top == "O" and tr == "O":
        winner = 2
        break
    elif left == "O" and mid == "O" and right == "O":
        winner = 2
        break
    elif bl == "O" and bot == "O" and br == "O":
        winner = 2
        break
    elif tl == "O" and mid == "O" and br == "O":
        winner = 2
        break
    elif tr == "O" and mid == "O" and bl == "O":
        winner = 2
        break
    elif tl == "O" and left == "O" and bl == "O":
        winner = 2
        break
    elif top == "O" and mid == "O" and bot == "O":
        winner = 2
        break
    elif tr == "O" and right == "O" and br == "O":
        winner = 2
        break

os.system('clear')
print(Fore.RED + Style.BRIGHT)
if winner == 1:
    print("\n\n\n")
    print("0000  0      000  0   0 00000 0000     00     0     0 00000 0    0  0000  00".center(z))
    print("0   0 0     0   0  0 0  0     0   0   0 0     0     0   0   00   0 0      00".center(z))
    print("0000  0     00000   0   0000  0000      0     0  0  0   0   0 0  0  000   00".center(z))
    print("0     0     0   0   0   0     0   0     0     0 0 0 0   0   0  0 0     0    ".center(z))
    print("0     00000 0   0   0   00000 0   0   00000    0   0  00000 0   00 0000   00".center(z))
elif winner == 2:
    print("\n\n\n")
    print("0000  0      000  0   0 00000 0000     000    0     0 00000 0    0  0000  00".center(z))
    print("0   0 0     0   0  0 0  0     0   0   0   0   0     0   0   00   0 0      00".center(z))
    print("0000  0     00000   0   0000  0000      00    0  0  0   0   0 0  0  000   00".center(z))
    print("0     0     0   0   0   0     0   0   00      0 0 0 0   0   0  0 0     0    ".center(z))
    print("0     00000 0   0   0   00000 0   0   00000    0   0  00000 0   00 0000   00".center(z))
elif winner == 3:
    print("\n\n\n")
    print("00000 00000  0  0000     000     00000 00000 00000  00".center(z))
    print("  0     0   0  0        0   0      0     0   0      00".center(z))
    print("  0     0       000     00000      0     0   0000   00".center(z))
    print("  0     0          0    0   0      0     0   0        ".center(z))
    print("00000   0      0000     0   0      0   00000 00000  00".center(z))