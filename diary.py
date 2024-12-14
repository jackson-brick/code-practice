import time 
import json
import os

z = os.get_terminal_size()
z = z[0]

userNum = "a"

with open('diaryusers.json','r') as file:
        diaryusers = json.load(file)
diaryAtUser = diaryusers["user"]


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
        



