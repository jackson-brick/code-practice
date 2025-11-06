import os
import time
#import random
from colorama import Back,Style#,Fore
z = os.get_terminal_size()[0]
width = 3
moveCount = 3
levelCount = 0
mt = "EMT"
yellow = Back.YELLOW + Style.BRIGHT + " ! " + Style.RESET_ALL
blue = Back.BLUE + Style.BRIGHT + " $ " + Style.RESET_ALL
red = Back.RED + Style.BRIGHT+" + " + Style.RESET_ALL
cyan = Back.CYAN + Style.BRIGHT + " X " + Style.RESET_ALL
magenta = Back.MAGENTA + Style.BRIGHT + " ? " + Style.RESET_ALL
white = Back.WHITE + Style.BRIGHT + " # " + Style.RESET_ALL
light_red = Back.LIGHTRED_EX + "   " + Style.RESET_ALL
light_yellow = Back.LIGHTYELLOW_EX + "   " + Style.RESET_ALL
light_blue = Back.LIGHTBLUE_EX + "   " + Style.RESET_ALL
light_magenta = Back.LIGHTMAGENTA_EX + "   " + Style.RESET_ALL
light_cyan = Back.LIGHTCYAN_EX + "   " + Style.RESET_ALL
light_white = Back.LIGHTWHITE_EX + "   " + Style.RESET_ALL
obs = Back.GREEN +Style.BRIGHT+ "///" + Style.RESET_ALL


def findY(backColorCount,lightColorCount,brightColorCount):
    return (int(9*backColorCount)+lightColorCount+(4*brightColorCount))

def resetCells():
    global row1Color,row2Color,row3Color,row4Color,row5Color,row6Color,row7Color,row1,row2,row3,row4,row5,row6,row7,rowList
    row1Color = 0
    row2Color = 0
    row3Color = 0
    row4Color = 0
    row5Color = 0
    row6Color = 0
    row7Color = 0
    
    row1 = ["   ","   ","   ","   ","   ","   ","   "]
    row2 = ["   ","   ","   ","   ","   ","   ","   "]
    row3 = ["   ","   ","   ","   ","   ","   ","   "]
    row4 = ["   ","   ","   ","   ","   ","   ","   "]
    row5 = ["   ","   ","   ","   ","   ","   ","   "]
    row6 = ["   ","   ","   ","   ","   ","   ","   "]
    row7 = ["   ","   ","   ","   ","   ","   ","   "]
    rowList = [row1,row2,row3,row4,row5,row6,row7]
    
def countColors(row):
    colorCount = 0
    for i in row:
        if i != "   " and i != "XXX":
            colorCount += 1

    return colorCount
def countLightColors(row):
    lightColorCount = 0
    for i in row:
        if i != "   " and i != "XXX":
            if i == light_red or i == light_blue or i == light_yellow or i == light_cyan or i == light_magenta or i == light_white:
                lightColorCount += 1
    return lightColorCount
def countBrightColors(row):
    brightColorCount = 0
    for i in row:
        if i != "   " and i != "XXX":
            tempList = []
            tempList.append(i)
            if "x1b[1m" in str(tempList):
                brightColorCount += 1
    return brightColorCount

def threeXThree():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row1Light = countLightColors(row1)
    row2Light = countLightColors(row2)
    row3Light = countLightColors(row3)
    row1Bright = countBrightColors(row1)
    row2Bright = countBrightColors(row2)
    row3Bright = countBrightColors(row3)
    print(f"+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|".center(z+findY(row1Color,row1Light,row1Bright)))
    print(f"|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|".center(z+findY(row2Color,row2Light,row2Bright)))
    print(f"|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|".center(z+findY(row3Color,row3Light,row3Bright)))
    print(f"+---+---+---+".center(z))
    print("")
    print(f"Level: {levelCount}/11".center(z))
    print(f"Moves: {moveCount}".center(z))

def fourXFour():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    row1Light = countLightColors(row1)
    row2Light = countLightColors(row2)
    row3Light = countLightColors(row3)
    row4Light = countLightColors(row4)
    row1Bright = countBrightColors(row1)
    row2Bright = countBrightColors(row2)
    row3Bright = countBrightColors(row3)
    row4Bright = countBrightColors(row4)
    print(f"+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|".center(z+findY(row1Color,row1Light,row1Bright)))
    print(f"|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|".center(z+findY(row2Color,row2Light,row2Bright)))
    print(f"|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|".center(z+findY(row3Color,row3Light,row3Bright)))
    print(f"|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|".center(z+findY(row4Color,row4Light,row4Bright)))
    print(f"+---+---+---+---+".center(z))
    print("")
    print(f"Level: {levelCount}/11".center(z))
    print(f"Moves: {moveCount}".center(z))

def fiveXFive():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    row5Color = countColors(row5)
    row1Light = countLightColors(row1)
    row2Light = countLightColors(row2)
    row3Light = countLightColors(row3)
    row4Light = countLightColors(row4)
    row5Light = countLightColors(row5)
    row1Bright = countBrightColors(row1)
    row2Bright = countBrightColors(row2)
    row3Bright = countBrightColors(row3)
    row4Bright = countBrightColors(row4)
    row5Bright = countBrightColors(row5)
    print(f"+---+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|{row1[4]}|".center(z+findY(row1Color,row1Light,row1Bright)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|{row2[4]}|".center(z+findY(row2Color,row2Light,row2Bright)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|{row3[4]}|".center(z+findY(row3Color,row3Light,row3Bright)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|{row4[4]}|".center(z+findY(row4Color,row4Light,row4Bright)))
    print(f"|---|---|---|---|---|".center(z))
    print(f"|{row5[0]}|{row5[1]}|{row5[2]}|{row5[3]}|{row5[4]}|".center(z+findY(row5Color,row5Light,row5Bright)))
    print(f"+---+---+---+---+---+".center(z))
    print("")
    print(f"Level: {levelCount}/11".center(z))
    print(f"Moves: {moveCount}".center(z))

def sixXSix():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    row5Color = countColors(row5)
    row6Color = countColors(row6)
    row1Light = countLightColors(row1)
    row2Light = countLightColors(row2)
    row3Light = countLightColors(row3)
    row4Light = countLightColors(row4)
    row5Light = countLightColors(row5)
    row6Light = countLightColors(row6)
    row1Bright = countBrightColors(row1)
    row2Bright = countBrightColors(row2)
    row3Bright = countBrightColors(row3)
    row4Bright = countBrightColors(row4)
    row5Bright = countBrightColors(row5)
    row6Bright = countBrightColors(row6)
    print(f"+---+---+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|{row1[4]}|{row1[5]}|".center(z+findY(row1Color,row1Light,row1Bright)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|{row2[4]}|{row2[5]}|".center(z+findY(row2Color,row2Light,row2Bright)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|{row3[4]}|{row3[5]}|".center(z+findY(row3Color,row3Light,row3Bright)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|{row4[4]}|{row4[5]}|".center(z+findY(row4Color,row4Light,row4Bright)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row5[0]}|{row5[1]}|{row5[2]}|{row5[3]}|{row5[4]}|{row5[5]}|".center(z+findY(row5Color,row5Light,row5Bright)))
    print(f"|---|---|---|---|---|---|".center(z))
    print(f"|{row6[0]}|{row6[1]}|{row6[2]}|{row6[3]}|{row6[4]}|{row6[5]}|".center(z+findY(row6Color,row6Light,row6Bright)))
    print(f"+---+---+---+---+---+---+".center(z))
    print("")
    print(f"Level: {levelCount}/11".center(z))
    print(f"Moves: {moveCount}".center(z))

def sevenXSeven():
    row1Color = countColors(row1)
    row2Color = countColors(row2)
    row3Color = countColors(row3)
    row4Color = countColors(row4)
    row5Color = countColors(row5)
    row6Color = countColors(row6)
    row7Color = countColors(row7)
    row1Light = countLightColors(row1)
    row2Light = countLightColors(row2)
    row3Light = countLightColors(row3)
    row4Light = countLightColors(row4)
    row5Light = countLightColors(row5)
    row6Light = countLightColors(row6)
    row7Light = countLightColors(row7)
    row1Bright = countBrightColors(row1)
    row2Bright = countBrightColors(row2)
    row3Bright = countBrightColors(row3)
    row4Bright = countBrightColors(row4)
    row5Bright = countBrightColors(row5)
    row6Bright = countBrightColors(row6)
    row7Bright = countBrightColors(row7)
    print(f"+---+---+---+---+---+---+---+".center(z))
    print(f"|{row1[0]}|{row1[1]}|{row1[2]}|{row1[3]}|{row1[4]}|{row1[5]}|{row1[6]}|".center(z+findY(row1Color,row1Light,row1Bright)))
    print(f"|---|---|---|---|---|---|---|".center(z))
    print(f"|{row2[0]}|{row2[1]}|{row2[2]}|{row2[3]}|{row2[4]}|{row2[5]}|{row2[6]}|".center(z+findY(row2Color,row2Light,row2Bright)))
    print(f"|---|---|---|---|---|---|---|".center(z))
    print(f"|{row3[0]}|{row3[1]}|{row3[2]}|{row3[3]}|{row3[4]}|{row3[5]}|{row3[6]}|".center(z+findY(row3Color,row3Light,row3Bright)))
    print(f"|---|---|---|---|---|---|---|".center(z))
    print(f"|{row4[0]}|{row4[1]}|{row4[2]}|{row4[3]}|{row4[4]}|{row4[5]}|{row4[6]}|".center(z+findY(row4Color,row4Light,row4Bright)))
    print(f"|---|---|---|---|---|---|---|".center(z))
    print(f"|{row5[0]}|{row5[1]}|{row5[2]}|{row5[3]}|{row5[4]}|{row5[5]}|{row5[6]}|".center(z+findY(row5Color,row5Light,row5Bright)))
    print(f"|---|---|---|---|---|---|---|".center(z))
    print(f"|{row6[0]}|{row6[1]}|{row6[2]}|{row6[3]}|{row6[4]}|{row6[5]}|{row6[6]}|".center(z+findY(row6Color,row6Light,row6Bright)))
    print(f"|---|---|---|---|---|---|---|".center(z))
    print(f"|{row7[0]}|{row7[1]}|{row7[2]}|{row7[3]}|{row7[4]}|{row7[5]}|{row7[6]}|".center(z+findY(row7Color,row7Light,row7Bright)))
    print(f"+---+---+---+---+---+---+---+".center(z))
    print("")
    print(f"Level: {levelCount}/11".center(z))
    print(f"Moves: {moveCount}".center(z))

def action(keyPress,width):
    global moveCount
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
    global moveCount
    tempRowList = []
    for i in rowList:
        myList = []
        for j in i:
            myList.append(j)
        tempRowList.append(myList)
    if direction == "up":
        for i in range(width-1):
            for j in range(width):
                if rowList[i][j] == "   ":
                    if rowList[i+1][j] != obs:
                        rowList[i][j] = rowList[i+1][j]
                        rowList[i+1][j] = "   "
            
    elif direction == "down":
        for i in range(width-1):
            for j in range(width):
                if rowList[width-(i+1)][j] == "   ":
                    if rowList[width-(i+2)][j] != obs:
                        rowList[width-(i+1)][j] = rowList[width-(i+2)][j]
                        rowList[width-(i+2)][j] = "   "

    elif direction == "left":
        for i in range(width):
            for j in range(width):
                if j!=0:
                    if rowList[i][j-1] == "   " and rowList[i][j]!=obs:
                        rowList[i][j-1] = rowList[i][j]
                        rowList[i][j] = "   "

    elif direction == "right":
        for i in range(width):
            for j in range(width):
                
                if j!=0 and width-j-1>=0:
                    if rowList[i][width-j] == "   " and rowList[i][(width-j-1)]!= obs:
                        rowList[i][width-j] = rowList[i][(width-j-1)]
                        rowList[i][(width-j-1)] = "   "

    if tempRowList != rowList:
        moveCount -= 1


def voidRest(width=0):
    global rowList
    for row in range(len(rowList)-width):
        for cell in range(len(rowList[row])-width):
            if rowList[row+width][cell+width] == "   ":
                rowList[row+width][cell+width] = "XXX"
    for row in range(len(rowList)-width):
        for cell in range(len(rowList[row])-width):
            if rowList[row+width][cell+width] == mt:
                rowList[row+width][cell+width] = "   "

def cleanBoard(width):
    global rowList
    for row in range(width):
        for cell in range(width):
            if rowList[row][cell] == "XXX":
                rowList[row][cell] = "   "

def levelOneSettings():
    global width
    width = 3
    colorList = [yellow, yellow, red,
                 yellow, mt, red,
                 red, yellow, red
                 ]
    makeLevel(colorList,width)

def levelTwoSettings():
    global width
    width = 4
    colorList = [mt, blue, yellow, yellow,
                 red, mt, blue, mt,
                 mt, blue, yellow,blue,
                 red, red, red, yellow]
    makeLevel(colorList, width)
def levelThreeSettings():
    global width
    width = 4
    colorList = [blue, yellow,mt,red,
                 blue,mt,mt,red,
                 yellow,yellow,yellow,red,
                 blue,blue,red,obs]
    makeLevel(colorList,width)
def levelFourSettings():
    global width
    width = 4
    colorList = [yellow, mt, red, red,
                 yellow,obs,red,blue,
                 yellow, red, blue, mt,
                 obs, yellow, blue, blue]
    makeLevel(colorList,width)
def levelFiveSettings():
    global width
    width = 4
    colorList = [red, red, mt, yellow,
                 blue, blue, red, red, 
                 mt, blue, yellow, yellow,
                 blue, obs, obs,yellow]
    makeLevel(colorList, width)
def levelSixSettings():
    global width
    width = 5
    colorList = [cyan,red,red,cyan,cyan,
                 obs,red,blue,red,cyan,
                 mt,obs,mt,blue,mt,
                 yellow,yellow,blue,blue,yellow,
                 obs,mt,mt,yellow,mt]
    makeLevel(colorList,width)
def levelSevenSettings():
    global width
    width = 5
    colorList = [blue,cyan,obs,cyan,cyan,
                 blue,mt,obs,cyan,mt,
                 blue,red,blue,yellow,mt,
                 obs,mt,red,yellow,mt,
                 yellow,red,red,mt,yellow]
    makeLevel(colorList,width)
def levelEightSettings():
    global width
    width = 6
    colorList = [red,obs,cyan,obs,obs,mt,
                 mt,mt,magenta,cyan,cyan,mt,
                 magenta,magenta,red,blue,cyan,blue,
                 red,magenta,obs,mt,mt,blue,
                 mt,mt,mt,mt,yellow,blue,
                 mt,red,yellow,mt,yellow,yellow]
    makeLevel(colorList,width)
def levelNineSettings():
    global width
    width = 6
    colorList = [magenta,obs,mt,cyan,magenta,magenta,
                 cyan,cyan,magenta,mt,mt,mt,
                 red,cyan,blue,obs,mt,yellow,
                 red,blue,mt,mt,mt,yellow,
                 blue,blue,red,red,mt,mt,
                 obs,yellow,yellow,obs,mt,mt]
    makeLevel(colorList,width)
def levelTenSettings():
    global width
    width = 7
    colorList = [blue,blue,mt,mt,mt,mt,mt,
                 mt,red,blue,magenta,mt,mt,mt,
                 mt,obs,yellow,magenta,magenta,obs,blue,
                 mt,yellow,magenta,red,mt,mt,mt,
                 white,yellow,mt,mt,obs,yellow,red,
                 mt,obs,white,white,obs,cyan,red,
                 white,cyan,mt,cyan,mt,cyan,mt]
    makeLevel(colorList,width)
def levelElevenSettings():
    global width
    width = 7
    colorList = [mt,obs,blue,red,red,blue,blue,
                 mt,mt,obs,mt,magenta,mt,mt,
                 white,white,cyan,mt,white,mt,blue,
                 white,cyan,mt,red,yellow,magenta,magenta,
                 mt,mt,cyan,yellow,obs,red,mt,
                 obs,mt,cyan,yellow,obs,yellow,magenta,
                 mt,mt,mt,mt,mt,mt,mt]
    makeLevel(colorList,width)

def testSettings():
    global width
    width = 3
    colorList = [mt,mt,mt,
                 mt,cyan,mt,
                 mt,mt,mt]
    makeLevel(colorList, width)

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
        elif row == row7:
            return row6
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
        elif row == row6:
            return row7
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
                if rowList[row][cell] != "   " and rowList[row][cell] != obs:
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
                    
                else:
                    trashList.append([row,cell])
    if len(delList) >0:
        delAnimation(delList,width)
        for i in delList:
            for j in i:
                rowList[j[0]][j[1]] = "   "

def delAnimation(givenList,width):
    global moveCount
    moveCount += 1
    for i in givenList:
        
        for j in i:
            os.system('clear')
            cell = rowList[j[0]][j[1]]
            if cell == red:
                rowList[j[0]][j[1]] = light_red
            elif cell == yellow:
                rowList[j[0]][j[1]] = light_yellow
            elif cell == blue:
                rowList[j[0]][j[1]] = light_blue
            elif cell == magenta:
                rowList[j[0]][j[1]] = light_magenta
            elif cell == cyan:
                rowList[j[0]][j[1]] = light_cyan
            elif cell == white:
                rowList[j[0]][j[1]] = light_white
            if width == 3:
                threeXThree()
            elif width == 4:
                fourXFour()
            elif width == 5:
                fiveXFive()
            elif width == 6:
                sixXSix()
            elif width == 7:
                sevenXSeven()
            time.sleep(0.15)
            #print(findY(countColors(rowList[j[0]]),countLightColors(rowList[j[0]])))
            #input()
        time.sleep(0.35)
        for j in i:
            os.system('clear')
            rowList[j[0]][j[1]] = " "+Back.BLACK+" "+Style.RESET_ALL+" "
        if width == 3:
            threeXThree()
        elif width == 4:
            fourXFour()
        elif width == 5:
            fiveXFive()
        elif width == 6:
            sixXSix()
        elif width == 7:
            sevenXSeven()
        time.sleep(0.15)
        #input()

def checkWin(width):
    count = 0
    for i in range(width):
        for j in range(width):
            if rowList[i][j] == "   " or rowList[i][j] == obs:
                count+=1
    return count == width*width
        
def playGame():
    global moveCount
    tempMoveCount = moveCount
    while True:
        os.system('clear')
        if width == 3:
            threeXThree()
        elif width == 4:
            fourXFour()
        elif width == 5:
            fiveXFive()
        elif width == 6:
            sixXSix()
        elif width == 7:
            sevenXSeven()
        if checkWin(width):

            if moveCount >= tempMoveCount:
                print("PERFECT".center(z))
                moveCount += 1
                time.sleep(1)
                break
            else:
                print("NICE".center(z))
                time.sleep(1)
                break
        act = input()
        action(act,width)
        checkCells(width)
        if moveCount == 0:
            os.system('clear')
            if width == 3:
                threeXThree()
            elif width == 4:
                fourXFour()
            elif width == 5:
                fiveXFive()
            elif width == 6:
                sixXSix()
            elif width == 7:
                sevenXSeven()
            print("GAME OVER".center(z))
            quit()

def makeLevel(listOfColors,width):
    global rowList, levelCount
    levelCount += 1
    count = 0
    for i in range(width):
        for j in range(width):
            rowList[i][j] = listOfColors[count]
            count+=1
    voidRest()

def introSequence():
    os.system('clear')
    print("COLOR TILES".center(z))
    print("USE WASD (hit ENTER to lock in your move) TO MOVE".center(z))
    print("MATCH UP THE COLORS IN THE LEAST AMOUNT OF MOVES".center(z))
    print("")
    print(("OBSTACLES DON'T MOVE:   " + obs).center(z+10))
    print("")
    print("PRESS ENTER TO BEGIN".center(z))
    input()


introSequence()
resetCells()
levelOneSettings()
#testSettings()
#level 1
playGame()
#level 2
resetCells()
levelTwoSettings()
playGame()
#level 3
resetCells()
levelThreeSettings()
playGame()
#level 4
resetCells()
levelFourSettings()
playGame()
#level 5
resetCells()
levelFiveSettings()
playGame()
#level 6
resetCells()
levelSixSettings()
playGame()
#level 7 (5)
resetCells()
levelSevenSettings()
playGame()
#level 8 (6)
resetCells()
levelEightSettings()
playGame()
#level 9
resetCells()
levelNineSettings()
playGame()

#level 10
resetCells()
levelTenSettings()
playGame()

#level 11
resetCells()
levelElevenSettings()
playGame()

os.system('clear')
print("YOU BEAT THE GAME! CONGRATULATIONS".center(z))
print("")
input()
#level 12

#level 13

#level 14

#level 15

#level 16

#level 17

#level 18

#level 19

#level 20

    
    
    

