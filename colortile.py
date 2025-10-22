import os
from colorama import Back,Style,Fore
z = os.get_terminal_size()[0]

def findY(backColorCount):
    return (len(Back.RED + Back.RESET)*backColorCount)

def resetCells():
    global row1Color,row2Color,row3Color,row4Color,row5Color,row6Color,row1,row2,row3,row4,row5,row6
    row1Color = 0
    row2Color = 0
    row3Color = 0
    row4Color = 0
    row5Color = 0
    row6Color = 0
    
    row1 = ["   ","   ","   ","   ","   ","   "]
    row2 = ["   ","   ","   ","   ","   ","   "]
    row3 = ["   ","   ","   ","   ","   ","   "]
    row4 = ["   ","   ","   ","   ","   ","   "]
    row5 = ["   ","   ","   ","   ","   ","   "]
    row6 = ["   ","   ","   ","   ","   ","   "]
    
def countColors(row):
    colorCount = 0
    for i in row:
        if i != "   ":
            colorCount += 1
    return colorCount

def threeXThree():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    print(f"+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|".center(z+findY(row1Color)))
    print(f"|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|".center(z+findY(row2Color)))
    print(f"|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|".center(z+findY(row3Color)))
    print(f"+---+---+---+".center(z))

def fourXFour():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    print(f"+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|".center(z+findY(row1Color)))
    print(f"|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|".center(z+findY(row2Color)))
    print(f"|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|".center(z+findY(row3Color)))
    print(f"|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|".center(z+findY(row4Color)))
    print(f"+---+---+---+---+".center(z))

def fiveXFive():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    row5Color = countColors(row5)
    print(f"+---+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|{row1[4]}|".center(z+findY(row1Color)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|{row2[4]}|".center(z+findY(row2Color)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|{row3[4]}|".center(z+findY(row3Color)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|{row4[4]}|".center(z+findY(row4Color)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row5[0]}|{row5[1]}|{row5[2]}|{row5[3]}|{row5[4]}|".center(z+findY(row5Color)))
    print(f"+---+---+---+---+---+".center(z))

def sixXSix():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    row5Color = countColors(row5)
    row6Color = countColors(row6)
    print(f"+---+---+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|{row1[4]}|{row1[5]}|".center(z+findY(row1Color)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|{row2[4]}|{row2[5]}|".center(z+findY(row2Color)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|{row3[4]}|{row3[5]}|".center(z+findY(row3Color)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|{row4[4]}|{row4[5]}|".center(z+findY(row4Color)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row5[0]}|{row5[1]}|{row5[2]}|{row5[3]}|{row5[4]}|{row5[5]}|".center(z+findY(row5Color)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row6[0]}|{row6[1]}|{row6[2]}|{row6[3]}|{row6[4]}|{row6[5]}|".center(z+findY(row6Color)))
    print(f"+---+---+---+---+---+---+".center(z))

def action(keyPress):
    keyPress = keyPress.lower().strip()
    if keyPress == "a":
        shift("left")
    elif keyPress == "d":
        shift("right")
    elif keyPress == "w":
        shift("up")
    elif keyPress == "s":
        shift("down")

def shift(direction):
    if direction == "up":
        for i in range(len(row2)):
            if row1[i] == "   ":
                row1[i] = row2[i]
                row2[i] = "   "
            if row2[i] == "   ":
                row2[i] = row3[i]
                row3[i] = "   "
            if row3[i] == "   ":
                row3[i] = row4[i]
                row4[i] = "   "
            if row4[i] == "   ":
                row4[i] = row5[i]
                row5[i] = "   "
            if row5[i] == "   ":
                row5[i] = row6[i]
                row6[i] = "   "
    #elif direction == "down":

    #elif direction == "left":

    #elif direction == "right":

def levelOneSettings():
    global row1,row2,row3
    row1[0] = Back.RED + "   " + Back.RESET
    row1[1] = Back.RED + "   " + Back.RESET
    row1[2] = Back.RED + "   " + Back.RESET
    row3[2] = Back.RED + "   " + Back.RESET
    row2[0] = Back.YELLOW + "   " + Back.RESET
    row2[2] = Back.YELLOW + "   " + Back.RESET
    row3[0] = Back.YELLOW + "   " + Back.RESET
    row3[1] = Back.YELLOW + "   " + Back.RESET

def aboveOrBelow(row,pos):
    if pos == "above":
        if row == row2:
            return row1
        elif row == row3:
            return row2
        elif row == row4:
            return row3
        elif row == row5:
            return row4
        elif row == row6:
            return row5
    elif pos == "below":
        if row == row1:
            return row2
        elif row == row2:
            return row3
        elif row == row3:
            return row4
        elif row == row4:
            return row5
        elif row == row5:
            return row6
    return 0


def checkCells():
    rowsList = [row1,row2,row3,row4,row5,row6]
    matchList = []
    trashList = []
    for row in rowsList:
        for i in range(len(row)):
            matchList.append(row[i])
            above = aboveOrBelow(row,"above")
            if above != 0:
                if above == row[i]:
                    matchList.append(above)


resetCells()
levelOneSettings()


