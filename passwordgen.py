import random
import csv
import os
os.system('clear')
z=os.get_terminal_size()[0]

passwords = []
with open('passwords.csv','r') as file:
    password = csv.DictReader(file)
    for line in password:
        passwords.append(line)


while True:
    os.system('clear')
    print("Are you using a website or an app?".center(z))
    webApp = input()
    if webApp.strip().lower() == "website":
        webApp = "website"
        break
    elif webApp.strip().lower() == "app":
        webApp = "app"
        break
    elif webApp == "1114100930":
        break

while True:
    if webApp == "1114100930":
        break
    name = ""
    firstDot = 0
    os.system('clear')
    if webApp == "website":
        while True:
            os.system('clear')
            print("Enter the full url of the website you need the password for".center(z))
            website = input()
            if website.count(".") == 1:
                for i in website:
                    if firstDot == 0 and i != ".":
                        name += i
                    elif i == ".":
                        firstDot += 1
                break
            elif website.count(".") == 2:
                for i in website:
                    if firstDot == 1 and i != ".":
                        name += i
                    elif i == ".":
                        firstDot += 1
                break
            else:
                os.system('clear')
                print("That is not a url. Press ENTER to try again.".center(z))
                input()
            while " " in name:
                name = name.replace(" ","")
    else:
        while True:
            os.system('clear')
            print("Enter the name of the app you need the password for".center(z))
            app = input()
            if app.strip().isalpha():
                name = app.lower().strip()
                break
    while True:
        os.system('clear')
        print(f"Is {name} correct?".center(z))
        yesOrNo = input()
        if yesOrNo.strip().lower() == "yes":
            break
        elif yesOrNo.strip().lower() == "no":
            break
    if yesOrNo.strip().lower() == "yes":
        break

charList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","{","}","[","]","|","\\","\'","\"",":",";","<",">",",",".","?","/"]
charListNoSpecial = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

jacksonKey = {
            "a": "(",
            "b": "X",
            "c": "0",
            "d": ".",
            "e": "m",
            "f": "5",
            "g": "u",
            "h": "h",
            "i": "B",
            "j": "y",
            "k": "'",
            "l": "+",
            "m": "n",
            "n": "x",
            "o": "_",
            "p": "M",
            "q": "d",
            "r": "|",
            "s": "c",
            "t": "R",
            "u": "}",
            "v": "g",
            "w": "F",
            "x": "?",
            "y": "E",
            "z": "2",
            "A": ";",
            "B": "P",
            "C": "U",
            "D": "o",
            "E": "J",
            "F": ",",
            "G": "z",
            "H": "`",
            "I": "s",
            "J": "I",
            "K": "G",
            "L": "O",
            "M": "V",
            "N": "p",
            "O": "k",
            "P": "!",
            "Q": "w",
            "R": "Y",
            "S": "r",
            "T": "a",
            "U": "Z",
            "V": "-",
            "W": "8",
            "X": "*",
            "Y": "b",
            "Z": "&",
            "1": "$",
            "2": "4",
            "3": "7",
            "4": "6",
            "5": "<",
            "6": "\"",
            "7": "e",
            "8": "v",
            "9": "N",
            "0": "A",
            "!": "=",
            "@": ">",
            "#": "%",
            "$": ")",
            "%": "~",
            "^": "[",
            "&": "j",
            "*": "q",
            "(": " ",
            ")": "t",
            "-": "^",
            "_": "i",
            "=": "@",
            "+": "W",
            "`": "D",
            "~": "S",
            "{": "9",
            "}": "1",
            "[": "K",
            "]": "{",
            "|": "H",
            "\\": "Q",
            "'": "3",
            "\"": "L",
            ":": "/",
            ";": "f",
            "<": "C",
            ">": "]",
            ",": "\\",
            ".": ":",
            "?": "#",
            "/": "T",
            " ": "l"}

while True:
    if webApp == "1114100930":
        break
    os.system('clear')
    print("Are special characters allowed?".center(z))
    specChar = input()
    if specChar.lower().strip() == "yes":
        specChar = "yes"
        break
    elif specChar.lower().strip() == "no":
        specChar = "no"
        break

while True:
    if webApp == "1114100930":
        break
    os.system('clear')
    finalPassword = ''
    for i in range(6):
        if specChar == "yes":
            finalPassword += random.choice(charList)
        else:
            finalPassword += random.choice(charListNoSpecial)
    finalPassword += name.upper()
    for i in range(7):
        if specChar == "yes":
            finalPassword += random.choice(charList)
        else:
            finalPassword += random.choice(charListNoSpecial)
    while True:
        print(f"Is the password \"{finalPassword}\" good?".center(z))
        finalCheck = input()
        if finalCheck.lower().strip() == "yes":
            break
        elif finalCheck.lower().strip() == "no":
            break
    if finalCheck.lower().strip() == "yes":
        break
if webApp != "1114100930":    
    os.system('clear')
    print("Congrats! Your new password has been saved!".center(z))
    tempPass = []
    for ele in finalPassword:
        tempPass.append(ele)
    encryptedPassword = ''
    print(tempPass)
    input()
    for i in finalPassword:
        encryptedPassword+= jacksonKey[i]
    print(encryptedPassword)
    input()
    passwords.append({'password':finalPassword,'siteName':name})
    with open('passwords.csv','w',newline='') as file:
        field_names = ['password','siteName']
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        for line in passwords:
            writer.writerow(line)
        

else:
    os.system('clear')

