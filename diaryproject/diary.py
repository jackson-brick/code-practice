import time 
import json
import os
from colorama import Fore, Style, Back
import random

z = os.get_terminal_size()
z = z[0]


with open('diaryusers.json','r') as file:
    diaryusers = json.load(file)
diaryAtUser = diaryusers["users"]

with open('diaryentry.json','r') as file:
    diaryentry = json.load(file)
diaryAtEntry = diaryentry["entry"]

def encrypt(pswrd):
    global encryptedPass
    unencryptedPass = []
    for ele in range(len(pswrd)):
         unencryptedPass.append(pswrd[ele])
    encryptedPass = []
    for ele in unencryptedPass:
        encryptedPass.append(diaryusers["users"][userNum]["key"][ele])
    encryptedPass = ''.join(encryptedPass)

def new_user(username,pswrd):
    global entryNum
    newUser = []
    newUserEntry = []
    charList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","{","}","[","]","|","\\","\'","\"",":",";","<",">",",",".","?","/"," "]
    tempCharList = []
    for ele in charList:
        tempCharList.append(ele)
    randomCharList = []
    for item in range(len(tempCharList)):
        randomCharList.append(random.choice(tempCharList))
        tempCharList.remove(randomCharList[item])
    keyDict = {"a":"","b":"","c":"","d":"","e":"","f":"","g":"","h":"","i":"","j":"","k":"","l":"","m":"","n":"","o":"","p":"","q":"","r":"","s":"","t":"","u":"","v":"","w":"","x":"","y":"","z":"","A":"","B":"","C":"","D":"","E":"","F":"","G":"","H":"","I":"","J":"","K":"","L":"","M":"","N":"","O":"","P":"","Q":"","R":"","S":"","T":"","U":"","V":"","W":"","X":"","Y":"","Z":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","0":"","!":"","@":"","#":"","$":"","%":"","^":"","&":"","*":"","(":"",")":"","-":"","_":"","=":"","+":"","`":"","~":"","{":"","}":"","[":"","]":"","|":"","\\":"","\'":"","\"":"",":":"",";":"","<":"",">":"",",":"",".":"","?":"","/":""," ":""}
    for item in range(len(charList)):
        keyDict[charList[item]] = randomCharList[item]
    unencryptedPass = []
    for ele in range(len(pswrd)):
         unencryptedPass.append(pswrd[ele])
    encryptedPass = []
    for ele in unencryptedPass:
        encryptedPass.append(keyDict[ele])
    encryptedPass = ''.join(encryptedPass)
    newUser.append({"key":keyDict,"name":username,"password":encryptedPass})
    diaryAtUser.append(newUser[0])
    newUserEntry.append({"name":username,"0":""})
    diaryAtEntry.append(newUserEntry[0])
    with open('diaryusers.json','w') as outfile:
        jsonVar = json.dumps(diaryAtUser,indent=4)
        outfile.write('{\n"users": ' + jsonVar + '\n}')
    with open('diaryentry.json','w') as outfile:
        jsonVar = json.dumps(diaryAtEntry,indent=4)
        outfile.write('{\n"entry": ' + jsonVar + '\n}')
    
    

def user_intro():
    global userNum
    global userName
    global key
    global password
    global entryNum
    while True:
        userNum = -2
        os.system('clear')
        print("Have an account already? Type LOG IN".center(z) + "\n" + "Need to create an account? Type SIGN UP".center(z) + "\n")
        logOrSign = input()
        if logOrSign.lower() == "log in":
            os.system('clear')
            print("Username:     ".center(z))
            userName = input()
            print("Password:     ".center(z))
            password = input()
            for lcv in range(len(diaryAtUser)):
                if userName == diaryusers["users"][lcv]['name']:
                    userNum = lcv
            if userNum >= 0:
                encrypt(password)
                if encryptedPass == diaryusers["users"][userNum]['password']:
                    key = diaryusers["users"][userNum]['key']
                    for ele in range(len(diaryAtEntry)):
                        if diaryentry["entry"][ele]["name"] == userName:
                            entryNum = ele
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Your username or password is incorrect".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
            else:
                print(Fore.RED + Style.BRIGHT + "Your username or password is incorrect".center(z) + Fore.RESET + Style.NORMAL)
                time.sleep(3)
                    
        elif logOrSign.lower() == "sign up":
            while True:
                userNameCorrect = 0
                userNameMatch = 0
                os.system('clear')
                print("Create a username:     ".center(z))
                userName = input()
                print("Create a password:     ".center(z))
                password = input()
                for user in range(len(diaryAtUser)):
                    if userName == diaryusers["users"][user]["name"]: #checks to see if a username is already taken, if it is then local variable userNameMatch is not set to p to let the code know later that the username is taken
                        userNameMatch = "fail"
                if len(userName) < 5 or len(userName) > 15:
                    os.system('clear')
                    print(Fore.RED + Style.BRIGHT + "Username must be between 5 and 15 digits!".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
                elif len(password) < 8 or len(password) > 24:
                    os.system('clear')
                    print(Fore.RED + Style.BRIGHT + "Password must be between 8 and 24 digits!".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
                elif userNameMatch == "fail":
                    os.system('clear')
                    print(Fore.RED + Style.BRIGHT + "That username is already taken!".center(z) + Fore.RESET + Style.NORMAL)
                    userNameMatch = 0
                    time.sleep(3)
                else:
                    userNameCorrect = "p"
        
                if userNameCorrect == "p":
                    while True:
                        os.system('clear')
                        print(f"Username: {userName}".center(z) + "\n" + (f"Password: {password[0]}{password[1]}" + ("*" * (len(password) - 3)) + f"{password[-1]}").center(z) + "\n" + "Does this information look correct?".center(z)) #neat little display of username and password with password being covered up
                        checkInfo = input()
                        if checkInfo.lower() == "yes":
                            new_user(userName,password)
                            break
                        elif checkInfo.lower() == "no":
                            break
                        else:
                            pass
                    if checkInfo.lower() == "yes":
                        print(Style.BRIGHT + "You can now log in with your account!".center(z) + Style.NORMAL)
                        time.sleep(3)
                        break


def start():
    while True:
        os.system('clear')
        print(Style.BRIGHT + "REMEMBER: Type HOME to exit ".center(z) + Style.NORMAL + Fore.RESET)
        print("")
        if diaryentry["entry"][entryNum]["0"] == "":
            print(Style.DIM + "Your story starts here..." + Style.NORMAL)
            print("\n\n")
        else:
            if diaryentry["entry"][entryNum]["1"] == "":
                print(diaryentry["entry"][entryNum]["0"])
                print("\n\n")
            else:
                if diaryentry["entry"][entryNum]["2"] == "":
                    print(diaryentry["entry"][entryNum]["0"])
                    print(diaryentry["entry"][entryNum]["1"])
                    print("\n")
                else:
                    print(diaryentry["entry"][entryNum][f"{len(diaryentry["entry"][entryNum]) - 5}"])
                    print(diaryentry["entry"][entryNum][f"{len(diaryentry["entry"][entryNum]) - 4}"])
                    print(diaryentry["entry"][entryNum][f"{len(diaryentry["entry"][entryNum]) - 3}"])
                    print("")
        startInput = input()
        if startInput.lower().strip() == "home":
            break
        elif startInput.lower().strip() == "quit":
            os.system('clear')
            quit()
        else:
            diaryAtEntry[entryNum][f"{len(diaryentry["entry"][entryNum]) - 2}"] = startInput
            diaryAtEntry[entryNum][f"{len(diaryentry["entry"][entryNum]) - 1}"] = ""
            
def edit():
    while True:
        if diaryentry["entry"][entryNum]["0"] == "":
            print(Style.BRIGHT + Fore.RED + "You have to being writing to edit!".center(z) + Style.NORMAL + Fore.RESET)
            break
        print(Style.BRIGHT + "Type the number of the sentence you would like to edit!".center(z))
        print("Type home to return home!".center(z) + Style.NORMAL + Fore.RESET)
        for entry in range(len(diaryentry["entry"][entryNum])):
            if entry == 0:
                pass
            else:
                print(f"({entry}) {diaryentry["entry"][entryNum][entry]}")
        editInput = input()
        if editInput.lower().strip() == "home":
            break

    
os.system('clear')
user_intro()

while True:
    os.system('clear')
    print(Style.BRIGHT + "COMMAND OPTIONS:  START, EDIT, VIEW, HELP, QUIT".center(z) + Style.NORMAL)
    userInput = input("\n\n\n\n\n\n\n")
    if userInput.lower().strip() == "start":
        start()
    elif userInput.lower().strip() == "help":
        os.system('clear')
        print("Commands for diary use:".center(z))
        print("View: view the whole document".center(z))
        print("Edit: open text editor to edit sentences".center(z))
        print("Start: add sentences".center(z))
        print("*Note: hitting ENTER after each sentence added allows you to edit one sentence at a time".center(z))
        print("Press ENTER to go back".center(z))
        input()
    elif userInput.lower().strip() == "quit":
        os.system('clear')
        quit()