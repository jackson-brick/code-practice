import csv
import time
import random
import os
from colorama import Fore, Style, Back
z = os.get_terminal_size()
z = z[0]

#A mysterious organization hired you to interview people and decide whether or not to let them through

users = []
with open('resumeplease project/rpusers.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        users.append(line)

intro_phrases = []

def login(username, password):
    for user in users:
        if user['username'] == username:
            key = user['key']
            decrypted = []
            for i in password:
                decrypted.append(int(ord(i))*key)
            if user['password'] == decrypted:
                global identifiedUser
                identifiedUser = user
                users.remove(user)
                return True
    return False

def logout(user):
    users.append(identifiedUser)
    with open('rpusers.csv','w') as file:
        field_names = ["username","password","key","phone","checkpoint","iterations"]
        writer = csv.DictWriter(file,fieldnames=field_names)

def new_user(username,password,key,phone):
    password = list(password)
    encrypted = []
    for i in password:
        encrypted.append(int(ord(i))*key)
    users.append({'username':username,'password':encrypted,'key':key,'phone':phone,'checkpoint':0,'iteration':0})

while True:
    os.system('clear')
    print("Type LOGIN to log into your account!".center(z))
    print("")
    print("Don't have an account? Type SIGNUP to create one!".center(z))
    enter = input().lower().strip().replace(" ","")
    if enter == "login":
        os.system('clear')
        print("Type your username".center(z))
        username=input()
        print("Type your password".center(z))
        password = input()
        if login(username,password):
            break
        else:
            for i in range(3):
                os.system('clear')
                print("")
                print("INCORRECT USERNAME OR PASSWORD".center(z))
                print("")
                print(f"Returning to welcome screen in {3-i}".center(z))
                time.sleep(1)
    elif enter == "signup":
        userInList = False
        os.system('clear')
        print("Create a username".center(z))
        username = input()
        for i in users:
            if i['username'].lower().strip().replace(" ","") == username.lower().strip().replace(" ",''):
                userInList == True
        if not userInList:
            print("Create a password (Minimum 5 characters, maximum 16)".center(z))
            password = input()
            if len(password) >= 5 and len(password) <=16:
                print("Enter your phone number (used if you forget your password)".center(z))
                phone = input()
                if phone.isdigit():
                    key = random.randint(12345,99999)
                    new_user(username,password,key)
                    for i in range(3):
                        os.system('clear')
                        print("")
                        print("Now login on the welcome screen!".center(z))
                        print("")
                        print(f"{3-i}".center(z))
                        time.sleep(1)
                else:
                    for i in range(3):
                        os.system('clear')
                        print("")
                        print("Your phone is only numbers, please sign up again".center(z))
                        print("")
                        print(f"{3-i}".center(z))
                        time.sleep(1)
            else:
                for i in range(3):
                    os.system('clear')
                    print("")
                    print("Your password must be between 5 and 16 characters, please sign up again".center(z))
                    print("")
                    print(f"{3-i}".center(z))
                    time.sleep(1)
        else:
            for i in range(3):
                os.system('clear')
                print("")
                print("That username is taken, please sign up again".center(z))
                print("")
                print(f"{3-i}".center(z))
                time.sleep(1)





print(identifiedUser)
print(users)
input()


