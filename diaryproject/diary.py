import time 
import json
import os
from colorama import Fore, Style, Back
import random

z = os.get_terminal_size()
z = z[0]

opCommand = False
breakVar = False

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
    return encryptedPass

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
    
def write_to_diary_entry(entry,function):
    global encryptedEntry
    if entry != 0:
        unencryptedEntry = []
        for ele in range(len(entry)):
            unencryptedEntry.append(entry[ele])
        encryptedEntry = []
        for ele in unencryptedEntry:
            encryptedEntry.append(diaryusers["users"][userNum]["key"][ele])
        encryptedEntry = ''.join(encryptedEntry)
    if function == "start":
        diaryAtEntry[entryNum][f"{len(diaryentry["entry"][entryNum]) - 2}"] = encryptedEntry
        diaryAtEntry[entryNum][f"{len(diaryentry["entry"][entryNum]) - 1}"] = ""
    elif function == "edit":
        diaryAtEntry[entryNum][f"{editInput}"] = encryptedEntry
    elif function == "delete":
        counter = editInput
        while counter < (len(diaryentry["entry"][entryNum]) - 2):
            diaryAtEntry[entryNum][f"{counter}"] = diaryAtEntry[entryNum][f"{counter + 1}"]
            counter += 1
        del diaryAtEntry[entryNum][f"{len(diaryentry["entry"][entryNum]) - 2}"]
    with open('diaryentry.json','w') as outfile:
        jsonVar = json.dumps(diaryAtEntry,indent=4)
        outfile.write('{\n"entry": ' + jsonVar + '\n}')

def decrypt(encEntry):
    global decryptedEntry
    encryptedEntry = []
    for ele in range(len(encEntry)):
        encryptedEntry.append(encEntry[ele])
    decryptedEntry = []
    userKey = diaryusers["users"][userNum]["key"].items()
    for ele in encryptedEntry:
        for pair in userKey:
            if ele == pair[1]:
                decryptedEntry.append(pair[0])
    decryptedEntry = ''.join(decryptedEntry)
    return decryptedEntry

def op_decrypt(encEntry,key):
    global decryptedEntry
    encryptedEntry = []
    for ele in range(len(encEntry)):
        encryptedEntry.append(encEntry[ele])
    decryptedEntry = []
    userKey = key.items()
    for ele in encryptedEntry:
        for pair in userKey:
            if ele == pair[1]:
                decryptedEntry.append(pair[0])
    decryptedEntry = ''.join(decryptedEntry)
    return decryptedEntry

def user_intro():
    global userNum
    global userName
    global key
    global password
    global entryNum
    while True:
        userNum = -2
        logOrSign = ""
        os.system('clear')
        #if opCommand == False:
        print("Have an account already? Type LOG IN".center(z) + "\n" + "Need to create an account? Type SIGN UP".center(z) + "\n")
        logOrSign = input()
        if logOrSign.lower() == "log in":
            if opCommand == False:
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


def write():
    while True:
        os.system('clear')
        print(Style.BRIGHT + "Type HOME to exit!".center(z) + Style.NORMAL + Fore.RESET)
        print(Style.DIM + "WRITING MODE".center(z) + Style.NORMAL)
        print("")
        if diaryentry["entry"][entryNum]["0"] == "":
            print(Style.DIM + "Your story starts here..." + Style.NORMAL)
            print("\n\n")
        else:
            for entry in range(len(diaryentry["entry"][entryNum])):
                if entry == (len(diaryentry["entry"][entryNum]) - 1) or entry == (len(diaryentry["entry"][entryNum]) - 2):
                    pass
                else:
                    print(decrypt(diaryentry["entry"][entryNum][f"{entry}"]), end = " ")
            print("")
            print(Style.DIM + "Scroll up to see the whole thing" + Style.NORMAL)
            print("")
        startInput = input()
        if startInput.lower().strip() == "home":
            break
        elif startInput.lower().strip() == "quit":
            os.system('clear')
            quit()
        elif startInput.lower().strip() == "hide":
            while True:
                os.system('clear')
                print(Style.BRIGHT + "Type HOME to exit!".center(z) + Style.NORMAL + Fore.RESET)
                print(Style.DIM + "WRITING MODE".center(z) + Style.NORMAL)
                print("")
                if diaryentry["entry"][entryNum]["0"] == "":
                    print(Style.DIM + "Your story starts here..." + Style.NORMAL)
                    print("\n\n")
                else:
                    for entry in range(len(diaryentry["entry"][entryNum])):
                        if entry == (len(diaryentry["entry"][entryNum]) - 1) or entry == (len(diaryentry["entry"][entryNum]) - 2):
                            pass
                        else:
                            print(diaryentry["entry"][entryNum][f"{entry}"], end = " ")
                    print("")
                    print(Style.DIM + "Scroll up to see the whole thing" + Style.NORMAL)
                    print("")
                startInput = input()
                if startInput.lower().strip() == "home":
                    break
                elif startInput.lower().strip() == "quit":
                    os.system('clear')
                    quit()
                elif startInput.lower().strip() == "reveal":
                    break
                else:
                    write_to_diary_entry(startInput,"start")
            if startInput.lower().strip() == "home":
                break
        else:
            write_to_diary_entry(startInput,"start")
            
            
def edit():
    global editInput
    global editChange
    while True:
        os.system('clear')
        if diaryentry["entry"][entryNum]["0"] == "":
            print(Style.BRIGHT + Fore.RED + "You have to begin writing to edit!".center(z) + Style.NORMAL + Fore.RESET)
            input()
            break
        print(f"Type the number of the sentence you would like to edit (1-{len(diaryentry["entry"][entryNum]) - 2})!".center(z) + Fore.RESET + Style.NORMAL)
        print("Type home to exit!".center(z))
        print(Style.DIM + "EDIT MODE".center(z) + Style.NORMAL)
        for entry in range(len(diaryentry["entry"][entryNum])):
            if entry == (len(diaryentry["entry"][entryNum]) - 1) or entry == (len(diaryentry["entry"][entryNum]) - 2):
                pass
            else:
                print(f"({entry + 1}) {decrypt(diaryentry["entry"][entryNum][f"{entry}"])}")
        print(Style.DIM + "Scroll up to see the whole thing" + Style.NORMAL)
        print("")
        editInput = input()
        if editInput.lower().strip() == "home":
            break
        elif editInput.lower().strip() == "quit":
            os.system('clear')
            quit()
        elif editInput.isdigit():
            editInput = int(editInput)
            if editInput >= 1 and editInput < (len(diaryentry["entry"][entryNum]) - 1):
                os.system('clear')
                editInput -= 1
                print(Style.BRIGHT + "Type CANCEL to cancel edit or DELETE to delete the entry!".center(z) + Style.NORMAL)
                print(Style.DIM + "OLD SENTENCE:".center(z) + Style.NORMAL)
                print(decrypt(diaryentry["entry"][entryNum][f"{editInput}"]).center(z))
                print("\n")
                print(Style.DIM + "NEW SENTENCE:" + Style.NORMAL)
                editChange = input()
                if editChange.lower().strip() != "cancel":
                    if editChange.lower().strip() == "delete":
                        write_to_diary_entry(0,"delete")
                    else:
                        write_to_diary_entry(editChange,"edit")
            else:
                print(Fore.RED + Style.BRIGHT)
        else:
            print(Fore.RED + Style.BRIGHT)
            
while True:
    os.system('clear')
    user_intro()

    while True:
        os.system('clear')
        print(Fore.BLUE + Style.BRIGHT + f"Welcome {diaryusers["users"][userNum]["name"].upper()}".center(z) + Style.NORMAL + Fore.RESET)
        print(Style.BRIGHT + "COMMAND OPTIONS:  WRITE, EDIT, HELP, QUIT, LOG OUT".center(z) + Style.NORMAL)
        userInput = input("\n")
        if userInput.lower().strip() == "write":
            write()
        elif userInput.lower().strip() == "help":
            os.system('clear')
            print("Commands for diary use:".center(z))
            print("View: view the whole document".center(z))
            print("Edit: open text editor to edit sentences".center(z))
            print("Start: add sentences".center(z))
            print("Hide/Reveal: hide or reveal sentences being worked on in case of nosy people".center(z))
            print("*Note: hitting ENTER after each sentence added allows you to edit one sentence at a time".center(z))
            print("Press ENTER to go back".center(z))
            input()
        elif userInput.lower().strip() == "quit":
            os.system('clear')
            quit()
        elif userInput.lower().strip() == "edit":
            edit()
        elif userInput == "decode":
            os.system('clear')
            print("Copy and paste whatever you wanna decode".center(z))
            decodeInput = input()
            while True:
                print(decrypt(decodeInput).center(z))
                decodeInput = decrypt(decodeInput)
                codeInput = input()
                if codeInput == "done":
                    break
        elif userInput == "encode":
            os.system('clear')
            print("Copy and paste whatever you wanna encode, type DONE when done".center(z))
            encodeInput = input()
            while True:
                print(encrypt(encodeInput).center(z))
                encodeInput = encrypt(encodeInput)
                codeInput = input()
                if codeInput == "done":
                    break
        elif userInput == "opcommands":
            if userName == "operatorcommand":
                opCommand == True
                while True:
                    os.system('clear')
                    print(Style.DIM + "Operator Commands: " + Style.NORMAL + Style.BRIGHT + Fore.GREEN + "ONLINE" + Style.NORMAL + Fore.RESET)
                    opInput = input()
                    if opInput == "exit":
                        break
                    elif opInput == "logins":
                        userList = []
                        for entry in range (len(diaryentry["entry"])):
                            if diaryusers["users"][entry]["name"] == "operatorcommand":
                                pass
                            else:
                                usernameVar = diaryusers["users"][entry]["name"]
                                passwordVar = op_decrypt(diaryusers["users"][entry]["password"],diaryusers["users"][entry]["key"])
                                combinedVar = str(usernameVar + " : " + passwordVar)
                                newVar = ""
                                for letter in range(len(combinedVar)):
                                    os.system('clear')
                                    print(Style.DIM + "Operator Commands: " + Style.NORMAL + Style.BRIGHT + Fore.GREEN + "ONLINE" + Style.NORMAL + Fore.RESET)
                                    print("")
                                    for item in userList:
                                        print(item)
                                        print("")
                                    newVar = newVar + combinedVar[letter]
                                    print(newVar)
                                    time.sleep(0.02)
                                userList.append(newVar)
                        print("")
                        loginInput = input()
                        for lcv in range(len(diaryAtUser)):
                            if loginInput == diaryusers["users"][lcv]['name']:
                                userName = diaryusers["users"][lcv]["name"]
                                password = op_decrypt(diaryusers["users"][lcv]["password"],diaryusers["users"][lcv]["key"])
                                breakVar = True
                                opCommand = True
                                break
                    if breakVar == True:
                        break
            else:
                os.system('clear')
                print(Style.DIM + "Operator Commands: " + Fore.RED + Style.NORMAL + Style.BRIGHT + "OFFLINE" + Fore.RESET + Style.NORMAL)
                input()
        elif userInput == "opreturn":
            if opCommand == True:
                userName = "operatorcommand"
                for i in range(len(diaryusers["users"])):
                    if diaryusers["users"][i]["name"] == userName:
                        userNum = i
                password = op_decrypt(diaryusers["users"][userNum]["password"],diaryusers["users"][userNum]["key"])
                breakVar = True
        elif userInput.lower().strip() == "log out":
            user_intro()
        if breakVar == True:
            breakVar = False
            break
