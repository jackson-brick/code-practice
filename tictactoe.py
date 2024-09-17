
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


print(f"\n\n{row1}")
print(f"{row2}")
print(f"{row3}")
print(f"{row4}")
print(f"{row5}\n\n")

move1 = input("What is your first move? ")
while move1.lower() != "left" or move1.lower() != "right" or move1.lower() != "middle" or move1.lower() != "top mid" or move1.lower() != "top right" or move1.lower() != "top left" or move1.lower() != "bot mid" or move1.lower() != "bot right" or move1.lower() != "bot left" or not move1.isalpha():
    print("That is not a valid move!")
    move1 = input("What is your first move? ")
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

print(tl)

print(f"\n\n{row1}")
print(f"{row2}")
print(f"{row3}")
print(f"{row4}")
print(f"{row5}\n\n")








