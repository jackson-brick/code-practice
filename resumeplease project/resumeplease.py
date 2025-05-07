import csv
import time
import random
import os
from colorama import Fore, Style, Back
z = os.get_terminal_size()
z = z[0]

#A mysterious organization hired you to interview people and decide whether or not to let them through

def speakNar(sentence,speaker):
    if speaker == "continuation":
        toPrint = ""
    else:
        toPrint = speaker + ": "
    print(toPrint.center(z))
    time.sleep(0.5)
    for i in sentence:
        if i == ".":
            x = 0.5
        else:
            x = 0.05
        os.system('clear')
        toPrint+=i
        print(toPrint.center(z))
        time.sleep(x)

def toCont():
    time.sleep(0.5)
    print("Press ENTER to continue".center(z))
    input()



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
                decrypted.append(int(ord(i))*int(key))
            if forgot:
                if user['phone'] == decrypted or user['phone'] == str(decrypted):
                    identifiedUser = user
                    identifiedUser['checkpoint']=int(identifiedUser['checkpoint'])
                    identifiedUser['iterations'] =int(identifiedUser['iterations'])
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
                if user['password'] == decrypted or user['password'] == str(decrypted):
                    identifiedUser = user
                    identifiedUser['checkpoint']=int(identifiedUser['checkpoint'])
                    identifiedUser['iterations'] =int(identifiedUser['iterations'])
                    users.remove(user)
                    return True
    return False

def save(user):
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
    users.append({'username':username,'password':encrypted,'key':key,'phone':hiddenPhone,'checkpoint':int(0),'iterations':int(0)})


while True:
    os.system('clear')
    print("Type LOGIN to log into your account!".center(z))
    print("")
    print("Don't have an account? Type SIGNUP to create one!".center(z))
    enter = input().lower().strip().replace(" ","")
    if enter == "openter":
        login("ViperBrick","1114100930",False)
        break
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
            if login(username,password,forgot) == True:
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
                            elif infoValid == "show":
                                show = True
                            elif infoValid == "hide":
                                show = False
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

#+----------------------------------------------------------------------+
#THIS IS THE START OF THE CODE FOR THE ACTUAL GAME, NOT THE LOGIN PROCESS
#+----------------------------------------------------------------------+

def escape_menu():
    while True:
        os.system('clear')
        print("GAME PAUSED".center(z))
        print("")
        print("Resume            |            Quit".center(z))
        print("")
        print("Settings          |                ".center(z))
        print("")
        print("Type the name of the option you want".center(z))
        escape = input().lower().strip().replace(" ","")
        if escape == "quit":
            while True:
                os.system('clear')
                print("Are you sure you want to quit?".center(z))
                quitSecure = input().lower().strip().replace(" ","")
                if quitSecure == "yes":
                    save(identifiedUser)
                    os.system('clear')
                    quit()
                elif quitSecure == "no":
                    break
        elif escape == "resume":
            break

def desk(introCheck):
    print("+--------------------------------------------+        +========================+")
    print("|                                            |        |                        |")
    print("|              R  E  S  U  M  E              |        |       GUIDELINES       |")
    print("|                                            |        |                        |")
    print("|                                            |        +========================+")
    if introCheck:
        read = ""
    else:
        read = input("|                                            |    ").lower().strip().replace(" ","")
    if read == "resume":
        resume()
    elif read == "guidelines":
        guidelines()
def resume(introCheck,name,dob):
    print("---------------------------------------------------------------------------------------------")
    print("")
    print(name)
    print(dob)
    if introCheck:
        readResume = ""
    else:
        readResume = input().lower().strip().replace(" ","")
    if readResume == "back":
        return readResume
def guidelines(introCheck):
    print("+----------------------------------------------------------------------+")
    print("+                                                                      +")
    print("+  1. Reject anyone whose name starts with a letter from the second    +")
    print("+     half of the alphabet.                                            +")
    if introCheck:
        readGuidelines = ""
    else:
        readGuidelines = input().lower().strip().replace(" ","")
    if readGuidelines == "back":
        return readGuidelines


def intro():
    os.system('clear')
    speakNar("Thank you for attending this interview. Tell me why you think you deserve this position.","Interviewer")
    print("")
    input("YOUR RESPONSE >> ")
    os.system('clear')
    speakNar(". . . Yes, that will do. You are hired.","Interviewer")
    toCont()
    os.system('clear')
    speakNar("Your job is to conduct interviews. You will receive a set of guidelines so you know who to accept and who to deny.","Boss")
    toCont()
    os.system('clear')
    speakNar("This is your desk. You will review any materials they bring here.","Boss")
    desk(True)
    time.sleep(1)
    toCont()
    os.system('clear')
    speakNar("In general, typing the name of something will allow you to inspect it. Try it here.","Boss")
    desk(True)
    sawResume = False
    sawGuidelines = False
    while sawResume == False or sawGuidelines == False:
        introDesk = input().lower().strip().replace(" ","")
        if introDesk == "resume":
            os.system('clear')
            speakNar("You will be able to read people's resumes here.","Boss")
            speakNar("You must review their resume to decide whether to hire or not.","continuation")
            resume(True,"Jackson Brick","09/30/2001")
            if sawResume == False and sawGuidelines == False:
                speakNar("Type BACK when you want to go back to your desk.","Boss")
                speakNar("Remember that no commands are case sensitive. You can type UPPERCASE, lowercase, ","continuation")
                speakNar("or sOmeWHerE iN B eT wEE n. Go on, try it.","continuation")
                while True:
                    os.system('clear')
                    print("Boss: You will be able to read people's resumes here.".center(z))
                    print("You must review their resume to decide whether to hire or not.".center(z))
                    resume(True,"Jackson Brick","09/30/2001")
                    print("Boss: Type BACK when you want to go back to your desk.".center(z))
                    print("Remember that no commands are case sensitive. You can type UPPERCASE, lowercase, ".center(z))
                    print("or sOmeWHerE iN B eT wEE n. Go on, try it.".center(z))
                    learnBack = input().lower().strip().replace(" ","")
                    if learnBack == "back":
                        sawResume = True
                        break
            else:
                speakNar("Type BACK when you want to return to your desk.","Boss")
                while True:
                    os.system('clear')
                    print("Boss: You will be able to read people's resumes here.".center(z))
                    print("You must review their resume to decide whether to hire or not.".center(z))
                    resume(True,"Jackson Brick","09/30/2001")
                    print("Boss: Type BACK when you want to return to your desk".center(z))
                    learnBack = input().lower().strip().replace(" ","")
                    if learnBack == "back":
                        sawResume = True
                        break
                    
                    
        elif introDesk == "guidelines":
            os.system('clear')
            speakNar("Here you can find the rules that you must follow. Deviation from these rules will result","Boss")
            speakNar("in consequences.","continuation")
            guidelines(True)
            if sawResume == False and sawGuidelines == False:
                speakNar("Type BACK when you want to go back to your desk.","Boss")
                speakNar("Remember that no commands are case sensitive. You can type UPPERCASE, lowercase, ","continuation")
                speakNar("or sOmeWHerE iN B eT wEE n. Go on, try it.","continuation")
                while True:
                    os.system('clear')
                    print("Here you can find the rules that you must follow. Deviation from these rules will result".center(z))
                    print("in consequences.".center(z))
                    guidelines(True)
                    print("Boss: Type BACK when you want to go back to your desk.".center(z))
                    print("Remember that no commands are case sensitive. You can type UPPERCASE, lowercase, ".center(z))
                    print("or sOmeWHerE iN B eT wEE n. Go on, try it.".center(z))
                    learnBack = input().lower().strip().replace(" ","")
                    if learnBack == "back":
                        sawGuidelines = True
                        break
            else:
                speakNar("Type BACK when you want to return to your desk.","Boss")
                while True:
                    os.system('clear')
                    print("Here you can find the rules that you must follow. Deviation from these rules will result".center(z))
                    print("in consequences.".center(z))
                    guidelines(True)
                    learnBack = input().lower().strip().replace(" ","")
                    if learnBack == "back":
                        sawGuidelines = True
                        break

        else:
            os.system('clear')
            print("Boss: In general, typing the name of something will allow you to inspect it. Try it here.".center(z))
            desk(True)
            introDesk = input().lower().strip().replace(" ","")
    os.system('clear')
    speakNar("Follow the rules and you will get paid. Do not make us regret hiring you.","Boss")
    toCont()
    identifiedUser['iterations'] += 1
    save(identifiedUser)


while True:
    os.system('clear')
    if identifiedUser['iterations'] == 0:
        intro()
    game = input().lower().strip().replace(" ","")
    if game == "escape":
        escape_menu()


