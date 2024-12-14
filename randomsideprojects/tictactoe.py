
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")
print("|                                  |")
print("|           Tic-Tac-Toe            |")
print("|                                  |")
print("|             Welcome              |")
print("|                                  |")
print("|                                  |")
print("|-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-|")
print("|                                  |")
print("|                                  |")
print("|  top left | top mid | top right  |")
print("| -------------------------------- |")
print("|     left  |  middle |  right     |")
print("| -------------------------------- |")
print("|  bot left | bot mid | bot right  |")
print("|                                  |")
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")





winner = 0

tl = " "
tr = " "
top = " "
bl = " "
br = " "
bot = " "
left = " "
right = " "
mid = " "

print(f" {tl} | {top} | {tr} ")
print("-----------")
print(f" {left} | {mid} | {right} ")
print("-----------")
print(f" {bl} | {bot} | {br} ")

while winner == 0:
    move1 = input("Player 1's move: ")
    move1 = move1.lower()
    while move1 != "left" and move1 != "right" and move1 != "middle" and move1 != "top mid" and move1 != "top right" and move1 != "top left" and move1 != "bot mid" and move1 != "bot right" and move1 != "bot left":
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while not move1.isalpha:
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "top left" and tl.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "top mid" and top.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "top right" and tr.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "left" and left.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "middle" and mid.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "right" and right.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "bot left" and bl.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "bot mid" and bot.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    while move1 == "bot right" and br.isalpha():
        print("That is not a valid move!")
        move1 = input("Player 1's move: ")
    if move1 == "top left":
        tl = "X"
    elif move1 == "top mid":
        top = "X"
    elif move1 == "top right":
        tr = "X"
    elif move1 == "left":
        left = "X"
    elif move1 == "middle":
        mid = "X"
    elif move1 == "right":
        right = "X"
    elif move1 == "bot left":
        bl = "X"
    elif move1 == "bot mid":
        bot = "X"
    elif move1 == "bot right":
        br = "X"


    print(f" {tl} | {top} | {tr} ")
    print("-----------")
    print(f" {left} | {mid} | {right} ")
    print("-----------")
    print(f" {bl} | {bot} | {br} ")

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

    move2 = input("Player 2's move: ")
    move2 = move2.lower()
    while move2 != "left" and move2 != "right" and move2 != "middle" and move2 != "top mid" and move2 != "top right" and move2 != "top left" and move2 != "bot mid" and move2 != "bot right" and move2 != "bot left":
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while not move2.isalpha:
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "top left" and tl.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "top mid" and top.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "top right" and tr.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "left" and left.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "middle" and mid.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "right" and right.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "bot left" and bl.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "bot mid" and bot.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    while move2.lower() == "bot right" and br.isalpha():
        print("That is not a valid move!")
        move2 = input("Player 2's move: ")
    if move2.lower() == "top left":
        tl = "O"
    elif move2.lower() == "top mid":
        top = "O"
    elif move2.lower() == "top right":
        tr = "O"
    elif move2.lower() == "left":
        left = "O"
    elif move2.lower() == "middle":
        mid = "O"
    elif move2.lower() == "right":
        right = "O"
    elif move2.lower() == "bot left":
        bl = "O"
    elif move2.lower() == "bot mid":
        bot = "O"
    elif move2.lower() == "bot right":
        br = "O"

    print(f" {tl} | {top} | {tr} ")
    print("-----------")
    print(f" {left} | {mid} | {right} ")
    print("-----------")
    print(f" {bl} | {bot} | {br} ")

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

if winner == 1:
    print("Player 1 wins!")
elif winner == 2:
    print("Player 2 wins!")
elif winner == 3:
    print("It's a tie!")