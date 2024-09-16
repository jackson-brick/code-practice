
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")
print("+                                  +")
print("+           Sorting Hat            +")
print("+                                  +")
print("+             Welcome              +")
print("+                                  +")
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")

print("The sorting house algorithm will ask you some questions to decide which Hogwarts House you belong to.")

gryf = 0
rave = 0
huff = 0 
slyt = 0



brave = input("If you were in an unfamiliar place or situation, would you feel confident in knowing what to do to get to a better place?\n")
while brave.lower() != "yes" and brave.lower != "no":
    print("That is not a valid response. Please try again.")
    brave = input("If you were in an unfamiliar place or situation, would you feel confident in knowing what to do to get to a better place?\n")
if brave.lower() == "yes":
    gryf = gryf + 1
    rave = rave - 1
    huff = huff - 1
    slyt = slyt - 1
elif brave.lower() == "no":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff + 1
    slyt = slyt + 1
loyal = input("If your friend needed help but your dignity was at stake, would you help them?\n")
while loyal.lower() != "yes" and loyal.lower() != "no":
    print("That is not a valid response. Please try again.")
    loyal = input("If your friend needed help but your dignity was at stake, would you help them?\n")
if loyal.lower() == "yes":
    gryf = gryf + 1
    rave = rave - 1
    huff = huff - 1
    slyt = slyt - 1
elif loyal.lower() == "no":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff + 1
    slyt = slyt + 1
chival = input("If someone else was in trouble, would you help them?\n")
while chival.lower() != "yes" and chival.lower != "no":
    print("That is not a valid response. Please try again.")
    chival = input("If someone else was in trouble, would you help them?\n")
if chival.lower() == "yes":
    gryf = gryf + 1
    rave = rave - 1
    huff = huff - 1
    slyt = slyt - 1
elif chival.lower() == "no":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff + 1
    slyt = slyt + 1
curious = input("Does the world around you and the way it works strike you as interesting?\n")
while curious.lower() != "yes" and curious.lower != "no":
    print("That is not a valid response. Please try again.")
    curious = input("Does the world around you and the way it works strike you as interesting?\n")
if curious.lower() == "yes":
    gryf = gryf - 1
    rave = rave - 1
    huff = huff + 1
    slyt = slyt - 1
elif curious.lower() == "no":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff - 1
    slyt = slyt + 1
create = input("Do you enjoy creating new things unseen or heard of before?\n")
while create.lower() != "yes" and create.lower != "no":
    print("That is not a valid response. Please try again.")
    create = input("Do you enjoy creating new things unseen or heard of before?\n")
if create.lower() == "yes":
    gryf = gryf - 1
    rave = rave - 1
    huff = huff + 1
    slyt = slyt - 1
elif create.lower() == "no":
    gryf = gryf + 1
    rave = rave + 1
    huff = huff - 1
    slyt = slyt + 1
kind = input("Do you like helping others in need even when not asked or compelled to do so?\n")
while kind.lower() != "yes" and kind.lower != "no":
    print("That is not a valid response. Please try again.")
    kind = input("Do you like helping others in need even when not asked or compelled to do so?\n")
if kind.lower() == "yes":
    gryf = gryf + 1
    rave = rave - 1
    huff = huff + 1
    slyt = slyt - 1
elif kind.lower() == "no":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff - 1
    slyt = slyt + 1
friend = input("Do you find yourself constantly making new friends and easily talking to strangers?\n")
while friend.lower() != "yes" and friend.lower != "no":
    print("That is not a valid response. Please try again.")
    friend = input("Do you find yourself constantly making new friends and easily talking to strangers?\n")
if friend.lower() == "yes":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff - 1
    slyt = slyt - 1
elif friend.lower() == "no":
    gryf = gryf + 1
    rave = rave - 1
    huff = huff + 1
    slyt = slyt + 1
pati = input("When others do things you do not like, are you usually able to keep your cool?\n")
while pati.lower() != "yes" and pati.lower != "no":
    print("That is not a valid response. Please try again.")
    pati = input("When others do things you do not like, are you usually able to keep your cool?\n")
if pati.lower() == "yes":
    gryf = gryf - 1
    rave = rave + 1
    huff = huff - 1
    slyt = slyt - 1
elif pati.lower() == "no":
    gryf = gryf + 1
    rave = rave - 1
    huff = huff + 1
    slyt = slyt + 1
ambi = input("Are you willing to do anything to achieve your goals?\n")
while ambi.lower() != "yes" and ambi.lower != "no":
    print("That is not a valid response. Please try again.")
    ambi = input("Are you willing to do anything to achieve your goals?\n")
if ambi.lower() == "yes":
    gryf = gryf - 1
    rave = rave - 1
    huff = huff - 1
    slyt = slyt + 1
elif ambi.lower() == "no":
    gryf = gryf + 1
    rave = rave + 1
    huff = huff + 1
    slyt = slyt - 1
comp = input("When someone is better than you at something does that upset you?\n")
while comp.lower() != "yes" and comp.lower != "no":
    print("That is not a valid response. Please try again.")
    comp = input("When someone is better than you at something does that upset you?\n")
if comp.lower() == "yes":
    gryf = gryf - 1
    rave = rave - 1
    huff = huff - 1
    slyt = slyt + 1
elif comp.lower() == "no":
    gryf = gryf + 1
    rave = rave + 1
    huff = huff + 1
    slyt = slyt - 1

if gryf >= rave and gryf >= huff and gryf >= slyt:
    print("Your Hogwarts house is Gryffindor!")
elif rave > gryf and rave >= huff and rave >= slyt:
    print("Your Hogwarts house is Ravenclaw!")
elif huff > gryf and huff > rave and huff >= slyt:
    print("Your Hogwarts house is Hufflepuff!")
elif slyt > gryf and slyt > rave and slyt > huff:
    print("Your Hogwarts house is Slytherin!")













