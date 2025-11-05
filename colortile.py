import os
import time
from colorama import Back,Style,Fore
z = os.get_terminal_size()[0]

def findY(backColorCount):
    return (int(len(Back.RED + Back.RESET)*backColorCount))

def resetCells():
    global row1Color,row2Color,row3Color,row4Color,row5Color,row6Color,row1,row2,row3,row4,row5,row6,rowList
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
    rowList = [row1,row2,row3,row4,row5,row6]
    
def countColors(row):
    colorCount = 0
    for i in row:
        if i != "   " and i != "XXX":
            tempList = []
            tempList.append(i)
            colorCount += 1

            if str(tempList)[3:10] == "x1b[103" or str(tempList)[3:10] == "x1b[101":
                colorCount += 0.1

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

def action(keyPress,width):
    keyPress = keyPress.lower().strip()
    if keyPress == "a":
        shift("left",width)
    elif keyPress == "d":
        shift("right",width)
    elif keyPress == "w":
        shift("up",width)
    elif keyPress == "s":
        shift("down",width)

def shift(direction,width):
    
    while True:
        tempRow1 = []
        tempRow2 = []
        tempRow3 = []
        tempRow4 = []
        tempRow5 = []
        tempRow6 = []
        for i in row1:
            tempRow1.append(i)
        for i in row2:
            tempRow2.append(i)
        for i in row3:
            tempRow3.append(i)
        for i in row4:
            tempRow4.append(i)
        for i in row5:
            tempRow5.append(i)
        for i in row6:
            tempRow6.append(i)
        
        tempRowList = [tempRow1,tempRow2,tempRow3,tempRow4,tempRow5,tempRow6]
        if direction == "up":
            for i in range(width-1):
                for j in range(width):
                    if rowList[i][j] == "   ":
                        rowList[i][j] = rowList[i+1][j]
                        rowList[i+1][j] = "   "
                
        elif direction == "down":
            for i in range(width-1):
                for j in range(width):
                    if rowList[width-(i+1)][j] == "   ":
                        rowList[width-(i+1)][j] = rowList[width-(i+2)][j]
                        rowList[width-(i+2)][j] = "   "

        elif direction == "left":
            for i in range(width):
                for j in range(width):
                    if j!=0:
                        if rowList[i][j-1] == "   ":
                            rowList[i][j-1] = rowList[i][j]
                            rowList[i][j] = "   "

        elif direction == "right":
            for i in range(width):
                for j in range(width):
                    if j!=width:
                        if rowList[i][j+1] == "   ":
                            rowList[i][j+1] = rowList[i][j]
                            rowList[i][j] = "   "
        
        if tempRowList==rowList:
            #print(tempRowList)
            #print(rowList)
            #input()
            break

def voidRest(width=0):
    global row1, row2, row3, row4, row5, row6
    rowList = [row1,row2,row3,row4,row5,row6]
    for row in range(len(rowList)-width):
        for cell in range(len(rowList[row])-width):
            if rowList[row+width][cell+width] == "   ":
                rowList[row+width][cell+width] = "XXX"
    for row in range(len(rowList)-width):
        for cell in range(len(rowList[row])-width):
            if rowList[row+width][cell+width] == "EMT":
                rowList[row+width][cell+width] = "   "

def cleanBoard(width):
    global row1,row2,row3,row4,row5,row6
    rowList = [row1,row2,row3,row4,row5,row6]
    for row in range(width):
        for cell in range(width):
            if rowList[row][cell] == "XXX":
                rowList[row][cell] = "   "

def levelOneSettings():
    global row1,row2,row3,width
    width = 3
    row1[0] = Back.RED + "   " + Back.RESET
    row1[1] = Back.RED + "   " + Back.RESET
    row1[2] = Back.RED + "   " + Back.RESET
    row3[2] = Back.RED + "   " + Back.RESET
    row2[0] = Back.YELLOW + "   " + Back.RESET
    row2[2] = Back.YELLOW + "   " + Back.RESET
    row3[0] = Back.YELLOW + "   " + Back.RESET
    row3[1] = Back.YELLOW + "   " + Back.RESET
    row2[1] = "EMT"
    voidRest()


def testSettings():
    global row2
    row2[1] = Back.RED + "   " + Back.RESET
    row1[0] = "EMT"
    row1[1] = "EMT"
    row1[2] = "EMT"
    row2[0] = "EMT"
    row2[2] = "EMT"
    row3[0] = "EMT"
    row3[1] = "EMT"
    row3[2] = "EMT"
    voidRest()

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

def getStringRow(cell):
    return "row"+cell[1]

def checkCells(width):
    matchList = []
    trashList = []
    delList = []
    for row in range(width):
        for cell in (range(width)):
            if [row,cell] not in trashList:
                if rowList[row][cell] != "   ":
                    matchList.append([row,cell])
                    try:
                        above = rowList[row-1][cell]
                        if above == "XXX":
                            above = "DNE"
                    except:
                        above = "DNE"
                    try:
                        below = rowList[row+1][cell]
                        if below == "XXX":
                            below = "DNE"
                    except:
                        below = "DNE"
                    try:
                        left = rowList[row][cell-1]
                        if left == "XXX":
                            left = "DNE"
                    except:
                        left = "DNE"
                    try:
                        right = rowList[row][cell+1]
                        if right == "XXX":
                            right = "DNE"
                    except:
                        right = "DNE"
                    if above == rowList[row][cell]:
                        matchList.append([row-1,cell])
                    if below == rowList[row][cell]:
                        matchList.append([row+1,cell])
                    if left == rowList[row][cell]:
                        matchList.append([row,cell-1])
                    if right == rowList[row][cell]:
                        matchList.append([row,cell+1])
                    if len(matchList) > 1:
                        for lcv in matchList:
                            if matchList.index(lcv) != 0:
                                try:
                                    above = rowList[lcv[0]-1][lcv[1]]
                                    if above == "XXX":
                                        above = "DNE"
                                except:
                                    above = "DNE"
                                try:
                                    below = rowList[lcv[0]+1][lcv[1]]
                                    if below == "XXX":
                                        below = "DNE"
                                except:
                                    below = "DNE"
                                try:
                                    left = rowList[lcv[0]][lcv[1]-1]
                                    if left == "XXX":
                                        left = "DNE"
                                except:
                                    left = "DNE"
                                try:
                                    right = rowList[lcv[0]][lcv[1]+1]
                                    if right == "XXX":
                                        right = "DNE"
                                except:
                                    right = "DNE"
                                if above == rowList[lcv[0]][lcv[1]]:
                                    if [lcv[0]-1,lcv[1]] not in matchList:
                                        matchList.append([lcv[0]-1,lcv[1]])
                                if below == rowList[lcv[0]][lcv[1]]:
                                    if [lcv[0]+1,lcv[1]] not in matchList:
                                        matchList.append([lcv[0]+1,lcv[1]])
                                if left == rowList[lcv[0]][lcv[1]]:
                                    if [lcv[0],lcv[1]-1] not in matchList:
                                        matchList.append([lcv[0],lcv[1]-1])
                                if right == rowList[lcv[0]][lcv[1]]:
                                    if [lcv[0],lcv[1]+1] not in matchList:
                                        matchList.append([lcv[0],lcv[1]+1])

                        if len(matchList) == 4:
                            delList.append([matchList[0],matchList[1],matchList[2],matchList[3]])
                            
                        for i in matchList:
                            trashList.append([i[0],i[1]])
                        if matchList != []:
                            matchList = []
                    #This prints the values around the cell that we care about for debugging
                    #print(f"Above: {above}")
                    #print(f"Below: {below}")
                    #print(f"Left: {left}")
                    #print(f"Right: {right}")
                    #input()
                else:
                    trashList.append([row,cell])
    if len(delList) >0:
        delAnimation(delList,3)
        for i in delList:
            for j in i:
                rowList[j[0]][j[1]] = "   "

def delAnimation(givenList,width):
    for i in givenList:
        for j in i:
            os.system('clear')
            tempList = []
            tempList.append(rowList[j[0]][j[1]])
            if str(tempList)[3:10] == "x1b[41m":
                rowList[j[0]][j[1]] = Back.LIGHTRED_EX + "   " + Back.RESET
            elif str(tempList)[3:10] == "x1b[43m":
                rowList[j[0]][j[1]] = Back.LIGHTYELLOW_EX + "   " + Back.RESET
            if width == 3:
                threeXThree()
            elif width == 4:
                fourXFour()
            elif width == 5:
                fiveXFive()
            elif width == 6:
                sixXSix()
            time.sleep(0.35)
        for j in i:
            os.system('clear')
            rowList[j[0]][j[1]] = " "+Back.BLACK+" "+Back.RESET+" "
        if width == 3:
            threeXThree()
        elif width == 4:
            fourXFour()
        elif width == 5:
            fiveXFive()
        elif width == 6:
            sixXSix()
        time.sleep(0.35)
        




resetCells()
levelOneSettings()
#testSettings()
while True:
    os.system('clear')
    
    threeXThree()
    act = input()
    action(act,3)
    checkCells(3)
    
    

