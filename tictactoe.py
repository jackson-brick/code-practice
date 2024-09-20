
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







tl = " "
tr = " "
top = " "
bl = " "
br = " "
bot = " "
left = " "
right = " "
mid = " "

row1 = f" {tl} | {top} | {tr} "
row2 = "-----------"
row3 = f" {left} | {mid} | {right} "
row4 = "-----------"
row5 = f" {bl} | {bot} | {br} "


print(f" {tl} | {top} | {tr} ")
print("-----------")
print(f" {left} | {mid} | {right} ")
print("-----------")
print(f" {bl} | {bot} | {br} ")

move1 = input("Player 1's move: ")
while move1.lower() != "left" and move1.lower() != "right" and move1.lower() != "middle" and move1.lower() != "top mid" and move1.lower() != "top right" and move1.lower() != "top left" and move1.lower() != "bot mid" and move1.lower() != "bot right" and move1.lower() != "bot left" and not move1.isalpha():
    print("That is not a valid move!")
    move1 = input("Player 1's move: ")
if move1.lower() == "top left":
    tl = "X"
elif move1.lower() == "top mid":
    top = "X"
elif move1.lower() == "top right":
    tr = "X"
elif move1.lower() == "left":
    left = "X"
elif move1.lower() == "middle":
    mid = "X"
elif move1.lower() == "right":
    right = "X"
elif move1.lower() == "bot left":
    bl = "X"
elif move1.lower() == "bot mid":
    bot = "X"
elif move1.lower() == "bot right":
    br = "X"


print(f" {tl} | {top} | {tr} ")
print("-----------")
print(f" {left} | {mid} | {right} ")
print("-----------")
print(f" {bl} | {bot} | {br} ")

move2 = input("Player 2's move: ")
while move2.lower() != "left" and move2.lower() != "right" and move2.lower() != "middle" and move2.lower() != "top mid" and move2.lower() != "top right" and move2.lower() != "top left" and move2.lower() != "bot mid" and move2.lower() != "bot right" and move2.lower() != "bot left" and not move2.isalpha():
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




