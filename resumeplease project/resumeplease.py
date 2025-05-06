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

def login(username, password,forgot):
    global identifiedUser
    for user in users:
        if user['username'] == username:
            key = user['key']
            decrypted = []
            for i in password:
                decrypted.append(int(ord(i))*key)
            if forgot:
                if user['phone'] == decrypted:
                    identifiedUser = user
                    users.remove(user)
                    os.system('clear')
                    actualPass = []
                    for i in user['password']:
                        actualPass.append(chr(int(i/key)))
                    print(f"Your password is {"".join(actualPass)}".center(z))
                    print("Press ENTER to continue".center(z))
                    input()
                    return True
            else:
                if user['password'] == decrypted:
                    identifiedUser = user
                    users.remove(user)
                    return True
    return False

def logout(user):
    users.append(user)
    with open('resumeplease project/rpusers.csv','w',newline="") as file:
        field_names = ["username","password","key","phone","checkpoint","iterations"]
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        for line in users:
            writer.writerow(line)

def new_user(username,password,key,phone):
    password = list(password)
    phone = list(phone)
    encrypted = []
    hiddenPhone = []
    for i in password:
        encrypted.append(int(ord(i))*key)
    for i in phone:
        hiddenPhone.append(int(ord(i))*key)
    users.append({'username':username,'password':encrypted,'key':key,'phone':hiddenPhone,'checkpoint':0,'iterations':0})

while True:
    os.system('clear')
    print("Type LOGIN to log into your account!".center(z))
    print("")
    print("Don't have an account? Type SIGNUP to create one!".center(z))
    enter = input().lower().strip().replace(" ","")
    if enter == "login":
        forgot = False
        os.system('clear')
        print("Type your username".center(z))
        username=input().strip()
        print("")
        print("Type your password (If you forgot your password, type FORGOT)".center(z))
        password = input().strip()
        try:
            if password.lower().strip().replace(" ","") == "forgot":
                print("")
                print("Enter the phone number associated with your account".center(z))
                phone = input().strip().replace("-","").replace(" ","").replace("(","").replace(")","")
                forgot = True
        except:
            pass

        if forgot:
            if login(username,phone,forgot):
                break
            else:
                for i in range(3):
                    os.system('clear')
                    print("")
                    print("INCORRECT USERNAME OR PASSWORD".center(z))
                    print("")
                    print(f"Returning to welcome screen in {3-i}".center(z))
                    time.sleep(1)
        else:        
            if login(username,password,forgot):
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
        while True:
            userInList = False
            os.system('clear')
            print("Create a username (3 to 16 characters)".center(z))
            username = input().strip()
            for i in users:
                if i['username'].lower().strip().replace(" ","") == username.lower().strip().replace(" ",''):
                    userInList == True
            if not userInList and len(username) >=3 and len(username)<=16:
                print("Create a password (Minimum 5 characters, maximum 16)".center(z))
                password = input().strip()
                if len(password) >= 5 and len(password) <=16:
                    print("Enter your phone number (used if you forget your password)".center(z))
                    phone = input().strip().replace(" ","").replace("-","").replace("(","").replace(")","")
                    if phone.isdigit() and len(phone) == 10:
                        infoValidCheck = False
                        show = False
                        while True:
                            if not show:
                                os.system('clear')
                                print(f"Username: {username}".center(z))
                                print(f"Password: {len(password)*"*"} (Type SHOW to show password)".center(z))
                                print(f"Phone #: ({phone[:3]}) {phone[3:6]}-{phone[6:]}".center(z))
                                print("")
                            else:
                                os.system('clear')
                                print(f"Username: {username}".center(z))
                                print(f"Password: {password} (Type HIDE to hide password)".center(z))
                                print(f"Phone #: ({phone[:3]}) {phone[3:6]}-{phone[6:]}".center(z))
                                print("")
                            print("Does this information look correct?".center(z))
                            infoValid = input().lower().strip().replace(" ","")
                            if infoValid == "yes":
                                infoValidCheck = True
                                key = random.randint(12345,99999)
                                new_user(username,password,key,phone)
                                for i in range(3):
                                    os.system('clear')
                                    print("")
                                    print("Now login on the welcome screen!".center(z))
                                    print("")
                                    print(f"{3-i}".center(z))
                                    time.sleep(1)
                                break
                            elif infoValid == "no":
                                break
                        if infoValidCheck == True:
                            break
                    else:
                        for i in range(3):
                            os.system('clear')
                            print("")
                            print("Phone number is invalid, please sign up again".center(z))
                            print("")
                            print(f"{3-i}".center(z))
                            time.sleep(1)
                        break
                else:
                    for i in range(3):
                        os.system('clear')
                        print("")
                        print("Your password must be between 5 and 16 characters, please sign up again".center(z))
                        print("")
                        print(f"{3-i}".center(z))
                        time.sleep(1)
                    break
            else:
                for i in range(3):
                    os.system('clear')
                    print("")
                    print("That username is taken or does not follow length rules, please sign up again".center(z))
                    print("")
                    print(f"{3-i}".center(z))
                    time.sleep(1)
                break





print(identifiedUser)
print(users)
input()

logout(identifiedUser)
