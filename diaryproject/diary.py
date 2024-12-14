import time 
import json
import os
from colorama import Fore, Style, Back

z = os.get_terminal_size()
z = z[0]

userNum = "a"

with open('diaryusers.json','r') as file:
        diaryusers = json.load(file)
diaryAtUser = diaryusers["user"]

def encrypt():
     

def new_user():

def user_intro():
    global userNum
    global userName
    global key
    global password
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
            if userName == diaryusers["user"][lcv]['name']:
                userNum = lcv
        if userNum.isdigit():
            if password == diaryusers["user"][userNum]['password']:
                key = diaryusers["user"][userNum]['key']
                fontColor = diaryusers["user"][userNum]['fontColor']
                fontBold = diaryusers["user"][userNum]['fontBold']
                
            else:
                userNum = "a"
                
    elif logOrSign.lower() == "sign up":
        os.system('clear')
        print("Create a username:     ".center(z))
        userName = input()
        print("Create a password:     ".center(z))
        password = input()
        for user in range(len(diaryAtUser)):
            if userName == diaryusers["user"][user]["name"]: #checks to see if a username is already taken, if it is then local variable userNameMatch is not set to p to let the code know later that the username is taken
                userNameMatch = "fail"
            else:
                pass
        if len(userName) < 5 or len(userName) > 15:
            os.system('clear')
            print(Fore.RED + Style.BRIGHT + "Username must be between 5 and 15 digits!".center(z) + Fore.RESET + Style.NORMAL)
            time.sleep(3)
            break
        elif len(password) < 8 or len(password) > 24:
            os.system('clear')
            buddy_face_talkOption3()
            print("")
            print(Fore.RED + Style.BRIGHT + "Password must be between 8 and 24 digits!".center(z) + Fore.RESET + Style.NORMAL)
            time.sleep(3)
            break
        elif userNameMatch == "fail":
            os.system('clear')
            buddy_face_talkOption3()
            print("")
            print(Fore.RED + Style.BRIGHT + "That username is already taken!".center(z) + Fore.RESET + Style.NORMAL)
            time.sleep(3)
            break
        else:
            userNameCorrect = "p"

        if userNameCorrect == "p":
            while True:
                os.system('clear')
                buddy_face_question()
                print("")
                print(f"Username: {userName}".center(z) + "\n" + (f"Password: {password[0]}{password[1]}" + ("*" * (len(password) - 3)) + f"{password[-1]}").center(z) + "\n" + "Does this information look correct?".center(z)) #neat little display of username and password with password being covered up
                checkInfo = input()
                if checkInfo.lower() == "yes":
                    break
                elif checkInfo.lower() == "no":
                    break
                else:
                    pass
            if checkInfo.lower() == "yes":
                break



