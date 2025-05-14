import time
import os
import random
z = os.get_terminal_size()[0]
os.system('clear')

d1 = " /\\ "
d2 = "|  |"
d3 = " \\/ "
  
c1 = " () "
c2 = "()()"
c3 = " || "

h1 = "/\\/\\"
h2 = "\\  /"
h3 = " \\/ "

s1 = " /\\ "
s2 = "(  )"
s3 = " || "


deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
chosenCards = []

def displayCard(value1,suit1,value2,suit2,ten0,ten1):
    if ten0:
        al = value1
        ar = value1
    else:
        al = value1 + " "
        ar = " " + value1
    if ten1:
        bl = value2
        br = value2
    else:
        bl = value2 + " "
        br = " " + value2

    
    if suit1 == "D":
        row1c1 = d1
        row2c1 = d2
        row3c1 = d3
    elif suit1 == "H":
        row1c1 = h1
        row2c1 = h2
        row3c1 = h3
    elif suit1 == "C":
        row1c1 = c1
        row2c1 = c2
        row3c1 = c3
    elif suit1 == "S":
        row1c1 = s1
        row2c1 = s2
        row3c1 = s3
    if suit2 == "D":
        row1c2 = d1
        row2c2 = d2
        row3c2 = d3
    elif suit2 == "H":
        row1c2 = h1
        row2c2 = h2
        row3c2 = h3
    elif suit2 == "C":
        row1c2 = c1
        row2c2 = c2
        row3c2 = c3
    elif suit2 == "S":
        row1c2 = s1
        row2c2 = s2
        row3c2 = s3
    print(f"+------------+       +------------+".center(z))
    print(f"| {al}      {ar} |       | {bl}      {br} |".center(z))
    print(f"|            |       |            |".center(z))
    print(f"|    {row1c1}    |       |    {row1c2}    |".center(z))
    print(f"|    {row2c1}    |       |    {row2c2}    |".center(z))
    print(f"|    {row3c1}    |       |    {row3c2}    |".center(z))
    print(f"|            |       |            |".center(z))
    print(f"| {al}      {ar} |       | {bl}      {br} |".center(z))
    print(f"+------------+       +------------+".center(z))


def printPlayerCards():
    if "10" in playerCards[0]:
        if "10" in playerCards[1]:
            displayCard(playerCards[0][:2],playerCards[0][-1],playerCards[1][:2],playerCards[1][-1],True,True)
        else:
            displayCard(playerCards[0][:2],playerCards[0][-1],playerCards[1][0],playerCards[1][-1],True,False)
    elif "10" in playerCards[1]:
        displayCard(playerCards[0][0],playerCards[0][-1],playerCards[1][:2],playerCards[1][-1],False,True)
    else:
        displayCard(playerCards[0][0],playerCards[0][-1],playerCards[1][0],playerCards[1][-1],False,False)
playerCards = []
for i in range(2):
    x = random.choice(deck)
    deck.remove(x)
    playerCards.append(x)

os.system('clear')
print("Your cards".center(z))
print("")
printPlayerCards()
