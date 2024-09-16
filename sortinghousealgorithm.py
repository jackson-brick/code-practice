
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")
print("+                                  +")
print("+           Sorting Hat            +")
print("+                                  +")
print("+             Welcome              +")
print("+                                  +")
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")

print("The sorting house algorithm will ask you some questions to decide which Hogwarts House you belong to.")

gryf = 1
rave = 1
huff = 1 
slyt = 1



brave = input("If you were in an unfamiliar place or situation, would you feel confident in knowing what to do to get to a better place?\n")
while brave.lower() != "yes" and brave.lower != "no":
    print("That is not a valid response. Please try again.")
    brave = input("If you were in an unfamiliar place or situation, would you feel confident in knowing what to do to get to a better place?\n")
if brave.lower() == "yes":
    gryf = gryf + 1
elif brave.lower() == "no":
    rave = rave + 1
    huff = huff + 1
    slyt = slyt + 1
loyal = input("If your friend needed help but your dignity was at stake, would you help them?\n")
while loyal.lower() != "yes" and loyal.lower() != "no":
    print("That is not a valid response. Please try again.")
    loyal = input("If your friend needed help but your dignity was at stake, would you help them?\n")
if loyal.lower() == "yes":
    gryf =  gryf + 1
chival = input("If someone else was in trouble, would you help them?\n")
curious = input("Does the world around you and the way it works strike you as interesting?\n")
create = input("Do you enjoy creating new things unseen or heard of before?\n")
kind = input("Do you like helping others in need even when not asked or compelled to do so?\n")
friend = input("Do you find yourself constantly making new friends and easily talking to strangers?\n")
pati = input("When others do things you do not like, are you usually able to keep your cool?\n")
ambi = input("Are you willing to do anything to achieve your goals?\n")
comp = input("When someone is better than you at something does that upset you?\n")















