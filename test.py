import os
from colorama import Fore, Style, Back
z=os.get_terminal_size()[0]

testList = ["poop"]

for i in range(len(testList)):
    if testList[i] == "poop":
        testList.append("fart")

x = "poop"
testDict = {}
testDict[x] = "fart"
testDict["mr"] = "johnson"
print(testDict)
for i in testDict:
    print(i)
myList = [Back.LIGHTRED_EX + "   "+ Back.RESET]
print(myList[0])
print(myList)
print(str(myList))
print(str(myList)[3:10])
print((Back.LIGHTYELLOW_EX+"|   |"+Back.RESET).center(z+10))
print("|   |".center(z))
print(len(Back.YELLOW+Back.RESET)==len(Back.LIGHTYELLOW_EX+Back.RESET))
x = Back.YELLOW + "   " + Back.RESET
print(len(x))
print(len(" "+Back.BLACK+" "+Back.RESET+" "))